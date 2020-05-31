from flask import Flask , Blueprint , render_template, jsonify, request, abort ,redirect, url_for
from app.models import Product
products_bp = Blueprint("products_bp", __name__, template_folder="templates/products")


@products_bp.route("/<product>")
def main(product):
	product_name = product
	product = Product(product)
	product_items = product.return_items()
	page = int(request.args.get("page") or 1)
	previous = page - 1
	start = previous * 8
	end = start + 8

	if product_items is None:
		abort(404)
	else:
		product_items= [dict(p) for p in product_items]
		return render_template("list.html", 
		 products= product_items[start:end],
		 title=product_name , 
		 length=len(product_items))
	
@products_bp.route("/<product>/<product_item>")
def view_product(product, product_item):
	product = Product(product)
	product_items = product.return_items()
	product_items = [dict(p) for p in product.return_items()] 
	product_name = [p for p in product_items if p['name'].lower() == product_item.lower()]
	if len(product_name) == 0:
		abort(404)
	else:
		return render_template("view.html", 
			results={"item":product_name, 
			"keyword":product_item}, 
			title=product_item) 

@products_bp.route("/view")
def view():
	id = int(request.args.get("id"))
	product = Product()
	product_items = product.show_all_items()
	product_items = [dict(p) for p in product_items if p['id'] == id]
	print(product_items)
	return render_template("view.html", 
			results={"item":product_items},
			title="Product View"
			)

