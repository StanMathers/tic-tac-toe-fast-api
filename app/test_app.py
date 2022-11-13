from fastapi.testclient import TestClient
from typing import List, Dict

from .app import app

client = TestClient(app)


def test_create_game():
    response = client.get("/start")
    assert response.status_code == 200


def test_check_game():
    response = client.get("/check/5")
    assert response.status_code == 201
    assert response.json() == {"game": "finished", "winner": "X"}


def test_history():
    response = client.get("/history")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_move():
    """
    Test a move already on a finished game. It must return a 400 error since it's finished.
    """
    response = client.post("/move/1", json={"position": 1, "type": "O"})
    assert response.status_code == 400
    assert response.json() == {"message": "game is finished"}


def test_move_2():
    """
    Test a move on a new game.\n
    
    `response`\n
    It must return a 201 status code and a success message when starting new game.\n

    `response_` makes a move in a new game\n
    `response_2` makea a move in a new game\n
    `response_3` makea a move in a new game\n
    All the 3 responses, must return 201 status code and a success message\n
    
    `response_4` makea a move in a new game, it must return 400 bad request and message that game is finished\n
    
    """
    # Starting a new game
    response = client.get("/start")
    assert response.status_code == 201
    
    response_data = response.json()["message"]
    
    # Making a move in a new game
    response_ = client.post(f"/move/{response_data}", json={"position": 0, "type": "O"})
    assert response_.status_code == 201
    assert response_.json() == {"message": "success"}
    
    # Making a move in a new game
    response_2 = client.post(
        f"/move/{response_data}", json={"position": 1, "type": "O"}
    )
    assert response_2.status_code == 200
    assert response_2.json() == {"message": "success"}
    
    # Making a move in a new game
    response_3 = client.post(
        f"/move/{response_data}", json={"position": 2, "type": "O"}
    )
    assert response_3.status_code == 200
    assert response_3.json() == {"message": "success"}
    
    # Making a move in a new game
    response_4 = client.post(
        f"/move/{response_data}", json={"position": 3, "type": "O"}
    )
    assert response_4.status_code == 400
    assert response_4.json() == {"message": "game is finished"}
