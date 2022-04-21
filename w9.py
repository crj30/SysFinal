from flask import Flask, redirect, request, render_template, url_for
from flask_bootstrap import Bootstrap
import sqlite3 as sql

app = Flask(__name__)
Bootstrap(app)

@app.route("/w9/")
def w9():
    return render_template("w9.htm")

@app.route("/home/")
def home():
    return render_template("home.htm")

@app.route("/addrec", methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        name = request.form["name"]
        desc = request.form["desc"]
        quantity = request.form["quantity"]
        checkinDate = request.form["checkinDate"]
    
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO inventory (name, desc, quantity, checkinDate) VALUES ('{0}', '{1}', '{2}', '{3}')".format(name,desc,quantity,checkinDate))
        con.commit()
        message = "Inventory record added successfully"

    return render_template("result.htm", msg = message)

@app.route("/list/")
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM inventory")

    rows = cur.fetchall()
    return render_template("list.htm", rows = rows)

if __name__ == "__main__":
    app.run(debug=True)   