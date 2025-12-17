from fastapi import APIRouter
from backend.api_client import get_teams

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.get("/")
def teams():
    return get_teams()
