from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(blog_url).json()


@app.route('/')
def home():
    return render_template("index.html", posts=blog_response)


@app.route("/<int:blog_id>")
def get_blog(blog_id):
    for post in blog_response:
        if post["id"] == blog_id:
            return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
