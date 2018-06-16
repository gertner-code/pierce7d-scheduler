from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from psycopg2.extras import DateTimeRange
from sqlalchemy.dialects.postgresql import TSRANGE
import postgresql

Base = declarative_base()

class User(Base):
    """docstring for user"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    discord_username = Column(String(40), nullable=False)
    games = Column(postgresql.ARRAY(String(40), dimensions=4), nullable=True)
    country = Column(String(60), nullable=False)


class Event(Base):
    """docstring for Event."""
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    time = Column(TSRANGE())  # timestamp range
    comment = Column(String(250), nullable=True)
    game = Column(String(40), nullable=False)
