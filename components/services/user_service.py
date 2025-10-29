# components/services/user_service.py
from components.db import get_connection
from werkzeug.utils import secure_filename
from flask import current_app
import os, decimal

class UserService:
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Check if file is valid
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in UserService.ALLOWED_EXTENSIONS

    # Fetch jeepneys for route page
    @staticmethod
    def get_all_jeepneys():
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
        return jeepneys

    # Search nearby jeepneys
    @staticmethod
    def search_nearby(lat, lng):
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
        return nearby

    # Fetch or update profile
    @staticmethod
    def get_profile():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_profile LIMIT 1")
        profile = cursor.fetchone()
        cursor.close()
        conn.close()
        return profile

    @staticmethod
    def save_profile(data, file):
        conn = get_connection()
        cursor = conn.cursor()

        profile = UserService.get_profile()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        country = data.get("country")
        province = data.get("province")
        city = data.get("city")

        # Handle image upload
        if file and UserService.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(current_app.static_folder, "uploads", filename)
            os.makedirs(os.path.dirname(upload_path), exist_ok=True)
            file.save(upload_path)
            profile_pic_path = f"uploads/{filename}"
        else:
            profile_pic_path = profile["profile_pic"] if profile else "images/default-user.jpg"

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
        cursor.close()
        conn.close()
