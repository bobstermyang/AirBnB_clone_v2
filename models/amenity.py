#!/usr/bin/python3
from models import *
from models.base_model import BaseModel, Base, Column, String, Table
import os


class Amenity(BaseModel, Base):
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
