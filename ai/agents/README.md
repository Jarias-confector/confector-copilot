# ai/agents

Especialistas de responsabilidad única (08_AGENT_ARCHITECTURE). MVP: SecretaryAgent (primer agente oficial, Sprint 5). Futuros: RiskAgent, QualityAgent, Analyst, Scheduler, Designer.

**Reglas**: nunca `SuperAgent`/`GeneralAgent`. Un agente resuelve un solo problema. Nunca almacena datos, nunca accede a SQLite directamente, nunca llama a otro agente directamente — solo publica eventos (07_EVENT_ARCHITECTURE). Nunca conoce React ni FastAPI.

**Ciclo de vida**: recibir evento → construir contexto (`knowledge-os/context`) → consultar memoria → razonar → ejecutar → publicar eventos.
