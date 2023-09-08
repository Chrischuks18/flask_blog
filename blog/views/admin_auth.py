from flask import Blueprint, render_template
from ..config.database import get_connection

admin = Blueprint("admin", __name__)
get_connection()

@admin.get("/")
def login_page():
    return render_template("admin/login.html")

@admin.get("/register")
@admin.get("/signup")
def reginster_page():
    return render_template("admin/register.html")