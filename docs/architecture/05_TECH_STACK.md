# 05_TECH_STACK.md

# Arquitectura Tecnológica

> Este documento define el stack tecnológico oficial de CONFECTOR Copilot.
>
> Toda nueva dependencia o tecnología deberá justificarse y respetar los principios definidos en `01_PRODUCT_PRINCIPLES.md`.

---

# Filosofía Tecnológica

CONFECTOR Copilot está diseñado bajo los siguientes principios:

- Local First
- AI First
- Modular
- AI Agnostic
- Escalable
- Offline Friendly
- Fácil de mantener
- Independiente del proveedor de IA

El objetivo es construir una plataforma que pueda evolucionar durante años sin depender de una tecnología específica.

---

# Arquitectura General

```
                  CONFECTOR Copilot

                ┌──────────────────────┐
                │   Desktop Application │
                │   React + Tauri       │
                └──────────┬────────────┘
                           │
                    Local API (FastAPI)
                           │
 ┌─────────────────────────┼─────────────────────────┐
 │                         │                         │
 ▼                         ▼                         ▼
SQLite                 ChromaDB              Graph Engine
 │                         │                         │
 └─────────────────────────┼─────────────────────────┘
                           │
                    AI Orchestrator
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 OpenAI API         Claude API          Ollama Local
 Gemini API         OpenRouter
```

---

# Monorepo

El proyecto utilizará una arquitectura Monorepo.

```
confector-copilot/

apps/
    desktop/
    api/

packages/
    ai-engine/
    automation-engine/
    knowledge-engine/
    graph-engine/
    template-engine/
    shared/
    ui/

storage/

resources/

scripts/

tests/

docs/
```

---

# Frontend

## React

Motivo:

- Ecosistema maduro
- Gran comunidad
- Excelente integración con TypeScript
- Compatible con Tauri

---

## Vite

Motivo:

- Desarrollo extremadamente rápido
- Excelente experiencia para escritorio
- Build optimizado

---

## TypeScript

Obligatorio.

Todo el código frontend deberá escribirse en TypeScript.

No se permitirá JavaScript puro.

---

## TailwindCSS

Framework principal de estilos.

---

## shadcn/ui

Biblioteca oficial de componentes.

Razones:

- Accesible
- Personalizable
- Moderna
- Fácil mantenimiento

---

## React Query (TanStack Query)

Para manejo de estado del servidor.

No almacenar datos remotos manualmente.

---

## React Hook Form

Formularios.

---

## Zod

Validación compartida.

---

# Desktop

## Tauri

Decisión oficial.

No Electron.

Razones:

- Muchísimo menor consumo de memoria.
- Ejecutables pequeños.
- Excelente integración con Rust.
- Acceso nativo al sistema.
- Ideal para aplicaciones IA.

---

# Backend

## Python

Lenguaje oficial.

Todo el backend será desarrollado en Python.

---

## FastAPI

Framework oficial.

Razones:

- Alto rendimiento.
- Async.
- Tipado.
- OpenAPI automático.
- Excelente para IA.

---

## Uvicorn

Servidor ASGI.

---

## Pydantic

Validación de modelos.

---

## SQLModel

ORM principal.

Combina SQLAlchemy + Pydantic.

---

# Base de Datos

## SQLite

Versión MVP.

Almacenará:

- Usuarios
- Proyectos
- Configuración
- Documentos
- Versiones
- Historial
- Automatizaciones

---

## PostgreSQL

Migración futura.

No será necesario modificar el dominio.

---

# Base Vectorial

## ChromaDB

Decisión oficial.

Razones:

- Persistencia local.
- Fácil integración.
- Excelente rendimiento.
- Open Source.
- Sin infraestructura compleja.

---

# Knowledge Graph

## MVP

NetworkX

Razones:

- Muy ligero.
- Todo local.
- Sin servidor adicional.
- Excelente para pruebas.

---

## V2

Neo4j

o

Memgraph

Cuando el volumen de datos lo justifique.

---

# Procesamiento IA

## Whisper

Transcripción oficial.

---

## WhisperX

Versión futura.

Permite:

- Speaker Diarization
- Timestamps precisos
- Mejor alineación

---

## OCR

PaddleOCR

Razones:

- Mucho mejor que Tesseract.
- Soporta documentos complejos.
- Mejor precisión.

