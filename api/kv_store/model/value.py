import logging

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

Base = declarative_base()

class Value(Base):
    __tablename__ = 'value'

    key = Column(String, primary_key=True)
    value = Column(String, nullable=False)
