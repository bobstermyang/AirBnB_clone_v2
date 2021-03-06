#!/usr/bin/python3
from models import *
import models
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
        @property
        def cities(self):
            valid_cities = []
            state_cities = models.storage.all("City")
            for city_id, val_city in state_cities.items():
                if val_city.state_id == self.id:
                    valid_cities.append(val_city)
            return valid_cities
