# knowledge-os/embeddings

Vectorización y similarity search (ChromaDB, 05_TECH_STACK). Modelos recomendados: BAAI/bge-large-en-v1.5, BAAI/bge-m3, jina-embeddings-v3 — nunca dependemos de OpenAI para esto.

**Eventos publicados**: EmbeddingGenerated (07_EVENT_ARCHITECTURE).

**No hace**: no decide qué modelo de embeddings usar en tiempo de ejecución para el negocio — eso es configuración, no lógica de dominio.