---

## Documentos

PyMuPDF

Lectura PDF.

---

python-docx

Word.

---

python-pptx

PowerPoint.

---

openpyxl

Excel.

---

Pillow

Imágenes.

---

Markdown

Soporte nativo.

---

# Embeddings

No dependeremos de OpenAI.

Modelos recomendados:

- BAAI/bge-large-en-v1.5
- BAAI/bge-m3
- jina-embeddings-v3

Los embeddings deberán poder cambiarse fácilmente.

---

# LLM Adapter

Toda IA deberá implementarse mediante adaptadores.

Nunca consumir APIs directamente desde la lógica de negocio.

```
LLMProvider

↓

OpenAIProvider

ClaudeProvider

GeminiProvider

OllamaProvider

OpenRouterProvider
```

Todos deberán implementar la misma interfaz.

---

# AI Engine

```
ai-engine/

providers/

prompts/

vision/

audio/

ocr/

embeddings/

reasoning/

classification/

summarization/

validation/

utils/
```

El AI Engine nunca conocerá React.

Nunca conocerá SQLite.

Nunca conocerá la interfaz.

---

# Knowledge Engine

```
knowledge-engine/

ingestion/

entity-extractor/

relationship-extractor/

graph-builder/

timeline/

memory/

search/

reasoning/

context/
```

Su responsabilidad es convertir información en conocimiento.

---

# Automation Engine

```
automation-engine/

minutas/

reportes/

presentaciones/

dashboards/

bitacoras/

riesgos/

cronologias/

pendientes/
```

Cada automatización será completamente independiente.

---

# Template Engine

```
template-engine/

branding/

word/

powerpoint/

excel/

pdf/

html/

assets/
```

Todo documento generado pasa por aquí.

---

# Logging

Loguru.

---

# Configuración

Pydantic Settings.

Variables:

.env

.env.local

.env.production

---

# Testing

pytest

pytest-asyncio

coverage

---

# Calidad de Código

ruff

black

mypy

pre-commit

---

# Seguridad

python-dotenv

keyring

Las API Keys nunca deberán almacenarse en texto plano.

Siempre usar almacenamiento seguro cuando el sistema operativo lo permita.

---

# Almacenamiento

```
storage/

projects/

cache/

temp/

exports/

backups/

models/
```

---

# Caché

DiskCache

Para:

Embeddings

OCR

Transcripciones

Resultados IA

Reducir costos.

---

# Comunicación Interna

REST para el MVP.

Arquitectura preparada para migrar posteriormente a:

- gRPC
- Message Queue
- Event Bus

---

# Exportación

Formatos soportados:

- Word
- PDF
- PowerPoint
- Excel
- Markdown
- HTML

---

# Dependencias Prohibidas

No utilizar:

- Electron
- Flask
- Django
- FAISS (MVP)
- Dependencias que oculten excesivamente la lógica del negocio

---

# Decisiones Técnicas

## Preferimos escribir nuestra propia lógica antes que depender de frameworks complejos.

El producto debe ser entendible.

No mágico.

---

## El conocimiento pertenece al dominio.

No al modelo de IA.

---

## Toda IA debe poder reemplazarse sin modificar la aplicación.

---

## Toda automatización debe reutilizar el mismo motor de conocimiento.

---

## Ningún módulo debe depender directamente de otro módulo.

Toda comunicación se realizará mediante interfaces claramente definidas.

---

# Arquitectura Objetivo

```
                     CONFECTOR Copilot

                            UI

                             │

                      Command Center

                             │

                      AI Orchestrator

                             │

      ┌──────────────────────┼──────────────────────┐

      ▼                      ▼                      ▼

Knowledge Engine      Automation Engine     Template Engine

      │                      │                      │

      └──────────────────────┼──────────────────────┘

                             ▼

                    Storage Layer

      SQLite + ChromaDB + Graph Engine

                             ▼

                  Document Processing Pipeline

                             ▼

Audio │ PDF │ Word │ Excel │ Images │ Email │ Markdown
```

---

# Principio Final

La tecnología es un medio.

El verdadero producto es el conocimiento.

Toda decisión técnica deberá contribuir a capturar, comprender y reutilizar el conocimiento generado durante la ejecución de un proyecto.