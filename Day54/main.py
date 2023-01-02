from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/bye')
def say_bye():
    return '<h1>Bye!</h1>'