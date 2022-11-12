from pydantic import BaseModel
from typing import Literal, List

PLAYERS: List[str] = Literal["X", "O"]
POSITIONS: List[int] = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]


class PositionsSchema(BaseModel):
    type: PLAYERS
    position: POSITIONS


class PositionSchema(BaseModel):
    id: int
    playerer_id: int
    position: int

    class Config:
        orm_mode = True


class HistorySchema(BaseModel):
    id: int
    game_positions: List[PositionSchema]

    class Config:
        orm_mode = True
