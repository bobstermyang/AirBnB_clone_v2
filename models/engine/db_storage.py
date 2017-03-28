#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.base_model import BaseModel
from models.base_model import Base
from models.place import Place, PlaceAmenity
from models.review import Review
from models.user import User
from sqlalchemy.orm.scoping import scoped_session
import os


class DBStorage:
    __engine = None
    __session = None

    valid_classes = {"Amenity": Amenity, "City": City, "State": State,
                     "Place": Place, "Review": Review,
                     "User": User, "PlaceAmenity": PlaceAmenity}

    def __init__(self):
        mysql_usr = os.getenv('HBNB_MYSQL_USER')
        mysql_pwd = os.getenv('HBNB_MYSQL_PWD')
        mysql_host = os.getenv('HBNB_MYSQL_HOST')
        mysql_db = os.getenv('HBNB_MYSQL_DB')
        mysql_env = os.getenv('HBNB_MYSQL_ENV')

        eng_str = "mysql+mysqldb://{}:{}@{}/{}".format(mysql_usr,
                                                       mysql_pwd,
                                                       mysql_host,
                                                       mysql_db)

        self.__engine = create_engine(eng_str)
        Session = sessionmaker(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = Session()
        if mysql_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        query_info = {}
        if cls is None:
            for val_key, val_cls in self.valid_classes.items():
                for instance in self.__session.query(val_cls):
                    query_info[instance.id] = instance
        else:
            for instance in self.__session.query(cls):
                query_info[instance.id] = instance
        return query_info

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        self.__session.remove()

    def reload(self):
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
        Base.metadata.create_all(self.__engine)
