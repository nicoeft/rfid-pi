from sqlalchemy import DateTime, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class Provider(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String(32), index=True)
    balance = Column(Float, server_default='0', nullable=False)
    payment_amount = Column(Float, server_default='0', nullable=False)
    is_active = Column(Boolean, default=False)
    transactions = relationship('Transaction',backref='provider')
