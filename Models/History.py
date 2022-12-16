from datetime import datetime
from sqlalchemy import Column, Date, Float, ForeignKey, ForeignKeyConstraint, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from Models.Base import Base

class History(Base):
    __tablename__ = "history"

    id                      = Column(Integer, primary_key=True)
    name                    = Column(String(255), ForeignKey("library.name"), nullable=False)
    total_mill_smileys      = Column(Integer, default=0) 
    no_mill_smiley_earned   = Column(Integer, default=0)  
    active                  = Column(Integer, default=0)      
    issued_qr               = Column(Integer, default=0)
    sold_tablets            = Column(Integer, default=0)
    no_accounts             = Column(Integer, default=0)
    no_delivered_tablets    = Column(Integer, default=0)    
    no1m_acc_rate           = Column(Float, default=0.0)
    sold_delivered_rate     = Column(Float, default=0.0)    
    avail_tablets           = Column(Integer, default=0)
    unused_accounts         = Column(Integer, default=0)
    no_kcse_complete        = Column(Integer, default=0)
    date_of_change          = Column(Date, default=datetime.now())
    
    library                 = relationship("Library", back_populates="history")
    ForeignKeyConstraint(["name"], ["library.name"])


    def __init__(self, data) -> None:
        for field in data:
            setattr(self, field, data[field])