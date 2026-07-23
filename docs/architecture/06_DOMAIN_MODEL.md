# 06_DOMAIN_MODEL.md

# Domain Model

> "El software debe representar cómo funciona el negocio, no cómo funciona la base de datos."

---

# Objetivo

Este documento define el dominio de negocio de CONFECTOR Copilot utilizando principios de Domain-Driven Design (DDD).

Aquí se describen las entidades principales, sus responsabilidades, reglas de negocio, relaciones y comportamientos.

Este documento es independiente de cualquier tecnología.

Nunca debe contener detalles de implementación.

---

# Filosofía

CONFECTOR Copilot no administra documentos.

Administra conocimiento.

No administra archivos.

Administra proyectos.

No administra IA.

Administra procesos.

La IA únicamente acelera esos procesos.

---

# Ubiquitous Language

Todos los desarrolladores deberán utilizar exactamente estos términos.

Nunca inventar nuevos nombres para el mismo concepto.

## Proyecto

Unidad principal de trabajo.

Representa una obra, desarrollo o servicio administrado por CONFECTOR.

---

## Workspace

Espacio operativo donde trabaja el usuario.

No es una carpeta.

No es una pantalla.

Es el entorno de trabajo del proyecto.

---

## Documento

Cualquier archivo cargado al sistema.

Ejemplos:

- PDF
- Word
- Excel
- Imagen
- Audio
- Video
- Email
- Markdown
- ZIP

El documento es únicamente una fuente de información.

---

## Conversación

Representa cualquier interacción humana.

Puede provenir de:

- Reunión
- Llamada
- Nota de voz
- WhatsApp
- Teams
- Zoom

Una conversación puede producir múltiples entidades.

---

## Minuta

Documento generado automáticamente.

Nunca es el origen del conocimiento.

Es un resultado.

---

## Conocimiento

Información estructurada derivada del análisis IA.

Ejemplos:

Acuerdos.

Pendientes.

Responsables.

Fechas.

Cambios.

Riesgos.

Decisiones.

---

## Automatización

Proceso completo ejecutado por el sistema.

Ejemplos.

Crear minuta.

Generar presentación.

Crear Dashboard.

Extraer acuerdos.

Actualizar cronología.

Una automatización consume conocimiento.

Nunca documentos directamente.

---

# Bounded Contexts

El sistema se divide en contextos independientes.

---

## Core Context

Responsable de:

Usuarios.

Empresas.

Proyectos.

Configuraciones.

Permisos.

Licencias.

---

## Knowledge Context

Responsable de:

Documentos.

Embeddings.

Relaciones.

Graph.

Memoria.

Extracción.

---

## Automation Context

Responsable de:

Flujos automáticos.

Generación de entregables.

Exportaciones.

---

## Workspace Context

Responsable de:

Edición.

Versiones.

Comentarios.

Aprobaciones.

---

## AI Context

Responsable de:

Modelos.

Prompts.

Embeddings.

Clasificación.

Reasoning.

Orquestación.

---

## Branding Context

Responsable de:

Plantillas.

Diseño.

Colores.

Tipografía.

Logos.

Exportaciones.

---

# Aggregate Roots

Las siguientes entidades son Aggregate Roots.

Nunca deberán modificarse desde otro agregado.

---

## Project

Es la raíz principal.

Contiene:

Workspace.

Documentos.

Conversaciones.

Automatizaciones.

Memoria.

Cronología.

Dashboard.

---

## Workspace

Contiene.

Resultados.

Versiones.

Comentarios.

Exportaciones.

---

## Automation

Contiene.

Estado.

Resultados.

Historial.

Errores.

---

## Knowledge Base

Contiene.

Embeddings.

Entidades.

Relaciones.

Memoria.

---

# Entidades del Dominio

## Project

Responsabilidad.

Representar una obra.

Propiedades.

ID

Nombre

Cliente

Estado

Ubicación

Fecha Inicio

Fecha Fin

Configuración IA

Branding

Usuarios

Workspace

Knowledge Base

---

