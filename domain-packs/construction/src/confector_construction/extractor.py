import re

from confector_knowledge_os import Entity, Relationship

from .entity_types import AGREEMENT, CON_FECHA, DATE, PERSON, RESPONSABLE_DE

_RESPONSIBLE_PATTERN = re.compile(
    r"([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)?)\s+"
    r"(?:queda responsable de|es responsable de|se encarga de|estará a cargo de|"
    r"está a cargo de)\s+(.+)",
)

_MESES = (
    "enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre"
)
_DATE_PATTERN = re.compile(rf"\d{{1,2}}\s+de\s+(?:{_MESES})(?:\s+de\s+\d{{4}})?", re.IGNORECASE)


def extract(text: str, project_id: str, source_document_id: str | None) -> tuple[list[Entity], list[Relationship]]:
    """Extractor heurístico (regex) para minutas en español — NO usa LLM.

    Detecta el patrón 'Persona queda/es responsable de <tarea>' y fechas en formato
    'N de <mes>'. Es deliberadamente simple: cubre el caso más común de una minuta de
    obra sin depender de un proveedor de IA. Cuando el AI Orchestrator (Sprint 5,
    Secretary Agent) esté disponible, este extractor puede convivir como fallback o
    ser reemplazado por uno basado en LLM sin tocar knowledge-os ni el resto del sistema.
    """
    entities: list[Entity] = []
    relationships: list[Relationship] = []
    persons: dict[str, Entity] = {}
    agreements: list[Entity] = []

    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    for sentence in sentences:
        match = _RESPONSIBLE_PATTERN.search(sentence)
        if match:
            name, task_desc = match.group(1).strip(), match.group(2).strip().rstrip(".")
            person = persons.get(name)
            if person is None:
                person = Entity(project_id=project_id, type=PERSON, label=name, source_document_id=source_document_id)
                persons[name] = person
                entities.append(person)

            agreement = Entity(
                project_id=project_id, type=AGREEMENT, label=task_desc, source_document_id=source_document_id
            )
            entities.append(agreement)
            agreements.append(agreement)
            relationships.append(
                Relationship(project_id=project_id, from_entity_id=person.id, type=RESPONSABLE_DE, to_entity_id=agreement.id)
            )

        for date_match in _DATE_PATTERN.finditer(sentence):
            date_entity = Entity(
                project_id=project_id, type=DATE, label=date_match.group(0), source_document_id=source_document_id
            )
            entities.append(date_entity)
            if agreements:
                relationships.append(
                    Relationship(
                        project_id=project_id,
                        from_entity_id=agreements[-1].id,
                        type=CON_FECHA,
                        to_entity_id=date_entity.id,
                    )
                )

    return entities, relationships
