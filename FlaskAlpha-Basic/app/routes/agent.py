from flask import Blueprint, render_template

agent_bp = Blueprint('agent', __name__)

@agent_bp.route("/")
def agent_home():
    return render_template("agent.html")
