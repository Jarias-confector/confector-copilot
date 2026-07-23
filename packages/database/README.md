# packages/database

Acceso a datos compartido (SQLite MVP → PostgreSQL futuro, 05_TECH_STACK).

**Responsabilidad**: conexión, esquema, migraciones, Repository Pattern (06_DOMAIN_MODEL §"Repository Pattern").

**No hace**: nunca contiene lógica de negocio — los módulos nunca acceden a la base de datos directamente, siempre vía Repository (11_DEVELOPMENT_GUIDELINES §15).
