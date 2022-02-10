"""
A module to represent a user
"""
from dataclasses import dataclass, field
from uuid import uuid4
from im.model import Entity
from im.validators.username_validator import UsernameValidator
from im.validators.email_validator import EmailValidator
from im.validators.password_validator import PasswordValidator


@dataclass()
class User(Entity):
    """
    A class to represent a user
    """

    _username: str = field()
    _password: str = field()
    _email: str = field()
    _token: str = field()
    _email_verified: bool = False

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
        return self._token

    @property
    def email_verified(self) -> bool:
        return self._email_verified

    def verify_email(self, token: str):
        if token == self.token:
            self.email_verified = True
        else:
            raise ValueError("Failed to verify user. Invalid token")

    @classmethod
    def next_id(cls) -> str:
        """
        str: Generate next id for a user
        Examples:
            user = User(User.next_id(), "name", "password", "email@example")
        """
        return str(uuid4())
