from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Games(Base):
    """
    This table represents the game itself identified by its `id`
    """

    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    game_statuses = relationship("GameStatus")
    game_positions = relationship("Positions")


class Status(Base):
    """
    This table represents the status of the game.\n
    1 - in_progress
    2 - finished
    """

    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Player(Base):
    """
    This table represents the players of the game.\n
    1 - O
    2 - X
    3 - null
    """

    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class GameStatus(Base):
    """
    This table represents the status of the game.\n
    Default values are created with `start` method which are\n
    1 (in_progress) for status_id and 3 (null) for winner_player_id
    """

    __tablename__ = "game_status"
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    winner_player_id = Column(Integer, ForeignKey("player.id"), default=3)
    status_id = Column(Integer, ForeignKey("status.id"), default=1)

    status_parent = relationship("Status")
    winner_parent = relationship("Player")


class Positions(Base):
    """
    This table respresents the positions of the game from 0-8.\n
    """

    __tablename__ = "positions"
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    playerer_id = Column(Integer, ForeignKey("player.id"))
    position = Column(Integer)

    game_parent = relationship("Games")

    def __init__(self, game_id: int, playerer_id: int, position: int) -> None:
        self.game_id = game_id
        self.playerer_id = playerer_id
        self.position = position
