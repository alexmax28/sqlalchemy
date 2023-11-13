from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, or_, and_
from create_table import Users

engine = create_engine("mysql+pymysql://root:12345678@192.168.100.210:3306/flask_test")

session = sessionmaker(engine)
db_session = session()
# # 撈全部
# user_list = db_session.query(Users).all()
# for i in user_list:
#     print(i.name)
# print(user_list)

# # 撈條件
# user_list = db_session.query(Users).filter(Users.name == 'jason').first()
# print(user_list.name)


# # 撈條件 or_
# user_list = db_session.query(Users).filter(or_(Users.name == "alex",Users.name == "alan")).all()
# for i in user_list:
#     print(i.name)

# 撈條件 and_
user_list = db_session.query(Users).filter(and_(Users.name == "alex",Users.id == 1)).all()
for i in user_list:
    print(i.name)