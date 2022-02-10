from abc import ABC, abstractmethod
from im.model import Entity


class Repository(ABC):
    @abstractmethod
    def by_id(self, id_: str) -> Entity:
        pass

    @abstractmethod
    def insert(self, entity: Entity):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def list(self) -> [Entity]:
        pass
