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

    @property
    def serialize(self):
        """Return object data in easily readable format."""
        return {
            'id': self.id,
            'email': self.email,
            'discord_username': self.discord_username,
            'games': self.games,
            'country': self.country,
        }


class Event(Base):
    """docstring for Event."""
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    time = Column(TSRANGE())  # timestamp range
    comment = Column(String(250), nullable=True)
    game = Column(String(40), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily readable format."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'time': self.time,
            'comment': self.comment,
            'game': self.game,
        }


class Image(Base):
    """Stores names of all uploaded images."""
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    image_name = Column(String(50), nullable=False)


engine = create_engine('postgresql://pierce7d.db')


Base.metadata.create_all(engine)
