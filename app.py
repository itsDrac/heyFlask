from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = {}

@app.get('/')
def home():
    return render_template('index.html', todos = todos)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        index = len(todos) + 1
        todos[index] = request.form.get("todo")
        print(todos)
        return redirect(url_for('home'))
    return render_template('add.html')
