# CONFECTOR Copilot

Knowledge Operating System para gerencia de proyectos de construcción. Captura información dispersa (audio, PDF, Word, Excel, fotos, correos) y la transforma en conocimiento estructurado y entregables profesionales (minutas, reportes, presentaciones).

Primer producto de la plataforma Confector.

## Documentación

Toda la arquitectura vive en [`docs/architecture/`](docs/architecture/) — léela antes de tocar código:

| Documento | Contenido |
|---|---|
| [00_VISION.md](docs/architecture/00_VISION.md) | Visión, problema, misión |
| [01_PRODUCT_PRINCIPLES.md](docs/architecture/01_PRODUCT_PRINCIPLES.md) | Principios innegociables |
| [02_PRODUCT_ARCHITECTURE.md](docs/architecture/02_PRODUCT_ARCHITECTURE.md) | Módulos y comunicación |
| [03_USER_EXPERIENCE.md](docs/architecture/03_USER_EXPERIENCE.md) | UX y filosofía de navegación |
| [04_KNOWLEDGE_MODEL.md](docs/architecture/04_KNOWLEDGE_MODEL.md) | Modelo de conocimiento (entidades/relaciones) |
| [05_TECH_STACK.md](docs/architecture/05_TECH_STACK.md) | Stack tecnológico |
| [06_DOMAIN_MODEL.md](docs/architecture/06_DOMAIN_MODEL.md) | Domain-Driven Design |
| [07_EVENT_ARCHITECTURE.md](docs/architecture/07_EVENT_ARCHITECTURE.md) | Arquitectura orientada a eventos |
| [08_AGENT_ARCHITECTURE.md](docs/architecture/08_AGENT_ARCHITECTURE.md) | Arquitectura de agentes IA |
| [09_SYSTEM_BLUEPRINT.md](docs/architecture/09_SYSTEM_BLUEPRINT.md) | Blueprint completo del sistema |
| [10_MVP_ROADMAP.md](docs/architecture/10_MVP_ROADMAP.md) | Roadmap del MVP por sprints |
| [11_DEVELOPMENT_GUIDELINES.md](docs/architecture/11_DEVELOPMENT_GUIDELINES.md) | Reglas obligatorias de desarrollo |
| [12_PROJECT_STRUCTURE.md](docs/architecture/12_PROJECT_STRUCTURE.md) | Estructura física del repositorio |
| [13_ARCHITECT.md](docs/architecture/13_ARCHITECT.md) | Contexto para agentes de desarrollo IA |

Decisiones de arquitectura (ADRs) en [`docs/decisions/`](docs/decisions/).

## Estructura

```
apps/           web y desktop (Tauri + React)
packages/       módulos reutilizables (core, ui, database, events, templates, exporters, shared)
knowledge-os/   núcleo agnóstico de dominio (memory, graph, search, embeddings, retrieval, context, indexing)
domain-packs/   vocabulario específico de industria (construction)
ai/             agentes, modelos, prompts, herramientas, orquestación
docs/           arquitectura, decisiones, guías
resources/      logos, fuentes, plantillas
scripts/        automatizaciones
tests/          integración y e2e (unit tests viven dentro de cada módulo)
```

## Estado

Fase de inicialización — estructura y documentación completas. Sin código de producto todavía (ver `docs/decisions/` para las decisiones que preceden la implementación).
