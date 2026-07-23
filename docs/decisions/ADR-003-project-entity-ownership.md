# ADR-003: Propiedad de la entidad Project — packages/core vs domain-packs/construction

## Estado
Aceptado.

## Contexto
`06_DOMAIN_MODEL.md` ubica "Proyecto" en el *Core Context* (junto a Usuarios, Empresas, Configuraciones, Permisos, Licencias) — es decir, como concepto genérico de plataforma. Sin embargo, `12_PROJECT_STRUCTURE.md` y `13_ARCHITECT.md` proponen la jerarquía `Knowledge OS → Construction Domain Pack → CONFECTOR Copilot`, y ubican entidades como `Project` dentro de `domain-packs/construction/entities`. `13_ARCHITECT.md` §10 exige explícitamente que "Knowledge OS debe poder existir sin CONFECTOR" — es decir, sin vocabulario de construcción. Si `Project` fuera puramente de construcción, no podría existir una plataforma multi-producto futura (12§17 menciona `products/{confector, legal, manufacturing}`) sin duplicar el concepto de proyecto/tenant en cada domain pack.

## Decisión
Se separa el concepto en dos capas:

- **`packages/core`**: `Project` como contenedor/tenant genérico — id, nombre, usuarios, workspace, knowledge base asociada. Reutilizable por cualquier producto futuro sobre la plataforma Confector.
- **`domain-packs/construction`**: vocabulario y reglas específicas de construcción que *decoran* ese contenedor — `Contract`, `ChangeOrder`, tipos de reunión de obra, plantillas de minuta, `Risk`/`Agreement` con semántica de obra.
- **`knowledge-os/`**: permanece 100% agnóstico de dominio — solo mecánica (memory, graph, search, embeddings, retrieval, indexing, context). Nunca sabe qué es un "Acuerdo" o una "Minuta", solo entidades y relaciones genéricas.

## Consecuencias
- Un futuro `domain-packs/legal` o `domain-packs/manufacturing` podría reutilizar `packages/core` (Project/User/Company) y `knowledge-os/` sin cambios, tal como exige 12§17.
- El *Core Context* de `06_DOMAIN_MODEL.md` mapea a `packages/core`; el resto de sus Bounded Contexts (Knowledge, Automation, Workspace, AI, Branding) mapean a `knowledge-os/`, `ai/`, `packages/events`, `packages/ui`/`apps/*` y `packages/templates` respectivamente.
