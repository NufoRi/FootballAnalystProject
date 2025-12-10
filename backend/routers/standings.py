from fastapi import APIRouter
from api_client import get_standings

router = APIRouter(prefix="/standings", tags=["Standings"])

@router.get("/")
def standings():
    data = get_standings()
    # Extract relevant standings part
    try:
        standings = data["response"][0]["league"]["standings"][0]
    except:
        return {"error": "Could not parse standings"}

    return standings
