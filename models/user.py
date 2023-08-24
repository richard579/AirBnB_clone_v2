#!/usr/bin/python3
"""User subclass that inherits from BaseModel"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """User class to represent new users"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place",
                          cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review",
                           cascade='all, delete, delete-orphan',
                           backref="user")
