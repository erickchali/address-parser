from parser.address_handler import default_address_handler


def parse_street_address(address: str) -> dict:
    handler = default_address_handler()
    return handler.parse(sanitize_address(address))


def sanitize_address(address: str):
    return address.strip().replace(",", "")
