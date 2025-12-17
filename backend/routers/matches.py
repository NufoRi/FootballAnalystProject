from fastapi import APIRouter
from backend.api_client import get_matches

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.get("/")
def matches():
    return get_matches()
