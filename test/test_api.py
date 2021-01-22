import pytest
from flask import current_app
from app import create_app

app = create_app()
healthcheck_endpoint = "/"
parser_endpoint = "/address/parse"
headers = {}


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            assert current_app.config["ENV"] == "production"
        yield client


def test_healthcheck(client):
    response = client.get(healthcheck_endpoint)
    assert response.status_code == 200


def test_missing_parameter(client):
    response = client.post(parser_endpoint, json={"wrong_parameter": "calle 66"})
    assert response.status_code == 400
    assert response.json["message"] == "parameter address is required"
    response = client.post(parser_endpoint)
    assert response.status_code == 400
    assert response.json["message"] == "parameter address is required"


def test_unaccepted_values(client):
    wrong_data_types = [[], {}, 100, None]
    for data_type in wrong_data_types:
        response = client.post(parser_endpoint, json={"address": data_type})
        assert response.status_code == 400
        assert response.json["message"] == "address must be a string value."


def test_non_supported_address_format(client):
    response = client.post(parser_endpoint, json={"address": "Lorem Ipsum is simply dummy text."})
    assert response.status_code == 400
    assert response.json["message"] == "Unable to parse given address :("


def test_supported_address_format(client):
    response = client.post(parser_endpoint, json={"address": "77, Bleecker Street"})
    assert response.status_code == 200
    assert response.json["street_name"] == "Bleecker Street"
    assert response.json["house_number"] == "77"
