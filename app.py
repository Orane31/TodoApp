from flask import Flask, app
from flask import render_template, jsonify, request, redirect, url_for

from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from config import Config


load_dotenv("./.flaskenv")

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
import models
from models import Task
from forms import TaskForm


@app.route("/")
def index():
    name = "Orane"
    tasks = Task.query.all()

    print(tasks)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        # jsonify(tasks) = Le dictionnaire contenant toutes les cartes todo
        return jsonify(tasks)

    return render_template("index.html", name=name, tasks=tasks)


@app.route("/create", methods=["GET", "POST"])
def create_task():
    # variable user_data pour récupérer l'input utilisateur : en JSON
    import pdb

    pdb.set_trace()
    user_input = request.get_json()

    form = TaskForm(data=user_input)

    if form.validate():
        task = Task(title="form.title.data")
        db.session.add(task)
        db.session.commit()

        return jsonify(task)
    return redirect(url_for("index"))


@app.route("/delete", methods=["POST"])
def delete_task():
    task_id = request.get_json().get("id")
    task = Task.query.filter_by(id="task_id").first()
    print(task)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"result": "Supprimé"}), 200


if __name__ == "__main__":
    app.run()
