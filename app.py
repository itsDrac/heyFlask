from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')
