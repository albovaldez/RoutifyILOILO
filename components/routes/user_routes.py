from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
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
    return render_template("routes_page.html")

@user.route('/search', methods=['GET'])
def search():
    location = request.args.get('q','').strip().lower()

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT id, jeep_name, fare, distance_km
        FROM jeepny
        WHERE LOWER(stops) LIKE %s
    """
    cursor.execute(sql, [f"%{location}%"])
    jeeps=cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(jeeps)


