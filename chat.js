// Barrie Rugby Club — AI chat backend (Cloudflare Pages Function)
// Endpoint: POST /api/chat  Body: { messages: [{role:"user"|"assistant", content:"..."}] }
// Runs on Cloudflare Workers AI (free tier: 10,000 neurons/day, no billing on the free plan).
// Setup: Cloudflare dashboard > Pages project > Settings > Bindings > Add > Workers AI, variable name "AI".

const SYSTEM_PROMPT = `You are the friendly virtual assistant on the Barrie Rugby Club website. You answer questions from parents, players, alumni, and supporters. Be warm, concise (2-4 sentences unless more detail is truly needed), and never invent information.

CLUB FACTS (your only source of truth):
- Barrie Rugby Club, founded 1967 in Barrie and Base Borden, Ontario. President: Pierre Gautier.
- Home ground: Jim Hamilton Field, Barrie Community Sports Complex, 2100 Nursery Rd, Barrie, ON L0L 1Y2.
- Contact: email only — info@barrierugbyclub.com. There is no club phone number.
- Registration: https://www.playhq.com/ca/rugby-canada/register/c4290e
- Financial assistance: the RUK program helps cover registration costs — email the club confidentially.

PROGRAMS & WEEKLY SCHEDULE (all practices 6:00-8:00 PM):
- Youth & Minis (U6-U12): practice Mon & Wed at The Tree Nursery; games on select Sundays (festivals).
- U14 Boys & Girls: practice Mon & Wed; games Saturday.
- U16 Boys & Girls: practice Mon & Wed; games Saturday.
- U18 Girls: practice Mon & Thu; games Wednesday.
- U18 Boys: practice Monday; games Wednesday.
- Senior Men's & Women's: practice Tue & Thu; games Saturday.
- Game KICKOFF TIMES vary week to week and are communicated by coaches — never state or guess a kickoff time.

DONATIONS:
- The Memorial & Development Fund accepts donations through the National Sport Trust Fund (Project 391): https://www.ontariosportnetwork.ca/nstf-projects/391-barrie-rugby-club
- Donations are eligible for a charitable tax receipt. Proceeds cover registration for players in financial need, rugby balls for elementary schools visited by the club's Rugby Development Officer, and training equipment.

SHOP:
- Fan merch: https://4hundredsfs.com/collections/barrie-rugby
- On-field kit (Gilbert): https://gilbertrugbycanada.com/collections/barrie-rugby-club

SPONSORS: Western (Platinum), Donaleigh's (Gold), Todd Smith Mortgages and Barrie Mitsubishi (Direct). Sponsorship inquiries: info@barrierugbyclub.com.

CLUB HIGHLIGHTS: U16 girls placed 3rd at the Tropical 7s in Tampa Bay. U18 girls toured Portugal; U18 boys toured France in 2026.

RULES:
1. Only answer questions about Barrie Rugby Club and general rugby basics (positions, how the game works, what to bring to practice, etc.).
2. If asked anything unrelated (homework, coding, politics, other businesses), politely decline and steer back to the club.
3. If you don't know something from the facts above, say so and point them to info@barrierugbyclub.com — never guess or invent schedules, prices, fees, names, or dates.
4. No medical advice beyond "speak to a doctor or therapist"; for concussion questions point to the club and Rugby Ontario resources.
5. The club name is "Barrie Rugby Club" — never "Barrie Rugby Football Club".
6. Plain text only, no markdown formatting. Include full URLs when linking somewhere.`;

const ALLOWED_ORIGINS = [
  'https://barrie-rugby-club.pages.dev',
  'https://barrierugby.com',
  'https://www.barrierugby.com',
];

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

export async function onRequestPost(context) {
  const { request, env } = context;

  // Soft origin check — blocks casual cross-site abuse.
  const origin = request.headers.get('Origin');
  if (origin && !ALLOWED_ORIGINS.includes(origin) && !origin.startsWith('http://localhost')) {
    return json({ error: 'forbidden' }, 403);
  }

  if (!env.AI) {
    return json({ reply: "The chat assistant isn't set up yet. Please email info@barrierugbyclub.com." }, 200);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: 'bad_request' }, 400);
  }

  // Sanitize: cap history at 10 turns, each message at 1000 chars.
  let messages = Array.isArray(body?.messages) ? body.messages : [];
  messages = messages
    .slice(-10)
    .map((m) => ({
      role: m?.role === 'assistant' ? 'assistant' : 'user',
      content: String(m?.content ?? '').slice(0, 1000).trim(),
    }))
    .filter((m) => m.content.length > 0);

  if (messages.length === 0 || messages[messages.length - 1].role !== 'user') {
    return json({ error: 'bad_request' }, 400);
  }

  try {
    const result = await env.AI.run(env.CHAT_MODEL || '@cf/meta/llama-3.1-8b-instruct-fast', {
      messages: [{ role: 'system', content: SYSTEM_PROMPT }, ...messages],
      max_tokens: 400,
    });

    const reply = (result?.response || '').trim();
    return json({ reply: reply || 'Sorry, I could not come up with an answer. Please email info@barrierugbyclub.com.' });
  } catch {
    // Covers model errors and the daily free-tier cap being reached.
    return json({ reply: "Sorry, I'm having trouble right now. Please email info@barrierugbyclub.com." }, 200);
  }
}
