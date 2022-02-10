from im.validators import Validator as DomainValidator
from cerberus.validator import Validator


class EmailValidator(DomainValidator):
    def __init__(self):
        schema = {
            "email": {
                "type": "string",
                "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
            }
        }
        self.__validator = Validator(schema)

    def validate(self, value: str) -> bool:
        is_valid = self.__validator.validate({"email": value})
        return is_valid
