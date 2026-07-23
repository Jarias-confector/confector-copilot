# Convención de tests

`11_DEVELOPMENT_GUIDELINES.md` §17 exige unit e integration tests por módulo. `05_TECH_STACK.md` y `12_PROJECT_STRUCTURE.md` además piden un `tests/` de nivel raíz. Para evitar duplicidad:

- `tests/unit/`, `tests/integration/` (raíz): solo pruebas de integración entre módulos y pruebas end-to-end (`tests/e2e/`).
- Cada módulo (`packages/*`, `knowledge-os/*`, `domain-packs/construction`, `ai/*`, `apps/*/`) mantiene su propio `tests/` con sus unit tests, junto a `domain/`, `application/`, `infrastructure/` cuando aplique (11§6).

Prioridad de cobertura (11§17): Domain → Application → Infrastructure → UI.
