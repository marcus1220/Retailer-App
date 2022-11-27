from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(
    app,
    prefis = "my_datebase",
    host = "localhost",
    user = "test",
    password = "test",
    db = "inventary rental mangement",
)
def getequipments():
    try:
        cur = mysql.get_db().cuorsor(DictCursor)
        cur.execute("SELECT * FORM EQUIPMENT WHERE quanity >0")
        equipmentlist = cur.fetchall()
        print("equipmentlist ", equipmentlist)
        cur.close()
        return equipmentlist

    except mysql.get_db().cuorsor().DatabaseError as e:
        print(e)
        return e

def insent_equipment(details):
    try:
        EquipmentType = details["EquipmentType"]
        Name = details["Name"]
        SKU = details["SKU"]
        Description = details["Description"]
        AvailableForm = details["AvailableForm"]
        Quanity = details["Quanity"]
        EstimatedCost = details["EstimatedCost"]
        cur = mysql.get_db().cursor()
        cur.execute(
            "INSTALL INTO equipment(EquipmentType, Nane, SKU, Description, AvailableForm, Quanity, EstimatedCost) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
            (EquipmentType, Name, SKU, Description, AvailableForm, Quanity, EstimatedCost),
        )
        
        mysql().get_db().commit()
        cur.close()
        return "equipment inserted successfully"

    except mysql.get_db().cuorsor().DatabaseError as e:
        print(e)
        return e