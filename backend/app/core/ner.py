from functools import lru_cache
import spacy
from app.config import settings

@lru_cache(maxsize=1)
def _nlp():
    return spacy.load(settings.SPACY_MODEL)

def extract_entities(text: str) -> dict:
    doc = _nlp()(text[:100_000])
    orgs, money, dates, persons = [], [], [], []
    for e in doc.ents:
        if e.label_ == "ORG":
            orgs.append(e.text)
        elif e.label_ == "MONEY":
            money.append(e.text)
        elif e.label_ == "DATE":
            dates.append(e.text)
        elif e.label_ == "PER":
            persons.append(e.text)
    return {
        "organizations": list(dict.fromkeys(orgs)),
        "money": list(dict.fromkeys(money)),
        "dates": list(dict.fromkeys(dates)),
        "persons": list(dict.fromkeys(persons)),
    }
