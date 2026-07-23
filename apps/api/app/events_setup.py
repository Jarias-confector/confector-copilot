from confector_events import EventBus, event_types

from app.logging import logger

_bus = EventBus()


def _log_subscriber(event) -> None:
    logger.info(f"[event] {event.type} project={event.project_id} id={event.id}")


for _event_type in (
    event_types.PROJECT_CREATED,
    event_types.DOCUMENT_UPLOADED,
    event_types.DOCUMENT_PROCESSED,
    event_types.ENTITY_DETECTED,
    event_types.RELATIONSHIP_DETECTED,
    event_types.KNOWLEDGE_UPDATED,
    event_types.TIMELINE_UPDATED,
):
    _bus.subscribe(_event_type, _log_subscriber)


def get_event_bus() -> EventBus:
    return _bus
