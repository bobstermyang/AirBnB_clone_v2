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
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        self.cls = HBNBCommand()
        super().__init__(*args, **kwargs)


    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        def cities(self):
            storage.all('City')
