from os import getenv
from dotenv import load_dotenv

load_dotenv()   

base_url = getenv("FRAPPE_BASE_URL")
api_key = getenv("FRAPPE_API_KEY")
api_secret = getenv("FRAPPE_API_SECRET")

STYTCH_PROJECT_ID= getenv("STYTCH_PROJECT_ID")
STYTCH_DOMAIN= getenv("STYTCH_DOMAIN")
STYTCH_API_SECRET= getenv("STYTCH_API_SECRET")