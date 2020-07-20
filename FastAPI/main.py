from fastapi import FastAPI
import pymysql

app = FastAPI()

db = pymysql.connect("192.168.39.104", "root", "5555", "test")
cursor = db.cursor()

@app.get('/')
def root():
    return {"Message":"Hello World!"}

@app.get('/gender')
def genderFunc(gender:str = 'F'):
    sql = "select * from employees where gender = {};".format(gender)
    cursor.execute(sql)
    dataList = cursor.fetchall()
    Info = {}
    num = 1
    for data in dataList:
        Info[num] = {"emp_no":data[0],"birth_date":data[1],"first_name":data[2],"last_name":data[3],"gender":data[4],"hire_data":data[5]}
        num = num + 1
    return  Info
    
