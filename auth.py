import email
from email.mime import image
import functools

from .__init__ import db
from sqlite3 import IntegrityError
from .models import User

from flask import (
    Blueprint, flash, redirect, render_template, render_template_string, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_remembered, login_required, login_user, current_user, logout_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash( user.password, password):
                flash("you have logged in congrats", category="success")
                login_user(user, remember=True)
            else:
                flash("the password is false",category="error")
        else:
            flash("no such email in the database",category="error")

        

    return render_template("login.html", text="testingzz")
    


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password23")
        firstname = request.form.get("firstname")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("no there is already same email",category="error")
        elif len(email) < 4:
            flash("email  must be longed than 4 character", category="error")
        elif len(firstname) < 2:
            flash("firstname must be longed than 2 character", category="error")
        elif password  != password2:
            flash("password 1 and 2 are not same", category="error")
        else:
            #add user to database or fuck them all there is already a user
            new_user = User(email=email, frist_name=firstname, password=generate_password_hash(password)) #, method="sha-256"
            db.session.add(new_user)
            db.session.commit()
            flash("congrats user account created", category="success")
            login_user(user, remember=True)
            return redirect(url_for("views.home"))


    return render_template("register.html")




