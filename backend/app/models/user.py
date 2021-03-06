from sqlalchemy import DateTime, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    username = Column(String(32), index=True)
    password = Column(String(32), nullable=False)
    balance = Column(Float, server_default='0', nullable=False)
    is_admin = Column(Boolean, default=False)
    transactions = relationship('Transaction', backref='user')
    rfid_uuid = Column(String(255))
