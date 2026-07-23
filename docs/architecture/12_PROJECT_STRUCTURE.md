# 12_PROJECT_STRUCTURE.md

# CONFECTOR Copilot - Project Structure

> "La estructura del proyecto refleja la arquitectura del producto."

---

# 1. Objetivo

Este documento define la organización física del repositorio.

La estructura debe permitir:

- Separación de responsabilidades.
- Desarrollo paralelo.
- Escalabilidad.
- Fácil navegación para humanos y agentes IA.
- Reutilización del Knowledge OS.

---

# 2. Filosofía del Repositorio

CONFECTOR Copilot se divide en tres grandes áreas:

```
Knowledge OS

↓

Domain Packs

↓

Products
```

---

# 3. Arquitectura General

```
confector-platform/

│
├── apps/
│
├── packages/
│
├── knowledge-os/
│
├── domain-packs/
│
├── ai/
│
├── docs/
│
├── resources/
│
├── scripts/
│
└── tests/
```

---

# 4. Estructura Principal

```
confector-platform/

├── apps/
│
├── packages/
│
├── knowledge-os/
│
├── domain-packs/
│
├── ai/
│
├── docs/
│
├── resources/
│
├── scripts/
│
├── tests/
│
├── .env.example
│
├── README.md
│
└── package.json
```

---

# 5. Apps

Contiene aplicaciones completas.

```
apps/

├── web/
│
└── desktop/
```

---

# 5.1 Web App

Responsable de:

- Dashboard.
- Workspace.
- Proyectos.
- Configuración.
- Visualización.

Tecnología:

React.

---

Ejemplo:

```
apps/web/

src/

components/

pages/

features/

hooks/

services/

```

---

# 5.2 Desktop App

Aplicación local.

Responsable de:

- Ejecución offline.
- Archivos locales.
- Acceso al sistema.
- Instalación empresarial.

Tecnología:

Tauri.

---

# 6. Packages

Contiene módulos reutilizables.

```
packages/

├── ui/

├── database/

├── events/

├── templates/

├── exporters/

└── shared/
```

---

# 6.1 UI Package

Componentes visuales compartidos.

Ejemplo:

Buttons.

Cards.

Tables.

Forms.

Layouts.

---

# 6.2 Events Package

Sistema de eventos.

Responsable de:

Event Bus.

Eventos.

Handlers.

Subscriptions.

---

Ejemplo:

```
DocumentUploaded

KnowledgeUpdated

MinuteGenerated
```

---

# 6.3 Templates Package

Sistema visual corporativo.

Contiene:

Logos.

Colores.

Fuentes.

Layouts.

Componentes de documentos.

---

# 6.4 Exporters Package

Conversión de información.

Genera:

DOCX.

PDF.

PPTX.

XLSX.

HTML.

---

# 7. Knowledge OS

El núcleo reutilizable.

```
knowledge-os/

├── memory/

├── graph/

├── search/

├── embeddings/

├── retrieval/

├── context/

└── indexing/
```

---

# 7.1 Memory

Gestiona:

Project Memory.

Working Memory.

Organization Memory.

---

# 7.2 Graph

Knowledge Graph.

Responsable de:

Entidades.

Relaciones.

Consultas.

---

Ejemplo:

```
Carlos

↓

Responsable de

↓

Instalación eléctrica

↓

Relacionado con

↓

Casa Vida
```

---

# 7.3 Search

Sistema de búsqueda.

Incluye:

Keyword search.

Semantic search.

Hybrid search.

---

# 7.4 Embeddings

Gestiona:

Vectorización.

Similarity search.

RAG.

---

# 7.5 Context

Construcción del contexto para IA.

Ejemplo:

Usuario pregunta:

"¿Qué pasó con el presupuesto?"

Context Builder obtiene:

Proyecto.

Reuniones.

Cambios.

Acuerdos.

Documentos.

---

# 8. Domain Packs

Aquí vive la lógica específica de cada industria.

```
domain-packs/

└── construction/
```

---

# Construction Pack

Responsable de:

Obras.

Gerencia.

Contratos.

Avances.

Riesgos.

Minutas.

---

Ejemplo:

