from app import app


def test_home():
    res = app.test_client().get("/")
    assert res.status_code == 200
    assert "second version" in res.get_json()["message"]


def test_health():
    res = app.test_client().get("/health")
    assert res.get_json() == {"status": "ok"}
