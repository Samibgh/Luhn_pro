"""Luhn error definitions"""


#permets de catch les erreurs envoyé depuis la fonction isvalid
class Unimplemented(Exception):

    def __init__(self, error_type="Unimplemented"):
        self.error_type = error_type
        super().__init__(f"{error_type}")

    def __str__(self):
        return self.error_type