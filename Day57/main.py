from random import randint
from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello_world():
    random = randint(1, 10)
    return render_template('index.html', rand=random, year=date.today().year)
