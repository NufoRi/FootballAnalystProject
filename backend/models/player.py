from pydantic import BaseModel

class PlayerBase(BaseModel):
    id: int
    team_id: int
    name: str
    position: str | None = None
    age: int | None = None


class PlayerCreate(BaseModel):
    team_id: int
    name: str
    position: str | None = None
    age: int | None = None


class PlayerOut(PlayerBase):
    class Config:
        orm_mode = True
