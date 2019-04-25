#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref=backref("State", cascade="delete"))

    @property
    def cities(self):
        """returns list of city
        instances with
        matching state_id
        """
        cities = models.storage.all(models.City)
        return [c for c in cities.values() if c.state_id == self.id]
