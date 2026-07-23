import os
import tempfile
from dataclasses import dataclass, field

_model = None


@dataclass
class TranscriptionResult:
    text: str | None
    language: str | None = None
    duration_seconds: float | None = None
    segments: int = 0
    error: str | None = None
    metadata: dict = field(default_factory=dict)


def _get_model():
    """Carga perezosa — un solo modelo Whisper compartido por proceso (05_TECH_STACK: Whisper, transcripción oficial)."""
    global _model
    if _model is None:
        from faster_whisper import WhisperModel

        _model = WhisperModel("tiny", device="cpu", compute_type="int8")
    return _model


def transcribe(content: bytes, suffix: str) -> TranscriptionResult:
    """Convierte audio en texto. Nunca lanza — degrada con error explícito (01_PRODUCT_PRINCIPLES #9, Explainable AI)."""
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        model = _get_model()
        segments_iter, info = model.transcribe(tmp_path)
        segments = list(segments_iter)
        text = " ".join(seg.text.strip() for seg in segments).strip()

        return TranscriptionResult(
            text=text or None,
            language=info.language,
            duration_seconds=round(info.duration, 1),
            segments=len(segments),
        )
    except Exception as exc:
        return TranscriptionResult(text=None, error=str(exc))
    finally:
        if tmp_path:
            os.remove(tmp_path)
