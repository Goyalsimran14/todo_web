from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime, nullable=True)

# Create DB if not exists
if not os.path.exists('todo.db'):
    with app.app_context():
        db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    now = datetime.now()

    if request.method == "POST":
        task = request.form.get("task")
        date_str = request.form.get("due_date")
        hour = int(request.form.get("due_hour"))
        minute = int(request.form.get("due_minute"))
        ampm = request.form.get("due_ampm")

        if ampm == "PM" and hour != 12:
            hour += 12
        elif ampm == "AM" and hour == 12:
            hour = 0

        if date_str:
            due_date = datetime.strptime(date_str, "%Y-%m-%d")
            due_datetime = datetime(
                year=due_date.year,
                month=due_date.month,
                day=due_date.day,
                hour=hour,
                minute=minute
            )
        else:
            due_datetime = None

        new_task = Todo(task=task, due_date=due_datetime)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("index"))

    todos = Todo.query.order_by(Todo.due_date.asc().nulls_last(), Todo.id.asc()).all()
    return render_template("index.html", todos=todos, now=now)

@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
