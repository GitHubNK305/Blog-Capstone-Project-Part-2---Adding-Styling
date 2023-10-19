from flask import Flask, render_template, url_for
import requests

BLOG_URL = "https://api.npoint.io/131e4732b62e02054dea"
response = requests.get(BLOG_URL)
response.raise_for_status()
content = response.json()
blogs = content
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/<int:index>')
def show_post(index):
    requested_post = None
    for blog in blogs:
        if blog["id"] == index:
            requested_post = blog
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
