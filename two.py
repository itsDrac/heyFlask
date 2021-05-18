from flask import Flask

myapp = Flask("two")

@myapp.get('/')
def home():
    return f"<h1> Hello World this file is {__name__}"
