from pydantic import BaseModel
from typing import Literal, List

PLAYERS: List[str] = Literal['X', 'O']
POSITIONS: List[int] = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]

class PositionsSchema(BaseModel):
    type: PLAYERS
    position: POSITIONS
