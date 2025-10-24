from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from components.db import get_connection
import decimal

user = Blueprint("user", __name__)

@user.route("/home")
def home_page():
    if "email" in session:
        return render_template("home.html", email=session["email"])
    else:
        flash("Please log in first.")
        return redirect(url_for("auth.login"))


@user.route("/routes")
def route_page():
    if "email" not in session:
        flash("Please log in first.")
        return redirect(url_for("auth.login"))

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        SELECT jeepney_name, route, fare, start_lat, start_lng, end_lat, end_lng
        FROM jeepny
    """
    cursor.execute(sql)
    jeepneys = cursor.fetchall()

    cursor.close()
    conn.close()

    # Convert decimal → float
    for jeep in jeepneys:
        for key in ["start_lat", "start_lng", "end_lat", "end_lng"]:
            if isinstance(jeep.get(key), decimal.Decimal):
                jeep[key] = float(jeep[key])

    return render_template("routes.html", jeepneys=jeepneys)


@user.route("/search")
def search():
    # 🔹 Get latitude and longitude from query params instead of name text
    lat = request.args.get("lat", type=float)
    lng = request.args.get("lng", type=float)

    conn = get_connection()
    cursor = conn.cursor()

    # 🔹 Fetch all jeepneys with their coordinates from the DB
    sql = "SELECT jeepney_name, route, fare, distance_km, lat, lng FROM jeepny"
    cursor.execute(sql)
    jeepneys = cursor.fetchall()

    # 🔹 Find which jeepneys are near the searched location
    nearby = []
    for jeep in jeepneys:
        jeep_lat = jeep["lat"]
        jeep_lng = jeep["lng"]

        if jeep_lat is None or jeep_lng is None:
            continue

        # ✅ Convert Decimal to float if needed
        if isinstance(jeep_lat, decimal.Decimal):
            jeep_lat = float(jeep_lat)
        if isinstance(jeep_lng, decimal.Decimal):
            jeep_lng = float(jeep_lng)

        # simple distance formula (approximate)
        distance = ((lat - jeep_lat)**2 + (lng - jeep_lng)**2)**0.5 * 111  # km

        if distance <= 3.0:  # within 3 km radius
            jeep["distance_km"] = round(distance, 2)
            nearby.append(jeep)

    cursor.close()
    conn.close()

    return jsonify(nearby)