from flask import Blueprint, jsonify, request
from parser.street_parser import parse_street_address

address_bp = Blueprint("address", __name__)


@address_bp.route("/parse", methods=["POST"])
def add_address():
    if request.json and "address" in request.json.keys():
        try:
            parsed_address = parse_street_address(request.json.get("address", ""))
            if parsed_address:
                return jsonify(parsed_address)
            else:
                return jsonify({"message": "Unable to parse given address :("}), 400
        except AttributeError:
            return jsonify({"message": "address must be a string value."}), 400
    return jsonify({"message": "parameter address is required"}), 400
