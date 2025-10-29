from werkzeug.security import generate_password_hash, check_password_hash
from components.db import get_connection

class AuthService:
    """Handles all user authentication and registration logic."""

    @staticmethod
    def find_user_by_email(email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_account WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def find_user_by_username_or_email(username, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_account WHERE username = %s OR email = %s", (username, email))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def register_user(username, email, password):
        conn = get_connection()
        cursor = conn.cursor()
        hashed_password = generate_password_hash(password)
        cursor.execute("""
            INSERT INTO user_account (username, email, password)
            VALUES (%s, %s, %s)
        """, (username, email, hashed_password))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def validate_login(email, password):
        user = AuthService.find_user_by_email(email)
        if user and check_password_hash(user["password"], password):
            return True, user
        return False, None
