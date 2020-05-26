from flask import Blueprint, Flask , jsonify, render_template, session, request, redirect
from app.models import User
auth_bp = Blueprint("auth_bp", __name__, template_folder = "templates/auth/")
user = User()
@auth_bp.route("/login", methods=["GET", "POST"])
def main():
    if request.method == "POST":
    	pass
    else:
        return render_template("login.html")

@auth_bp.route("/register", methods=["GET","POST"])
def signup():
	if request.method == "POST":
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		user.add(name,email,password)
		return jsonify("success")
	else:
		return render_template("signup.html")
