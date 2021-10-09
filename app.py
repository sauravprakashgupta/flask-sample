from flask import Flask, render_template, request, redirect
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from playsound import playsound

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


@app.route('/delete/<int:sno>', methods=['POST','GET'])
def delete(sno):
    if request.method == 'POST':
        sno_del = request.form['title']
        todo=Todo.query.filter_by(sno=sno_del).first()
        db.session.delete(todo)
        db.session.commit()
        # playsound('delete-sound.mp3')
        return redirect("/")       
    todo=Todo.query.filter_by(sno=sno).first()
    return render_template('delete.html', todo=todo)
    

@app.route('/edit/<int:sno>', methods=['POST','GET'])
def edit(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, 
                    desc=desc
                    )
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo=Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)
    
    # db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=3333)
