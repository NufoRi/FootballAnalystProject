from fastapi import APIRouter
from backend.api_client import get_standings

router = APIRouter(prefix="/standings", tags=["Standings"])

@router.get("/")
def standings():
    data = get_standings()

    try:
        table = data["response"][0]["league"]["standings"][0]
        return table
    except Exception as e:
        return {
            "error": "Could not parse standings",
            "details": str(e),
            "raw": data
        }
