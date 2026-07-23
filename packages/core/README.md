# packages/core

Dominio genérico de plataforma (ADR-003), reutilizable por futuros productos (12§17: legal, manufacturing, etc.).

**Responsabilidad**: entidades Project (contenedor/tenant), User, Company, configuración, permisos, licencias (06_DOMAIN_MODEL Core Context).

**No hace**: no conoce vocabulario de construcción (eso vive en `domain-packs/construction`), no conoce IA ni frameworks (Domain Layer, 11_DEVELOPMENT_GUIDELINES §5).
