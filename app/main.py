from fastapi import FastAPI
from api import movies_api
from api.movies_api import get_movies

app = FastAPI()

app.include_router(movies_api.router, prefix="/api/movies", tags=["Movies"])