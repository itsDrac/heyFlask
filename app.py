from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('index.html')

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        print("url_for => ", url_for('home'))
        return redirect(url_for('home'))
    return render_template('add.html')
