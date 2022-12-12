from datetime import datetime
from sqlalchemy import Column, Date, Float, ForeignKey, ForeignKeyConstraint, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from Models.Base import Base

class AllTime(Base):
    __tablename__ = "alltime"

    id                      = Column(Integer, primary_key=True)
    name                    = Column(String(255), nullable=False)
    total_mill_smileys      = Column(Integer) 
    mill_smiley_earned      = Column(Integer)     
    issued_qr               = Column(Integer)
    sold_tablets            = Column(Integer)
    no_accounts             = Column(Integer)
    no_delivered_tablets    = Column(Integer)    
    no1m_acc_rate           = Column(Float)
    sold_delivered_rate     = Column(Float)    
    avail_tablets           = Column(Integer)
    unused_accounts         = Column(Integer)
    no_kcse_complete        = Column(Integer)
    ForeignKeyConstraint(["name"], ["library.name"])
