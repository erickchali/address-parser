import pytest
from parser.street_parser import parse_street_address


def test_parse_empty_string():
    assert isinstance(parse_street_address(""), dict)


def test_parse_non_string_value():
    with pytest.raises(AttributeError):
        assert isinstance(parse_street_address(123), dict)
        assert isinstance(parse_street_address([]), dict)
        assert isinstance(parse_street_address({}), dict)
        assert isinstance(parse_street_address(None), dict)


def test_simple_street_address():
    parsed_address = parse_street_address("Winterallee 3")
    assert isinstance(parsed_address, dict)
    assert parsed_address.get("street") == "Winterallee"
    assert parsed_address.get("house_number") == "3"

    parsed_address = parse_street_address("Musterstrasse 45")
    assert isinstance(parsed_address, dict)
    assert parsed_address.get("street") == "Musterstrasse"
    assert parsed_address.get("house_number") == "45"

    parsed_address = parse_street_address("Blaufeldweg 123B")
    assert isinstance(parsed_address, dict)
    assert parsed_address.get("street") == "Blaufeldweg"
    assert parsed_address.get("house_number") == "123B"


def test_complicated_street_address():
    parsed_address = parse_street_address("Am Bächle 23")
    assert isinstance(parsed_address, dict)
    assert parsed_address.get("street") == "Am Bächle"
    assert parsed_address.get("house_number") == "23"

    parsed_address = parse_street_address("Auf der Vogelwiese 23 b")
    assert isinstance(parsed_address, dict)
    assert parsed_address.get("street") == "Auf der Vogelwiese"
    assert parsed_address.get("house_number") == "23 b"


def test_other_countries_address():
    parsed_address = parse_street_address("4, rue de la revolution")
    assert isinstance(parsed_address, dict)
    assert parsed_address.get("street") == "rue de la revolution"
    assert parsed_address.get("house_number") == "4"

    parsed_address = parse_street_address("200 Broadway Av")
    assert isinstance(parsed_address, dict)
    assert parsed_address.get("street") == "Broadway Av"
    assert parsed_address.get("house_number") == "200"

    parsed_address = parse_street_address("Calle Aduana, 29")
    assert isinstance(parsed_address, dict)
    assert parsed_address.get("street") == "Calle Aduana"
    assert parsed_address.get("house_number") == "29"
