from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Contract
from app.schemas import ScanResult
from app.core.loader import load_document
from app.core.patterns import scan_text
from app.core.ner import extract_entities
from app.core.scorer import risk_score
from app.storage.minio_client import upload
import uuid

router = APIRouter()

@router.post("/upload", response_model=ScanResult, status_code=201)
async def upload_contract(file: UploadFile = File(...),
                          db: Session = Depends(get_db)):
    data = await file.read()
    if not data:
        raise HTTPException(400, "Empty file")
    try:
        text = load_document(file.filename, data)
    except ValueError as e:
        raise HTTPException(415, str(e))

    key = f"{uuid.uuid4().hex}_{file.filename}"
    upload(key, data, content_type=file.content_type or "application/octet-stream")

    findings = scan_text(text)
    score = risk_score(findings)
    entities = extract_entities(text)

    c = Contract(
        filename=file.filename,
        storage_key=key,
        text=text,
        risk_score=score["total_score"],
        risk_level=score["level"],
        findings=findings,
        entities=entities,
    )
    db.add(c)
    db.commit()
    db.refresh(c)
    return ScanResult(
        contract_id=c.id,
        filename=c.filename,
        risk_score=c.risk_score,
        risk_level=c.risk_level,
        findings=findings,
        entities=entities,
        created_at=c.created_at,
    )

@router.get("", response_model=List[ScanResult])
def list_contracts(db: Session = Depends(get_db)):
    rows = db.query(Contract).order_by(Contract.created_at.desc()).all()
    return [ScanResult(
        contract_id=r.id, filename=r.filename,
        risk_score=r.risk_score, risk_level=r.risk_level,
        findings=r.findings or [], entities=r.entities or {},
        created_at=r.created_at) for r in rows]

@router.get("/{contract_id}", response_model=ScanResult)
def get_contract(contract_id: int, db: Session = Depends(get_db)):
    r = db.query(Contract).get(contract_id)
    if not r:
        raise HTTPException(404, "Not found")
    return ScanResult(
        contract_id=r.id, filename=r.filename,
        risk_score=r.risk_score, risk_level=r.risk_level,
        findings=r.findings or [], entities=r.entities or {},
        created_at=r.created_at)
