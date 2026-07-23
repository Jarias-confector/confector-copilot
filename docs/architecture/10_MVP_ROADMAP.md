# 10_MVP_ROADMAP.md

# CONFECTOR Copilot - MVP Roadmap

> "Construir primero el flujo completo de valor, después agregar inteligencia."

---

# 1. Objetivo del MVP

El MVP tiene como objetivo validar que CONFECTOR Copilot puede reducir significativamente el tiempo que un gerente de obra invierte en transformar información desordenada en entregables profesionales.

---

# 2. Hipótesis Principal

Actualmente los gerentes de obra reciben información en múltiples formatos:

- Audios de reuniones.
- Notas personales.
- Correos.
- PDFs.
- Excel.
- Fotografías.
- Mensajes.

Esta información requiere horas de procesamiento manual para convertirse en:

- Minutas.
- Reportes.
- Seguimientos.
- Presentaciones.
- Resúmenes ejecutivos.

---

## Hipótesis

Si CONFECTOR Copilot puede capturar, estructurar y transformar automáticamente esta información, entonces reducirá significativamente el tiempo administrativo de la gerencia de proyectos.

---

# 3. Alcance MVP

El MVP NO busca construir todo el sistema final.

El MVP construirá únicamente:

## Entrada

Audio.

PDF.

Word.

Excel básico.

Texto.

---

## Procesamiento

Transcripción.

Extracción de información.

Clasificación.

Resumen.

Detección de acuerdos.

Detección de pendientes.

Detección de responsables.

---

## Salida

Minuta profesional.

Resumen ejecutivo.

Lista de pendientes.

Cronología básica.

Exportación Word/PDF.

---

# 4. Flujo Principal MVP

```
Usuario

↓

Crear Proyecto

↓

Subir archivo

↓

Sistema analiza

↓

Extrae información

↓

Genera conocimiento

↓

Usuario revisa

↓

Genera documento

↓

Exporta resultado
```

---

# 5. Sprint 0 - Foundation

## Objetivo

Crear la base técnica.

---

## Entregables

Repositorio creado.

Monorepo configurado.

Frontend inicial.

Backend inicial.

Base de datos.

Sistema de configuración.

Logging.

Variables de entorno.

---

## Resultado esperado

La aplicación abre.

El usuario puede crear un proyecto.

---

# 6. Sprint 1 - Project Workspace

## Objetivo

Crear el espacio donde vive cada proyecto.

---

## Funcionalidades

Crear proyecto.

Editar proyecto.

Eliminar proyecto.

Seleccionar proyecto.

Ver información básica.

---

## Entidades

Project.

User.

Company.

Workspace.

---

## Resultado esperado

Un gerente puede organizar sus obras dentro del sistema.

---

# 7. Sprint 2 - Document Intelligence

## Objetivo

Permitir recibir información.

---

## Entradas soportadas

PDF.

Word.

Excel.

TXT.

Audio.

---

## Procesos

Carga.

Almacenamiento.

Clasificación.

Metadatos.

Extracción inicial.

---

## Eventos

DocumentUploaded.

DocumentProcessed.

---

## Resultado esperado

El sistema entiende qué tipo de información recibió.

---

# 8. Sprint 3 - Audio Intelligence

## Objetivo

Resolver uno de los mayores problemas actuales.

Las reuniones.

---

## Funcionalidades

Subir audio.

Transcribir.

Separar hablantes.

Detectar temas.

Extraer acuerdos.

Detectar pendientes.

---

## Tecnología inicial

Whisper.

WhisperX futuro.

---

## Resultado esperado

Un audio de una reunión se convierte en información estructurada.

---

# 9. Sprint 4 - Knowledge Engine MVP

## Objetivo

Crear la primera memoria del proyecto.

---

## Funcionalidades

Guardar entidades.

Guardar relaciones.

Crear timeline.

Buscar información.

---

## Entidades iniciales

Personas.

Empresas.

Acuerdos.

Pendientes.

Fechas.

Decisiones.

Riesgos.

---

## Resultado esperado

El sistema recuerda lo ocurrido dentro del proyecto.

---

# 10. Sprint 5 - Secretary Agent

## Primer agente oficial.

---

## Responsabilidad

Convertir conversaciones en documentación profesional.

---

## Capacidades

Analizar reuniones.

Crear minuta.

Identificar responsables.

Crear seguimiento.

---

## Entrada

ConversationProcessed.

---

## Salida

MinuteGenerated.

AgreementCreated.

TaskCreated.

---

# 11. Sprint 6 - Template Engine

## Objetivo

Crear documentos con identidad CONFECTOR.

---

## Funcionalidades

Logo.

Colores.

Tipografía.

Membrete.

Numeración.

Portadas.

---

## Plantillas iniciales

Minuta.

Reporte ejecutivo.

Seguimiento semanal.

---

## Resultado esperado

El documento generado parece creado por la empresa.

---

# 12. Sprint 7 - Copilot Interface

## Objetivo

Crear interacción inteligente.

---

## Funcionalidades

Preguntar sobre proyectos.

Buscar información.

Solicitar documentos.

Explicar decisiones.

---

Ejemplo:

Usuario:

"¿Qué pendientes tiene Casa Vida?"

Sistema:

"Encontré 8 pendientes activos..."

---

# 13. Sprint 8 - Quality Agent

## Objetivo

Revisión automática.

---

## Funciones

Detectar información faltante.

Detectar inconsistencias.

Revisar formato.

Validar responsables.

---

# 14. Funcionalidades Post MVP

## V2

Project Analyst Agent.

Risk Detection.

Dashboard automático.

Presentaciones.

Excel avanzado.

---

## V3

Integraciones.

Outlook.

Teams.

WhatsApp.

Google Drive.

SharePoint.

---

## V4

Inteligencia predictiva.

Predicción de atrasos.

Predicción de costos.

Análisis histórico.

---

# 15. Funciones fuera del MVP

No construir inicialmente:

BIM.

ERP.

Control financiero completo.

Aplicación móvil.

Multiempresa.

Marketplace.

---

# 16. Métricas de Éxito

El MVP será exitoso si:

---

## Tiempo

Reduce 70% o más el tiempo de creación de minutas.

---

## Calidad

Los documentos requieren mínima edición humana.

---

## Uso

Los ingenieros lo utilizan semanalmente.

---

## Retención

Los proyectos permanecen activos dentro del sistema.

---

# 17. Prioridad de Desarrollo

Orden oficial:

```
1. Workspace

2. Document Processing

3. Audio Pipeline

4. Knowledge Engine

5. Secretary Agent

6. Templates

7. Copilot

8. Additional Agents
```

---

# 18. Regla Principal

Nunca construir una función que no aumente:

- Captura de conocimiento.
- Organización.
- Automatización.
- Calidad de entregables.

---

# 19. Visión del MVP

El primer objetivo no es crear una inteligencia artificial avanzada.

El primer objetivo es demostrar:

"CONFECTOR Copilot puede tomar información desordenada de una obra y convertirla en conocimiento accionable y documentos profesionales."

Cuando ese flujo funcione perfectamente, todos los agentes futuros serán una extensión natural del sistema.