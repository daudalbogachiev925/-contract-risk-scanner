from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class Finding(BaseModel):
    category: str
    severity: int
    snippet: str
    match: str
    hint: str

class ScanResult(BaseModel):
    contract_id: int
    filename: str
    risk_score: float
    risk_level: str
    findings: List[Finding]
    entities: Dict[str, Any]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True
