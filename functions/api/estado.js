// Cloudflare Pages Function · /api/estado
// Almacena y sirve el ÚLTIMO estado publicado del mapa SOSDPZ (dotación por
// parque + fecha) en Cloudflare KV, para que el enlace fijo muestre siempre lo
// último sin re-desplegar.
//   GET  /api/estado            -> { b:[9 enteros], d:"YYYY-MM-DD", ts } | null
//   POST /api/estado            -> guarda el estado. Requiere cabecera
//                                  X-Pub-Key == env.PUB_KEY (clave del equipo).
// Bindings: env.ESTADO (KV namespace), env.PUB_KEY (secret).

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type,X-Pub-Key',
};

function json(obj, status = 200, extra = {}) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', ...CORS, ...extra },
  });
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS });
}

export async function onRequestGet(context) {
  const v = await context.env.ESTADO.get('actual');
  return new Response(v || 'null', {
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', ...CORS },
  });
}

export async function onRequestPost(context) {
  const key = (context.request.headers.get('X-Pub-Key') || '').trim();
  const expected = String(context.env.PUB_KEY || '').trim();
  if (!expected || key !== expected) {
    return json({ error: 'clave de publicación incorrecta' }, 403);
  }
  let body;
  try { body = await context.request.json(); } catch (e) { return json({ error: 'json no válido' }, 400); }
  if (!body || !Array.isArray(body.b) || body.b.length !== 9) {
    return json({ error: 'estado no válido (se esperan 9 valores de dotación)' }, 400);
  }
  const estado = {
    b: body.b.map(x => Math.max(0, Math.min(30, parseInt(x, 10) || 0))),
    d: String(body.d || '').slice(0, 10),
    ts: Date.now(),
  };
  await context.env.ESTADO.put('actual', JSON.stringify(estado));
  return json({ ok: true, estado });
}
