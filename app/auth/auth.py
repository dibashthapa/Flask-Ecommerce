from flask import Blueprint, Flask , jsonify, render_template, session, request, redirect

auth_bp = Blueprint("auth_bp", __name__, template_folder="templates/auth", static_folder="static/css", url_prefix="/auth")
@auth_bp.route("/login", methods=["GET", "POST"])
def main():
	return render_template("login.html")

@auth_bp.route("/register", methods=["GET","POST"])
def signup():
	if request.method == "POST":
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		return jsonify("success")
	else:
		return render_template("signup.html")
