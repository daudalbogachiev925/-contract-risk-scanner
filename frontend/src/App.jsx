import { useEffect, useState } from "react";
import Upload from "./components/Upload.jsx";
import Report from "./components/Report.jsx";
import { listContracts } from "./api.js";

export default function App() {
  const [contracts, setContracts] = useState([]);
  const [selected, setSelected] = useState(null);

  async function refresh() {
    setContracts(await listContracts());
  }

  useEffect(() => { refresh(); }, []);

  return (
    <div style={{ fontFamily: "system-ui", padding: 24, maxWidth: 1100, margin: "auto" }}>
      <h1>Contract Risk Scanner</h1>
      <Upload onUploaded={refresh} />
      <h2>Договоры</h2>
      <table width="100%" cellPadding="8" style={{ borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th align="left">Файл</th>
            <th>Score</th>
            <th>Уровень</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {contracts.map(c => (
            <tr key={c.contract_id} style={{ borderBottom: "1px solid #eee" }}>
              <td>{c.filename}</td>
              <td align="center">{c.risk_score}</td>
              <td align="center">{c.risk_level}</td>
              <td align="center">
                <button onClick={() => setSelected(c)}>Отчёт</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {selected && <Report contract={selected} onClose={() => setSelected(null)} />}
    </div>
  );
}
