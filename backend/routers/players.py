from fastapi import APIRouter
from database import get_db_connection
from models.player import PlayerOut

router = APIRouter(prefix="/players")

@router.get("/", response_model=list[PlayerOut])
def get_players(team_id: int | None = None):
    conn = get_db_connection()
    cur = conn.cursor()

    if team_id:
        cur.execute("SELECT * FROM players WHERE team_id = ?", (team_id,))
    else:
        cur.execute("SELECT * FROM players")

    rows = cur.fetchall()
    conn.close()

    return [dict(row) for row in rows]
