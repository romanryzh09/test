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

class Enemies(Base):
    __tablename__ = "enemies"
    id = Column(Integer, primary_key= True, nullable= False)
    name = Column(String)
    hp = Column(Integer, default= 90)
    damage = Column(Integer, default= 15)

Session = sessionmaker(bind= engine)
s = Session()

# enem = Enemies(id= 101, name= "Окунь")
# enem1 = Enemies(id= 102, name= "Сом")
# s.merge(enem)
# s.merge(enem1)
# s.commit()

# hero = Users(id= 123, name= "Саня Карась")
# s.add(hero)
# s.merge(hero)
# s.commit()

# hero1 = Users(id= 400, name= "Палыч Шиномонтаж")
# hero2 = Users(id= 401, name= "Саныч Окунь")
# hero3 = Users(id= 402, name= "Сергеич Кедровый")
# hero4 = Users(id= 403, name= "Олегыч Бутылка")
# hero5 = Users(id= 404, name= "Дмитрич Резина")
# s.merge(hero1)
# s.merge(hero2)
# s.merge(hero3)
# s.merge(hero4)
# s.merge(hero5)
# s.commit()

# clients_a = s.query(Users).filter(Users.name.startswith("А"), Users.id > 300)
# for user in clients_a:
#     print(f"ID: {user.id}, name: {user.name}")

# s.query(Users).filter(Users.id == 401).update({"name": "Дмитрич Карась"})
# s.commit()

# s.query(Users).filter(Users.id == 333).delete()
# s.commit()

# s.query(Users).filter(Users.id <= 200).delete()
# s.commit()

s.query(Users).filter(Users.id % 2 == 0).update({"name": "Jackie Chan"})
s.commit()

# for x in range(1, 400):
#     name = fake.first_name()
#     obj = Users(id= x, name= name)
#     s.merge(obj)
#     s.commit()


data = s.query(Users).all()
# print(data)

# print(data[0].name)

# for user in data:
#     print(user.name)

Base.metadata.create_all(engine)
