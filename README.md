# Tic-Tac-Toe API

## Endpoints

```
/start
```

Starts a new session and returns unique game identifier
* {"message": id}

```
/move/{game_id}
```

Takes unique game identifier as a path paramenter and a body request.

* Body request: {"type": type, "position": position}
    * type is either "X" or "O"
    * position is an optional number in the range of 0 to 8

If an error occurs, the response object is {"result": "error", "error_code": "invalid_position"}, else {"result": "success"}

```
/check/{game_id}
```

Takes unique game identifier as a path parameter and returns

* {"game": "finished", "winner": type} if either of player won
* {"game": "finished", "winner": null} if game ended up tie
* {"game": "in_progress"} if game is not finished

```
/history
```

Returns all the positions grouped by game identifier

****For simplicity, you can also check out /docs URL****

# Installation

Step 1:
```
git clone https://github.com/StanMathers/tic-tac-toe-fast-api.git
```

Step 2:

Go into the cloned directory
```
cd .\tic-tac-toe-fast-api\
```

Step 3:

Install dependencies
```
pip install -r requirements.txt
```

# Run

Make sure you are in **...\tic-tac-toe-fast-api** directory.

Run API

```
uvicorn app:app
```

Optionally you can add **--reload** parameter for hot-reloading

```
uvicorn app:app --reload
```

# Run tests

In order to run tests, you need to use **pytest**

Make sure you are in **...\tic-tac-toe-fast-api** directory.

Now run tests

```
pytest .\app\
```

# File structure
* app
    * __init\__.py
    * models/
        * game.py
    * routers/
        * getop.py
        * postop.py
    * app.py
    * database.py
    * schemas.py
    * test_app.py
* migrations/
    ...
* alembic.ini
* sql_app.db

# Short description of files
* app
    * **models/** directory, contains **game.py** where SQLAlchemy models are stored.

    * **routers/** directory, contains get and post operation handlers. **getop.py** (Get request handlers), **postop.py** (Post request handlers)

    * **app.py** is the main file that binds app to routers

    * **database.py** contains a main structure of SQLAlchemy setup for SQLite database

    * **schemas.py** contains Pydantic response models (or model serializers)

    * **test_app** contains simple **pytest** tests for application

* **migrations** is a directory for database migrations used by **alembic**
    * **env.py** contains settings for **--autogenerated** database migrations
* **alembic.ini** contains settings for database migrations
* **sql_app.db** main SQLite database