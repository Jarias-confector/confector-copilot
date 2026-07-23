from pathlib import Path

from confector_core import Project


def generate_project_summary(project: Project, ai_output: str, exports_dir: Path) -> Path:
    """Primer Document Generator del walking skeleton (13_ARCHITECT §20). No decide contenido ni diseño — ver packages/templates."""
    exports_dir.mkdir(parents=True, exist_ok=True)
    path = exports_dir / f"{project.id}-resumen.md"
    content = (
        f"# Resumen ejecutivo — {project.name}\n\n"
        f"Cliente: {project.client or 'N/A'}\n\n"
        f"Estado: {project.status.value}\n\n"
        f"## Generado por IA\n\n{ai_output}\n"
    )
    path.write_text(content, encoding="utf-8")
    return path
