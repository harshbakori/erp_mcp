from backend.mcp_main import mcp
from backend.tools import list_users
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run(
            host="0.0.0.0", 
            port=8000,
            transport="http",
            middleware=[Middleware(
                                CORSMiddleware,allow_origins=["*"],
                                                allow_credentials=True,
                                                allow_methods=["*"],
                                                allow_headers=["*"]
                            )
                ]
            )