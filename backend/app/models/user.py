from api.app.db.base_class import Base
from sqlalchemy import Column, String, DateTime, text, Column, Integer, String, Float
from sqlalchemy.sql import func


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_on =  Column(DateTime(timezone=True), server_default=func.utcnow())
    username = Column(String, index=True)
    password = Column(String, nullable=False)
    balance = Column(Float,default=0,nullable=False)