from create_table import Users
from create_table import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:12345678@192.168.100.210:3306/flask_test")
# 建立會話
session = sessionmaker(engine)
# 開啟db會話
db_session = session()
# 新增user資料
user_obj = Users(name = "bbb")
db_session.add(user_obj)
# 提交會話裡的所有操作
db_session.commit()
# 關閉會話
db_session.close()