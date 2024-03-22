#!/usr/bin/python3
"""this module Defines the DBStorage engine."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                environ["HBNB_MYSQL_USER"],
                environ["HBNB_MYSQL_PWD"],
                environ["HBNB_MYSQL_HOST"],
                environ["HBNB_MYSQL_DB"],
            ),
            pool_pre_ping=True,
        )
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        all_objs = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                all_objs[key] = obj
        else:
            classes = [
                State, City, User, Place, Amenity, Review
            ]
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    all_objs[key] = obj
        return all_objs

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()
