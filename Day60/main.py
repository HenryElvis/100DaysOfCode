from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def Receive_Data():
    name = request.form['username']
    password = request.form['password']
    return f"<h1>Name: {name}, Password: {password}</h1>"