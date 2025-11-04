from flask import Flask, request, redirect, url_for, flash,  render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret'
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == '__main__':
    app.run()
