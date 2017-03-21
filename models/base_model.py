#!/usr/bin/python3
import datetime
import uuid
import models
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """The base class for all storage objects in this project"""
    #grab env variable
    #if 'db' do

    def __init__(self, *args, **kwargs):
        """initialize class object"""
        self.created_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        for name, val in kwargs.items():
            setattr(self, name, val)

    def save(self):
        """method to update self"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        if ("updated_at" in dupe):
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe
