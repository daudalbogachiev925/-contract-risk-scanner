import { useState } from "react";
import { uploadContract } from "../api.js";

export default function Upload({ onUploaded }) {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState(null);

  async function handle(e) {
    const file = e.target.files[0];
    if (!file) return;
    setBusy(true); setError(null);
    try {
      await uploadContract(file);
      onUploaded();
    } catch (err) {
      setError(String(err));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div style={{ padding: 16, border: "1px dashed #ccc", borderRadius: 8 }}>
      <input type="file" accept=".pdf,.docx,.txt" onChange={handle} disabled={busy} />
      {busy && <span style={{ marginLeft: 12 }}>Анализ...</span>}
      {error && <div style={{ color: "red", marginTop: 8 }}>{error}</div>}
    </div>
  );
}
