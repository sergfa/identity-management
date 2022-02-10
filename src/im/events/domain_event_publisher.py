"""
A module to represent domain event publisher
"""
from im.events import DomainEventConsumer, DomainEvent


class DomainEventPublisher:
    """
    A class to represent domain event publisher
    """

    subscribers: list[DomainEventConsumer]

    def __init__(self):
        self.subscribers = []

    def subscribe(self, consumer: DomainEventConsumer) -> None:
        """
        A method that allows to subscribe to events

        :param consumer: A consumer of the event

        :return: None
        """
        if consumer not in self.subscribers:
            self.subscribers.append(consumer)

    def unsubscribe(self, consumer: DomainEventConsumer):
        """
        Unsubscribe consumer from events

        :param consumer: A consumer to unsubscribe

        :return: None
        """
        if consumer in self.subscribers:
            self.subscribers.remove(consumer)

    def publish(self, event: DomainEvent) -> None:
        """
        Publish event to all subscribers

        :param event: Event to publish

        :return:  None
        """
        for subscriber in self.subscribers:
            subscriber.handle_event(event)
