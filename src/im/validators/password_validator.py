from cerberus import Validator
from im.validators import Validator as DomainValidator


class PasswordValidator(DomainValidator):
    """Minimum eight and maximum 16 characters, at least one uppercase letter, one lowercase letter, one number and
    one special character"""

    def __init__(self):
        schema = {
            "password": {
                "type": "string",
                "regex": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$",
            }
        }
        self.__validator = Validator(schema)

    def validate(self, value) -> bool:
        is_valid = self.__validator.validate({"password": value})
        return is_valid
