const API = "/api";

export async function uploadContract(file) {
  const form = new FormData();
  form.append("file", file);
  const r = await fetch(`${API}/contracts/upload`, { method: "POST", body: form });
  if (!r.ok) throw new Error(await r.text());
  return r.json();
}

export async function listContracts() {
  const r = await fetch(`${API}/contracts`);
  return r.json();
}

export async function getRecommendations(id) {
  const r = await fetch(`${API}/analysis/${id}/recommendations`);
  return r.json();
}
