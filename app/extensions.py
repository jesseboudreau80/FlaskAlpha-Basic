from flask_cors import CORS
from flask_talisman import Talisman
from prometheus_flask_exporter import PrometheusMetrics

cors = CORS()
talisman = Talisman()
metrics = PrometheusMetrics.for_app_factory()
