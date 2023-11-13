from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create_table import Users

engine = create_engine("mysql+pymysql://root:12345678@192.168.100.210:3306/flask_test")

session = sessionmaker(engine)
db_session = session()

res = db_session.query(Users).filter(Users.name =="Alex").update({"name":"alex"})

db_session.commit()
db_session.close()