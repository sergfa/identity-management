"""
A module to represent domain event
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class DomainEvent(ABC):
    """
    An abstract class to represent domain event
    """

    """
    Event creation time in seconds.
    """
    created: int


class DomainEventConsumer(ABC):
    """
    An abstract class to represent a consumer of the domain event
    """

    @abstractmethod
    def handle_event(self, event: DomainEvent) -> None:
        """
        This method is invoked by event publisher, see observer/observable pattern

        :param event:  Domain event to handle

        :return: None
        """
        pass


@dataclass(frozen=True)
class UserRegisteredDomainEvent(DomainEvent):
    """
    A class to represent event after user was registered to system

    Attributes:
        user_id, username
    """

    user_id: str
    username: str
