# components/routes/user_routes.py
from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from components.services.user_service import UserService

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

    jeepneys = UserService.get_all_jeepneys()
    return render_template("routes.html", jeepneys=jeepneys)

# 🔍 Search Endpoint
@user.route("/search")
def search():
    lat = request.args.get("lat", type=float)
    lng = request.args.get("lng", type=float)
    nearby = UserService.search_nearby(lat, lng)
    return jsonify(nearby)

# 👤 Profile
@user.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        UserService.save_profile(request.form, request.files.get("profile_pic"))
        flash("Profile updated successfully!")
        return redirect(url_for("user.profile"))

    profile = UserService.get_profile()
    profile_pic = profile["profile_pic"] if profile and profile["profile_pic"] else "images/default-user.jpg"
    return render_template("profile.html", profile=profile, profile_pic=profile_pic)
