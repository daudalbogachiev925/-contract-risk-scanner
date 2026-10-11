import io
from pathlib import Path
from pypdf import PdfReader
from docx import Document

def load_pdf(data: bytes) -> str:
    reader = PdfReader(io.BytesIO(data))
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def load_docx(data: bytes) -> str:
    doc = Document(io.BytesIO(data))
    return "\n".join(p.text for p in doc.paragraphs)

def load_txt(data: bytes) -> str:
    return data.decode("utf-8", errors="ignore")

def load_document(filename: str, data: bytes) -> str:
    suffix = Path(filename).suffix.lower()
    if suffix == ".pdf":
        return load_pdf(data)
    if suffix == ".docx":
        return load_docx(data)
    if suffix in (".txt", ".md"):
        return load_txt(data)
    raise ValueError(f"Unsupported format: {suffix}")
