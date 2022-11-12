from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import HistorySchema
from ..models.game import Games, GameStatus, Positions

router = APIRouter()


@router.get("/start")
def start(db: Session = Depends(get_db)):
    """
    This endpoint start a new game session and returns its identifier.
    """

    """
    This function starts a new game and returns its `id` as a unique game identifier\n
    
    `game` is used to create a new game with autoincremented id and save it in the database\n
    `game_status` is used to create a new game status with autoincremented `game_id` and default values and save it in the database\n
    """
    game = Games()
    db.add(game)
    db.commit()
    db.refresh(game)

    game_status = GameStatus()
    game_status.game_id = game.id
    db.add(game_status)
    db.commit()
    db.refresh(game_status)

    return {"message": game.id}


@router.get("/check/{game_id}")
def check(game_id: int, db: Session = Depends(get_db)):
    """
    This function checks the status of the game and returns the status of the game.\n
    """
    game_status = db.query(GameStatus).filter(GameStatus.game_id == game_id).first()

    # If the game is not finished return in_progress
    if game_status.status_parent.name == "in_progress":
        return {"message": "in_progress"}

    return {"game": "finished", "winner": game_status.winner_parent.name}


@router.get("/history", response_model=List[HistorySchema])
def history(db: Session = Depends(get_db)):
    return db.query(Games).all()
