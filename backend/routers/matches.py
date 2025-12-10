from fastapi import APIRouter
from backend.database import get_db_connection
from backend.models.match import MatchOut

router = APIRouter(prefix="/matches")

@router.get("/", response_model=list[MatchOut])
def get_matches(team_id: int | None = None):
    conn = get_db_connection()
    cur = conn.cursor()

    if team_id:
        cur.execute("""
            SELECT * FROM matches 
            WHERE home_team = ? OR away_team = ?
        """, (team_id, team_id))
    else:
        cur.execute("SELECT * FROM matches")

    rows = cur.fetchall()
    conn.close()

    return [dict(row) for row in rows]
