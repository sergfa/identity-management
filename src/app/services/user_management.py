"""
A module to manage users
"""
import time
from im.repositories.users import UserRepository
from im.model.user import User
from im.services.password_hash_service import PasswordHashingService
from im.events.domain_event_publisher import DomainEventPublisher
from im.events import UserRegisteredDomainEvent


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
        hashed_password = User.generate_password(password, self.pwd_hash_srv)

        new_user = User(
            _uid=self.user_repo.next_identifier(),
            _username=username,
            _password=hashed_password,
            _email=email,
            _email_verified=False,
            _token=self.user_repo.next_identifier(),
        )

        if self.user_repo.by_username(username) is not None:
            raise ValueError("User with specified username already exist")

        if self.user_repo.by_email(email=email) is not None:
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
