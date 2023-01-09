from random import randint
from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    random = randint(1, 10)
    return render_template('index.html', rand=random, year=date.today().year)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"

    gender_response = requests.get(gender_url).json()
    age_response = requests.get(age_url).json()["age"]

    gender = gender_response["gender"]
    age = age_response["age"]
    
    return render_template('guess.html', name=name.capitalize(), gender=gender, age=age)