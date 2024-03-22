#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models import storage

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column(
                          'place_id',
                          String(60),
                          ForeignKey('places.id'),
                          primary_key=True,
                          nullable=False
                      ),
                      Column(
                          'amenity_id',
                          String(60),
                          ForeignKey('amenities.id'),
                          primary_key=True,
                          nullable=False
                      )
                      )


class Place(BaseModel, Base):
    """ Place class """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    amenities = relationship(
        'Amenity', secondary=place_amenity, viewonly=False
    )

    if storage_type != 'db':
        @property
        def amenities(self):
            """ Getter attribute amenities """
            from models import amenities
            return [
                amenities.get(amenity_id)
                for amenity_id in self.amenity_ids
            ]

        @amenities.setter
        def amenities(self, obj):
            """ Setter attribute amenities """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
