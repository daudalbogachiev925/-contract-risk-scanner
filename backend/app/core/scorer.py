from typing import List, Dict

def risk_score(findings: List[Dict]) -> Dict:
    total = sum(f["severity"] for f in findings)
    by_cat: Dict[str, int] = {}
    for f in findings:
        by_cat[f["category"]] = by_cat.get(f["category"], 0) + 1
    if total > 25:
        level = "high"
    elif total > 12:
        level = "medium"
    else:
        level = "low"
    return {"total_score": total, "level": level, "categories": by_cat}
