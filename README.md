# Guía de Ejecución de un Proyecto

## Comandos de Ejecución

### Ejecución Básica
El comando genérico para iniciar la aplicación con Uvicorn es:
```bash
uvicorn nombre_archivo:nombre_de_tu_app
```

Para este proyecto en concreto, el comando es:
```bash
uvicorn main:app
```

## Opciones de Configuración

### Cambiar el Puerto
Por defecto, la aplicación corre en el puerto `8000`. Si deseas especificar uno diferente (por ejemplo, el 5000), usa la bandera `--port`:
```bash
uvicorn main:app --port 5000
```

### Modo de Recarga Automática (Reload)
Para que los cambios en el código se reflejen automáticamente sin necesidad de detener y reiniciar el servidor (ideal para desarrollo), añade `--reload`:
```bash
uvicorn main:app --port 5000 --reload
```

### Acceso desde la Red Local
Si quieres permitir que otros dispositivos en la misma red accedan a la aplicación, utiliza la bandera `--host`:
```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

## Documentación de la API

FastAPI genera documentación automática e interactiva para tus endpoints. Puedes acceder a ella a través de tu navegador web:

*   **Si usas el puerto por defecto:**  
    http://localhost:8000/docs

*   **Si usas un puerto personalizado (ej. 5000):**  
    http://localhost:5000/docs
