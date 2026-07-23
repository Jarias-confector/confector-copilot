# ai/models

Adaptadores de proveedores IA (LLM Adapter, 05_TECH_STACK). Un agente nunca llama una API de IA directamente — siempre a través de este módulo.

```
LLMProvider
  OpenAIProvider
  ClaudeProvider
  GeminiProvider
  OllamaProvider
  OpenRouterProvider
```

Todos implementan la misma interfaz — principio AI Agnostic (01_PRODUCT_PRINCIPLES #4).
