from app import app
from flask import render_template,request,session
from helpers.user_helpers import validateuser,getUserByID

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu", methods=["GET","POST"])
def menu():
    if requst.method == "POST":
        formData = requst.form
        user = validateuser(formData)

        if len(user)==0:
            return render_template(
                "index.html", msg="please enter correct user name and password"
            )

        for ID in user:
            roleID = ID["RoleID"]
        
        if RoleID ==1:
            username = session["username"]
            userinfo=UserByID(username)
            return render_template("admin/menu.html",msg=userinfo)

        elif roleID == 2:
            username = session["username"]
            userinfo=UserByID(username)
            return render_template("admin/menu.html",msg=userinfo)

        elif roleID == 2:
            username = session["username"]
            userinfo=UserByID(username)
            return render_template("admin/menu.html",msg=userinfo)

        else:
            render_template("/index.html", msg="please enter correct password and username")

    else:
        render_template("/index.html")

@app.route("/equipment",methods=["GET"])
def equipment():
    return render_template("/admin/equipment.html")

from helpers.inventary_helpers import getequipments, insent_equipment

@app.route("/viewequipment",methods=["GET","POST"])
def viewequipments():
    equipmentlist=getequipments()
    return render_template("/admin/viewequipment.html", msg=equipmentlist)

@app.route("/viewusrer",methods=["GET","POST"])
def viewusers():
    userlist=getuser()
    return render_template("/admin/viewuser.html", msg=userlist)

@app.route("/adduser",methods={"GET","POST"})
def adduser():
    return render_template("/admin/adduser.html", msg=adduser)

@app.route("/addequipment",methods={"POST"})
def addequipment():
    if requst.method=="POST":
        details=requst.form
        result=insertequipment(details)
        return render_template("/admin/addequipment.html", msg=result)

@app.route("/newuser",methods={"POST"})
def newuser():
    if requst.method=="POST":
        details=requst.form
        result=insertnewuser(details)
        return render_template("/admin/newuser.html", msg=result)

@app.route("/logout",methods={"GET"})
def logout():
    session.pop("username",None)
    return render_template("/index.html")