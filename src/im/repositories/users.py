from abc import abstractmethod
from im.repositories import Repository
from im.model.user import User


class UserRepository(Repository):
    @abstractmethod
    def by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def by_username_and_password(self, username: str, password: str) -> User:
        pass
