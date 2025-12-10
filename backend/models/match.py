from pydantic import BaseModel

class MatchBase(BaseModel):
    id: int
    home_team: int
    away_team: int
    date: str
    status: str | None = None
    home_goals: int | None = 0
    away_goals: int | None = 0


class MatchCreate(BaseModel):
    home_team: int
    away_team: int
    date: str
    status: str | None = None
    home_goals: int | None = 0
    away_goals: int | None = 0


class MatchOut(MatchBase):
    class Config:
        orm_mode = True
