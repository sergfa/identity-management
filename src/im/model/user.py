"""
A module to represent a user
"""
from dataclasses import dataclass, field
from uuid import uuid4
from im.model import Entity
from im.validators.username_validator import UsernameValidator
from im.validators.email_validator import EmailValidator
from im.validators.password_validator import PasswordValidator
from im.services.password_hash_service import PasswordHashingService


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
    def create_user(
        cls, hash_srv: PasswordHashingService, username: str, password: str, email: str
    ) -> "User":
        """
        Create an instance of the user from provided parameters, also hashes the password

        :param hash_srv:  A service to hash the password

        :param username: A username

        :param password: A plain password

        :param email: An email address

        :return: User

        :raises ValueError: if one of the specified parameters is not valid
        """
        if not UsernameValidator().validate(username):
            raise ValueError(
                "Username can consist of alphanumeric characters, minimum 4 and maximum 16 characters"
            )

        if not PasswordValidator().validate(password):
            raise ValueError(
                "Password must be minimum eight and maximum 16 characters, at least one uppercase "
                "letter, one lowercase "
                "letter, one number and one special character "
            )

        if not EmailValidator().validate(email):
            raise ValueError("Email address in not correct")

        hashed_password = hash_srv.hash_password(password)
        return User(
            _uid=User.next_id(),
            _username=username,
            _password=hashed_password,
            _email=email,
            _token=User.next_id(),
        )

    @classmethod
    def next_id(cls) -> str:
        """
        str: Generate next id for a user
        Examples:
            user = User(User.next_id(), "name", "password", "email@example")
        """
        return str(uuid4())
