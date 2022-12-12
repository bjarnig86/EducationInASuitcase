from datetime import datetime
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from Models.Base import Base

class Library(Base):
    __tablename__ = "library"

    id      = Column(Integer, primary_key=True) 
    name    = Column(String(255), unique=True)
    lat     = Column(String(255))
    long    = Column(String(255))

