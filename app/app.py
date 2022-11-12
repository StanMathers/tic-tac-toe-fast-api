import uvicorn
from fastapi import FastAPI

from .routers import getop, postop

app = FastAPI()



app.include_router(getop.router)
app.include_router(postop.router)

if __name__ == '__main__':
    uvicorn.run(app)

