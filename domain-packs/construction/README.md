# domain-packs/construction

Lógica y vocabulario específicos de gerencia de proyectos de construcción (12§8, ADR-003).

**Responsabilidad**: entidades de negocio (Contract, Meeting, Task, Risk, ChangeOrder), reglas propias de obra (ej. "todo acuerdo debe tener responsable", "un riesgo nunca se elimina, solo cambia de estado" — 06_DOMAIN_MODEL §"Reglas de Negocio").

**No hace**: no implementa mecánica de memoria/grafo/búsqueda (eso es `knowledge-os/`, agnóstico de dominio), no conoce React/FastAPI/proveedores IA (11_DEVELOPMENT_GUIDELINES §5).
