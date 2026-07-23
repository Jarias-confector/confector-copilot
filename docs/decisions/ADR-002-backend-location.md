# ADR-002: El backend vive en apps/api, no en una carpeta raíz backend/

## Estado
Aceptado.

## Contexto
`05_TECH_STACK.md` ubica el backend en `apps/api`. `12_PROJECT_STRUCTURE.md` §10 describe un `backend/` de nivel raíz con subcarpetas `api/`, `services/`, `repositories/`, `database/`, `workers/` — pero la "Estructura Final Esperada" del mismo documento (§18) no incluye ningún `backend/` raíz. Sin resolver esto, no queda claro dónde vive el código del servidor FastAPI.

## Decisión
El backend FastAPI vive en `apps/api/`, siguiendo ADR-001. La organización interna descrita en 12§10 (`api/`, `services/`, `repositories/`, `database/`, `workers/`) se implementa **dentro** de `apps/api/`, no como carpeta raíz separada:

```
apps/api/
  api/            (endpoints)
  services/       (casos de uso)
  repositories/   (acceso a datos, nunca lógica)
  database/       (conexión, migraciones)
  workers/        (procesos largos: audio, generación de documentos)
```

## Consecuencias
- Coherente con la "Estructura Final Esperada" de 12§18, que no tiene `backend/` raíz.
- `apps/api` depende de `packages/*`, `knowledge-os/*`, `domain-packs/construction` y `ai/*`, nunca al revés (regla de dependencias de 12§16).
