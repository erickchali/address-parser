import re
from abc import ABC, abstractmethod


class BaseHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def parse(self, address):
        pass


class StreetAddressParser(BaseHandler):
    _next_handler: BaseHandler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def parse(self, address: str) -> dict:
        if self._next_handler:
            return self._next_handler.parse(address)
        return {}


class StreetHouseAddressParser(StreetAddressParser):
    def parse(self, address: str) -> dict:
        pattern = re.compile(STREET_HOUSE_REGEX)
        pattern_match = pattern.match(address)
        if pattern_match:
            return pattern_match.groupdict()
        return super().parse(address)


class OtherCountriesAddressParser(StreetAddressParser):
    def parse(self, address: str) -> dict:
        pattern = re.compile(OTHER_COUNTRIES_REGEX)
        pattern_match = pattern.match(address)
        if pattern_match:
            return pattern_match.groupdict()
        return super().parse(address)


def default_address_handler():
    simple_address = StreetHouseAddressParser()
    complicated_address = OtherCountriesAddressParser()

    simple_address.set_next(complicated_address)
    return simple_address


STREET_HOUSE_REGEX = r"""
    (?x)
    (?i)
    (?P<street_name>\b[a-zA-Z](\w+?\s?){1,10}\b)\s+
    (?P<house_number>\d+[a-zA-Z]?\s?[a-zA-Z]?)
"""


OTHER_COUNTRIES_REGEX = r"""
    (?x)
    (?i)
    (?P<house_number>\d+)\s*?
    (?P<street_name>\b[a-zA-Z](\w+?\s?){1,10}\b)
"""
