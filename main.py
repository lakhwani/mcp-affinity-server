from mcp.server.fastmcp import FastMCP
import os
import httpx
from typing import Optional, Dict, Any, List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mcp = FastMCP("Affinity")

# Get API key from environment variable
AFFINITY_API_KEY = os.getenv("AFFINITY_API_KEY")
AFFINITY_BASE_URL = "https://api.affinity.co"


async def _make_affinity_request(
    endpoint: str, params: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Helper function to make requests to Affinity API"""
    if not AFFINITY_API_KEY:
        return {"error": "AFFINITY_API_KEY environment variable is not set"}

    headers = {
        "Authorization": f"Bearer {AFFINITY_API_KEY}",
        "Accept": "application/json",
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{AFFINITY_BASE_URL}{endpoint}", headers=headers, params=params
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 400:
                return {"error": "Bad request", "details": response.json()}
            elif response.status_code == 403:
                return {
                    "error": "Forbidden - check permissions",
                    "details": response.json(),
                }
            else:
                return {
                    "error": f"API request failed with status {response.status_code}",
                    "details": response.text,
                }

    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}


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
    if limit is not None and (limit < 1 or limit > 100):
        return {"error": "Limit must be between 1 and 100"}

    params = {}
    if cursor:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    return await _make_affinity_request("/v2/lists", params)


@mcp.tool()
async def get_companies(
    cursor: Optional[str] = None,
    limit: Optional[int] = 100,
    ids: Optional[List[int]] = None,
    field_ids: Optional[List[str]] = None,
    field_types: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Get all Companies from Affinity API.

    Requires the "Export All Organizations directory" permission.

    Args:
        cursor: Cursor for the next or previous page
        limit: Number of items to include in the page (1-100, default: 100)
        ids: Company IDs to filter by
        field_ids: Field IDs for which to return field data
        field_types: Field Types for which to return field data ("enriched", "global", "relationship-intelligence")

    Returns:
        Dict containing companies data and pagination info
    """
    if limit is not None and (limit < 1 or limit > 100):
        return {"error": "Limit must be between 1 and 100"}

    params = {}
    if cursor:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    # Handle array parameters
    if ids:
        for id_val in ids:
            params.setdefault("ids", []).append(id_val)
    if field_ids:
        for field_id in field_ids:
            params.setdefault("fieldIds", []).append(field_id)
    if field_types:
        valid_types = ["enriched", "global", "relationship-intelligence"]
        for field_type in field_types:
            if field_type not in valid_types:
                return {
                    "error": f"Invalid field_type: {field_type}. Must be one of {valid_types}"
                }
            params.setdefault("fieldTypes", []).append(field_type)

    return await _make_affinity_request("/v2/companies", params)


@mcp.tool()
async def get_company_fields(
    cursor: Optional[str] = None, limit: Optional[int] = 100
) -> Dict[str, Any]:
    """
    Get metadata on Company Fields from Affinity API.

    Use the returned Field IDs to request field data from the companies endpoints.

    Args:
        cursor: Cursor for the next or previous page
        limit: Number of items to include in the page (1-100, default: 100)

    Returns:
        Dict containing field metadata and pagination info
    """
    if limit is not None and (limit < 1 or limit > 100):
        return {"error": "Limit must be between 1 and 100"}

    params = {}
    if cursor:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    return await _make_affinity_request("/v2/companies/fields", params)


@mcp.tool()
async def get_persons(
    cursor: Optional[str] = None,
    limit: Optional[int] = 100,
    ids: Optional[List[int]] = None,
    field_ids: Optional[List[str]] = None,
    field_types: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Get all Persons from Affinity API.

    Requires the "Export All People directory" permission.

    Args:
        cursor: Cursor for the next or previous page
        limit: Number of items to include in the page (1-100, default: 100)
        ids: Person IDs to filter by
        field_ids: Field IDs for which to return field data
        field_types: Field Types for which to return field data ("enriched", "global", "relationship-intelligence")

    Returns:
        Dict containing persons data and pagination info
    """
    if limit is not None and (limit < 1 or limit > 100):
        return {"error": "Limit must be between 1 and 100"}

    params = {}
    if cursor:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    # Handle array parameters
    if ids:
        for id_val in ids:
            params.setdefault("ids", []).append(id_val)
    if field_ids:
        for field_id in field_ids:
            params.setdefault("fieldIds", []).append(field_id)
    if field_types:
        valid_types = ["enriched", "global", "relationship-intelligence"]
        for field_type in field_types:
            if field_type not in valid_types:
                return {
                    "error": f"Invalid field_type: {field_type}. Must be one of {valid_types}"
                }
            params.setdefault("fieldTypes", []).append(field_type)

    return await _make_affinity_request("/v2/persons", params)


@mcp.tool()
async def get_person_fields(
    cursor: Optional[str] = None, limit: Optional[int] = 100
) -> Dict[str, Any]:
    """
    Get metadata on Person Fields from Affinity API.

    Use the returned Field IDs to request field data from the persons endpoints.

    Args:
        cursor: Cursor for the next or previous page
        limit: Number of items to include in the page (1-100, default: 100)

    Returns:
        Dict containing field metadata and pagination info
    """
    if limit is not None and (limit < 1 or limit > 100):
        return {"error": "Limit must be between 1 and 100"}

    params = {}
    if cursor:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    return await _make_affinity_request("/v2/persons/fields", params)
