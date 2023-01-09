from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

all_post = requests.get("https://api.npoint.io/41c7c3f73a51845ba137").json()

posts = []

for post in all_post:
    p = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts.append(p)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:index>')
def show_post(index):
    for post in posts:
        if post.id == index:
            return render_template("post.html", post=post)