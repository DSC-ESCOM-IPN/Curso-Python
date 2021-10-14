from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200  # ok
    assert response.json() == {"msg": "hello world"}


def test_create_user():
    body = {"name": "Jose", "password": "Rivera", "age": 22}
    response = client.post("/users/", data=body, headers={})
    assert response.status_code == 200  # created
    assert response.json() == {"msg": "user added"}


# def suma(x, y):
#     try:
#         x = int(x)
#         y = int(y)
#     except ValueError:
#         return "Error en el input"
#     return int(x) + int(y)

# def test_suma():
#     assert suma("2.3", 2.3) == "Error en el input"
#     assert suma("2", 5) == 7
