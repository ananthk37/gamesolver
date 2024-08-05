import pytest

def test_health(client):
    response = client.get("/health")
    assert response.json == "Hello!"