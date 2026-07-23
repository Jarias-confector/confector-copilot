import os

from .provider import LLMProvider, MockProvider


def get_default_provider() -> LLMProvider:
    """Selecciona proveedor según variables de entorno. Sin API keys configuradas -> MockProvider.

    Nuevos proveedores (OpenAI, Claude, Gemini, Ollama, OpenRouter) se agregan aquí
    implementando LLMProvider, sin tocar el resto del sistema (05_TECH_STACK §"LLM Adapter").
    """
    if os.getenv("OPENAI_API_KEY"):
        # TODO: implementar OpenAIProvider cuando se agregue el SDK correspondiente.
        pass
    return MockProvider()
