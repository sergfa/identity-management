from cerberus import Validator
from im.validators import Validator as DomainValidator


class UsernameValidator(DomainValidator):

    """Usernames can consist of alphanumeric characters, minimum 4 and maximum 16 characters"""

    def __init__(self):
        schema = {"username": {"type": "string", "regex": "[a-zA-Z]{4,16}$"}}
        self.__validator = Validator(schema)

    def validate(self, value: str) -> bool:
        is_valid = self.__validator.validate({"username": value})
        return is_valid
