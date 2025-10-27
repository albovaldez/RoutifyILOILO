from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify, current_app
from components.db import get_connection
from werkzeug.utils import secure_filename
import os
import decimal

# 🟢 Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

user = Blueprint("user", __name__)

# 🏠 Home Page
@user.route("/home")
def home_page():
    if "email" in session:
        return render_template("home.html", email=session["email"])
    else:
        flash("Please log in first.")
        return redirect(url_for("auth.login"))


# 🚌 Route Page
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

    # Convert Decimal → float
    for jeep in jeepneys:
        for key in ["start_lat", "start_lng", "end_lat", "end_lng"]:
            if isinstance(jeep.get(key), decimal.Decimal):
                jeep[key] = float(jeep[key])

    return render_template("routes.html", jeepneys=jeepneys)


# 🔍 Search Endpoint
@user.route("/search")
def search():
    lat = request.args.get("lat", type=float)
    lng = request.args.get("lng", type=float)

    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT jeepney_name, route, fare, distance_km, lat, lng FROM jeepny"
    cursor.execute(sql)
    jeepneys = cursor.fetchall()

    nearby = []
    for jeep in jeepneys:
        jeep_lat = jeep["lat"]
        jeep_lng = jeep["lng"]

        if jeep_lat is None or jeep_lng is None:
            continue

        # Convert Decimal → float if needed
        if isinstance(jeep_lat, decimal.Decimal):
            jeep_lat = float(jeep_lat)
        if isinstance(jeep_lng, decimal.Decimal):
            jeep_lng = float(jeep_lng)

        # Simple distance formula (approx)
        distance = ((lat - jeep_lat) ** 2 + (lng - jeep_lng) ** 2) ** 0.5 * 111  # km
        if distance <= 3.0:
            jeep["distance_km"] = round(distance, 2)
            nearby.append(jeep)

    cursor.close()
    conn.close()

    return jsonify(nearby)


@user.route("/profile", methods=["GET", "POST"])
def profile():
    conn = get_connection()
    cursor = conn.cursor()

    # Fetch the first profile (for now, no login/session)
    cursor.execute("SELECT * FROM user_profile LIMIT 1")
    profile = cursor.fetchone()

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        country = request.form.get("country")
        province = request.form.get("province")
        city = request.form.get("city")

        # Handle image upload
        file = request.files.get("profile_pic")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(current_app.static_folder, "uploads", filename)
            os.makedirs(os.path.dirname(upload_path), exist_ok=True)
            file.save(upload_path)
            profile_pic_path = f"uploads/{filename}"
        else:
            profile_pic_path = profile["profile_pic"] if profile else "images/default-user.jpg"

        # Insert or update
        if profile:
            cursor.execute("""
                UPDATE user_profile
                SET first_name=%s, last_name=%s, country=%s, province=%s, city=%s, profile_pic=%s
                WHERE id=%s
            """, (first_name, last_name, country, province, city, profile_pic_path, profile["id"]))
        else:
            cursor.execute("""
                INSERT INTO user_profile (first_name, last_name, country, province, city, profile_pic)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, country, province, city, profile_pic_path))

        conn.commit()
        flash("Profile updated successfully!")
        return redirect(url_for("user.profile"))

    # Re-fetch latest profile
    cursor.execute("SELECT * FROM user_profile LIMIT 1")
    profile = cursor.fetchone()

    cursor.close()
    conn.close()

    profile_pic = profile["profile_pic"] if profile and profile["profile_pic"] else "images/default-user.jpg"

    return render_template("profile.html", profile=profile, profile_pic=profile_pic)



# ⚙️ Account Settings
@user.route("/setting")
def setting_page():
    return render_template("setting.html")
