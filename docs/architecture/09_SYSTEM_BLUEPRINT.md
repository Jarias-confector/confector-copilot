# 09_SYSTEM_BLUEPRINT.md

# CONFECTOR Copilot - System Blueprint

> "El Blueprint es el mapa completo del sistema.
> Define cómo interactúan todos los módulos, cómo fluye la información y cuáles son las responsabilidades de cada componente."

---

# 1. Objetivo

El propósito de este documento es describir la arquitectura funcional completa de CONFECTOR Copilot.

Este documento responde preguntas como:

- ¿Qué ocurre cuando un usuario sube un archivo?
- ¿Cómo se genera una minuta?
- ¿Cómo colaboran los agentes?
- ¿Dónde se almacena el conocimiento?
- ¿Cómo fluye la información entre módulos?
- ¿Cómo se construye la memoria del proyecto?

No contiene detalles de implementación.

No contiene código.

No describe APIs.

Describe únicamente el funcionamiento del sistema.

---

# 2. Principios Arquitectónicos

Toda decisión dentro del sistema debe respetar estos principios.

## Local First

Toda la información pertenece al usuario.

El sistema debe funcionar completamente en local.

Las APIs de IA son opcionales.

---

## Event Driven

Nada ocurre por llamadas directas.

Todo ocurre mediante eventos.

---

## Knowledge First

Los documentos son temporales.

El conocimiento es permanente.

---

## AI Agnostic

El sistema nunca dependerá de un proveedor específico.

Todos los modelos son reemplazables.

---

## Modular

Cada componente debe poder reemplazarse sin afectar al resto.

---

## Domain Driven

Toda la lógica pertenece al dominio.

Nunca a la IA.

---

# 3. Arquitectura General

```text
                        Usuario
                           │
                    Command Center
                           │
                   Project Director
                           │
                Event Bus / Orchestrator
                           │
 ┌──────────────┬──────────────┬──────────────┬──────────────┐
 │              │              │              │
 ▼              ▼              ▼              ▼
Knowledge     Agent        Automation      Workspace
 Engine      Runtime         Engine         Manager
 │              │              │              │
 └──────────────┴──────┬───────┴──────────────┘
                        ▼
                 Template Engine
                        │
                        ▼
                   Export Engine
                        │
                        ▼
                 Word / PPT / PDF
```

---

# 4. Capas del Sistema

El sistema está dividido en siete capas.

## Presentación

Responsable de:

- Interfaz
- Navegación
- Dashboard
- Workspace
- Configuración

Nunca contiene lógica del negocio.

---

## Aplicación

Coordina los casos de uso.

Ejemplos:

Crear Proyecto.

Generar Minuta.

Procesar Audio.

Buscar Información.

---

## Director

Es el cerebro del sistema.

No ejecuta tareas.

Decide qué agentes participan.

Construye planes de ejecución.

Optimiza recursos.

Selecciona modelos IA.

Controla prioridades.

---

## Agentes

Especialistas independientes.

Nunca conocen otros agentes.

Nunca modifican directamente el sistema.

Siempre publican eventos.

---

## Knowledge Engine

Centro de conocimiento.

Responsable de:

- Memoria
- Embeddings
- Relaciones
- Timeline
- Contexto
- Búsquedas
- Historial

Todo agente consulta primero este módulo.

---

## Automation Engine

Convierte conocimiento en acciones.

Ejemplos.

Crear minuta.

Crear presentación.

Crear dashboard.

Crear reporte.

Actualizar cronología.

---

## Infrastructure

Responsable únicamente de:

SQLite

ChromaDB

FastAPI

Archivos

OCR

Whisper

APIs IA

---

# 5. Flujo Principal

Todo comienza con una acción del usuario.

Ejemplo.

Usuario sube un audio.

↓

DocumentUploaded

↓

Secretary Agent

↓

ConversationTranscribed

↓

Knowledge Engine

↓

Entity Extraction

↓

Graph Updated

↓

Timeline Updated

↓

Risk Detection

↓

Knowledge Updated

↓

Automation Suggested

↓

Usuario recibe resultados

---

# 6. Flujo del Conocimiento

Todo el conocimiento sigue el mismo recorrido.

Documento

↓

Extracción

↓

Clasificación

↓

Entidades

↓

Relaciones

↓

Knowledge Graph

↓

Memoria

↓

Búsqueda

↓

Automatizaciones

Nunca se consulta directamente un documento.

Siempre se consulta conocimiento estructurado.

---

# 7. Project Director

El Director coordina todo.

Responsabilidades.

Analizar solicitudes.

Construir planes.

