def test_upload_txt(client):
    files = {"file": ("c.txt", b"Unilateral termination clause.", "text/plain")}
    r = client.post("/api/contracts/upload", files=files)
    assert r.status_code == 201
    body = r.json()
    assert body["filename"] == "c.txt"
    assert "risk_level" in body

def test_list(client):
    r = client.get("/api/contracts")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
