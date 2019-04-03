#!/usr/bin/python3
"""This is the place class"""
import models
from models.amenity import Amenity
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", cascade="all, delete", backref="place")
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))
    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Reviews getter for class attribute reviews"""
            return self.reviews

        @property
        def amenities(self):
            """Returns value of amenities collection"""
            retList = []
            objAm = models.storage.all(Amenity)
            for id, key in (self.amenity_ids, objAm):
                if id in key:
                    retList.append(objAm[key])
            return retList

        @amenities.setter
        def amenities(self, obj):
            """amenity_ids setter handles id append"""
            if type(obj).__name__ == Amenity:
                self.amenity_ids.append(obj.id)
