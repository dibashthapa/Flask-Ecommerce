from flask import Blueprint, render_template

cart_bp = Blueprint("cart_bp", __name__, template_folder = "templates")

@cart_bp.route("/view")
def main():
	return render_template("cart/view.html")

