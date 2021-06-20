from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