## User

Responsabilidad.

Interactuar con el sistema.

Puede pertenecer a múltiples proyectos.

---

## Company

Representa una empresa.

Puede ser.

Cliente.

Proveedor.

Contratista.

Consultor.

---

## Person

Representa personas físicas.

Ejemplos.

Arquitecto.

Ingeniero.

Supervisor.

Cliente.

Residente.

Director.

---

## Document

Representa cualquier archivo.

No contiene lógica.

Solo metadatos.

---

## Conversation

Representa una reunión.

Una llamada.

Una nota de voz.

Una transcripción.

---

## Agreement

Representa un compromiso.

Debe tener.

Responsable.

Fecha.

Origen.

Estado.

---

## Task

Pendiente.

Debe poder cambiar de estado.

No depende de IA.

---

## Decision

Resolución tomada.

Siempre pertenece a una conversación.

---

## Risk

Representa un riesgo detectado.

Puede generarse automáticamente.

Puede agregarlo un usuario.

---

## Change

Representa un cambio.

Ejemplos.

Cambio técnico.

Cambio económico.

Cambio alcance.

---

## Timeline Event

Evento histórico.

Todo cambio importante genera uno.

---

## Automation

Representa la ejecución de un proceso.

Nunca el proceso en sí.

---

## Template

Representa una plantilla corporativa.

No conoce IA.

---

# Value Objects

No tienen identidad propia.

Solo representan valores.

Ejemplos.

Fecha.

Dirección.

Ubicación.

Prioridad.

Estado.

Tipo Documento.

Tipo Riesgo.

Nivel Impacto.

Nivel Urgencia.

Color Branding.

Tipografía.

Configuración IA.

---

# Domain Events

Todo cambio importante genera eventos.

Ejemplos.

DocumentUploaded

ConversationProcessed

AgreementCreated

TaskAssigned

RiskDetected

PresentationGenerated

MinuteGenerated

KnowledgeUpdated

GraphUpdated

ProjectArchived

---

# Reglas de Negocio

## Proyecto

Todo documento pertenece a un proyecto.

Nunca puede existir un documento sin proyecto.

---

## Conversación

Toda conversación puede producir:

Acuerdos.

Pendientes.

Decisiones.

Riesgos.

Cambios.

Cronología.

---

## Acuerdo

Todo acuerdo debe tener responsable.

Si la IA no detecta uno.

Se marca como pendiente de revisión.

---

## Riesgos

Nunca pueden eliminarse.

Solo cambiar estado.

Abierto.

Mitigado.

Cerrado.

---

## Pendientes

Siempre pertenecen a alguien.

Nunca pueden quedar huérfanos.

---

## Cronología

Todo cambio importante genera un evento.

Nunca se edita.

Solo agrega nuevos eventos.

---

# Servicios del Dominio

Project Service

Gestiona proyectos.

---

Knowledge Service

Gestiona conocimiento.

---

Automation Service

Ejecuta automatizaciones.

---

Graph Service

Gestiona relaciones.

---

Timeline Service

Construye la historia del proyecto.

---

Branding Service

Aplica identidad visual.

---

AI Service

Orquesta modelos IA.

Nunca contiene reglas del negocio.

---

# Repository Pattern

Cada Aggregate Root tendrá su Repository.

Ejemplos.

ProjectRepository

KnowledgeRepository

AutomationRepository

ConversationRepository

WorkspaceRepository

TemplateRepository

Nunca acceder directamente a la base de datos.

---

# Domain Layer

El dominio nunca conocerá.

FastAPI.

SQLite.

React.

OpenAI.

Claude.

Gemini.

Tauri.

Todo eso pertenece a Infrastructure.

---

# Dependency Rule

Infrastructure

↓

Application

↓

Domain

Nunca al revés.

---

# Objetivo Final

El dominio representa la realidad de una gerencia de proyectos.

La tecnología únicamente es el medio para implementarlo.

Si algún día cambiamos completamente el stack tecnológico, este documento deberá seguir siendo válido sin modificaciones.