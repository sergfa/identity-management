"""
A module to manage users
"""
import time
from im.repositories.users import UserRepository
from im.model.user import User
from im.services.password_hash_service import PasswordHashingService
from im.events.domain_event_publisher import DomainEventPublisher
from im.events import UserRegisteredDomainEvent
from im.validators.email_validator import EmailValidator
from im.validators.password_validator import PasswordValidator
from im.validators.username_validator import UsernameValidator


class UserManagementService:
    """
    A class to manage users
    """

    def __init__(
        self,
        user_repo: UserRepository,
        pwd_hash_srv: PasswordHashingService,
        event_publisher: DomainEventPublisher,
    ):
        self.user_repo = user_repo
        self.pwd_hash_srv = pwd_hash_srv
        self.event_publisher = event_publisher

    def register_user(self, username: str, password: str, email: str):
        """
        Register a new user

        :param username:  A username

        :param password:  A user password

        :param email: A user email

        :raises ValueError: if one of the provided arguments is not valid or if user with specified username or email
        already exists

        :return:  None
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

        hashed_password = self.pwd_hash_srv.hash_password(password)

        new_user = User(
            _uid=User.next_id(),
            _username=username,
            _password=hashed_password,
            _email=email,
            _token=User.next_id(),
        )

        user_with_username = self.user_repo.by_username(username)

        if user_with_username is not None:
            raise ValueError("User with specified username already exist")

        user_with_email = self.user_repo.by_email(email=email)

        if user_with_email is not None:
            raise ValueError("User with specified email already exists")

        self.user_repo.insert(new_user)
        self.event_publisher.publish(
            UserRegisteredDomainEvent(
                created=int(time.time()),
                username=new_user.username,
                user_id=new_user.uid,
            )
        )

    def list_users(self):
        return self.user_repo.list()
