from fastapi import APIRouter
from backend.api_client import get_top_scorers, get_top_assisters, get_star_performers

router = APIRouter(prefix="/players", tags=["Players"])

@router.get("/topscorers")
def top_scorers():
    return get_top_scorers()

@router.get("/topassists")
def top_assists():
    return get_top_assisters()

@router.get("/star-performers")
def star_performers():
    return get_star_performers()
