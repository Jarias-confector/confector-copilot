from confector_events import EventBus, event_types

from app.logging import logger

_bus = EventBus()


def _log_subscriber(event) -> None:
    logger.info(f"[event] {event.type} project={event.project_id} id={event.id}")


_bus.subscribe(event_types.DOCUMENT_UPLOADED, _log_subscriber)
_bus.subscribe(event_types.DOCUMENT_PROCESSED, _log_subscriber)
_bus.subscribe(event_types.PROJECT_CREATED, _log_subscriber)


def get_event_bus() -> EventBus:
    return _bus
