import networkx as nx

from .entities import Entity, Relationship


def build_graph(entities: list[Entity], relationships: list[Relationship]) -> nx.MultiDiGraph:
    """NetworkX en MVP (05_TECH_STACK). Construido on-demand a partir de lo persistido — sin estado propio."""
    graph = nx.MultiDiGraph()
    for entity in entities:
        graph.add_node(entity.id, type=entity.type, label=entity.label, **entity.properties)
    for rel in relationships:
        if rel.from_entity_id in graph and rel.to_entity_id in graph:
            graph.add_edge(rel.from_entity_id, rel.to_entity_id, type=rel.type, id=rel.id)
    return graph


def related_entities(graph: nx.MultiDiGraph, entity_id: str) -> list[str]:
    """Vecinos directos (entrantes y salientes) — base para 'encontrar impactos y dependencias' (04_KNOWLEDGE_MODEL)."""
    if entity_id not in graph:
        return []
    return list(set(graph.successors(entity_id)) | set(graph.predecessors(entity_id)))
