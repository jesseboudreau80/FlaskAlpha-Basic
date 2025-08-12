from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)


@bp.get("/healthz")
def healthz():
    return jsonify(status="ok"), 200


@bp.get("/")
def index():
    return jsonify(app="FlaskAlpha-Basic", status="running"), 200
