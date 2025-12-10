from pydantic import BaseModel

class TeamBase(BaseModel):
    id: int
    name: str
    logo: str | None = None


class TeamCreate(BaseModel):
    name: str
    logo: str | None = None


class TeamOut(TeamBase):
    class Config:
        orm_mode = True
