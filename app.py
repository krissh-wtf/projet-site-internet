from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eleves.db"
db = SQLAlchemy(model_class=Base)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/eleves", methods=["GET", "POST"])
def eleves():
    if request.method == "GET":
        return render_template("eleves.html")
    elif request.method == "POST":
        prenom = request.form["prenom"]
        classe = request.form["classe"]

@app.route("/eleves/<prenom>", methods=["GET", "DELETE", "POST"])
def eleve(prenom):
    if request.method == "GET":
        return render_template(f"eleves/{prenom}/index.html")
    elif request.method == "DELETE":
        pass
    elif request.method == "POST":
        pass

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)