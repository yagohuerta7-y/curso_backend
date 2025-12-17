# app/schemas


from pydantic import BaseModel


# Clase para el schema de lsitado de peliculas
class listMovies(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str