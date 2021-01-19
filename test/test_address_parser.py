import pytest
from parser.street_parser import parse_street_address


def test_parse_empty_string():
    assert isinstance(parse_street_address(""), dict)


def test_parse_non_string_value():
    with pytest.raises(TypeError):
        assert isinstance(parse_street_address(123), dict)
        assert isinstance(parse_street_address([]), dict)
        assert isinstance(parse_street_address({}), dict)
        assert isinstance(parse_street_address(None), dict)


def test_simple_street_address():
    address_dict = parse_street_address("Winterallee 3")
    assert isinstance(address_dict, dict)
    assert address_dict.get("street") == "Winterallee"
    assert address_dict.get("housenumber") == "3"

    address_dict = parse_street_address("Musterstrasse 45")
    assert isinstance(address_dict, dict)
    assert address_dict.get("street") == "Musterstrasse"
    assert address_dict.get("housenumber") == "45"

    address_dict = parse_street_address("Blaufeldweg 123B")
    assert isinstance(address_dict, dict)
    assert address_dict.get("street") == "Blaufeldweg"
    assert address_dict.get("housenumber") == "123B"


def test_complicated_street_address():
    address_dict = parse_street_address("Am Bächle 23")
    assert isinstance(address_dict, dict)
    assert address_dict.get("street2") == "Am Bächle"
    assert address_dict.get("housenumber2") == "23"

    address_dict = parse_street_address("Auf der Vogelwiese 23 b")
    assert isinstance(address_dict, dict)
    assert address_dict.get("street2") == "Auf der Vogelwiese"
    assert address_dict.get("housenumber2") == "23 b"
