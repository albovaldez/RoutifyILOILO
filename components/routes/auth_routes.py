from components.services.auth_service import AuthService
from flask import Blueprint, render_template, request, redirect, url_for, session, flash


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email_inp")
        password = request.form.get("pass_inp")

        valid, user = AuthService.validate_login(email, password)
        if valid:
            session["email"] = email
            flash("Login successful!", "success")
            return redirect(url_for("user.home_page"))
        else:
            flash("Invalid email or password!", "danger")
    return render_template("auth/login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("user_inp")
        email = request.form.get("email_inp")
        password = request.form.get("pass_inp")

        if AuthService.find_user_by_username_or_email(username, email):
            flash("Username or email already exists. Please try again.")
            return render_template("auth/register.html")
        else:
            AuthService.register_user(username, email, password)
            flash("Account created successfully!", "success")
            return redirect(url_for("auth.login"))
    return render_template("auth/register.html")


@auth.route("/logout")
def logout():
    session.pop("email", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("combo.landing_page"))
