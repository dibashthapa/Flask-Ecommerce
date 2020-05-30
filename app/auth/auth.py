from flask import Blueprint, Flask , jsonify, render_template, session, request, redirect

auth_bp = Blueprint("auth_bp", __name__, template_folder="templates/auth")
@auth_bp.route("/login", methods=["GET", "POST"])
def main():
	return render_template("login.html", title="Login")

@auth_bp.route("/register", methods=["GET","POST"])
def signup():
	if request.method == "POST":
		name = request.form['name']
		email = request.form['email']
		lpassword = request.form['password']
		return jsonify(name, email, password)
	else:
		return render_template("signup.html", title ="register")

@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_pass():
	return render_template("forgot_password.html", title="forgot password")