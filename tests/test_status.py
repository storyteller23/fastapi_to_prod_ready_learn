from fastapi.testclient import TestClient
from fastapi_learn.main import app
from fastapi_learn.settings import settings


def test_answer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}
