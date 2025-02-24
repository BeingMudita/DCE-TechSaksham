import mysql.connector

import os
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
try:
    con = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_NAME)
    cur = con.cursor()
    cur.execute("Show databases;")
    print(cur.fetchall())
    con.close()
except Exception as e:
    print(e)

def signup(data):
    try:
        con = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_NAME)
        cur = con.cursor()
        cur.execute(f"select * from student_record where roll = {data[0]}")
        if cur.fetchone():
            con.close()
            return False
        else:
            myquery = "INSERT INTO student_record (roll, name, password, branch, admission_year, percentage_10th, percentage_12) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(myquery, data)
            con.commit()
            con.close()
            return True
    except Exception as e:
        print(e)

def signin(data):
    try:
        con = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_NAME)
        cur = con.cursor()
        cur.execute(f"select * from student_record where roll = {data[0]}")
        result = cur.fetchone()
        if result!= None and result[0] == data[0] and result[2] == data[1]:
            con.close()
            return True
        else:
            con.close()
            return False
    except Exception as e:
        print(e)

def search (roll):
    try:
        con = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_NAME)
        cur = con.cursor()
        cur.execute(f"select roll, name, branch, admission_year, percentage_10th, percentage_12 from student_record where roll = {roll}")
        result = cur.fetchone()
        if result!= None:
            con.close()
            return result
        else:
            con.close()
            return ()
    except Exception as e:
        print(e)

def displayAll():
    try:
        con = mysql.connector.connect(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_NAME)
        cur = con.cursor()
        cur.execute(f"select roll, name, branch, admission_year, percentage_10th, percentage_12 from student_record")
        result = cur.fetchall()
        return result
    except Exception as e:
        print(e)


    
print("*" * 45 + "Welcome to DCE Data Analysis" + "*" * 45)
while True:
    print("\n1. Signin \n2. Signup \n3. Search \n4. Display all records \n5. Exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        roll = int(input("Enter your Roll Number:"))
        password = input("Enter your Password:")
        if signin((roll, password)):
            print("Login Successfull")
        else:
            print("Invalid Roll Number or Password")

    elif ch == 2:
        roll = int(input("Enter your Roll Number:"))
        name = input("Enter your Name:")    
        password = input("Enter your Password:")
        branch = input("Enter your Branch:")
        admission_year = input("Enter your Addmission year:")
        percentage_10th = int(input("Enter your 10th percentage:"))
        percentage_12 = int(input("Enter your 12th percentage:"))
        if signup((roll, name, password, branch, admission_year, percentage_10th, percentage_12)):
            print("Signup successful")
        else:
            print("Signup failed")

    elif ch == 3:
        roll = int(input("Enter the Roll Number of the student you want to search:"))
        info = search(roll)
        print(info)
        
    elif ch ==4:
        all = displayAll()
        for i in all :
            print(f"Rollno: {i[0]}\n Name: {i[1]}\n Branch: {i[2]}\n Admission Year: {i[3]}\n 10th Percentage: {i[4]}\n 12th Percentage: {i[5]}")
    elif ch ==5:
        break
    else:
        print("wrong choice!")