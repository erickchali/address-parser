import pytest

healthcheck_endpoint = "/"
parser_endpoint = "/address/parse"
headers = {}


@pytest.fixture(scope='session')
def app(request):
    from app import create_app
    return create_app()


@pytest.fixture(autouse=True)
def app_context(app):
    with app.app_context():
        yield app


@pytest.fixture
def client(app_context):
    return app_context.test_client()


@pytest.fixture
def db(app_context):
    from database.db_models import db
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
    db.get_engine(app_context).dispose()


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


def test_supported_address_format(client, db):
    response = client.post(parser_endpoint, json={"address": "77, Bleecker Street"})
    assert response.status_code == 200
    assert response.json["street_name"] == "Bleecker Street"
    assert response.json["house_number"] == "77"
