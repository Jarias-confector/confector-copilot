from .entities import Entity


def search_entities(query: str, entities: list[Entity]) -> list[Entity]:
    """Keyword search (MVP). Semantic search vía embeddings queda para cuando el volumen lo justifique (05_TECH_STACK)."""
    needle = query.lower().strip()
    if not needle:
        return []
    return [e for e in entities if needle in e.label.lower() or needle in str(e.properties).lower()]
