from app.core.patterns import scan_text

def test_detects_unilateral():
    text = "Исполнитель вправе в одностороннем порядке изменить условия."
    findings = scan_text(text)
    cats = [f["category"] for f in findings]
    assert "unilateral" in cats

def test_detects_auto_renewal():
    text = "Договор подлежит автопродлению на 12 месяцев."
    findings = scan_text(text)
    assert any(f["category"] == "auto_renewal" for f in findings)

def test_no_false_positive():
    text = "Обычный текст без условий."
    findings = scan_text(text)
    assert findings == []
