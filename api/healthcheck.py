from datetime import datetime
from flask import Blueprint, jsonify

healthcheck_bp = Blueprint("healthcheck", __name__)


@healthcheck_bp.route("/", methods=["GET"])
def api_healthcheck():
    return jsonify({"message": str(datetime.now())})
