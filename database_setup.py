from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    discord_username = Column(String(40), nullable=False)
    games = Column(postgresql.ARRAY(String(25), dimensions=4), nullable=True)
    country = Column(String(60), nullable=False)
    
