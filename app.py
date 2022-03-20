from flask import Flask, render_template, request
from mojeprogramy.funkcja_data import date_now
import random
from mojeprogramy.generator_hasla import password
from mojeprogramy.kamien_papier_nozyce import gra

app=Flask(__name__)
app.config["SECRET KEY"] = "secret key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bmi', methods=["POST", "GET"]) 
def bmi():
    bmi=""
    if request.method=="POST":
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))
        bmi = round(weight/((height/100)**2),2)
    return render_template("bmi.html", bmi=bmi)

@app.route("/generator", methods=["POST", "GET"])
def generator():
    passw = ""
    if request.method=="POST":
        number = int(request.form.get("number"))
        passw = password(number)
    return render_template("generator_hasla.html", passw = passw)

@app.route("/kamien", methods=["POST", "GET"])
def kamien():
    wynik = ""
    if request.method=="POST":
        choice = request.form.get("choice")
        wynik = gra(choice)
    return render_template("kamien.html", wynik = wynik)


@app.route("/date")
def date():
    content=date_now()
    return render_template("date.html", text=content)

if __name__=="__main__":
    app.run(debug =True)
