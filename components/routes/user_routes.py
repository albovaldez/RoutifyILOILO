from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from components.db import get_connection

user=Blueprint("user",__name__)

@user.route("/home")
def home_page():
    if "email" in session: 
        return render_template("home.html",email=session["email"])
    else:
        flash("Please log in first.")
        return redirect(url_for("auth.login"))

@user.route("/routes")
def route_page():
    query = request.args.get("query")

    connection = get_connection()
    cursor = connection.cursor()

    if query:
        cursor.execute("SELECT * FROM jeepny_route WHERE route_name LIKE %s", (f"%{query}%"))
    else:
        cursor.execute("SELECT * FROM jeepny_route")

    routes = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return render_template("routes_page.html", routes = routes )