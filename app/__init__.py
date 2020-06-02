from flask import Flask, abort 
from app.general.general import general_bp
from app.ajax.ajax import ajax_bp
from app.products.products import  products_bp
from app.auth.auth import auth_bp	
from app.cart.cart import cart_bp
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
app.secret_key = "hhdhdhdhdh7788768"
app.register_blueprint(general_bp)  
app.register_blueprint(ajax_bp, url_prefix="/ajax")
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(cart_bp, url_prefix="/cart")
