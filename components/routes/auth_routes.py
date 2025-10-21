from flask import Blueprint, render_template, request, redirect, url_for , session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from components.db import get_connection

auth = Blueprint("auth",__name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email_inp")
        password = request.form.get("pass_inp")

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user_account WHERE email = %s", (email,))
        account =cursor.fetchone()
        
        if account and check_password_hash(account["password"], password):
            session["email"] = email
            flash("Login seccessful!", "success")
            return redirect(url_for("user.home_page"))
        else:
            flash("Invalid email or password!","danger")
    return render_template("auth/login.html")


@auth.route("/register", methods=["GET","POST"])
def register(): 
     if request.method == "POST":

        username = request.form.get("user_inp")
        email = request.form.get("email_inp")
        password = request.form.get("pass_inp")
        
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user_account WHERE username = %s OR email = %s", (username, email))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Username or email already exists. Please try again.")
            return render_template("auth/register.html")
        else:
            hashed_password = generate_password_hash(password)
            cursor.execute("INSERT INTO user_account (username, email, password) VALUES (%s,%s,%s)",(username, email, hashed_password))
            connection.commit()
            flash("Account created succesfully!", "success")
            return redirect(url_for("auth.login"))  
     return render_template("auth/register.html")


@auth.route("/logout")
def logout():
    session.pop("email", None)
    flash("You have been logged out.","info")
    return redirect(url_for("combo.landing_page"))
