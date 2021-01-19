import re

regex_pattern = r"""
    (?x)
    (?i)
    (?P<street>\w+)\s+
    (?P<housenumber>\d+[a-zA-Z]?)
"""
regex_pattern = re.compile(regex_pattern)


def parse_street_address(address: str) -> dict:
    match = regex_pattern.match(address)
    if match:
        return match.groupdict()
    return {}


def sanitize_address(address: str):
    return address.strip()
