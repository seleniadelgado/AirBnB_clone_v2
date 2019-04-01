#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    state_id = ""
    name = ""
    __tablename__ = "cities"
    name = Column(string(128), nullable=False),
    state_id = Column(string(60), ForeignKey("states.id"), nullable=False)
    """"""