# ADR-004: El MVP construye únicamente apps/desktop

## Estado
Aceptado.

## Contexto
`01_PRODUCT_PRINCIPLES.md` principio #5 (Local First) establece que los archivos deben permanecer en el equipo del usuario y el procesamiento local tiene prioridad. `05_TECH_STACK.md` decide explícitamente Tauri sobre Electron y describe la arquitectura general centrada en una "Desktop Application (React + Tauri)" con una API local. `12_PROJECT_STRUCTURE.md` lista tanto `apps/web` como `apps/desktop` sin priorizar uno sobre otro, y `10_MVP_ROADMAP.md` solo menciona "Frontend inicial" en el Sprint 0 sin especificar cuál.

## Decisión
El MVP (Sprints 0–8 de `10_MVP_ROADMAP.md`) construye únicamente `apps/desktop` (Tauri + React + API FastAPI local). `apps/web` queda como carpeta placeholder, documentada pero sin implementación, reservada para V2+ cuando el producto requiera acceso multiusuario/remoto (mencionado como V3 "Multiusuario, Sincronización" en `09_SYSTEM_BLUEPRINT.md` §20).

## Consecuencias
- Evita construir dos frontends en paralelo durante el MVP, contradiciendo el principio de "Simplicidad primero" de `11_DEVELOPMENT_GUIDELINES.md`.
- Todo el Walking Skeleton inicial (`13_ARCHITECT.md` §20: Frontend → Backend → DB → AI Provider → Document Generator) se implementa dentro de `apps/desktop` + `apps/api`.
