from app.models import Product
import traceback
from flask import Flask , Blueprint, jsonify, request, abort
import time

ajax_bp = Blueprint("ajax_bp", __name__)

@ajax_bp.route("/search")
def search_query():
    query = request.args.get("query")
    product = Product()
    product_items = product.show_all_items()
    return jsonify([dict(p) for p in product_items if p['name'].lower().startswith(query)])
