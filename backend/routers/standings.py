from fastapi import APIRouter
from api_client import get_standings

router = APIRouter(prefix="/standings")

@router.get("/")
def standings():
    return get_standings()
