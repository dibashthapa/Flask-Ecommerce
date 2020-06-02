from flask import Blueprint, Flask , jsonify, render_template, session, request, redirect, url_for
from app.models import User
from .forms import RegistrationForm, LoginForm
auth_bp = Blueprint("auth_bp", __name__, template_folder="templates/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def main():
	if request.method == "POST":
		form = LoginForm()
		user= User()
		email = request.form['email']
		password = request.form['password']
		result = user.verify(email, password)
		if result == True:
			session['email'] = email
			return redirect(url_for("general_bp.home"))
	return render_template("login.html", title="Login")

@auth_bp.route("/register", methods=["GET","POST"])
def signup():
	if request.method == "POST":
		form - LoginForm()
		user= User()
		fname = request.form['fname']
		lname = request.form['lname']
		email = request.form['email']
		password = request.form['password']
		user.add(fname,lname, email, password)
		return redirect(url_for("auth_bp.main"))
	else:
		return render_template("signup.html", title ="register")

@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_pass():
	return render_template("forgot_password.html", title="forgot password")