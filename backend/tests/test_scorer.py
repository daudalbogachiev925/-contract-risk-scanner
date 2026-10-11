from app.core.scorer import risk_score

def test_low_risk():
    findings = [{"category": "jurisdiction", "severity": 1}]
    r = risk_score(findings)
    assert r["level"] == "low"
    assert r["total_score"] == 1

def test_high_risk():
    findings = [{"category": "unilateral", "severity": 5}] * 6
    r = risk_score(findings)
    assert r["level"] == "high"
