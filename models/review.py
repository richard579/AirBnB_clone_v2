#!/usr/bin/python3
"""Review subclass that inherits from BaseModel"""
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """Review class that represents new reviews"""
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
