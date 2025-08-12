from flask import Flask
from .config import get_settings
from .extensions import cors, talisman, metrics
from .routes import bp as main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    settings = get_settings()

    # Core config
    app.config["ENV"] = settings.FLASK_ENV
    app.config["SECRET_KEY"] = settings.SECRET_KEY

    # Extensions
    cors.init_app(app, resources={r"/api/*": {"origins": settings.CORS_ORIGINS}})
    if settings.ENABLE_SECURITY_HEADERS:
        talisman.init_app(app, content_security_policy=None)

    # Prometheus metrics at /metrics
    metrics.init_app(app)

    # Blueprints
    app.register_blueprint(main_bp)

    return app
