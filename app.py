from flask import Flask, render_template, request, redirect
from flask.wrappers import Request
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


@app.route('/', methods=['POST','GET'] )
def home():
    if request.method == 'POST':
        todo = Todo(title=request.form['title'], 
                    desc=request.form['desc']
                    )
        db.session.add(todo)
        db.session.commit()
    all_todo = Todo.query.all()
    return render_template('index.html', all_todo=all_todo)


@app.route('/delete/<int:sno>')
def delete(sno):
    del_obj=Todo.query.filter_by(sno=sno).first()
    db.session.delete(del_obj)
    db.session.commit()
    return redirect("/")

@app.route('/edit/<int:sno>')
def edit(sno):
    edit_obj=Todo.query.filter_by(sno=sno).first()
    
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=3333)
