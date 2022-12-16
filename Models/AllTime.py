from datetime import datetime
from sqlalchemy import Column, Date, Float, ForeignKey, ForeignKeyConstraint, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from Models.Base import Base

class AllTime(Base):
    __tablename__ = "alltime"

    id                      = Column(Integer, primary_key=True)
    total_mill_smileys      = Column(Integer, nullable=False, default=0) 
    no_mill_smiley_earned   = Column(Integer, nullable=False, default=0)
    active                  = Column(Integer, nullable=False, default=0)     
    issued_qr               = Column(Integer, nullable=False, default=0)
    sold_tablets            = Column(Integer, nullable=False, default=0)
    no_accounts             = Column(Integer, nullable=False, default=0)
    no_delivered_tablets    = Column(Integer, nullable=False, default=0)    
    no1m_acc_rate           = Column(Float, nullable=False, default=0)
    sold_delivered_rate     = Column(Float, nullable=False, default=0)    
    avail_tablets           = Column(Integer, nullable=False, default=0)
    unused_accounts         = Column(Integer, nullable=False, default=0)
    no_kcse_complete        = Column(Integer, nullable=False, default=0)

    name                    = Column(String(255), ForeignKey("library.short_name"), nullable=False)
    library                 = relationship("Library", back_populates="alltime")

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
    

