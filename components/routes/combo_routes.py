from flask import Blueprint, render_template

combo = Blueprint("combo", __name__)

@combo.route("/")
def landing_page():
    return render_template("landing_page.html")

@combo.route("/about")
def about_page():
    return render_template("about.html")

@combo.route("/feature")
def feature_page():
    return render_template("feature.html")

@combo.route("/contact")
def contact_page():
    return render_template("contact.html")
