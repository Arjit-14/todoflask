from flask import Flask, redirect
from flask import render_template
from markupsafe import escape
from flask import url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db=SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.now)

def __repr__(self) -> str:
    return f"{self.sno} - {self.title}"



# app.config['SERVER_NAME'] = "localhost:5000"
#logic
# name= "himanjal"
# @app.route("/<name>")
# def hello(name):
    # return f"Hello {escape(name)}"

# @app.route("/")
# def welcome():
#     return "Welcome page"

# @app.route("/home")
# def hello():
    # return "Hello, World!"  

# @app.route("/user/<username>")
# def user(username):
#     return f"Hello {escape(username)}"

# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     return f"Post {post_id}"

# @app.route("/path/<path:subpath>")
# def show_subpath(subpath):
#     return f"Subpath is {escape(subpath)}"

# @app.route("/")
# def index():
    # return "Heloo"

# @app.route("/login")
# def Login():
#     return "Login page"

# @app.route("/signup")
# def signup():
#     return "Signup page"

# @app.route("/user/<username>")
# def profile(username):
    # return f"{escape(username)}'s profile"

# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("Login"))
#     print(url_for("signup"))
#     # print(url_for("profile"))
#     print(url_for("Login", next="/"))
#     print(url_for("profile", username="John"))

# @app.route("/login", methods=['GET', 'POST'])
# def hello():
#     if request.method == "POST":
#         return do_the_login()
#     else:
#         return show_the_login_form()

# def do_the_login():
#     return "hi"
# def show_the_login_form():
#     return "bye"

# @app.get("/login")
# def login_get():
#     return "login page"

# @app.post("/login")
# def login_post():
#     return "enter your details"

# with app.app_context():
#     print(url_for('static',filename='styles.css'))

# @app.route("/hello")
# @app.route("/hello/<name>")
# def hello(name=None):
#     return render_template('test.html', person=name)


@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title = title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template('test.html', allTodo = allTodo)

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()

    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    return render_template("update.html",todo=todo)

if __name__ == "__main__":
    with app.app_context(): 
        db.create_all()
    app.run(debug=True, port=5000)