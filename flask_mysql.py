
# main.py
import pymysql
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request

# from sqlalchemy import create_engine
 
# db = SQLAlchemy()
 
app = Flask(__name__)
 
db = pymysql.connect(host=f'192.168.100.210',
                     user=f'root',
                     password=f'12345678',
                     database=f'flask_test')

sqlcursor = db.cursor()

@app.route('/add',methods=["POST"])
def add():
    data = {
        "name":request.json["name"],
        "email":request.json["email"],
        "password":request.json["password"]
    }
 
    sql_cmd = f"""
        INSERT INTO users (name,email,password)
        VALUES ('{data["name"]}','{data["email"]}','{data["password"]}');
        """
    print(sql_cmd)
    
    sqlcursor.execute(sql_cmd)
    db.commit()
    
    return 'ok'
 
 
if __name__ == "__main__":
    app.run()