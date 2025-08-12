from app import create_app


def test_healthz():
    app = create_app()
    client = app.test_client()
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json.get("status") == "ok"
