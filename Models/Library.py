from datetime import datetime
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from Models.Base import Base
from Models.AllTime import AllTime
from Models.History import History

class Library(Base):
    __tablename__ = "library"

    id          = Column(Integer, primary_key=True, autoincrement=True) 
    short_name  = Column(String(255), primary_key=True, unique=True)
    long_name   = Column(String(1000))
    lat         = Column(String(255))
    long        = Column(String(255))
    start       = Column(String(255))
    libstart    = Column(String(255))

    alltime     = relationship("AllTime", back_populates="library")
    history     = relationship("History", back_populates="library")

    def __init__(self, data) -> None:
        self.short_name = data['short_name']
        self.long_name = data['long_name']
        self.lat = data['lat']
        self.long = data['long']
        self.start = data['start']
        self.libstart = data['libstart']