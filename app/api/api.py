from app.models import Product
import traceback
from flask import Flask , Blueprint, jsonify, request, abort
import time

api_bp = Blueprint("api_bp", __name__)
@api_bp.route("/products/<product_name>")
def main(product_name):
    product = Product(product_name)
    try:
        product_items = [dict(p) for p in product.return_items()]
    except TypeError:
        abort(404)
    start = int(request.args.get("start") or 0)
    end = int(request.args.get("end") or len(product_items)-1)
    data =[product_items[i] for i in range(start,end+1)]
    time.sleep(1)
    return jsonify(data)

@api_bp.route("/products/<product_name>/<product_item>")
def view(product_name, product_item):
	product = Product(product_name)
	product_items = [dict(p) for p in product.return_items()]
	return  jsonify([p for p in product_items if p['name'].lower().startswith(product_item)])
