from flask import Blueprint, render_template, request, abort
from app.models import Fashion, Jewelry, Bicycle, Apparel

products_bp = Blueprint("products_bp", __name__, template_folder="templates/products")


@products_bp.route("/apparels")
def apparels():
    page = int(request.args.get("page", 1))
    per_page = 10
    apparels = Apparel.query.paginate(page, per_page, error_out=False)
    if apparels is None:
        abort(404)
    else:
        return render_template("list.html", products=apparels, title="Apparels")


@products_bp.route("/bicycles")
def bicycle():
    page = int(request.args.get("page", 1))
    per_page = 10
    bicycles = Bicycle.query.paginate(page, per_page, error_out=False)
    if bicycles is None:
        abort(404)
    else:
        return render_template("list.html", products=bicycles, title="Bicycle")


@products_bp.route("/jewelry")
def jewelry():
    page = int(request.args.get("page", 1))
    per_page = 10
    jewelries = Jewelry.query.paginate(page, per_page, error_out=False)
    if jewelries is None:
        abort(404)
    else:
        return render_template("list.html", products=jewelries, title="Jewelry")


@products_bp.route("/fashion")
def fashion():
    page = int(request.args.get("page", 1))
    per_page = 10
    fashions = Fashion.query.paginate(page, per_page, error_out=False)
    if fashions is None:
        abort(404)
    else:
        return render_template("list.html", products=fashions, title="Fashions")


@products_bp.route("/<product>/<product_id>")
def view_product(product, product_item):
    product = Jewelry(product)
    product_items = product.return_items()
    product_items = [dict(p) for p in product.return_items()]
    product_name = [
        p for p in product_items if p["name"].lower() == product_item.lower()
    ]
    if len(product_name) == 0:
        abort(404)
    else:
        return render_template(
            "view.html",
            results={"item": product_name, "keyword": product_item},
            title=product_item,
        )


@products_bp.route("/view")
def view():
    id = int(request.args.get("id"))
    product = Jewelry()
    product_items = product.show_all_items()
    product_items = [dict(p) for p in product_items if p["id"] == id]
    print(product_items)
    return render_template(
        "view.html", results={"item": product_items}, title="Product View"
    )
