#!/usr/bin/python3
"""Definition of DataBase Storage class"""
from os import getenv
from sqlalchemy import create_engine


class DBStorage:
    """DBStorage class for database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """__init__ method for DBStorage class"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
        .format(getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """All method for DBStorage class"""
        