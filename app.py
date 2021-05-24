from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


'''
'<DATABASE_TYPE>://:memory:' --> Ram
'<DATABASE_TYPE>:///Database/database.db' -->relative Path
'<DATABASE_TYPE>:////c:/User/<username>/...' --> absolute Path
'''

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(20), nullable = False)


@app.get('/')
def home():
    todos = Todos.query.all()
    return render_template('index.html', todos = todos)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        todo = Todos(todo = request.form.get("todo"))
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')
