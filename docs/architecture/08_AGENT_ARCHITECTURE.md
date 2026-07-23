# 08_AGENT_ARCHITECTURE.md

# Agent Architecture

> "Un agente no es un modelo de IA.
>
> Un agente es un especialista que posee un objetivo, memoria, herramientas y responsabilidades claramente definidas."

---

# Filosofía

CONFECTOR Copilot no utiliza una única inteligencia artificial.

Utiliza un equipo de especialistas.

Cada agente tiene una única responsabilidad.

Nunca intenta resolver todo.

Los agentes colaboran entre sí mediante eventos y conocimiento compartido.

---

# Objetivos

La arquitectura de agentes debe permitir:

- Especialización
- Escalabilidad
- Independencia
- Reutilización
- Trazabilidad
- Fácil incorporación de nuevos agentes

---

# Arquitectura General

                    Usuario

                        │

                Command Center

                        │

                AI Orchestrator

                        │

        ┌───────────────┼───────────────┐

        ▼               ▼               ▼

  Operational       Knowledge      Communication

     Agents           Agents           Agents

        │               │               │

        └───────────────┼───────────────┘

                        ▼

                Knowledge Engine

                        ▼

                 Project Memory

---

# Tipos de Agentes

Los agentes se clasifican según su propósito.

---

## Operational Agents

Ejecutan tareas.

Ejemplos:

Secretary

Scheduler

Designer

Reporter

Exporter

---

## Knowledge Agents

Analizan información.

Ejemplos:

Analyst

Risk Detector

Entity Extractor

Relationship Builder

Timeline Builder

Knowledge Curator

---

## Communication Agents

Interactúan con el usuario.

Ejemplos:

Copilot

Explainer

Reviewer

QA Assistant

---

# Ciclo de Vida

Todo agente sigue el mismo flujo.

Recibir evento

↓

Construir contexto

↓

Consultar memoria

↓

Ejecutar razonamiento

↓

Generar resultado

↓

Publicar eventos

↓

Esperar siguiente tarea

---

# Componentes Internos

Todo agente posee.

Identidad.

Responsabilidad.

Objetivo.

Herramientas.

Contexto.

Memoria.

Prompts.

Configuración.

Eventos escuchados.

Eventos publicados.

---

# Interfaz Base

Todo agente implementa.

initialize()

handle_event()

build_context()

reason()

execute()

validate()

publish_events()

cleanup()

---

# Herramientas

Los agentes nunca implementan lógica directamente.

Utilizan herramientas.

Ejemplos.

Search

Summarize

Graph Search

OCR

Vision

Document Generator

PowerPoint Generator

Excel Generator

Timeline Builder

---

# Comunicación

Los agentes nunca hablan entre ellos directamente.

Siempre utilizan.

Event Bus

↓

Knowledge Engine

↓

Shared Memory

---

# Contexto

Antes de ejecutar cualquier tarea.

El agente construye contexto.

Proyecto

↓

Documentos relacionados

↓

Historial

↓

Memoria

↓

Graph

↓

Embeddings

↓

Preferencias usuario

↓

Prompt

↓

Modelo IA

---

# Memoria

Cada agente posee.

Memoria temporal.

Memoria de ejecución.

Nunca memoria permanente.

Toda memoria permanente pertenece al Knowledge Engine.

---

# AI Models

Cada agente puede utilizar distintos modelos.

Ejemplo.

Secretary

↓

Whisper

↓

GPT

---

Designer

↓

Claude

↓

HTML Renderer

---

Risk Detector

↓

Gemini

↓

Reasoning

---

El agente nunca conoce la API.

Solo conoce el LLM Adapter.

---

# Eventos

Todo agente escucha eventos.

Ejemplo.

Secretary

Escucha.

ConversationUploaded

ConversationTranscribed

---

Analyst

Escucha.

KnowledgeUpdated

TimelineUpdated

---

Designer

Escucha.

PresentationRequested

MinuteRequested

---

QA

Escucha.

DocumentGenerated

PresentationGenerated

---

# Reglas

Un agente solo resuelve un problema.

Nunca múltiples.

---

Los agentes nunca almacenan datos.

---

Nunca acceden directamente a SQLite.

---

Nunca llaman otro agente.

---

Nunca modifican conocimiento.

Publican eventos.

---

Nunca conocen React.

---

Nunca conocen FastAPI.

---

Nunca conocen la interfaz.

---

# Beneficios

Especialización.

Código simple.

Escalabilidad.

Mantenimiento.

Nuevos agentes.

Modelos IA independientes.

---

# Arquitectura Objetivo

                 AI Orchestrator

                        │

     ┌──────────────────┼──────────────────┐

     ▼                  ▼                  ▼

Secretary         Analyst           Scheduler

     ▼                  ▼                  ▼

Knowledge Engine    Graph Engine     Timeline

     ▼                  ▼                  ▼

Shared Memory    Shared Memory    Shared Memory

---

# Filosofía Final

No construimos una IA.

Construimos un equipo.

Cada agente representa un especialista.

El usuario nunca habla con modelos de lenguaje.

Habla con expertos virtuales que conocen profundamente el estado del proyecto.