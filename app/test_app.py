from fastapi.testclient import TestClient
from typing import List, Dict

from .app import app

client = TestClient(app)


def test_create_game():
    response = client.get("/start")
    assert response.status_code == 200


def test_check_game():
    response = client.get("/check/5")
    assert response.status_code == 200
    assert response.json() == {"game": "finished", "winner": "X"}


def test_history():
    response = client.get("/history")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_move():
    response = client.post("/move/1", json={"position": 1, "type": "O"})
    assert response.status_code == 200
    assert response.json() == {"message": "game is finished"}


def test_move_2():
    response = client.get("/start")
    assert response.status_code == 200
    response_data = response.json()["message"]
    response_ = client.post(f"/move/{response_data}", json={"position": 0, "type": "O"})
    assert response_.status_code == 200
    assert response_.json() == {"message": "success"}
    response_2 = client.post(
        f"/move/{response_data}", json={"position": 1, "type": "O"}
    )
    assert response_2.status_code == 200
    assert response_2.json() == {"message": "success"}
    response_3 = client.post(
        f"/move/{response_data}", json={"position": 2, "type": "O"}
    )
    assert response_3.status_code == 200
    assert response_3.json() == {"message": "success"}
    response_4 = client.post(
        f"/move/{response_data}", json={"position": 3, "type": "O"}
    )
    assert response_4.status_code == 200
    assert response_4.json() == {"message": "game is finished"}
