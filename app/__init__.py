from flask import Flask 
from flask_cors import CORS
from app.general.general import general_bp
from app.api.api import api_bp
from app.products.products import  products_bp
app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(general_bp)  
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(products_bp, url_prefix="/products")
