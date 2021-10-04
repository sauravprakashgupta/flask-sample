from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(500))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"


@app.route('/')
def hello_world():
    todo = Todo(title="This is title", desc="This is description")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')


@app.route('/add')
def show():
    return '<h1>This is under construction</h1>'

@app.route('/update')
def add():
    return '<h1>This is under construction</h1>'

@app.route('/delete')
def update():
    return '<h1>This is under construction</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=3333)
