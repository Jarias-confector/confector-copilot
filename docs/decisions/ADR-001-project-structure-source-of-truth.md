# ADR-001: 12_PROJECT_STRUCTURE.md como fuente de verdad de la estructura física

## Estado
Aceptado.

## Contexto
`05_TECH_STACK.md` propone una estructura de carpetas (`apps/{desktop,api} + packages/{ai-engine,automation-engine,knowledge-engine,graph-engine,template-engine,shared,ui}`) distinta de la que propone `12_PROJECT_STRUCTURE.md` (`apps/{web,desktop} + packages/{ui,database,events,templates,exporters,shared} + knowledge-os/ + domain-packs/construction/ + ai/{agents,models,prompts,tools,orchestration}`). Ambos documentos son parte de la documentación oficial y no se puede implementar ambas estructuras a la vez.

## Decisión
`12_PROJECT_STRUCTURE.md` es la fuente de verdad para la disposición física de carpetas del repositorio, incluyendo su sección 18 ("Estructura Final Esperada"). `05_TECH_STACK.md` sigue siendo la fuente de verdad para decisiones de lenguajes, frameworks y bases de datos (React, Tauri, FastAPI, SQLite, ChromaDB, NetworkX, Whisper, etc.) — estas decisiones no dependen de en qué carpeta viva el código, solo se reubican dentro de la estructura de 12.

## Consecuencias
- Los módulos que 05 agrupaba en `packages/` (ai-engine, knowledge-engine, graph-engine) se reparten ahora entre `knowledge-os/` (mecánica agnóstica) y `ai/` (agentes, modelos, prompts) según 12.
- `automation-engine` y `template-engine` de 05 corresponden a `ai/orchestration` + `packages/events` y `packages/templates` + `packages/exporters` respectivamente en la estructura de 12.
- Ver también ADR-002 (ubicación del backend) y ADR-003 (propiedad de la entidad Project), que resuelven ambigüedades derivadas de este cambio de estructura.
