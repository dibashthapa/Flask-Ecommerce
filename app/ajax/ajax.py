from app.models import Jewelry
from flask import Blueprint, jsonify, request

ajax_bp = Blueprint("ajax_bp", __name__)


@ajax_bp.route("/search")
def search_query():
    query = request.args.get("query")
    search_query = Jewelry.name.endswith(query)
    product_items = Jewelry.query.filter_by(name=search_query).all()
    return jsonify(product_items)
