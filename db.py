import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
import faker
import random

DATABASE_URL = "postgresql+psycopg2://postgres:11062009Ryzhinkov@localhost/lesson"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

fake = faker.Faker("ru_RU")

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    hp = Column(Integer, default=100)
    damage = Column(Integer, default=20)

class Cats(Base):
    __tablename__ = "cats"
    id = Column(Integer, primary_key= True, nullable= False)
    name = Column(String)
    color = Column(String)

Session = sessionmaker(bind= engine)
s = Session()

# hero = Users(id= 123, name= "Саня Карась")
# s.add(hero)
# s.merge(hero)
# s.commit()

for x in range(1, 400):
    name = fake.first_name()
    obj = Users(id= x, name= name)
    s.merge(obj)
    s.commit()




Base.metadata.create_all(engine)
