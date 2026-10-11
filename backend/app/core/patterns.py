import re
from typing import List, Dict

PATTERNS = {
    "auto_renewal": {
        "regex": r"(автопродлен|пролонгац|автоматическ.{0,20}продлен)",
        "severity": 3,
        "hint": "Проверить условия расторжения и уведомление",
    },
    "unilateral": {
        "regex": r"(односторонн|без согласия другой стороны|в одностороннем порядке)",
        "severity": 5,
        "hint": "Ограничить односторонние действия компенсацией",
    },
    "penalty": {
        "regex": r"(штраф|неустойк|пеня)",
        "severity": 4,
        "hint": "Проверить размер и симметричность штрафов",
    },
    "prepayment": {
        "regex": r"(предоплат|аванс|100%\s*оплат)",
        "severity": 2,
        "hint": "Разбить на этапы или уменьшить долю",
    },
    "limited_liability": {
        "regex": r"(ограниченн.{0,15}ответственност|не превыша.{0,20}сумм)",
        "severity": 4,
        "hint": "Оценить достаточность лимита",
    },
    "jurisdiction": {
        "regex": r"(арбитраж|суд.{0,20}город|подсудност)",
        "severity": 1,
        "hint": "Проверить удобство подсудности",
    },
    "confidentiality": {
        "regex": r"(конфиденциальн|nda|неразглашен)",
        "severity": 2,
        "hint": "Проверить срок и объём NDA",
    },
    "termination": {
        "regex": r"(расторж|прекращ|отказ от исполн)[^.]{0,200}",
        "severity": 3,
        "hint": "Проанализировать условия расторжения",
    },
    "exclusivity": {
        "regex": r"(эксклюзивн|исключительн.{0,20}прав)",
        "severity": 3,
        "hint": "Оценить ограничения конкуренции",
    },
    "force_majeure": {
        "regex": r"(форс-мажор|непреодолим.{0,20}сил)",
        "severity": 1,
        "hint": "Проверить перечень обстоятельств",
    },
}

def scan_text(text: str) -> List[Dict]:
    findings = []
    for category, cfg in PATTERNS.items():
        for m in re.finditer(cfg["regex"], text, re.IGNORECASE):
            start = max(0, m.start() - 120)
            end = min(len(text), m.end() + 120)
            findings.append({
                "category": category,
                "severity": cfg["severity"],
                "snippet": text[start:end].strip(),
                "match": m.group(),
                "hint": cfg["hint"],
            })
    return findings
