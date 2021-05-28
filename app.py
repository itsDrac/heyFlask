from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'de166576fad4be0b3f3a1bbc'
db = SQLAlchemy(app)


'''
'<DATABASE_TYPE>://:memory:' --> Ram
'<DATABASE_TYPE>:///Database/database.db' -->relative Path
'<DATABASE_TYPE>:////c:/User/<username>/...' --> absolute Path
'''

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(20), nullable = False)
    is_completed = db.Column(db.Boolean, default = False)

class TodoForm(FlaskForm):
    todo = StringField('todo', validators=[DataRequired()])

@app.get('/')
def home():
    todos = Todos.query.all()
    return render_template('index.html', todos = todos)

@app.get('/complete/all')
def complete_all():
    todos = Todos.query.all()
    todos = [ t for t in todos if t.is_completed ]
    return render_template('all.html', todos = todos)

@app.get('/add/complete/<int:id>')
def complete_todo(id):
    todo = Todos.query.get_or_404(id)
    todo.is_completed = True
    db.session.commit()
    return redirect(url_for('home'))

@app.get('/add/delete/<int:id>')
def delete_todo(id):
    todo = Todos.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todos(todo = form.todo.data)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)
