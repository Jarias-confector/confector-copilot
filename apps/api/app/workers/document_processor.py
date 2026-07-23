from pathlib import Path

from confector_core import DocumentKind

_EXTENSION_KIND = {
    ".pdf": DocumentKind.PDF,
    ".doc": DocumentKind.WORD,
    ".docx": DocumentKind.WORD,
    ".xls": DocumentKind.EXCEL,
    ".xlsx": DocumentKind.EXCEL,
    ".txt": DocumentKind.TEXT,
    ".md": DocumentKind.TEXT,
    ".mp3": DocumentKind.AUDIO,
    ".wav": DocumentKind.AUDIO,
    ".m4a": DocumentKind.AUDIO,
}

_MAX_EXTRACT_CHARS = 5000


def classify(filename: str) -> DocumentKind:
    return _EXTENSION_KIND.get(Path(filename).suffix.lower(), DocumentKind.OTHER)


def extract_text(kind: DocumentKind, content: bytes) -> str | None:
    """Extracción inicial (10_MVP_ROADMAP Sprint 2). Audio se procesa en Sprint 3 (Whisper)."""
    try:
        if kind == DocumentKind.PDF:
            return _extract_pdf(content)
        if kind == DocumentKind.WORD:
            return _extract_docx(content)
        if kind == DocumentKind.EXCEL:
            return _extract_xlsx(content)
        if kind == DocumentKind.TEXT:
            return content.decode("utf-8", errors="replace")[:_MAX_EXTRACT_CHARS]
    except Exception:
        return None
    return None


def _extract_pdf(content: bytes) -> str:
    import fitz  # PyMuPDF

    with fitz.open(stream=content, filetype="pdf") as doc:
        text = "\n".join(page.get_text() for page in doc)
    return text[:_MAX_EXTRACT_CHARS]


def _extract_docx(content: bytes) -> str:
    import io

    from docx import Document as DocxDocument

    doc = DocxDocument(io.BytesIO(content))
    text = "\n".join(p.text for p in doc.paragraphs)
    return text[:_MAX_EXTRACT_CHARS]


def _extract_xlsx(content: bytes) -> str:
    import io

    from openpyxl import load_workbook

    wb = load_workbook(io.BytesIO(content), read_only=True, data_only=True)
    lines = []
    for sheet in wb.worksheets:
        lines.append(f"# {sheet.title}")
        for row in sheet.iter_rows(max_row=20, values_only=True):
            lines.append(", ".join(str(cell) for cell in row if cell is not None))
    return "\n".join(lines)[:_MAX_EXTRACT_CHARS]
