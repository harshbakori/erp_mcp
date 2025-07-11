from config import base_url, api_key, api_secret
import requests
import json
from backend.mcp_main import mcp

def get_frappe_api_config():
    headers = {
        "Authorization": f"token {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }
    return base_url, headers

@mcp.tool()
def list_users() -> list:
    """ Use this tool to list all users from the ERP system using the Frappe REST API.

    Creative use cases:
    - Display all users in an admin dashboard.
    - Audit user accounts for compliance or security.
    - Sync ERP users with another system (e.g., CRM, HRMS).
    - Generate reports on user activity or status.
    - Bulk update or notify users.
    - Analyze user roles and permissions.
    - Export user data for backup or migration.
    - Identify inactive or duplicate accounts.
    - Integrate with analytics tools for user insights.
    - Automate onboarding/offboarding workflows.
    """
    base_url, headers = get_frappe_api_config()
    try: 
        resp = requests.get(f"{base_url}/api/resource/User", headers=headers)
        if resp.status_code == 200:
            users = resp.json().get("data", [])
            return [
                # {
                    user
                    # "name": user.get("full_name"),
                    # "email": user.get("name"),
                    # "enabled": user.get("enabled")
                # }
                for user in users
            ]
        else:
            return [{"error": resp.text}]
    except Exception as e:
        return [{"error": str(e)}]
    
@mcp.tool()
def list_doctypes(module: str = None) -> list:
    """ Use this tool to list all doctypes from the ERP system using the Frappe REST API, with optional filtering.

    Parameters:
    - module (str): The module to filter doctypes by.
    - is_custom (bool): Filter by custom doctypes (True for custom, False for standard).

    Creative use cases:
    - Display all available document types in an admin dashboard.
    - Generate documentation for developers or users.
    - Sync ERP doctypes with another system for integration purposes.
    - Analyze the structure of the ERP system for optimization.
    - Create custom forms or reports based on available doctypes.
    - Facilitate user training by providing a list of available document types.
    """
    base_url, headers = get_frappe_api_config()
    params = {}

    try: 
        if module:
            filters = [["module", "=", module]]
            resp = requests.get(f"{base_url}/api/resource/DocType", headers=headers, params={"filters": json.dumps(filters)})
        else:
            resp = requests.get(f"{base_url}/api/resource/DocType", headers=headers)
        if resp.status_code == 200:
            doctypes = resp.json().get("data", [])
            return [
                doctype
                for doctype in doctypes
            ]
        else:
            return [{"error": resp.text}]
    except Exception as e:
        return [{"error": str(e)}]
@mcp.tool()
def get_doctype_list(doctype: str, limit: int = 20, offset: int = 0) -> list:
    """ Use this tool to get a paginated list of records for a specific doctype from the ERP system using the Frappe REST API.

    Parameters:
    - doctype (str): The name of the doctype to retrieve records for.
    - limit (int, optional): Maximum number of records to return per page. Default is 20.
    - offset (int, optional): Number of records to skip (for pagination). Default is 0.

    Creative use cases:
    - Display all records of a specific document type in an admin dashboard with pagination.
    - Generate reports based on the records of a specific doctype.
    - Sync records with another system for integration purposes.
    - Analyze data trends within a specific document type.
    - Facilitate user training by providing examples of records.
    """
    base_url, headers = get_frappe_api_config()
    params = {
        "limit": limit,  # Number of DocTypes to fetch per request
        "offset": offset  # Number of DocTypes to skip for pagination
    }
    try: 
        resp = requests.get(f"{base_url}/api/resource/{doctype}", headers=headers, params=params)
        if resp.status_code == 200:
            records = resp.json().get("data", [])
            return [
                record
                for record in records
            ]
        else:
            return [{"error": resp.text}]
    except Exception as e:
        return [{"error": str(e)}]


@mcp.tool()
def get_doctype_list_with_filters(
    doctype: str,
    field: str = None,
    value: str = None,
    operator: str = "=",
    limit: int = 20,
    order_by: str = None
) -> list:
    """ Use this tool to get a filtered list of records for a specific doctype from the ERP system using the Frappe REST API.

    Parameters:
    - doctype (str): The name of the doctype to retrieve records for.
    - field (str, optional): The field to filter by.
    - value (str, optional): The value to filter the field by.
    - operator (str, optional): The filter operator (e.g., '=', '!=', 'like', '>', '<'). Default is '='.
    - limit (int, optional): Maximum number of records to return. Default is 20.
    - order_by (str, optional): Field to order the results by (e.g., 'creation desc').

    Creative use cases:
    - Filter records by status, date, or user.
    - Retrieve only active or inactive records.
    - Get top N records based on a field (e.g., latest, highest value).
    - Search for records matching a pattern or partial value.
    - Combine multiple filters for advanced queries.
    """
    base_url, headers = get_frappe_api_config()
    params = {"limit_page_length": limit}
    filters = []

    if field and value is not None:
        filters.append([field, operator, value])
    if filters:
        params["filters"] = json.dumps(filters)
    if order_by:
        params["order_by"] = order_by

    try:
        resp = requests.get(f"{base_url}/api/resource/{doctype}", headers=headers, params=params)
        if resp.status_code == 200:
            records = resp.json().get("data", [])
            return [
                record
                for record in records
            ]
        else:
            return [{"error": resp.text}]
    except Exception as e:
        return [{"error": str(e)}]
    
@mcp.tool()
def list_doctype_fields(doctype_name: str) -> list:
    """Fetch all fields of a specified DocType using the Frappe REST API.

    Parameters:
    - doctype_name (str): The name of the DocType to retrieve fields from.

    Returns:
    - list: A list of fields in the specified DocType or an error message.

    Creative use cases:
    - Dynamically generate forms or UI components based on DocType fields.
    - Build documentation or data dictionaries for ERP modules.
    - Validate data imports or exports by referencing field definitions.
    - Enable low-code or no-code app builders to configure workflows.
    - Analyze field usage for optimization or refactoring.
    - Automate test case generation for custom DocTypes.
    - Integrate with reporting tools to allow field selection.
    - Support user training by listing available fields and their types.
    """
    base_url, headers = get_frappe_api_config()  # Function to get base URL and headers
    try:
        # Construct the API endpoint for the specific DocType
        endpoint = f"{base_url}/api/resource/DocType/{doctype_name}"
        resp = requests.get(endpoint, headers=headers)

        if resp.status_code == 200:
            doctype = resp.json().get("data", {})
            fields = doctype.get("fields", [])
            return fields
        else:
            return [{"error": resp.text}]
    except Exception as e:
        return [{"error": str(e)}]
    
@mcp.tool()
def fetch_doctype_with_fields(doctype_name: str, fields: list, name: str) -> list:
    """Fetch a specific DocType record with only the given fields using the Frappe REST API.

    Parameters:
    - doctype_name (str): The name of the DocType to retrieve.
    - fields (list): A list of field names to include in the response.
    - name (str): The unique name (ID) of the record to fetch. This parameter is mandatory.

    Returns:
    - list: A list containing the record with the specified fields or an error message.

    Creative use cases:
    - Optimize data transfer by fetching only required fields for analytics or reporting.
    - Build lightweight dashboards or widgets that display selected information.
    - Integrate with external systems that require only specific fields.
    - Support mobile or low-bandwidth applications by reducing payload size.
    - Enable dynamic form generation based on user-selected fields.
    - Facilitate data migration or export tasks with custom field selection.
    - Implement privacy controls by exposing only non-sensitive fields.
    - Accelerate API responses for high-frequency queries.
    """
    if not name:
        return [{"error": "Parameter 'name' is mandatory."}]
    base_url, headers = get_frappe_api_config()  # Function to get base URL and headers
    try:
        # Construct the API endpoint for the specific DocType
        endpoint = f"{base_url}/api/resource/{doctype_name}/{name}"

        
        # Prepare the fields parameter for the API request
        params = {"fields": json.dumps(fields)}  # Convert fields list to JSON string
        
        # Make the API request
        resp = requests.get(endpoint, headers=headers, params=params)

        if resp.status_code == 200:
            data = resp.json().get("data", {})
            if data and fields:
                filtered_data = {field: data.get(field) for field in fields}
                return [filtered_data]
            elif data:
                return [data]
            return []
        else:
            return [{"error": resp.text}]
    except Exception as e:
        return [{"error": str(e)}]

@mcp.tool()
def get_url_for_doctype(doctype_name: str, name: str) -> str:
    """Construct the URL for a specific DocType record.

    Parameters:
    - doctype_name (str): The name of the DocType.
    - name (str): The unique name (ID) of the record.

    Returns:
    - str: The constructed URL for the record.

    Creative use cases:
    - Generate direct links for users to quickly access or edit specific records.
    - Embed record URLs in automated email notifications or alerts.
    - Integrate with external systems by providing deep links to ERP records.
    - Facilitate workflow automation by linking approval tasks to relevant records.
    - Build dashboards or widgets with clickable links to detailed record views.
    - Enable QR code generation for physical documents or assets that link to their ERP records.
    - Support audit trails by referencing exact record URLs in logs or reports.
    - Simplify user training by sharing direct links to example records.
    - Enhance collaboration by allowing team members to share record URLs.
    - Use in browser extensions or bookmarklets for quick access to frequently used records.
    """
    base_url, _ = get_frappe_api_config()
    doctype_slug = doctype_name.replace(" ", "-").lower()
    return f"{base_url}/app/{doctype_slug}/{name}"