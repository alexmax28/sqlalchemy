from sqlalchemy import create_engine, and_, or_
from create_table import Users
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:12345678@192.168.100.210:3306/flask_test")

session = sessionmaker(engine)

db = session()
res = db.query(Users).filter(or_(Users.name == "aaa",Users.name == "bbb")).delete()
print(res)
db.commit()
db.close()
