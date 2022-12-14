from datetime import datetime
from sqlalchemy import Column, Date, Float, ForeignKey, ForeignKeyConstraint, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from Models.Base import Base

class History(Base):
    __tablename__ = "history"

    id                      = Column(Integer, primary_key=True)
    name                    = Column(String(255), nullable=False)
    total_mill_smileys      = Column(Integer) 
    no_mill_smiley_earned   = Column(Integer)  
    active                  = Column(Integer)      
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


    def __init__(self, data) -> None:
        self.name = data["name"]
        self.total_mill_smileys = data["total_mill_smileys"]
        self.no_mill_smiley_earned = data["no_mill_smiley_earned"]
        self.active = data["active"]
        self.issued_qr = data["issued_qr"]
        self.sold_tablets = data["sold_tablets"]
        self.no_accounts = data["no_accounts"]
        self.no_delivered_tablets = data["no_delivered_tablets"]
        self.no1m_acc_rate = data["no1m_acc_rate"]
        self.sold_delivered_rate = data["sold_delivered_rate"]
        self.avail_tablets = data["avail_tablets"]
        self.unused_accounts = data["unused_accounts"]
        self.no_kcse_complete = data["no_kcse_complete"]
