from typing import Optional
from pydantic import BaseModel, UUID4, Field
from datetime import datetime

from sqlalchemy import Column, Integer, String
from database import base


class ElementAttributes(BaseModel):
    """ schema for the affected element's attributes """
    element_class: Optional[str] = Field(None,alias="class")
    element_id: Optional[str] = Field(None,alias="id")
    href: Optional[str] = Field(None)
    xmlns: Optional[str] = Field(None)
    fill: Optional[str] = Field(None)
    viewBox: Optional[str] = Field(None)                            # e.g. "0 0 24 24"
    stroke_width: Optional[float] = Field(None,alias="stroke-width")
    stroke: Optional[str] = Field(None)
    aria_hidden: Optional[bool] = Field(None,alias="aria-hidden")
    data_slot: Optional[str] = Field(None,alias="data-slot")


class EventProperties(BaseModel):
    """ schema for event properties """
    distinct_id: UUID4                                              # UUIDv4 único del usuario (microsoft GUID)
    session_id: UUID4                                               # UUIDv4 de la sesión (microsoft GUID)
    journey_id: UUID4                                               # UUIDv4 del journey (reserved)
    current_url: str = Field(alias="$current_url")                  # URL actual
    host: str = Field(alias="$host")                                # Hostname
    pathname: str = Field(alias="$pathname")                        # Path de la URL
    browser: str = Field(alias="$browser")                          # Navegador usado
    device: str = Field(alias="$device")                            # Tipo de dispositivo
    screen_height: int = Field(alias="$screen_height")              # Alto de la pantalla
    screen_width: int = Field(alias="$screen_width")                # Ancho de la pantalla
    eventType: str                                                  # Tipo de evento (ej: "click")
    elementType: str                                                # Tipo de elemento HTML
    elementText: str                                                # Texto del elemento
    elementAttributes: Optional[ElementAttributes] = Field(None)    # Atributos del elemento
    timestamp: datetime                                             # ISO timestamp
    x: int                                                          # Posición X del evento
    y: int                                                          # Posición Y del evento
    mouseButton: int                                                # Botón del mouse usado
    ctrlKey: bool                                                   # Si Ctrl esta presionado
    shiftKey: bool                                                  # Si Shift esta presionado
    altKey: bool                                                    # Si Alt esta presionado
    metaKey: bool                                                   # Si Meta esta presionado


class Event(BaseModel):
    """ schema for events """
    event: str                                                      # Tipo de evento (ej: "$click")
    properties: EventProperties
    timestamp: datetime                                             # ISO timestamp del evento


class EventList(BaseModel):
    """ schema for a list of events """
    events: list[Event]


class Event(Base):
    __tablename__ = "events"

    event: Column()                                                      # Tipo de evento (ej: "$click")
    properties: EventProperties
    timestamp: datetime                                             # ISO timestamp del evento

