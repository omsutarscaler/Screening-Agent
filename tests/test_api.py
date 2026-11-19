from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health() -> None:
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_screening_returns_boilerplate_result() -> None:
    response = client.post(
        "/api/screenings",
        json={
            "job_description": "Python developer with FastAPI experience",
            "resume_text": "Software engineer with Python and API experience",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["recommendation"] == "pending_review"
    assert body["overall_score"] == 0
