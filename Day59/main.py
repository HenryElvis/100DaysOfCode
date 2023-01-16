from flask import Flask, render_template
import requests

app = Flask(__name__)

API = "https://api.npoint.io/b4864fe025890c73f872"

posts = requests.get(API).json()

@app.route('/')
def Home():
    return render_template('index.html', all_posts=posts)

@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/contact')
def Contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)