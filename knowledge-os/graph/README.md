# knowledge-os/graph

Knowledge Graph — entidades y relaciones genéricas (04_KNOWLEDGE_MODEL). NetworkX en el MVP, Neo4j/Memgraph en V2 (05_TECH_STACK).

**Responsabilidad**: almacenar y consultar relaciones (ej. PERSONA → RESPONSABLE_DE → PENDIENTE), encontrar impactos y dependencias.

**Eventos escuchados**: EntityDetected, RelationshipDetected. **Eventos publicados**: GraphUpdated (07_EVENT_ARCHITECTURE).

**No hace**: no sabe qué significa una entidad para el negocio — eso lo define `domain-packs/construction`.
