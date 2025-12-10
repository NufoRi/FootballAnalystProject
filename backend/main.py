from fastapi import FastAPI
from backend.routers import teams, matches, players, standings, auth

app = FastAPI()

app.include_router(teams.router)
app.include_router(matches.router)
app.include_router(players.router)
app.include_router(standings.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Premier League Analyst API running"}
