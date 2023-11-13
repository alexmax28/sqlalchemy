from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

base = declarative_base()

class Users(base):
    __tablename__ ='users'
    id = Column(Integer,primary_key=True)
    name = Column(String(30),index=True)

engine = create_engine("mysql+pymysql://root:12345678@192.168.100.210:3306/flask_test?charset=utf8mb4")

base.metadata.create_all(engine)