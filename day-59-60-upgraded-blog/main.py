from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

app = Flask(__name__)

url = "https://api.npoint.io/dd2b08a683ed876fda65"
all_posts = requests.get(url).json()

load_dotenv("../../EnvVar/.env.txt")
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        message = f"Subject:New Message\n\nName: {data['name']}\nEmail: {data['email']}\nPhone: " \
                  f"{data['phone']}\nMessage:{data['message']}"
        send_mail(message)
        return render_template("contact.html", message="Successfully sent your message.")
    return render_template("contact.html", message="Contact me")


def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=message)


@app.route("/<int:blog_id>")
def get_blog(blog_id):
    for post in all_posts:
        if post["id"] == blog_id:
            return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
