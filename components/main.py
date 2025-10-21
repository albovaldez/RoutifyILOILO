from flask import Flask 
from flask_cors import CORS
from components.routes.combo_routes import combo
from components.routes.auth_routes import auth
from components.routes.user_routes import user

def create_app():
    app=Flask(__name__, template_folder="templates")

    app.config["SECRET_KEY"] = "Routifyiloilo123"
    CORS(app)

    #register blueprints 
    app.register_blueprint(combo)
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(user, url_prefix="/user")

    return app



