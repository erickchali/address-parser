import re

regex_pattern = r"""
    (?x)
    (?i)
    (?:
        (?:
            (?P<street>\w+)\s+
            (?P<housenumber>\d+[a-zA-Z]?)
        )
        |
        (?:
            (?P<street2>(\w*?\s*?){1,10})\s+
            (?P<housenumber2>\d+\s?[a-zA-Z]?)
        )
    )
"""
regex_pattern = re.compile(regex_pattern)


def parse_street_address(address: str) -> dict:
    match = regex_pattern.match(address)
    if match:
        return match.groupdict()
    return {}


def sanitize_address(address: str):
    return address.strip()
