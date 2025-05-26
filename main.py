from mcp.server.fastmcp import FastMCP
import os
import httpx
from typing import Optional, Dict, Any
from dotenv import load_dotenv

load_dotenv()
mcp = FastMCP("Demo")

# Get API key from environment variable
AFFINITY_API_KEY = os.getenv("AFFINITY_API_KEY")
AFFINITY_BASE_URL = "https://api.affinity.co"


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool()
async def get_lists(
    cursor: Optional[str] = None, limit: Optional[int] = 100
) -> Dict[str, Any]:
    """
    Get metadata on all Lists from Affinity API.

    Args:
        cursor: Cursor for the next or previous page
        limit: Number of items to include in the page (1-100, default: 100)

    Returns:
        Dict containing the lists data and pagination info
    """
    if not AFFINITY_API_KEY:
        return {"error": "AFFINITY_API_KEY environment variable is not set"}

    # Validate limit
    if limit is not None:
        if limit < 1 or limit > 100:
            return {"error": "Limit must be between 1 and 100"}

    # Build query parameters
    params = {}
    if cursor:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    # Make the API request
    headers = {
        "Authorization": f"Bearer {AFFINITY_API_KEY}",
        "Accept": "application/json",
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{AFFINITY_BASE_URL}/v2/lists", headers=headers, params=params
            )

            # Check if request was successful
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 400:
                return {"error": "Bad request", "details": response.json()}
            else:
                return {
                    "error": f"API request failed with status {response.status_code}",
                    "details": response.text,
                }

    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"
