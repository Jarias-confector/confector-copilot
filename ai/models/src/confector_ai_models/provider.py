from typing import Protocol


class LLMProvider(Protocol):
    """Todos los proveedores implementan esta interfaz. Un agente nunca llama una API de IA directamente (11_DEVELOPMENT_GUIDELINES §11)."""

    name: str

    def generate(self, prompt: str) -> str: ...


class MockProvider:
    """Proveedor por defecto cuando no hay API key configurada. Permite probar el flujo completo sin depender de un servicio externo."""

    name = "mock"

    def generate(self, prompt: str) -> str:
        return f"[mock] Resumen generado localmente a partir de: {prompt[:120]}"
