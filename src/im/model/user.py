"""
A module to represent a user
"""
from dataclasses import dataclass, field
from im.model import Entity
from im.validators.username_validator import UsernameValidator
from im.validators.email_validator import EmailValidator
from im.validators.password_validator import PasswordValidator
from im.services.password_hash_service import PasswordHashingService


@dataclass()
class User(Entity):
    """A class to represent a user"""

    _username: str = field()
    _password: str = field()
    _email: str = field()
    _token: str = field()
    _email_verified: bool = False

    def __post_init__(self):
        """Validate class's properties"""
        if not UsernameValidator().validate(self.username):
            raise ValueError(
                "Username can consist of alphanumeric characters, minimum 4 and maximum 16 characters"
            )

        if not EmailValidator().validate(self.email):
            raise ValueError("Email address in not correct")

    @property
    def username(self) -> str:
        """str: Get the username"""
        return self._username

    @property
    def password(self) -> str:
        """str: Get the hashed password"""
        return self._password

    @property
    def email(self) -> str:
        """str: Get the email"""
        return self._email

    @property
    def token(self) -> str:
        """str: Get the verification token"""
        return self._token

    @property
    def email_verified(self) -> bool:
        """bool: Get email verified flag"""
        return self._email_verified

    def verify_email(self, token: str) -> None:
        """Verify email with specified token

        :param token: str Token to verify
        :param token: str:
        :returns: None
        :raises ValueError: if token is not valid

        """
        if token == self.token:
            self.email_verified = True
        else:
            raise ValueError("Failed to verify user. Invalid token")

    @classmethod
    def generate_password(cls, password: str, hash_srv: PasswordHashingService) -> str:
        """
        A class method to generate a password
        :param password: str: A plain password
        :param hash_srv: PasswordHashingService: A service to hash the password
        :return: str: A hashed password
        """
        if not PasswordValidator().validate(password):
            raise ValueError(
                "Password must be minimum eight and maximum 16 characters, at least one uppercase "
                "letter, one lowercase "
                "letter, one number and one special character "
            )
        return hash_srv.hash_password(password)
