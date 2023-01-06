from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/template')
def template():
    return render_template('index.html')

@app.route('/personnal')
def personal():
    return render_template('personnal.html')