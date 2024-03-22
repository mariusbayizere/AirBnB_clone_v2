#!/usr/bin/python3
"""
Module for Amenity class.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity class that inherits from BaseModel and Base.
    Represents amenities in the database.
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")
