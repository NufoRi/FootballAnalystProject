from fastapi import APIRouter
from backend.database import get_db_connection
from backend.models.team import TeamOut

router = APIRouter(prefix="/teams")

@router.get("/", response_model=list[TeamOut])
def get_teams():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM teams")
    rows = cur.fetchall()
    conn.close()

    return [dict(row) for row in rows]
