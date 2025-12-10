from pydantic import BaseModel

class EventBase(BaseModel):
    id: int
    match_id: int
    team_id: int
    player_name: str | None = None
    type: str  # goal, yellowcard, redcard, subst, etc.
    minute: int


class EventCreate(BaseModel):
    match_id: int
    team_id: int
    player_name: str | None = None
    type: str
    minute: int


class EventOut(EventBase):
    class Config:
        orm_mode = True