```
construction/

entities/

Project

Contract

Meeting

Task

Risk

ChangeOrder
```

---

# 9. AI Layer

Todo lo relacionado con inteligencia artificial.

```
ai/

├── agents/

├── models/

├── prompts/

├── tools/

└── orchestration/
```

---

# 9.1 Agents

Todos los agentes.

```
agents/

├── secretary/

├── analyst/

├── scheduler/

├── designer/

└── quality/
```

---

# 9.2 Models

Adaptadores de modelos.

Ejemplo:

```
models/

openai/

anthropic/

gemini/

local/
```

---

Nunca llamar APIs directamente.

Siempre:

```
Agent

↓

Model Adapter

↓

Provider
```

---

# 9.3 Prompts

Todos los prompts versionados.

```
prompts/

secretary/

minute_v1.md

analyst/

risk_v1.md
```

---

# 9.4 Tools

Herramientas disponibles.

Ejemplo:

OCR.

Speech.

Vision.

Documents.

Search.

---

# 9.5 Orchestration

Director inteligente.

Responsable de:

Planes.

Ejecuciones.

Prioridades.

---

# 10. Backend

Puede vivir como servicio independiente.

```
backend/

├── api/

├── services/

├── repositories/

├── database/

└── workers/
```

---

# API

Endpoints.

Usuarios.

Proyectos.

Documentos.

Procesos.

---

# Services

Casos de uso.

Ejemplo:

GenerateMinuteService.

ProcessDocumentService.

---

# Repositories

Acceso a datos.

Nunca lógica.

---

# Workers

Procesos largos.

Ejemplo:

Procesamiento de audio.

Generación de documentos.

---

# 11. Documentation

```
docs/

├── architecture/

├── development/

├── decisions/

├── guides/

└── api/
```

---

# Architecture

Documentos principales.

```
00_VISION.md

09_SYSTEM_BLUEPRINT.md

```

---

# Decisions

ADR.

Ejemplo:

```
ADR-001-local-first.md

ADR-002-vector-db.md
```

---

# AI Context

Carpeta especial para agentes.

```
ai/

├── architect.md

├── rules.md

├── context.md

├── tasks.md

└── memory.md
```

---

# 12. Resources

Archivos del proyecto.

```
resources/

├── logos/

├── fonts/

├── templates/

├── examples/

└── samples/
```

---

# 13. Scripts

Automizaciones.

```
scripts/

setup.py

migration.py

backup.py

seed.py
```

---

# 14. Tests

```
tests/

├── unit/

├── integration/

└── e2e/
```

---

# 15. Flujo de Desarrollo

Ejemplo:

Crear nuevo agente.

```
ai/agents/

↓

crear carpeta

↓

definir responsabilidad

↓

crear eventos

↓

crear tools

↓

crear tests

↓

documentar
```

---

# 16. Reglas de Dependencias

Permitido:

```
App

↓

Packages

↓

Knowledge OS

↓

Infrastructure
```

---

No permitido:

```
Knowledge OS

↓

CONFECTOR App
```

---

El núcleo nunca depende del producto.

---

# 17. Futuro Multi Producto

La estructura permite:

```
products/

├── confector/

├── legal/

├── manufacturing/

```

Todos usando:

```
knowledge-os/
```

---

# 18. Estructura Final Esperada

```
confector-platform

│

├── apps
│   ├── web
│   └── desktop
│

├── knowledge-os
│   ├── memory
│   ├── graph
│   ├── search
│   └── context
│

├── ai
│   ├── agents
│   ├── prompts
│   └── models
│

├── domain-packs
│   └── construction
│

├── packages
│   ├── events
│   ├── templates
│   └── exporters
│

├── docs
│
└── resources
```

---

# 19. Filosofía Final

La estructura del repositorio no representa únicamente carpetas.

Representa responsabilidades.

Cada módulo tiene un propósito.

Cada dependencia tiene una razón.

Cada pieza puede evolucionar sin destruir el sistema.

CONFECTOR Copilot no está diseñado como una aplicación monolítica.

Está diseñado como una plataforma donde un producto especializado puede crecer sobre un núcleo inteligente reutilizable.