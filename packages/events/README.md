# packages/events

Event Bus interno del sistema (07_EVENT_ARCHITECTURE). Sin Kafka/RabbitMQ/Redis en el MVP — Event Dispatcher local, migrable después.

**Responsabilidad**: publish/subscribe, definiciones de eventos de dominio, idempotencia, reintentos, Event Store.

**Eventos**: ver catálogo completo en `docs/architecture/07_EVENT_ARCHITECTURE.md` (DocumentUploaded, KnowledgeUpdated, MinuteGenerated, etc.).

**No hace**: no decide qué hacer con un evento — eso lo deciden los módulos suscriptores.
