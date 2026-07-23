# 11_DEVELOPMENT_GUIDELINES.md

# CONFECTOR Copilot - Development Guidelines

> "El código debe seguir la arquitectura.
> La arquitectura nunca debe seguir al código."

---

# 1. Objetivo

Este documento define las reglas obligatorias de desarrollo para CONFECTOR Copilot.

Aplica para:

- Desarrolladores humanos.
- Agentes IA.
- Automatizaciones.
- Contribuidores externos.

---

# 2. Principios Fundamentales

## Simplicidad primero

La solución más simple que cumple el objetivo siempre es preferida.

No agregar complejidad futura sin necesidad actual.

---

## Arquitectura antes que velocidad

Antes de crear código:

Entender el dominio.

Revisar arquitectura.

Validar impacto.

---

## Código reemplazable

Todo módulo debe poder ser reemplazado.

Nunca crear dependencias innecesarias.

---

## La IA no decide arquitectura

Los modelos IA ayudan a programar.

No definen estructura del sistema.

---

# 3. Regla Principal

Antes de modificar cualquier módulo revisar:

```
00_VISION.md

01_PRODUCT_PRINCIPLES.md

02_PRODUCT_ARCHITECTURE.md

06_DOMAIN_MODEL.md

09_SYSTEM_BLUEPRINT.md
```

---

# 4. Arquitectura de Capas

La dirección de dependencia siempre será:

```
Presentation

↓

Application

↓

Domain

↓

Infrastructure
```

---

Nunca:

Infrastructure

↓

Domain

---

Ejemplo incorrecto:

```python
class Project:

    def save():

        sqlite.save()
```

---

Correcto:

```python
Project

↓

ProjectRepository

↓

SQLiteRepository
```

---

# 5. Domain Rules

El dominio nunca conoce:

- Bases de datos.
- APIs externas.
- Frameworks.
- Modelos IA.
- Interfaces.

---

Ejemplo incorrecto:

```python
class Minute:

    generate_with_gpt()
```

---

Correcto:

```text
Minute

↓

Application Service

↓

LLM Provider
```

---

# 6. Organización del Código

Cada módulo debe tener:

```
module/

domain/

application/

infrastructure/

tests/

README.md
```

---

Ejemplo:

```
knowledge-engine/

domain/

entities/

services/

repositories/


application/

commands/

queries/


infrastructure/

database/

vector/


tests/
```

---

# 7. Naming Convention

## Archivos

snake_case.

Correcto:

```
knowledge_service.py
```

Incorrecto:

```
KnowledgeService.py
```

---

## Clases

PascalCase.

Ejemplo:

```
KnowledgeService
```

---

## Funciones

snake_case.

Ejemplo:

```
extract_entities()
```

---

## Variables

snake_case.

Ejemplo:

```
project_context
```

---

# 8. Código Python

Obligatorio:

Python 3.12+

Type hints.

Docstrings.

Async cuando corresponda.

---

Ejemplo:

```python
async def process_document(
    document_id: str
) -> KnowledgeResult:
```

---

# 9. Frontend Rules

React:

Componentes pequeños.

No lógica de negocio.

No llamadas directas al backend.

---

Incorrecto:

```javascript
Button

↓

OpenAI API
```

---

Correcto:

```
Component

↓

Application API

↓

Backend

↓

AI Layer
```

---

# 10. API Rules

Toda API debe tener:

Validación.

Documentación.

Manejo de errores.

Logs.

Tests.

---

Nunca crear endpoints sin caso de uso definido.

---

# 11. AI Rules

## Nunca llamar modelos directamente.

Incorrecto:

```python
openai.chat()
```

---

Correcto:

```python
llm_provider.generate()
```

---

Todos los modelos deben pasar por:

```
LLM Adapter
```

---

# 12. Prompt Management

Los prompts nunca viven dentro del código.

Incorrecto:

```python
prompt="Analiza este documento"
```

---

Correcto:

```
prompts/

secretary/

minute_generation.md
```

---

Los prompts tienen versión.

Ejemplo:

```
minute_generation_v2.md
```

---

# 13. Agentes

Todo agente debe tener:

Identidad.

Responsabilidad.

Herramientas.

Eventos.

Memoria.

Validaciones.

---

Nunca crear agentes genéricos.

Incorrecto:

```
SuperAgent
```

---

Correcto:

```
SecretaryAgent

RiskAnalystAgent

QualityAgent
```

---

# 14. Eventos

Los módulos no se llaman directamente.

Incorrecto:

```
Secretary

calls

RiskAgent
```

---

Correcto:

```
Secretary

publishes

AgreementCreated


RiskAgent

listens
```

---

# 15. Base de Datos

Nunca acceder directamente desde módulos.

Siempre:

```
Repository

↓

Database
```

---

Nunca:

```
SELECT *

desde cualquier archivo
```

---

# 16. Manejo de errores

Todo error debe:

Registrarse.

Tener contexto.

Ser recuperable.

---

Nunca:

```python
except:
    pass
```

---

# 17. Testing

Cada módulo debe tener:

Unit tests.

Integration tests.

---

Prioridad:

Domain.

Application.

Infrastructure.

UI.

---

# 18. Documentación

Todo módulo nuevo requiere:

README.

Responsabilidad.

Dependencias.

Ejemplos.

---

Todo cambio arquitectónico requiere:

ADR.

---

# 19. Git Workflow

Branches:

```
main

develop

feature/

bugfix/

hotfix/
```

---

Commits:

Formato:

```
tipo: descripción
```

Ejemplo:

```
feat: add document processor

fix: resolve audio timeout

docs: update architecture
```

---

# 20. Pull Request Rules

Todo PR debe explicar:

Qué cambia.

Por qué cambia.

Qué módulos afecta.

Cómo probarlo.

---

# 21. Uso de IA durante desarrollo

La IA debe:

Proponer.

Explicar.

Generar.

Refactorizar.

---

La IA nunca debe:

Cambiar arquitectura sin aprobación.

Eliminar tests.

Crear dependencias innecesarias.

Modificar múltiples módulos sin explicar.

---

# 22. MCP Guidelines

Los MCP deben utilizarse para:

Investigación.

Automatización.

Documentación.

Validación.

---

Nunca delegar decisiones críticas sin revisión.

---

# 23. Performance

Prioridades:

1. Correctitud.

2. Mantenibilidad.

3. Rendimiento.

---

Optimizar solamente cuando exista evidencia.

---

# 24. Seguridad

Nunca guardar:

API Keys.

Contraseñas.

Tokens.

Información sensible.

---

Usar:

Variables ambiente.

Secret managers.

Sistema operativo.

---

# 25. Regla para nuevos módulos

Antes de crear un módulo responder:

¿Por qué existe?

¿Qué problema resuelve?

¿Puede vivir dentro de otro módulo?

¿Qué eventos consume?

¿Qué eventos produce?

---

# 26. Checklist antes de programar

Antes de escribir código:

[ ] Entiendo el problema.

[ ] Existe documento relacionado.

[ ] Existe entidad de dominio.

[ ] Existe flujo definido.

[ ] Sé dónde pertenece.

---

# 27. Checklist antes de entregar

[ ] Tests creados.

[ ] Documentación actualizada.

[ ] Logs agregados.

[ ] Arquitectura respetada.

[ ] No existen dependencias innecesarias.

---

# 28. Filosofía Final

CONFECTOR Copilot será desarrollado como un producto profesional.

La velocidad importa.

Pero la claridad importa más.

Un código que funciona hoy pero destruye el futuro no es una solución.

Cada línea debe acercarnos a una plataforma mantenible, escalable y preparada para evolucionar durante años.