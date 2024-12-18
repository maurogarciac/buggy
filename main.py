from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, UUID4, Field
from datetime import datetime


app = FastAPI()

class ElementAttributes(BaseModel):
    element_class: Optional[str] = Field(None,alias="class")
    element_id: Optional[str] = Field(None,alias="id")
    href: Optional[str] = Field(None)
    xmlns: Optional[str] = Field(None)
    fill: Optional[str] = Field(None)
    viewBox: Optional[str] = Field(None) # e.g. "0 0 24 24"
    stroke_width: Optional[float] = Field(None,alias="stroke-width")
    stroke: Optional[str] = Field(None)
    aria_hidden: Optional[bool] = Field(None,alias="aria-hidden")
    data_slot: Optional[str] = Field(None,alias="data-slot")

class EventProperties(BaseModel):
    """ schema for event properties """
    distinct_id: str    # ID único del usuario
    session_id: str     # ID de la sesión
    journey_id: str     # ID del journey
    current_url: str = Field(alias="$current_url")    # URL actual
    host: str = Field(alias="$host")          # Hostname
    pathname: str = Field(alias="$pathname")       # Path de la URL
    browser: str = Field(alias="$browser")        # Navegador usado
    device: str = Field(alias="$device")         # Tipo de dispositivo
    screen_height: int = Field(alias="$screen_height")  # Alto de la pantalla
    screen_width: int = Field(alias="$screen_width")    # Ancho de la pantalla
    eventType: str      # Tipo de evento (ej: "click")
    elementType: str    # Tipo de elemento HTML
    elementText: str    # Texto del elemento
    elementAttributes: Optional[ElementAttributes]  # Atributos del elemento
    timestamp: str      # ISO timestamp
    x: int              # Posición X del evento
    y: int              # Posición Y del evento
    mouseButton: int    # Botón del mouse usado
    ctrlKey: bool       # Si Ctrl estaba presionado
    shiftKey: bool      # Si Shift estaba presionado
    altKey: bool        # Si Alt estaba presionado
    metaKey: bool       # Si Meta estaba presionado 

class Event(BaseModel):
    """ schema for events """
    event: str
    properties: EventProperties
    timestamp: str

class EventList(BaseModel):
    """ schema for event lists """
    events: list[Event]


# POST /api/v1/events
@app.post("/api/v1/events")
def post_events(event_list: EventList):

    print(event_list)
    # Recibe un array de eventos
    # Valida el formato de los eventos
    #Almacena los eventos (puede ser en memoria o en una base de datos de tu elección)

    return {"Hello": "World"}


#GET /api/v1/stories
@app.get("/api/v1/stories")
def get_stories():
    #Retorna las historias de usuario identificadas
    #Permite filtrar por session_id
    return {"story": "value"}


#GET /api/v1/tests
@app.get("/api/v1/tests")
def get_tests():
    #Genera y retorna los tests de Playwright basados en las historias identificadas
    #Permite especificar qué historia convertir a test

    return {"test": "test"}
