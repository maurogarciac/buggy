from fastapi import FastAPI
from src.model import EventList


app = FastAPI()


# POST /api/v1/events
@app.post("/api/v1/events")
def post_events(event_list: EventList):

    print(event_list.events[0].event)
    # Recibe un array de eventos
    # Valida el formato de los eventos

    # todo save to sqlite-db
    # Almacena los eventos (puede ser en memoria o en una base de datos de tu elección)

    return {"Hello": "World"}


#GET /api/v1/stories
@app.get("/api/v1/stories")
def get_stories():
    # Agrupe eventos relacionados en "historias de usuario"
    # Identifique patrones comunes "login", "busqueda", "checkout"

    # asumo que cuando te envian una lista de eventos, esos van a ser una sola historia de usuario
    # 

    # Retorna las historias de usuario identificadas
    # Permite filtrar por session_id
    return {"story": "value"}


#GET /api/v1/tests
@app.get("/api/v1/tests")
def get_tests():
    # Genera y retorna los tests de Playwright basados en las historias identificadas
    # Permite especificar qué historia convertir a test

    return {"test": "test"}
