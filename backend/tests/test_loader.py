from app.core.loader import load_txt, load_document

def test_load_txt():
    assert load_txt(b"hello") == "hello"

def test_unsupported():
    import pytest
    with pytest.raises(ValueError):
        load_document("a.xyz", b"data")
