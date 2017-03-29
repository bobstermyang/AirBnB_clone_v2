#!/usr/bin/python3
from models import *
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base
import os


class State(BaseModel, Base):
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="State")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        def cities(id, self):
            valid_cities = {}
            state_cities = storage.all("City")
            if id is None or id == "":
                return state_cities
            else:
                for city_id, val_city in state_cities.items():
                    if val_city.state_id == id:
                        valid_cities[city_id] = val_city
                return valid_cities
