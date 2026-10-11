import { useEffect, useState } from "react";
import { getRecommendations } from "../api.js";

export default function Report({ contract, onClose }) {
  const [recs, setRecs] = useState([]);

  useEffect(() => {
    getRecommendations(contract.contract_id).then(d => setRecs(d.recommendations));
  }, [contract.contract_id]);

  return (
    <div style={{
      position: "fixed", top: 0, right: 0, width: 520, height: "100vh",
      background: "#fff", boxShadow: "-4px 0 12px rgba(0,0,0,0.1)",
      padding: 24, overflowY: "auto"
    }}>
      <button onClick={onClose} style={{ float: "right" }}>Закрыть</button>
      <h2>{contract.filename}</h2>
      <p>Score: {contract.risk_score} ({contract.risk_level})</p>
      <h3>Рекомендации</h3>
      <ol>
        {recs.map((r, i) => (
          <li key={i} style={{ marginBottom: 12 }}>
            <b>[{r.category}]</b> {r.action}
            <div style={{ fontSize: 12, color: "#666" }}>{r.excerpt}</div>
          </li>
        ))}
      </ol>
    </div>
  );
}
