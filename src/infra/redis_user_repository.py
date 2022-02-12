import redis
from redis.commands.json.path import Path
import json
from typing import Dict

from im.model import Entity
from im.model.user import User
from im.repositories.users import UserRepository


class UserJSONDataMapper:
    def data_to_user(self, data: dict) -> User:
        user = User(**json.loads(data))
        return user

    def user_to_data(self, user: User) -> Dict:
        data = json.dumps(user, default=lambda o: o.__dict__, indent=4)
        return data


class UserRedisRepository(UserRepository):
    def __init__(self, host="localhost", port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db)
        self.mapper = UserJSONDataMapper()
        self.root = "users_data"
        if self.client.json().get(self.root) is None:
            self.client.json().set(self.root, Path.rootPath(), {})

    def by_id(self, uid: str) -> User:
        user_data = self.client.json().get(self.root, Path.rootPath() + uid)
        user: User = (
            self.mapper.data_to_user(user_data) if user_data is not None else None
        )
        return user

    def insert(self, user: User):
        user_data = self.mapper.user_to_data(user)
        self.client.json().set(self.root, Path.rootPath() + user.uid, user_data)

    def update(self, entity: Entity) -> None:
        self.update(entity)

    def remove(self, uid: str) -> None:
        self.client.json().delete(self.root, Path.rootPath() + uid)

    def list(self) -> [User]:
        result = []
        users = self.client.json().get(self.root)
        if users is not None:
            for key in users:
                user = self.mapper.data_to_user(users[key])
                result.append(user)

        return result

    def by_username(self, username: str) -> User:
        users = self.client.json().get(self.root)
        if users is not None:
            for uid in users:
                user = self.mapper.data_to_user(users[uid])
                if user.username == username:
                    return user
        return None

    def by_username_and_password(self, username: str, password: str) -> User:
        users = self.client.json().get(self.root)
        if users is not None:
            for uid in users:
                user = self.mapper.data_to_user(users[uid])
                if user.username == username and user.password == password:
                    return user
        return None

    def by_email(self, email: str) -> User:
        users = self.client.json().get(self.root)
        if users is not None:
            for uid in users:
                user = self.mapper.data_to_user(users[uid])
                if user.email == email:
                    return user
        return None
