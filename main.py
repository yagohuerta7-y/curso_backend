# Importamos FastAPI
from fastapi import FastAPI

# Creamos una instancia de FastAPI
app = FastAPI()

# Creamos con el decorador una ruta básica usando el método 'get' que vaya al root de la aplicación
@app.get("/")
def home():
    return "Hola mundo!" # Esta función se va a ejecutar al acceder a la ruta root


# Para ejecutar es con este comando (de manera genérica):
# uvicorn nombre_archivo:nombre_de_tu_app
# En este ejemplo, sería:
# uvicorn main:app