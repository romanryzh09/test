import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

DATABASE_URL = "postgresql+psycopg2://postgres:11062009Ryzhinkov@localhost/lesson"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    hp = Column(Integer, default=100)
    damage = Column(Integer, default=20)








Base.metadata.create_all(engine)
