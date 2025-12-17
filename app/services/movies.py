# app/services
# Script para hacer la lógica de los servicios de la aplicación de películas


from typing import List
from typing import Dict
from json import load
from core.config import config 



class MoviesService:
    
    def query(self) -> List[Dict]:
        """
        Método para retornar toda las peliculas que están en el Json

        Args:
            data (List[Dict]): Lista de diccionarios con la información de las películas

        Returns:
            data (List[Dict]): Lista de diccionarios con la información de las películas
        """

        with open(config.pathJSON()) as file:
            data = load(file)

        return data

movies = MoviesService()