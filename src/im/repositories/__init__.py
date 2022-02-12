"""
A module to represent an interface for repository
"""
from abc import ABC, abstractmethod
from uuid import uuid4
from im.model import Entity


class Repository(ABC):
    """A class to represent an interface for repository"""

    @abstractmethod
    def by_id(self, id_: str) -> Entity:
        """
        Get entity by id
        :param id_: str: The id of the entity
        :return: Entity: The queried entity
        """
        pass

    @abstractmethod
    def insert(self, entity: Entity) -> None:
        """
        Add new entity
        :param entity: Entity: entity to add
        :return: None
        """
        pass

    @abstractmethod
    def update(self, entity: Entity) -> None:
        """
        Update entity
        :param entity: Entity: entity to update
        :return: None
        """
        pass

    @abstractmethod
    def remove(self, id_: str) -> None:
        """
        Remove entity
        :param id_: str: The id of the entity to remove
        :return: None
        """
        pass

    @abstractmethod
    def list(self) -> list[Entity]:
        """
        Get all entities
        :return: list [Entity]
        """
        pass

    @classmethod
    def next_identifier(cls) -> str:
        """
        Generate next identifier that will be used for creating a new entity
        :return: str: the identifier
        """
        return str(uuid4())
