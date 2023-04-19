#!/usr/bin/python3
""" Defines a City model that inherits from sqlalchemy Base
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base



class City(Base):
    """Represents a city for a MySQL database.
    Attributes:
        id (str): The city's id.
        name (sqlalchemy.String): The city's name.
        state_id (sqlalchemy.Integer): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
