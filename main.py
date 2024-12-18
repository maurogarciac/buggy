from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Crear los siguientes endpoints:

# POST /api/v1/events

#Recibe un array de eventos
#Valida el formato de los eventos
#Almacena los eventos (puede ser en memoria o en una base de datos de tu elección)

@app.post("/api/v1/events")
def post_events(events: list[Event]):
    return {"Hello": "World"}



#GET /api/v1/stories

#Retorna las historias de usuario identificadas
#Permite filtrar por session_id
@app.get("/api/v1/stories")
def get_stories():
    return {"story": "value"}


#GET /api/v1/tests

#Genera y retorna los tests de Playwright basados en las historias identificadas
#Permite especificar qué historia convertir a test
@app.get("/api/v1/tests")
def get_tests():
    return {"test": "test"}
