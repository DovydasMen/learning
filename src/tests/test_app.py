import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    responce = client.get("/")
    assert responce.status_code == 200
    assert responce.get_data(as_text=True) == "<p> Hello World! <p>"


def test_wind_route(client):
    responce = client.get("/wind?wind_side=west")
    assert responce.status_code == 200
    assert responce.get_data(as_text=True) == "<p> Wind is blowing from west <p>"

def test_calc_route_correct_vars_sum(client):
    responce = client.get("/calc?operand=+&value_a=20&value_b=10")
    assert responce.status_code == 200
    assert responce.get_data(as_text=True) == "Result = 30"

def test_calc_route_correct_vars_deduct(client):
    responce = client.get("/calc?operand=-&value_a=20&value_b=10")
    assert responce.status_code == 200
    assert responce.get_data(as_text=True) == "Result = 10"

def test_calc_route_correct_vars_multiply(client):
    responce = client.get("/calc?operand=x&value_a=20&value_b=10")
    assert responce.status_code == 200
    assert responce.get_data(as_text=True) == "Result = 200"

def test_calc_route_correct_vars_devide(client):
    responce = client.get("/calc?operand=/&value_a=20&value_b=10")
    assert responce.status_code == 200
    assert responce.get_data(as_text=True) == "Result = 2.0"

def test_calc_route_correct_vars_none(client):
    responce = client.get("/calc?operand=a&value_a=20&value_b=10")
    assert responce.status_code == 200
    assert responce.get_data(as_text=True) == "Result = None"

def test_calc_route_correct_vars_pydantic_error(client):
    responce = client.get("/calc?operand=+&value_a=-20&value_b=10")
    assert responce.status_code == 200
    assert responce.get_data(as_text=True) == "We reciewed wrong type of information, validation haven't passed."
