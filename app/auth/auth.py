from flask import Blueprint, Flask , jsonify, render_template, session

auth_bp = Blueprint("auth_bp", __name__, template_folder = "templates/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def main():
	return render_template("login.html")

@auth_bp.route("/register", methods=["GET","POST"])
def signup():
	return render_template("signup.html")
