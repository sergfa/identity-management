from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, value) -> bool:
        """Return: True if value is valid, otherwise returns False"""
        pass
