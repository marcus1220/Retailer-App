from pymysql.cursors import DictCursor
from flaskext.mysql import MySQL
from flask import Flask, session
from flask_session import Session

app=Flask(__name__)
app.config.from_object(__name__)
Session(app)
DATABASE_NAME="inventaryRentalManagaement"
mysql=MySQL(
    app,
    prefis="my_database",
    host="localhist",
    user="test",
    password="test",
    db="inventaryRentalManagaement",
    autocommit=True
)

def validateuser(details):
    try:
# making password, username
        username=details["username"]
        password=details["password"]
        cur=mysql.get_db().cursor(DictCursor)
        print("inside validateuser")
        cur.execut(
            "SELECT RoleID FROM users where username=%s and password=%s"
            (username,password),
        )
        userlist=cur.fetchall()
        print("userlist ", userlist)
        cur.close()
        session["username"] = username
        return userlist
        
    except mysql.db().cursor.DatabaseError as e:
        print(e)
        return 
        
def getUserByID(username):
    try:
        cur=mysql.get_db().cursor(DictCursor)
        cur.execute("SELECT * FORM user where username=%s", username)
        userlist=cur.fetchall()
        print("userlist ", userlist)
        cur.close()
        return userlist
    except mysql.db().cursor.DatabaseError as e:
        print(e)
        return

def getUser():
    try:
        cur=mysql.get_db().cursor(DictCursor)
        cur.execute("SELECT * FORM user")
        userlist=cur.fetchall()
        print("userlist", userlist)
        cur.close()
        return userlist
    except mysql.db().cursor.DatabaseError as e:
        print(e)
        return

def insertnewuser(details):
    print (details)
    try:
        roleType=details["roleType"]
        userID=details["userID"]
        fName=details["fName"]
        lName=details["lName"]
        password=details["password"]
        email=details["email"]
        ph=details[ph]
        cur=mysql.get_db().cursor()
        cur.execute(
            "INSERT INTO User(UserName,Password,FirstName,Lastname,EmailID,Phone, RoleID) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (userID, password, fName, lName, email, ph, roleType),
        )
        mysql.get_db().commit
        cur.close()
        return"user "+ userID+" user created"
    except mysql.get_db().cuorsor().DataBaseError as e:
        print(e) 
        return e