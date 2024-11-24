import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_full_user_flow():
    client = APIClient()
    user_data = {"username": "test_user", "name": "Test Name", "role": "admin"}
    response = client.post("/userAdd", user_data)
    assert response.status_code == 200
    assert response.data["username"] == "test_user"
    response = client.get("/userGet")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Test Name"
