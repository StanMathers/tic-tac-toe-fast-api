from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import PositionsSchema
from ..models.game import *

router = APIRouter()


def check_for_win_by_id(data: list, id: int) -> int:
    """
    This function takes list of SQLAlchemy objects and checks if there is a winner. If there is a winner, then it returns the winner player id\n
    """
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    p1 = [x.position for x in list(filter(lambda x: x.playerer_id == id, data))]

    for i in win_combinations:
        if p1 == i:
            return id


def check_for_tie(game_id: int, db: Session = Depends(get_db)) -> None:
    """
    This function checks if there is a tie in the game.

    If the number of positions is equal to 9 while there is no winner, then it is a tie.
    """
    data = db.query(Positions).filter(Positions.game_id == game_id).all()
    status = db.query(GameStatus).filter(GameStatus.game_id == game_id).first()

    if len(data) == 9 and status != "finished":
        status.status_id = 2
        db.commit()
        db.refresh(status)


@router.post("/move/{game_id}")
def move(
    game_id: int,
    play_body: PositionsSchema,
    response: Response,
    db: Session = Depends(get_db),
):
    # For docs
    """
    This endpoint receives a `game identifier` and a body request with `type` and `position` where `type` is X or O and `position` is a number from 0 to 8\n
    """

    """
    This function receives a `game_id`, `type` and a `position` and returns a `status` of the game.\n

    `get_chosen_position` is used to check if the position is already chosen. If it's not chosen, then it returns None\n
    `get_id_for_player` is used to get the id of the player. If the player is not valid, then it returns None\n
    `get_game_status` is used to check if the game is already finished or still in process. If it's in progress, then data is saved\n

    """

    get_chosen_position = (
        db.query(Positions)
        .filter(Positions.position == play_body.position, Positions.game_id == game_id)
        .first()
    )
    get_id_for_player = (
        db.query(Player).filter(Player.name == play_body.type).first().id
    )
    get_game_status = (
        db.query(GameStatus)
        .filter(GameStatus.game_id == game_id)
        .first()
        .status_parent.name
    )

    # If game is finished, return that the game is finished and do not continue
    if get_game_status == "finished":
        response.status_code = 400
        return {"message": "game is finished"}

    # If the chosen position is not in the database, then proceed
    if get_chosen_position is None:

        position = Positions(
            game_id=game_id, playerer_id=get_id_for_player, position=play_body.position
        )

        db.add(position)
        db.commit()
        db.refresh(position)

        # Check if there is a winner and change game status
        data = db.query(Positions).filter(Positions.game_id == game_id).all()

        if check_for_win_by_id(data, get_id_for_player):
            game_status = (
                db.query(GameStatus).filter(GameStatus.game_id == game_id).first()
            )
            game_status.status_id = 2
            game_status.winner_player_id = get_id_for_player
            db.commit()
            db.refresh(game_status)

        check_for_tie(game_id, db)
        response.status_code = 201
        return {"message": "success"}

    # If the chosen position is already in the database, then return that the position is invalid
    response.status_code = 400
    return {"result": "error", "error_code": "invalid_position"}
