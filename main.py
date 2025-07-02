from fastmcp import FastMCP
import requests
from config import base_url, api_key, api_secret

mcp = FastMCP("mcp",host="0.0.0.0", port=8000)

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def get_frappe_api_config():
    headers = {
        "Authorization": f"token {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }
    return base_url, headers

@mcp.tool()
def list_users() -> list:
    """ ues this tool to List all users from the erpsystem using Frappe REST API"""
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


if __name__ == "__main__":
    # x = list_users()
    # print(x)
    mcp.run(transport="streamable-http")