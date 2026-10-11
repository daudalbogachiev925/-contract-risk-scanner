from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Text
from sqlalchemy.sql import func
from app.database import Base

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    storage_key = Column(String, nullable=False)
    text = Column(Text)
    risk_score = Column(Float, default=0.0)
    risk_level = Column(String, default="low")
    findings = Column(JSON, default=list)
    entities = Column(JSON, default=dict)
    created_at = Column(DateTime, server_default=func.now())
