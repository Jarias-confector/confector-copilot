# knowledge-os/indexing

Indexación de documentos procesados para búsqueda y recuperación rápida.

**Eventos escuchados**: DocumentProcessed. **Eventos publicados**: DocumentIndexed (07_EVENT_ARCHITECTURE).

**No hace**: no procesa ni extrae contenido — eso ocurre antes, en `apps/api/workers` (Document Engine).
