from flask import Flask, request, render_template, redirect, url_for, flash, get_flashed_messages
import os, datetime
from .config.variables import SECRET_KEY


# To link it to you mysql, go to your CMD and install the mysql connector (pip install mysql-connector-python)
def create_app():
    app = Flask(__name__)
    
    # config
    app.config["SECRET_KEY"] = SECRET_KEY # THIS IS USED FOR OUR SESSIONS.  Go to the CMD and install (pip install python-dotvenv)
    
    # BLUEPRINT
    from .views.admin_auth import admin
    app.register_blueprint(admin, url_prefix="/owner")
    
    # ERROR ROUTES
    
    # 404 - ERROR
    @app.errorhandler(404)
    def errorhandler(error):
        error = render_template("error-404.html")
        return error
    
    # 500 - ERROR
    @app.errorhandler(500)
    def errorhandler(error):
        error = render_template("error-500.html")
        return error
    
    return app