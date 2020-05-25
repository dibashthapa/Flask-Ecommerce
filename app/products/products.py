from flask import Flask , Blueprint , render_template, jsonify, request, abort
from app.models import Product
import requests
products_bp = Blueprint("products_bp", __name__, template_folder="templates/products")
@products_bp.route("/<product>")
def main(product):
	try:
		product = Product(product)
	except Exception as e:
		abort(404)
	return render_template("list.html")

@products_bp.route("/<product>/<product_item>")
def view(product, product_item):
	# product = Product(product_name)
	# product_items = [dict(p) for p in product.return_items()]
	product = Product(product)
	product_items = [dict(p) for p in product.return_items()]
	product_name = [p for p in product_items if p['name'].lower() == product_item.lower()]
	
	return render_template("view.html", results={"item":product_name, "keyword":product_item})

