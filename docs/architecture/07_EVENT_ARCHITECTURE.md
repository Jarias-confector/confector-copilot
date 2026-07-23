# 07_EVENT_ARCHITECTURE.md

# Event Driven Architecture

> "Todo lo que ocurre en CONFECTOR Copilot es consecuencia de un evento."

---

# Objetivo

Diseñar un sistema desacoplado donde los módulos reaccionen a eventos del dominio en lugar de comunicarse directamente entre sí.

Esta arquitectura permite:

- Escalabilidad
- Modularidad
- Automatización
- Auditoría
- Trazabilidad
- Fácil mantenimiento

---

# Filosofía

El usuario realiza acciones.

Las acciones generan eventos.

Los módulos reaccionan.

Los módulos nunca se llaman directamente.

---

# Flujo General

Usuario

↓

Acción

↓

Evento

↓

Bus de Eventos

↓

Múltiples módulos reaccionan

↓

Nuevos eventos

↓

Nuevo conocimiento

---

# Event Bus

Durante el MVP existirá un Event Bus local.

No requiere Kafka.

No requiere RabbitMQ.

No requiere Redis.

Simplemente un Event Dispatcher interno.

Ejemplo.

```

DocumentUploaded

↓

EventBus.publish()

↓

Subscribers

↓

Knowledge Engine

↓

Timeline

↓

Notifications

↓

Automation Engine

```

En el futuro podrá migrarse fácilmente.

---

# Tipos de Eventos

## Dominio

Representan cambios del negocio.

---

## Sistema

Representan procesos internos.

---

## IA

Representan tareas relacionadas con modelos IA.

---

## Exportación

Representan generación de documentos.

---

## Usuario

Representan acciones realizadas por personas.

---

# Eventos del Proyecto

ProjectCreated

ProjectUpdated

ProjectArchived

ProjectDeleted

ProjectSettingsChanged

---

# Eventos de Documentos

DocumentUploaded

DocumentUpdated

DocumentDeleted

DocumentIndexed

DocumentProcessed

DocumentClassified

OCRCompleted

EmbeddingGenerated

---

# Eventos de Conversaciones

ConversationCreated

ConversationTranscribed

ConversationAnalyzed

ConversationMerged

ConversationTagged

---

# Eventos del Knowledge Engine

KnowledgeUpdated

EntityDetected

RelationshipDetected

GraphUpdated

MemoryUpdated

ContextRebuilt

---

# Eventos IA

PromptStarted

PromptCompleted

PromptFailed

LLMResponseGenerated

ClassificationCompleted

SummaryGenerated

ReasoningCompleted

---

# Eventos de Automatización

AutomationStarted

AutomationCompleted

AutomationFailed

TemplateApplied

DocumentGenerated

PresentationGenerated

MinuteGenerated

DashboardGenerated

---

# Eventos del Workspace

WorkspaceOpened

WorkspaceSaved

WorkspaceVersionCreated

WorkspaceApproved

WorkspaceExported

---

# Eventos del Timeline

TimelineUpdated

TimelineEventCreated

RiskDetected

DecisionDetected

AgreementDetected

TaskDetected

---

# Eventos de Usuario

UserLoggedIn

UserChangedSettings

APIKeyUpdated

ModelChanged

ProjectSelected

---

# Event Flow

Ejemplo.

Subir Audio

↓

DocumentUploaded

↓

Document Engine escucha

↓

Transcribe

↓

ConversationTranscribed

↓

Knowledge Engine escucha

↓

Extrae entidades

↓

EntityDetected

↓

Graph Engine escucha

↓

Actualiza relaciones

↓

GraphUpdated

↓

Timeline escucha

↓

TimelineUpdated

↓

Copilot recibe nuevo contexto

---

# Subscribers

Cada módulo define qué eventos escucha.

Ejemplo.

Knowledge Engine

Escucha.

DocumentUploaded

ConversationTranscribed

DocumentUpdated

---

Graph Engine

Escucha.

EntityDetected

RelationshipDetected

KnowledgeUpdated

---

Automation Engine

Escucha.

KnowledgeUpdated

ProjectOpened

WorkspaceApproved

---

Template Engine

Escucha.

PresentationGenerated

MinuteGenerated

ReportGenerated

---

# Event Store

Todos los eventos importantes deberán almacenarse.

Objetivos.

Auditoría.

Historial.

Depuración.

Analytics.

Aprendizaje futuro.

---

# Event Metadata

Todo evento contiene.

ID

Timestamp

Usuario

Proyecto

Tipo

Origen

Payload

Versión

---

# Idempotencia

Un evento nunca debe producir efectos duplicados.

Cada Subscriber debe verificar.

¿Ya procesé este evento?

---

# Retries

Si un módulo falla.

El evento permanece pendiente.

Debe poder reprocesarse.

---

# Prioridades

Alta

DocumentUploaded

ConversationProcessed

KnowledgeUpdated

---

Media

DashboardUpdated

SummaryGenerated

---

Baja

Analytics

Logs

Estadísticas

---

# Event Replay

El sistema debe poder reconstruir un proyecto únicamente reproduciendo eventos.

Esto permitirá.

Auditoría.

Debug.

Versionado.

Machine Learning futuro.

---

# Event Chaining

Un evento puede producir otros.

Ejemplo.

DocumentUploaded

↓

ConversationProcessed

↓

EntityDetected

↓

KnowledgeUpdated

↓

GraphUpdated

↓

TimelineUpdated

↓

AutomationSuggested

---

# Principios

Los eventos son inmutables.

Nunca se editan.

Nunca se eliminan.

Únicamente se agregan nuevos.

---

# Responsabilidades

Los eventos describen.

Qué ocurrió.

Nunca.

Qué debe hacerse.

Los módulos deciden cómo reaccionar.

---

# Beneficios

Desacoplamiento.

Escalabilidad.

Historial completo.

Procesamiento paralelo.

Mayor resiliencia.

Automatizaciones ilimitadas.

---

# Arquitectura

Usuario

↓

Core

↓

Event Bus

↓

Knowledge Engine

↓

Graph Engine

↓

Automation Engine

↓

Workspace

↓

Template Engine

↓

Exportación

---

# Visión

CONFECTOR Copilot no ejecuta funciones.

CONFECTOR Copilot responde a eventos.

Todo cambio dentro del sistema deja una huella.

Todo conocimiento nace de una cadena de eventos.

La historia completa de un proyecto puede reconstruirse únicamente reproduciendo dichos eventos.