Seleccionar agentes.

Elegir modelos.

Controlar costos.

Administrar contexto.

Detectar errores.

Solicitar validaciones.

Nunca realiza trabajo operativo.

---

# 8. Knowledge Engine

Es el núcleo del sistema.

Contiene.

Document Index

Entity Store

Relationship Store

Timeline

Memory

Embeddings

Search

Reasoning Context

Project State

Es la única fuente oficial de conocimiento.

---

# 9. Graph Engine

Representa relaciones.

Ejemplo.

Persona

↓

Participó

↓

Reunión

↓

Generó

↓

Acuerdo

↓

Relacionado con

↓

Riesgo

Esto permite consultas inteligentes.

---

# 10. Memory System

Tres niveles.

## Working Memory

Contexto temporal.

Solo vive durante una ejecución.

---

## Project Memory

Toda la historia del proyecto.

Nunca se pierde.

---

## Organizational Memory

Conocimiento reutilizable.

Plantillas.

Clientes.

Buenas prácticas.

Procesos.

Lecciones aprendidas.

---

# 11. Agent Runtime

Todos los agentes viven aquí.

Componentes.

Registry

Lifecycle

Scheduler

Context Builder

Prompt Builder

Model Selector

Execution

Validation

Logging

---

# 12. Automation Pipeline

Toda automatización sigue el mismo flujo.

Solicitud

↓

Director

↓

Contexto

↓

Knowledge

↓

Agente

↓

Validación

↓

Template

↓

Exportación

↓

Resultado

---

# 13. Template Engine

Responsable de la identidad corporativa.

Nunca genera contenido.

Solo aplica.

Colores.

Tipografía.

Logos.

Diseño.

Membretes.

Numeración.

Íconos.

Portadas.

Toda salida del sistema pasa por este módulo.

---

# 14. Export Engine

Genera.

Word

PowerPoint

PDF

Excel

Markdown

HTML

Todos utilizando el mismo Template Engine.

---

# 15. Event Bus

Todo el sistema se comunica mediante eventos.

Ventajas.

Desacoplamiento.

Escalabilidad.

Auditoría.

Procesamiento paralelo.

Reintentos.

---

# 16. AI Layer

Responsabilidades.

OCR.

Speech to Text.

Vision.

Reasoning.

Embeddings.

Classification.

Summarization.

Extraction.

Nunca contiene reglas del negocio.

---

# 17. Storage Layer

SQLite

↓

Metadatos

Configuraciones

Usuarios

Proyectos

Historial

---

ChromaDB

↓

Embeddings

Búsquedas

RAG

---

Filesystem

↓

Archivos originales

Exportaciones

Backups

Cache

---

# 18. Seguridad

Nunca modificar archivos originales.

Nunca sobrescribir resultados.

Toda exportación genera una nueva versión.

Toda IA trabaja sobre copias.

Toda ejecución queda registrada.

---

# 19. Escalabilidad

La arquitectura debe permitir incorporar nuevos módulos sin modificar los existentes.

Ejemplos.

Nuevo modelo IA.

Nuevo exportador.

Nuevo agente.

Nuevo proveedor OCR.

Nuevo buscador.

Nuevo template.

---

# 20. Roadmap Técnico

MVP

- Audio
- PDF
- Word
- Minutas
- Acuerdos
- Timeline

V2

- Dashboards
- Presentaciones
- Riesgos
- Reportes

V3

- Copilot Conversacional
- Multiusuario
- Sincronización

V4

- Automatizaciones Autónomas
- Predicción de Riesgos
- Integración BIM
- Microsoft Project
- Primavera P6

---

# 21. Blueprint General

```text
                               Usuario
                                   │
                           Command Center
                                   │
                          Project Director
                                   │
                             Event Bus
                                   │
      ┌──────────────┬──────────────┬──────────────┐
      ▼              ▼              ▼
Knowledge Engine   Agent Runtime   Automation Engine
      │              │              │
      └──────────────┴──────────────┘
                     │
               Template Engine
                     │
               Export Engine
                     │
      Word • PPT • PDF • Excel • HTML
```

---

# 22. Filosofía Final

CONFECTOR Copilot no es un generador de documentos.

Es una plataforma que transforma información dispersa en conocimiento estructurado.

Ese conocimiento es comprendido por un Director Inteligente, enriquecido por un conjunto de agentes especializados y convertido en entregables profesionales mediante procesos automatizados.

La inteligencia artificial es un acelerador.

El conocimiento es el activo principal.

La arquitectura está diseñada para crecer durante años sin depender de una tecnología, proveedor de IA o flujo de trabajo específico.