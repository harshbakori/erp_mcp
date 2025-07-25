from fastmcp import FastMCP
from starlette.requests import Request as StarletteRequest
from starlette.responses import JSONResponse
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.dependencies import get_access_token, AccessToken
from config import STYTCH_PROJECT_ID, STYTCH_DOMAIN, STYTCH_API_SECRET
# from jose import jwt
import os

auth = BearerAuthProvider(
    jwks_uri=f"{STYTCH_DOMAIN}/.well-known/jwks.json",
    issuer=STYTCH_DOMAIN,
    algorithm="RS256",
    audience=STYTCH_PROJECT_ID
)

mcp = FastMCP(name="mcp",auth=auth)

@mcp.custom_route("/.well-known/oauth-protected-resource", methods=["GET", "OPTIONS"])
def oauth_metadata(request: StarletteRequest) -> JSONResponse:
    base_url = str(request.base_url).rstrip("/")

    return JSONResponse(
        {
            "resource": base_url,
            "authorization_servers": [STYTCH_DOMAIN],
            "scopes_supported": ["read", "write"],
            "bearer_methods_supported": ["header", "body"]
        }
    )

