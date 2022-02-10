from abc import ABC
from dataclasses import dataclass, field


@dataclass()
class Entity(ABC):
    """An abstract class to represent an entity"""

    _uid: str = field(hash=True)

    @property
    def uid(self) -> str:
        return self._uid

    @classmethod
    def next_id(cls) -> str:
        pass
