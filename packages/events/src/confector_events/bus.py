from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any, Callable
from uuid import uuid4


@dataclass
class Event:
    """Metadata obligatoria por evento (07_EVENT_ARCHITECTURE §"Event Metadata")."""

    type: str
    payload: dict[str, Any]
    project_id: str | None = None
    id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))


Subscriber = Callable[[Event], None]


class EventBus:
    """Publish/subscribe en proceso. Los módulos nunca se llaman directamente, solo publican y escuchan eventos."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Subscriber]] = defaultdict(list)

    def subscribe(self, event_type: str, handler: Subscriber) -> None:
        self._subscribers[event_type].append(handler)

    def publish(self, event_type: str, payload: dict[str, Any], project_id: str | None = None) -> Event:
        event = Event(type=event_type, payload=payload, project_id=project_id)
        for handler in self._subscribers.get(event_type, []):
            handler(event)
        return event
