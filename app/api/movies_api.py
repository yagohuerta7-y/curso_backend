from typing import List
from schemas.movies_schemas import listMovies

from services.movies import movies

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status


router = APIRouter()


@router.get("/movies", tags=['Movies'], response_model=List[listMovies])
def get_movies() -> List[listMovies]:
    """
    Endpoint para ver todas las películas que tenemos
    """

    return movies.query()