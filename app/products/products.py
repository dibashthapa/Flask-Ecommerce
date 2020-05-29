from flask import Flask , Blueprint , render_template, jsonify, request, abort
from app.models import Product
products_bp = Blueprint("products_bp", __name__, template_folder="templates/products")


@products_bp.route("/<product>")
def main(product):
	product = Product(product)
	product_items = product.return_items()
	if product_items is None:
		abort(404)
	else:
		product_items= [dict(p) for p in product_items]
		return render_template("list.html")
	

@products_bp.route("/<product>/<product_item>")
def view(product, product_item):
	product = Product(product)
	product_items = product.return_items()
	product_items = [dict(p) for p in product.return_items()] 
	product_name = [p for p in product_items if p['name'].lower() == product_item.lower()]
	if len(product_name) == 0:
		abort(404)
	else:
		return render_template("view.html", results={"item":product_name, "keyword":product_item}) 

