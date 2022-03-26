from flask import Flask, session, redirect, render_template
from app.general.general import general_bp
from app.ajax.ajax import ajax_bp
from app.products.products import products_bp
from app.auth.auth import auth_bp
from app.cart.cart import cart_bp
from flask_cors import CORS
from .models import db as root_db
import os

DATABASE = os.path.join(os.path.dirname(__file__), "site.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE}"
root_db.init_app(app)
with app.app_context():
    root_db.create_all()
cors = CORS(app)
app.secret_key = "hhdhdhdhdh7788768"


@app.before_request
def check_auth():
    if "email" in session:
        redirect("/")
    else:
        redirect("/auth/login")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="Not Found")


app.register_blueprint(general_bp)
app.register_blueprint(ajax_bp, url_prefix="/ajax")
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(cart_bp, url_prefix="/cart")
