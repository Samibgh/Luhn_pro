"""Luhn error definitions"""


class Unimplemented(Exception):
    """A feature code is not implemented yet"""

    def __str__(self):
        return "Unimplemented"
