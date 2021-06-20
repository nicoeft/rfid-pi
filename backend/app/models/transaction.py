from sqlalchemy import DateTime, Column, Integer, Float, ForeignKey
from sqlalchemy.sql import func

from app.db.base_class import Base


class Transaction(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(
        Integer,
        ForeignKey('user.id', ondelete='CASCADE'),
        nullable=False,
    )
    provider_id = Column(
        Integer,
        ForeignKey('provider.id', ondelete='CASCADE'),
        nullable=False,
    )
    amount = Column(Float, nullable=False)
