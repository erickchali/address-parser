from flask import Blueprint, jsonify, request
from parser.street_parser import parse_street_address
from database.address import save_parsed_address, get_parsed_address_history

address_bp = Blueprint("address", __name__)


@address_bp.route("/parse", methods=["POST"])
def add_address():
    if request.json and "address" in request.json.keys():
        try:
            parsed_address = parse_street_address(request.json.get("address", ""))
            if parsed_address:
                save_parsed_address(parsed_address)
                return jsonify(parsed_address)
            else:
                return jsonify({"message": "Unable to parse given address :("}), 400
        except AttributeError:
            return jsonify({"message": "address must be a string value."}), 400
    return jsonify({"message": "parameter address is required"}), 400


@address_bp.route("/history", methods=["GET"])
def get_history():
    return jsonify(get_parsed_address_history())


@address_bp.errorhandler(500)
def handle500(error):
    return jsonify({"message": "Something went wrong."})


@address_bp.errorhandler(405)
def handle405(error):
    return jsonify({"message": "Nothing to see here."})
