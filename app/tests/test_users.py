import os
import uvicorn
from fastapi.testclient import TestClient
from dotenv import load_dotenv
from main import app

client = TestClient(app)
load_dotenv()


def test_create_user():
    response = client.post(
        "/signup",
        json={
            "email": "user8@example.com",
            "password1": "stringst",
            "password2": "stringst"
        },
    )
    assert response.status_code == 200


def test_login_user():
    response = client.post(
        "/login",
        headers={'Content-Type': 'application/json'},
        json={
            "username": "string",
            "password": "string"
        },
    )
    assert response.status_code == 200


def test_protected_endpoint():
    response = client.get(
        "/protected",
        headers={
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjAwNTQyOTksInN1YiI6InN0cmluZyJ9.SAqQkXiDDJ6wq-fZ1OUm2nNEPi3CUTFz7IxkNq23lyQ"
        },
    )
    assert response.status_code == 200


if __name__ == "__main__":
    os.environ["ALGORITHM"] = os.getenv('ALGORITHM')
    os.environ["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')  # should be kept secret
    os.environ["JWT_REFRESH_SECRET_KEY"] = os.getenv('JWT_REFRESH_SECRET_KEY')  # should be kept secret
    uvicorn.run(app, host="0.0.0.0", port=8000)
