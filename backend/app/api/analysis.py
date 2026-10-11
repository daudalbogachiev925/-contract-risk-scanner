from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Contract

router = APIRouter()

@router.get("/{contract_id}/recommendations")
def recommendations(contract_id: int, db: Session = Depends(get_db)):
    r = db.query(Contract).get(contract_id)
    if not r:
        raise HTTPException(404)
    recs = []
    for f in (r.findings or []):
        recs.append({
            "category": f["category"],
            "severity": f["severity"],
            "action": f["hint"],
            "excerpt": f["snippet"][:200],
        })
    recs.sort(key=lambda x: x["severity"], reverse=True)
    return {"contract_id": contract_id, "recommendations": recs}
