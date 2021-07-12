from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, redirect, request, flash, url_for


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash("Logged in successfully!", category="success")
            login_user(user, remember=True)

            return redirect(url_for("views.home"))
        else:
            flash("Incorrect email or password.", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


def check_info(user: str, email: str, name: str, password1: str, password2: str) -> bool:
    message = ''

    if user:
        message = "Email already exists."
    elif len(email) < 4:
        message = "Email must be greater than 3 characters."
    elif len(name) < 2:
        message = "First Name must be greater than 1 characters."
    elif password1 != password2:
        message = "Passwords don't match."
    elif len(password2) < 7:
        message = "Password must be greater than 6 characters."

    if message:
        flash(message, category="error")
        return False
    return True


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if check_info(user, email, name, password1, password2):
            new_user = User(email=email, name=name, password=generate_password_hash(
                password=password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash("Account created!", category="success")

            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)
