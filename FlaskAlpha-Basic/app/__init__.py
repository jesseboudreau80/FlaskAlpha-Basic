from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes.main import main_bp
    from .routes.agent import agent_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(agent_bp, url_prefix="/agent")

    return app
