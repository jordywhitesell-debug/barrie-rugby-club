import os

import sys
sys.path.insert(0, '/home/claude')
from sponsor_b64 import DONALEIGHS, WESTERN, MITSUBISHI, TODDSMITH

with open('/home/claude/logo_transparent_b64.txt') as f:
    LOGO = 'data:image/png;base64,' + f.read().strip()

CSS = """
:root{
  --navy: #142645; --navy-deep: #0c1a30;
  --sky: #7cc5ea; --sky-deep: #4fa3d1;
  --paper: #f7fafb; --ink: #1b2233;
  --red: #cc2b2b; --gold: #e3a73c;
  --line: rgba(20,38,69,0.12);
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:'Public Sans', sans-serif; color:var(--ink); background:var(--paper); -webkit-font-smoothing:antialiased;}
img{max-width:100%;display:block;}
a{color:inherit;text-decoration:none;}
.display{font-family:'Anton', sans-serif; text-transform:uppercase; letter-spacing:0.01em;}
.eyebrow{font-family:'Anton', sans-serif; font-size:12.5px; letter-spacing:0.22em; text-transform:uppercase; display:inline-flex; align-items:center; gap:10px;}
.eyebrow::before{content:""; width:22px;height:2px;background:currentColor;display:inline-block;}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px;}
@media (max-width:640px){.wrap{padding:0 20px;}}

header{position:sticky; top:0; z-index:100; background:rgba(20,38,69,0.96); backdrop-filter:blur(6px); border-bottom:1px solid rgba(255,255,255,0.08);}
nav.wrap{display:flex; align-items:center; justify-content:space-between; height:76px;}
.brand{display:flex; align-items:center; gap:12px;}
.brand img{height:46px; width:46px;}
.brand .word{font-family:'Anton', sans-serif; color:#fff; font-size:16px; letter-spacing:0.06em; line-height:1.15;}
.brand .word span{display:block; color:var(--sky); font-size:11px; letter-spacing:0.28em; margin-top:2px;}
.navlinks{display:flex; align-items:center; gap:30px;}
.navlinks a{color:rgba(255,255,255,0.82); font-size:13px; font-weight:700; letter-spacing:0.05em; text-transform:uppercase; transition:color .15s ease; white-space:nowrap;}
.navlinks a:hover, .navlinks a.active{color:var(--sky);}
.cta-btn{background:var(--sky); color:var(--navy-deep) !important; font-family:'Anton', sans-serif; letter-spacing:0.05em; font-size:13px; padding:12px 22px; border-radius:3px; text-transform:uppercase; transition:background .15s ease, transform .15s ease; white-space:nowrap;}
.cta-btn:hover{background:#fff; transform:translateY(-1px);}
@media (max-width:980px){ .navlinks{display:none;} }

.pagehero{position:relative; overflow:hidden; background:linear-gradient(180deg, var(--navy) 0%, var(--navy-deep) 100%); padding:88px 0 68px;}
.pagehero .sash{position:absolute; inset:0; z-index:0; pointer-events:none;}
.pagehero .sash span{position:absolute; background:linear-gradient(90deg, var(--sky) 0%, var(--sky-deep) 100%); opacity:0.12; width:180%; height:120px; transform:rotate(-9deg); left:-40%;}
.pagehero .sash span:nth-child(2){top:220px; opacity:0.07; left:-60%;}
.pagehero-inner{position:relative; z-index:1;}
.pagehero .eyebrow{color:var(--sky);}
.pagehero h1{color:#fff; font-size:clamp(34px,5.4vw,58px); line-height:1; margin:16px 0 16px;}
.pagehero p{color:rgba(255,255,255,0.72); font-size:16.5px; line-height:1.6; max-width:600px;}

.hero{position:relative; overflow:hidden; background:linear-gradient(180deg, var(--navy) 0%, var(--navy-deep) 100%); padding:110px 0 90px;}
.hero .sash{position:absolute; inset:0; z-index:0; pointer-events:none;}
.hero .sash span{position:absolute; background:linear-gradient(90deg, var(--sky) 0%, var(--sky-deep) 100%); opacity:0.14; width:180%; height:130px; transform:rotate(-9deg);}
.hero .sash span:nth-child(1){ top:-20px; left:-40%; }
.hero .sash span:nth-child(2){ top:280px; left:-60%; opacity:0.08; height:90px;}
.hero-inner{position:relative; z-index:1; display:grid; grid-template-columns:auto 1fr; gap:56px; align-items:center;}
@media (max-width:800px){ .hero-inner{grid-template-columns:1fr; text-align:center; justify-items:center;} }
.hero-crest img{width:190px; height:190px;}
@media (max-width:800px){ .hero-crest img{width:140px;height:140px;} }
.hero-copy .eyebrow{color:var(--sky);}
.hero-copy h1{color:#fff; font-size:clamp(38px, 6vw, 68px); line-height:0.98; margin:18px 0 22px;}
.hero-copy h1 em{color:var(--sky); font-style:normal;}
.hero-copy p{color:rgba(255,255,255,0.72); font-size:17px; line-height:1.6; max-width:520px; margin-bottom:34px;}
@media (max-width:800px){ .hero-copy p{margin-left:auto;margin-right:auto;} }
.hero-actions{display:flex; gap:14px; flex-wrap:wrap;}
@media (max-width:800px){ .hero-actions{justify-content:center;} }
.btn-ghost{border:1.5px solid rgba(255,255,255,0.35); color:#fff !important; font-family:'Anton', sans-serif; letter-spacing:0.05em; font-size:13px; padding:12px 22px; border-radius:3px; text-transform:uppercase; transition:border-color .15s ease, background .15s ease;}
.btn-ghost:hover{border-color:#fff; background:rgba(255,255,255,0.06);}

.strip{background:var(--sky); color:var(--navy-deep); padding:14px 0; overflow:hidden; white-space:nowrap;}
.strip .track{display:inline-flex; gap:40px; font-family:'Anton', sans-serif; font-size:13px; letter-spacing:0.14em; animation:scroll 26s linear infinite;}
.strip .track span.dot::before{content:"\\25CF"; margin-right:40px; font-size:6px; vertical-align:middle;}
@keyframes scroll{ from{transform:translateX(0);} to{transform:translateX(-50%);} }

section{padding:96px 0;}
@media (max-width:640px){ section{padding:64px 0;} }
.sec-head{max-width:640px; margin-bottom:56px;}
.sec-head .eyebrow{color:var(--sky-deep);}
.sec-head h2{font-size:clamp(30px,4vw,44px); margin-top:14px; color:var(--navy);}
.sec-head p.lede{margin-top:14px; font-size:16px; line-height:1.6; color:#5a6274;}

.about{background:#fff; border-top:1px solid var(--line); border-bottom:1px solid var(--line);}
.about-grid{display:grid; grid-template-columns:1.15fr 0.85fr; gap:70px; align-items:start;}
@media (max-width:860px){ .about-grid{grid-template-columns:1fr;} }
.about-copy p{font-size:16.5px; line-height:1.75; color:#39415a; margin-bottom:18px;}
.stat-grid{display:grid; grid-template-columns:1fr 1fr; gap:1px; background:var(--line); border:1px solid var(--line);}
.stat{background:#fff; padding:26px 24px;}
.stat .n{font-family:'Anton', sans-serif; font-size:34px; color:var(--navy);}
.stat .l{font-size:12px; letter-spacing:0.08em; text-transform:uppercase; color:#6b7284; margin-top:6px;}

.programs{background:var(--paper);}
.card-grid{display:grid; grid-template-columns:repeat(3,1fr); gap:22px;}
@media (max-width:900px){ .card-grid{grid-template-columns:1fr 1fr;} }
@media (max-width:600px){ .card-grid{grid-template-columns:1fr;} }
.card-grid.pathway{grid-template-columns:repeat(4,1fr);}
@media (max-width:1000px){ .card-grid.pathway{grid-template-columns:1fr 1fr;} }
@media (max-width:600px){ .card-grid.pathway{grid-template-columns:1fr;} }
.card{background:#fff; border:1px solid var(--line); border-radius:4px; padding:30px 26px; position:relative; overflow:hidden; transition:transform .18s ease, box-shadow .18s ease;}
.card:hover{transform:translateY(-3px); box-shadow:0 14px 30px rgba(20,38,69,0.09);}
.card::before{content:""; position:absolute; top:0; left:0; height:4px; width:100%; background:linear-gradient(90deg, var(--sky), var(--sky-deep));}
.card .tag{font-family:'Anton', sans-serif; font-size:11px; letter-spacing:0.14em; color:var(--sky-deep); text-transform:uppercase;}
.card h3{font-size:20px; margin:10px 0 10px; color:var(--navy);}
.card p{font-size:14.5px; line-height:1.6; color:#5a6274;}
.card ul{margin-top:12px; padding-left:18px;}
.card li{font-size:13.5px; line-height:1.7; color:#5a6274;}

/* program detail rows (programs.html) */
.prog-row{display:grid; grid-template-columns:200px 1fr; gap:40px; padding:36px 0; border-top:1px solid var(--line);}
.prog-row:last-child{border-bottom:1px solid var(--line);}
@media (max-width:760px){ .prog-row{grid-template-columns:1fr; gap:12px;} }
.prog-row .lbl{font-family:'Anton', sans-serif; font-size:12px; letter-spacing:0.1em; color:var(--sky-deep); text-transform:uppercase;}
.prog-row .age{font-family:'Anton', sans-serif; font-size:22px; color:var(--navy); margin-top:6px;}
.prog-row .body h3{font-size:22px; color:var(--navy); margin-bottom:10px;}
.prog-row .body p{font-size:15.5px; line-height:1.7; color:#454d64; margin-bottom:10px;}
.prog-row .meta{display:flex; gap:10px; flex-wrap:wrap; margin-top:14px;}
.pill{background:var(--paper); border:1px solid var(--line); border-radius:20px; padding:6px 14px; font-size:12.5px; color:var(--navy); font-weight:600;}

/* sponsors */
.tier-block{margin-bottom:46px;}
.tier-block:last-child{margin-bottom:0;}
.tier-label{display:flex; align-items:center; gap:14px; margin-bottom:22px;}
.tier-label .badge{font-family:'Anton', sans-serif; font-size:12px; letter-spacing:0.12em; text-transform:uppercase; padding:6px 14px; border-radius:3px; color:#fff;}
.badge.platinum{background:#5b6472;}
.badge.gold{background:#c79a3c;}
.badge.direct{background:var(--sky-deep);}
.badge.open{background:transparent; color:var(--navy); border:1.5px dashed var(--line);}
.tier-label .line{flex:1; height:1px; background:var(--line);}
.sponsor-grid{display:grid; grid-template-columns:repeat(3,1fr); gap:18px;}
@media (max-width:760px){ .sponsor-grid{grid-template-columns:1fr 1fr;} }
@media (max-width:480px){ .sponsor-grid{grid-template-columns:1fr;} }
.sponsor-card{background:#fff; border:1px solid var(--line); border-radius:4px; padding:26px 22px; display:flex; flex-direction:column; gap:6px; justify-content:center; min-height:96px;}
.sponsor-card.logo{align-items:center; justify-content:center; padding:22px;}
.sponsor-card.logo img{max-height:56px; max-width:100%; width:auto; object-fit:contain;}
.sponsor-card .sname{font-family:'Anton', sans-serif; font-size:17px; color:var(--navy); letter-spacing:0.01em;}
.sponsor-card .sdesc{font-size:13px; color:#6b7284;}
.sponsor-card.cta{border-style:dashed; align-items:flex-start; justify-content:center;}
.sponsor-card.cta a{font-size:13px; font-weight:700; color:var(--sky-deep); text-decoration:underline;}

/* donate */
.donate{background:var(--navy); border-top:3px solid var(--gold); color:#fff;}
.donate-grid{display:grid; grid-template-columns:1.15fr 0.85fr; gap:60px; align-items:center;}
@media (max-width:860px){ .donate-grid{grid-template-columns:1fr; gap:40px;} }
.donate .eyebrow{color:var(--gold);}
.donate h2{color:#fff; font-size:clamp(30px,4vw,44px); margin-top:14px;}
.donate p.lead{color:rgba(255,255,255,0.78); font-size:16.5px; line-height:1.7; margin-top:18px; max-width:560px;}
.donate ul{list-style:none; margin-top:22px; display:grid; grid-template-columns:1fr 1fr; gap:13px 26px; padding:0;}
@media (max-width:640px){ .donate ul{grid-template-columns:1fr;} }
.donate li b{color:#fff; font-weight:700;}
.donate li{color:rgba(255,255,255,0.85); font-size:15px; line-height:1.55; padding-left:26px; position:relative;}
.donate li::before{content:"\25C6"; position:absolute; left:0; top:4px; color:var(--gold); font-size:11px;}
.donate-card{border:1px solid rgba(255,255,255,0.18); border-radius:6px; padding:34px 32px; background:rgba(255,255,255,0.03);}
.donate-card .lbl{font-family:'Anton', sans-serif; font-size:12px; letter-spacing:0.18em; color:var(--sky); text-transform:uppercase;}
.donate-card .lbl a:hover{color:#fff;}
.donate-btn{display:inline-block; margin-top:18px; background:var(--gold); color:var(--navy-deep); font-family:'Anton', sans-serif; font-size:13px; letter-spacing:0.06em; text-transform:uppercase; padding:14px 26px; border-radius:3px; transition:background .15s ease;}
.donate-btn:hover{background:#fff;}
.donate-card .fine{margin-top:18px; font-size:13px; line-height:1.65; color:rgba(255,255,255,0.6);}
.donate-card .fine b{color:rgba(255,255,255,0.85);}

/* shop */
.shop-grid{display:grid; grid-template-columns:1fr 1fr; gap:22px;}
@media (max-width:720px){ .shop-grid{grid-template-columns:1fr;} }
.shop-card{background:#fff; border:1px solid var(--line); border-radius:4px; overflow:hidden; display:flex; flex-direction:column;}
.shop-card .swatch{height:8px; background:linear-gradient(90deg, var(--sky), var(--sky-deep));}
.shop-card .body{padding:30px 28px; flex:1; display:flex; flex-direction:column;}
.shop-card .tag{font-family:'Anton', sans-serif; font-size:11px; letter-spacing:0.14em; color:var(--sky-deep); text-transform:uppercase;}
.shop-card h3{font-size:22px; color:var(--navy); margin:10px 0 12px;}
.shop-card p{font-size:14.5px; line-height:1.65; color:#5a6274; margin-bottom:20px; flex:1;}
.shop-card .go{align-self:flex-start; font-family:'Anton', sans-serif; font-size:12.5px; letter-spacing:0.06em; text-transform:uppercase; background:var(--navy); color:#fff; padding:11px 20px; border-radius:3px; transition:background .15s ease;}
.shop-card .go:hover{background:var(--sky-deep);}

/* alumni */
.alumni-grid{display:grid; grid-template-columns:repeat(2,1fr); gap:20px;}
@media (max-width:720px){ .alumni-grid{grid-template-columns:1fr;} }
.alum-card{background:#fff; border:1px solid var(--line); border-radius:4px; padding:26px 26px; display:flex; gap:18px; align-items:flex-start;}
.alum-card .mono{font-family:'Anton', sans-serif; font-size:22px; color:var(--sky-deep); flex-shrink:0; width:44px;}
.alum-card h3{font-size:18px; color:var(--navy); margin-bottom:6px;}
.alum-card p{font-size:14px; line-height:1.6; color:#5a6274;}
.alum-note{background:#fff; border:1px solid var(--line); border-left:4px solid var(--sky); padding:22px 26px; border-radius:2px; font-size:14.5px; line-height:1.7; color:#454d64; margin-top:26px;}

/* matrix callout */
.matrix-callout{
  background:var(--navy); border-radius:6px; padding:34px 36px; margin-bottom:60px;
  display:flex; align-items:center; justify-content:space-between; gap:24px; flex-wrap:wrap;
  position:relative; overflow:hidden;
}
.matrix-callout::before{
  content:""; position:absolute; top:-30px; right:-30px; width:160px; height:160px;
  background:linear-gradient(135deg, var(--sky), var(--sky-deep)); opacity:0.15; border-radius:50%;
}
.matrix-callout .txt{position:relative; z-index:1;}
.matrix-callout .txt .eyebrow{color:var(--sky);}
.matrix-callout .txt h3{color:#fff; font-size:22px; margin-top:10px;}
.matrix-callout .txt p{color:rgba(255,255,255,0.68); font-size:14.5px; margin-top:6px; max-width:420px;}
.matrix-callout .go{position:relative; z-index:1; flex-shrink:0; font-family:'Anton', sans-serif; font-size:13px; letter-spacing:0.05em; text-transform:uppercase; background:var(--sky); color:var(--navy-deep) !important; padding:14px 26px; border-radius:3px; transition:background .15s ease;}
.matrix-callout .go:hover{background:#fff;}

/* schedule */
.sched-table{width:100%; border-collapse:collapse; background:#fff; border:1px solid var(--line); border-radius:4px; overflow:hidden;}
.sched-table th{
  background:var(--navy); color:#fff; font-family:'Anton', sans-serif; font-size:11.5px; letter-spacing:0.08em;
  text-transform:uppercase; text-align:left; padding:14px 18px;
}
.sched-table td{padding:16px 18px; border-top:1px solid var(--line); font-size:14.5px; color:#39415a;}
.sched-table tr:hover td{background:var(--paper);}
.sched-table .team{font-weight:700; color:var(--navy);}
.sched-note{font-size:13px; color:#6b7284; margin-top:14px; line-height:1.6;}
.sched-wrap{overflow-x:auto;}
@media (max-width:700px){ .sched-table{font-size:13px;} .sched-table th, .sched-table td{padding:10px 12px;} }

/* resources */
.res-grid{display:grid; grid-template-columns:1fr 1fr; gap:16px;}
@media (max-width:700px){ .res-grid{grid-template-columns:1fr;} }
.res-link{
  display:flex; align-items:center; justify-content:space-between; gap:14px;
  background:#fff; border:1px solid var(--line); border-radius:4px; padding:20px 22px;
  transition:border-color .15s ease, transform .15s ease;
}
.res-link:hover{border-color:var(--sky-deep); transform:translateX(2px);}
.res-link .t{font-weight:700; color:var(--navy); font-size:15.5px;}
.res-link .d{font-size:12.5px; color:#6b7284; margin-top:3px;}
.res-link .arrow{color:var(--sky-deep); font-family:'Anton', sans-serif; font-size:16px; flex-shrink:0;}
.res-group-label{font-family:'Anton', sans-serif; font-size:12px; letter-spacing:0.12em; text-transform:uppercase; color:var(--sky-deep); margin:44px 0 18px;}
.res-group-label:first-child{margin-top:0;}

/* contact */
.contact{background:var(--navy-deep); color:#fff; position:relative; overflow:hidden;}
.contact .sash{position:absolute; inset:0;}
.contact .sash span{position:absolute; width:180%; height:100px; left:-50%; background:linear-gradient(90deg, var(--sky), var(--sky-deep)); opacity:0.06; transform:rotate(-9deg);}
.contact .sash span:nth-child(1){top:-10px;}
.contact .sash span:nth-child(2){bottom:20px;}
.contact-inner{position:relative; z-index:1; display:grid; grid-template-columns:1fr 1fr; gap:70px;}
@media (max-width:860px){ .contact-inner{grid-template-columns:1fr; gap:44px;} }
.contact .sec-head h2{color:#fff;}
.contact .sec-head .eyebrow{color:var(--sky);}
.info-row{display:flex; gap:16px; padding:18px 0; border-top:1px solid rgba(255,255,255,0.12);}
.info-row:last-child{border-bottom:1px solid rgba(255,255,255,0.12);}
.info-row .ic{width:38px; height:38px; border-radius:50%; background:rgba(124,197,234,0.14); display:flex; align-items:center; justify-content:center; flex-shrink:0; color:var(--sky);}
.info-row .k{font-size:11.5px; letter-spacing:0.1em; text-transform:uppercase; color:var(--sky); margin-bottom:4px;}
.info-row .v{font-size:15.5px; line-height:1.55; color:rgba(255,255,255,0.9);}
.info-row a.v:hover{color:#fff; text-decoration:underline;}
.socials{display:flex; gap:12px; margin-top:28px;}
.socials a{width:42px; height:42px; border-radius:50%; border:1px solid rgba(255,255,255,0.25); display:flex; align-items:center; justify-content:center; transition:background .15s ease, border-color .15s ease;}
.socials a:hover{background:var(--sky); border-color:var(--sky); color:var(--navy-deep);}
.map-box{border:1px solid rgba(255,255,255,0.15); border-radius:4px; overflow:hidden; aspect-ratio:4/3; background:#0e1c34;}
.map-box iframe{width:100%; height:100%; border:0; filter:grayscale(0.3) contrast(1.05);}

footer{background:var(--navy-deep); border-top:1px solid rgba(255,255,255,0.08); padding:34px 0;}
.foot-inner{display:flex; align-items:center; justify-content:space-between; gap:20px; flex-wrap:wrap;}
.foot-brand{display:flex; align-items:center; gap:12px; color:rgba(255,255,255,0.55); font-size:13px;}
.foot-brand img{height:30px;width:30px;}
.foot-links{display:flex; gap:22px; flex-wrap:wrap;}
.foot-links a{color:rgba(255,255,255,0.55); font-size:13px; transition:color .15s ease;}
.foot-links a:hover{color:var(--sky);}
"""

HEAD = """<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Public+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{css}</style>
</head>"""

def nav(active):
    def cls(name):
        return ' class="active"' if name == active else ''
    return f"""<header>
  <nav class="wrap">
    <a class="brand" href="index.html">
      <img src="{LOGO}" alt="Barrie Rugby crest">
      <div class="word">BARRIE RUGBY<span>CLUB &middot; EST. 1967</span></div>
    </a>
    <div class="navlinks">
      <a href="index.html#about"{cls('about')}>About</a>
      <a href="programs.html"{cls('programs')}>Programs</a>
      <a href="alumni.html"{cls('alumni')}>Alumni</a>
      <a href="index.html#sponsors"{cls('sponsors')}>Sponsors</a>
      <a href="index.html#donate">Donate</a>
      <a href="index.html#shop"{cls('shop')}>Shop</a>
      <a href="resources.html"{cls('resources')}>Resources</a>
      <a href="index.html#contact"{cls('contact')}>Contact</a>
    </div>
    <a class="cta-btn" href="https://www.playhq.com/ca/rugby-canada/register/c4290e">Register</a>
  </nav>
</header>"""

FOOTER = f"""<footer>
  <div class="wrap foot-inner">
    <div class="foot-brand">
      <img src="{LOGO}" alt="Barrie Rugby crest">
      <span>&copy; 2026 Barrie Rugby Club. All rights reserved.</span>
    </div>
    <div class="foot-links">
      <a href="index.html#about">About</a>
      <a href="programs.html">Programs</a>
      <a href="alumni.html">Alumni</a>
      <a href="index.html#sponsors">Sponsors</a>
      <a href="index.html#donate">Donate</a>
      <a href="index.html#shop">Shop</a>
      <a href="resources.html">Resources</a>
      <a href="index.html#contact">Contact</a>
    </div>
  </div>
</footer>"""

CONTACT_SECTION = """
<section class="contact" id="contact">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Get In Touch</span>
      <h2>Come find us at Jim Hamilton Field.</h2>
    </div>
    <div class="contact-inner">
      <div class="info-col">
        <div class="info-row">
          <div class="ic"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
          <div><div class="k">Address</div><a class="v" href="https://maps.google.com/?q=2100+Nursery+Rd,+Barrie,+ON+L0L+1Y2" target="_blank" rel="noopener">2100 Nursery Rd, Barrie, ON L0L 1Y2</a></div>
        </div>
        <div class="info-row">
          <div class="ic"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 6l-10 7L2 6"/><rect x="2" y="4" width="20" height="16" rx="2"/></svg></div>
          <div><div class="k">Email</div><a class="v" href="mailto:info@barrierugbyclub.com">info@barrierugbyclub.com</a></div>
        </div>
        <div class="socials">
          <a href="https://www.instagram.com/barrierugby" target="_blank" rel="noopener" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg></a>
          <a href="https://www.facebook.com/barrierugbyclub/" target="_blank" rel="noopener" aria-label="Facebook"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12z"/></svg></a>
          <a href="https://www.tiktok.com/@barrierugby" target="_blank" rel="noopener" aria-label="TikTok"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 5.8a4.6 4.6 0 0 1-3.3-1.4v9.7a5.3 5.3 0 1 1-4.6-5.3v2.4a2.9 2.9 0 1 0 2.1 2.8V2h2.5a4.6 4.6 0 0 0 3.3 3.9z"/></svg></a>
          <a href="https://twitter.com/barrierugbyclub" target="_blank" rel="noopener" aria-label="X / Twitter"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 2H22l-7.6 8.7L23.3 22h-7l-5.5-6.8L4.5 22H1.4l8.1-9.3L1 2h7.2l5 6.3L18.9 2zm-1.2 18h1.7L7.3 4H5.5l12.2 16z"/></svg></a>
        </div>
      </div>
      <div class="map-box">
        <iframe src="https://maps.google.com/maps?q=2100%20Nursery%20Rd%2C%20Barrie%2C%20ON%20L0L%201Y2&t=&z=13&ie=UTF8&iwloc=&output=embed" loading="lazy"></iframe>
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# INDEX.HTML
# ---------------------------------------------------------------------------
index_body = f"""
<section class="hero">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap hero-inner">
    <div class="hero-crest"><img src="{LOGO}" alt="Barrie Rugby crest"></div>
    <div class="hero-copy">
      <span class="eyebrow">Barrie, Ontario &middot; Since 1967</span>
      <h1>RUGBY IS<br>BUILT<br><em>HERE.</em></h1>
      <p>Competitive and instructional rugby for Barrie and the surrounding area, from Under 6 through Senior Men's and Women's. On the pitch and off it, everyone gets a place on the team.</p>
      <div class="hero-actions">
        <a class="cta-btn" href="https://www.playhq.com/ca/rugby-canada/register/c4290e">Register Now</a>
        <a class="btn-ghost" href="#contact">Get In Touch</a>
      </div>
    </div>
  </div>
</section>

<div class="strip">
  <div class="track">
    <span class="dot">EST. 1967</span><span class="dot">JIM HAMILTON FIELD</span><span class="dot">U6 &rarr; U18</span><span class="dot">MEN'S &amp; WOMEN'S</span><span class="dot">BARRIE, ON</span>
    <span class="dot">EST. 1967</span><span class="dot">JIM HAMILTON FIELD</span><span class="dot">U6 &rarr; U18</span><span class="dot">MEN'S &amp; WOMEN'S</span><span class="dot">BARRIE, ON</span>
  </div>
</div>

<section class="about" id="about">
  <div class="wrap about-grid">
    <div class="about-copy">
      <div class="sec-head" style="margin-bottom:26px;">
        <span class="eyebrow">Our Club</span>
        <h2>Nearly six decades on Barrie pitches.</h2>
      </div>
      <p>Barrie Rugby was founded in 1967 by a group of athletes from Barrie and Base Borden. Today the club fields instructional and competitive teams for every age from Under 6 through Senior, welcoming new players regardless of experience.</p>
      <p>President Pierre Gautier puts it simply: rugby builds teamwork and discipline, and it's one of the most welcoming sports there is for someone trying it for the first time.</p>
      <p>Senior Men's and Women's teams play home matches on Jim Hamilton Field at the Barrie Community Sports Complex. Junior and youth programs run instructional and competitive streams right through to U18.</p>
    </div>
    <div class="stat-grid">
      <div class="stat"><div class="n">1967</div><div class="l">Club Founded</div></div>
      <div class="stat"><div class="n">U6&ndash;Sr.</div><div class="l">Age Groups</div></div>
      <div class="stat"><div class="n">2</div><div class="l">Senior Sides &mdash; M &amp; W</div></div>
      <div class="stat"><div class="n">4</div><div class="l">Ways To Follow Along</div></div>
    </div>
  </div>
</section>

<section class="programs" id="teams">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Programs</span>
      <h2>A place on the team, at every age.</h2>
      <p class="lede">Full age-by-age breakdown, schedules, and what to expect &mdash; <a href="programs.html" style="color:var(--sky-deep); font-weight:700; text-decoration:underline;">see the full Programs page &rarr;</a></p>
    </div>
    <div class="card-grid pathway" style="margin-bottom:22px;">
      <div class="card"><span class="tag">Minis</span><h3>U6 &ndash; U10</h3><p>First contact with the game &mdash; festival-style instructional rugby built around fun, footwork, and the fundamentals.</p></div>
      <div class="card"><span class="tag">Youth</span><h3>U12 &middot; U14 &mdash; Boys &amp; Girls</h3><p>The step into competitive rugby, with separate boys' and girls' teams at both ages and single-game fixtures each week.</p></div>
      <div class="card"><span class="tag">Junior</span><h3>U16 &middot; U18 &mdash; Boys &amp; Girls</h3><p>The top of the junior pathway &mdash; recent tours have taken teams to Portugal and France.</p></div>
      <div class="card"><span class="tag">Senior</span><h3>Men's &amp; Women's</h3><p>Competitive senior rugby on Jim Hamilton Field, open to new and returning players.</p></div>
    </div>
    <div class="card-grid">
      <div class="card"><span class="tag">In Schools</span><h3>Rugby Development Officers</h3><p>Our RDO program brings rugby into Barrie-area elementary and high schools.</p></div>
      <div class="card"><span class="tag">Access</span><h3>Financial Assistance</h3><p>The RUK program helps cover registration costs, because cost shouldn't decide who plays.</p></div>
      <div class="card"><span class="tag">Officiating</span><h3>Match Officials</h3><p>Rugby Ontario-registered officiating pathway for members who want to referee.</p></div>
    </div>
  </div>
</section>

<section id="sponsors" style="background:#fff; border-top:1px solid var(--line); border-bottom:1px solid var(--line);">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Thank You</span>
      <h2>Our Sponsors</h2>
      <p class="lede">Barrie Rugby runs on the back of local businesses who back the club year after year.</p>
    </div>

    <div class="tier-block">
      <div class="tier-label"><span class="badge platinum">Platinum</span><span class="line"></span></div>
      <div class="sponsor-grid">
        <div class="sponsor-card logo"><img src="{WESTERN}" alt="Western"></div>
      </div>
    </div>

    <div class="tier-block">
      <div class="tier-label"><span class="badge gold">Gold</span><span class="line"></span></div>
      <div class="sponsor-grid">
        <div class="sponsor-card logo"><img src="{DONALEIGHS}" alt="Donaleigh's"></div>
      </div>
    </div>

    <div class="tier-block">
      <div class="tier-label"><span class="badge direct">Direct</span><span class="line"></span></div>
      <div class="sponsor-grid">
        <div class="sponsor-card logo"><img src="{TODDSMITH}" alt="Todd Smith Mortgages"></div>
        <div class="sponsor-card logo"><img src="{MITSUBISHI}" alt="Barrie Mitsubishi"></div>
        <div class="sponsor-card cta"><div class="sname">Become a Sponsor</div><a href="mailto:info@barrierugbyclub.com">info@barrierugbyclub.com &rarr;</a></div>
      </div>
    </div>
  </div>
</section>

<section class="donate" id="donate">
  <div class="wrap donate-grid">
    <div>
      <span class="eyebrow">Support The Club</span>
      <h2>The Memorial &amp; Development Fund</h2>
      <p class="lead">Established to honour past members and grow the game they loved, the fund accepts donations through the National Sport Trust Fund &mdash; in memory of a clubmate, or simply in support of rugby in Barrie. Every dollar goes back onto the pitch, across six areas:</p>
      <ul>
        <li><b>Equipment</b> &mdash; repair and upgrades to training, match-day, and safety gear, from tackle bags to AEDs</li>
        <li><b>Coach development</b> &mdash; World Rugby and Rugby Ontario certifications, clinics, and Rugby Safe training</li>
        <li><b>Match official development</b> &mdash; certification and upgrading pathways for club members who referee</li>
        <li><b>Club development</b> &mdash; facilities, field maintenance, clubhouse projects, and club technology</li>
        <li><b>Training opportunities</b> &mdash; ID camps, rep program subsidies, strength &amp; conditioning, and pathway support</li>
        <li><b>Member retention &amp; assistance</b> &mdash; registration subsidies, kit help, and events that build belonging</li>
      </ul>
    </div>
    <div class="donate-card">
      <div class="lbl"><a href="https://www.ontariosportnetwork.ca/nstf-projects/391-barrie-rugby-club" target="_blank" rel="noopener">National Sport Trust Fund &middot; Project 391</a></div><br>
      <a class="donate-btn" href="https://forms.logiforms.com/formdata/user_forms/74769_1745267/345060/page1.html" target="_blank" rel="noopener">Donate Today &rarr;</a>
      <p class="fine">Donations are processed by the National Sport Trust Fund &ndash; Ontario and are eligible for a charitable tax receipt. On the donation form, select the club and the <b>Memorial and Development Fund</b> project.</p>
    </div>
  </div>
</section>

<section id="shop" class="programs">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Gear Up</span>
      <h2>Shop the club.</h2>
      <p class="lede">Two official stores &mdash; one for everyday fan wear, one for on-field kit.</p>
    </div>
    <div class="shop-grid">
      <div class="shop-card">
        <div class="swatch"></div>
        <div class="body">
          <span class="tag">Fan Store</span>
          <h3>Official Online Merch</h3>
          <p>Casual fan apparel and lifestyle wear in club colours &mdash; the everyday store for supporters, alumni, and families on the sideline. Hosted by 4th &amp; Standard.</p>
          <a class="go" href="https://4hundredsfs.com/collections/barrie-rugby" target="_blank" rel="noopener">Shop Merch &rarr;</a>
        </div>
      </div>
      <div class="shop-card">
        <div class="swatch"></div>
        <div class="body">
          <span class="tag">Playing Kit</span>
          <h3>On-Field Kit</h3>
          <p>Official match and training kit &mdash; jerseys, shorts, and playing gear supplied through Gilbert Rugby Canada, the sport's official ball and kit maker.</p>
          <a class="go" href="https://gilbertrugbycanada.com/collections/barrie-rugby-club" target="_blank" rel="noopener">Shop Kit &rarr;</a>
        </div>
      </div>
    </div>
  </div>
</section>

{CONTACT_SECTION}
"""

# ---------------------------------------------------------------------------
# PROGRAMS.HTML
# ---------------------------------------------------------------------------
programs_body = f"""
<section class="pagehero">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap pagehero-inner">
    <span class="eyebrow">Programs</span>
    <h1>A team for every age.</h1>
    <p>From first contact with the ball to competitive senior rugby, here's how Barrie Rugby's programs break down &mdash; and where you fit in.</p>
  </div>
</section>

<section style="padding-top:64px;">
  <div class="wrap">

    <div class="prog-row">
      <div><div class="lbl">Minis</div><div class="age">U6&ndash;U10</div></div>
      <div class="body">
        <h3>First touches, real fun</h3>
        <p>Festival-style instructional rugby built around ball skills, footwork, and enjoying the game &mdash; open to complete beginners. No experience needed, and no player is turned away for cost (see Financial Assistance below).</p>
        <div class="meta"><span class="pill">Instructional</span><span class="pill">Festival format</span><span class="pill">All experience levels</span></div>
      </div>
    </div>

    <div class="prog-row">
      <div><div class="lbl">Youth</div><div class="age">U12 &amp; U14</div></div>
      <div class="body">
        <h3>U12 &amp; U14 Boys &amp; Girls</h3>
        <p>Entry point into competitive age-grade rugby, with separate boys' and girls' teams at both ages, playing a full Rugby Ontario / Toronto Rugby Union (TRU) calendar including Regionals &mdash; U12s play single games on Sundays, U14s on Saturdays.</p>
        <div class="meta"><span class="pill">Competitive</span><span class="pill">Boys &amp; Girls sides</span><span class="pill">Regionals</span></div>
      </div>
    </div>

    <div class="prog-row">
      <div><div class="lbl">Junior</div><div class="age">U16</div></div>
      <div class="body">
        <h3>U16 Boys &amp; Girls</h3>
        <p>Competitive rugby with a track record on the road &mdash; recent squads have travelled to the Tropical 7s in Tampa Bay, where Barrie's U16 girls finished third overall, and hosted touring sides from overseas.</p>
        <div class="meta"><span class="pill">Competitive</span><span class="pill">Boys &amp; Girls sides</span><span class="pill">Touring history</span></div>
      </div>
    </div>

    <div class="prog-row">
      <div><div class="lbl">Junior</div><div class="age">U18</div></div>
      <div class="body">
        <h3>U18 Boys &amp; Girls</h3>
        <p>The top junior tier, playing TRU Regional Qualifiers and representative fixtures &mdash; recent U18 sides have toured internationally, including the girls' side's tour of Portugal and the boys' side's 2026 tour of France.</p>
        <div class="meta"><span class="pill">Competitive</span><span class="pill">Boys &amp; Girls sides</span><span class="pill">Pathway to Senior</span></div>
      </div>
    </div>

    <div class="prog-row">
      <div><div class="lbl">Senior</div><div class="age">Sr.</div></div>
      <div class="body">
        <h3>Men's &amp; Women's</h3>
        <p>Competitive senior rugby playing home matches on Jim Hamilton Field at the Barrie Community Sports Complex. Open to new and returning players &mdash; no prior club affiliation required.</p>
        <div class="meta"><span class="pill">Competitive</span><span class="pill">Jim Hamilton Field</span><span class="pill">New players welcome</span></div>
      </div>
    </div>

    <div class="prog-row">
      <div><div class="lbl">In Schools</div><div class="age">RDO</div></div>
      <div class="body">
        <h3>Rugby Development Officers</h3>
        <p>Barrie Rugby's RDO program partners with elementary and high schools across Simcoe County to introduce rugby in phys-ed classes, supporting teachers who are running the game for the first time.</p>
        <div class="meta"><span class="pill">School outreach</span><span class="pill">Teacher support</span><span class="pill">Elementary &amp; High School</span></div>
      </div>
    </div>

    <div class="prog-row">
      <div><div class="lbl">Access</div><div class="age">RUK</div></div>
      <div class="body">
        <h3>Financial Assistance Program</h3>
        <p>The RUK Financial Assistance Program helps cover registration costs for players and families who need it, because cost shouldn't decide who gets to play.</p>
        <div class="meta"><span class="pill">Registration support</span><span class="pill">Confidential</span></div>
      </div>
    </div>

    <div class="prog-row">
      <div><div class="lbl">Officiating</div><div class="age">Ref</div></div>
      <div class="body">
        <h3>Match Officials</h3>
        <p>A Rugby Ontario-registered officiating pathway for members who want to referee alongside &mdash; or instead of &mdash; playing or coaching.</p>
        <div class="meta"><span class="pill">Rugby Ontario registered</span><span class="pill">Open to all members</span></div>
      </div>
    </div>

  </div>
</section>

<section style="background:#fff; border-top:1px solid var(--line); padding-top:70px;">
  <div class="wrap">
    <div class="matrix-callout" id="matrix">
      <div class="txt">
        <span class="eyebrow">Reference</span>
        <h3>Age Grade Matrix</h3>
        <p>The full Rugby Ontario-aligned breakdown of which age group your player belongs in, contact rules, and format by age.</p>
      </div>
      <a class="go" href="https://www.barrierugby.com/_files/ugd/95a192_ac77f1b87a694696b5e5ce6cb2b75ec5.pdf" target="_blank" rel="noopener">View PDF &rarr;</a>
    </div>

    <div class="sec-head">
      <span class="eyebrow">Weekly Schedule</span>
      <h2>Practices &amp; game days.</h2>
      <p class="lede">Practice times below are confirmed &mdash; game kickoff times are set week to week and shared by your coaches.</p>
    </div>

    <h3 style="font-size:15px; color:var(--navy); margin-bottom:14px; font-family:'Anton', sans-serif; letter-spacing:0.04em; text-transform:uppercase;">Practices</h3>
    <div class="sched-wrap">
      <table class="sched-table">
        <tr><th>Team</th><th>Day</th><th>Time</th><th>Location</th></tr>
        <tr><td class="team">Minis (U6&ndash;U10)</td><td>Monday &amp; Wednesday</td><td>6:00&ndash;7:30 PM</td><td>The Tree Nursery</td></tr>
        <tr><td class="team">U12 Boys &amp; Girls</td><td>Monday &amp; Wednesday</td><td>6:00&ndash;7:30 PM</td><td>The Tree Nursery</td></tr>
        <tr><td class="team">U14 Boys &amp; Girls</td><td>Monday &amp; Wednesday</td><td>6:00&ndash;8:00 PM</td><td>Jim Hamilton Field</td></tr>
        <tr><td class="team">U16 Boys &amp; Girls</td><td>Monday &amp; Wednesday</td><td>6:00&ndash;8:00 PM</td><td>Jim Hamilton Field</td></tr>
        <tr><td class="team">U18 Girls</td><td>Monday &amp; Thursday</td><td>6:00&ndash;8:00 PM</td><td>Jim Hamilton Field</td></tr>
        <tr><td class="team">U18 Boys</td><td>Monday</td><td>6:00&ndash;8:00 PM</td><td>Jim Hamilton Field</td></tr>
        <tr><td class="team">Senior Men's</td><td>Tuesday &amp; Thursday</td><td>6:00&ndash;8:00 PM</td><td>Jim Hamilton Field</td></tr>
        <tr><td class="team">Senior Women's</td><td>Tuesday &amp; Thursday</td><td>6:00&ndash;8:00 PM</td><td>Jim Hamilton Field</td></tr>
      </table>
    </div>

    <h3 style="font-size:15px; color:var(--navy); margin:40px 0 14px; font-family:'Anton', sans-serif; letter-spacing:0.04em; text-transform:uppercase;">Game Days</h3>
    <div class="sched-wrap">
      <table class="sched-table">
        <tr><th>Team</th><th>Day</th><th>Kickoff</th><th>Location</th></tr>
        <tr><td class="team">Minis (U6&ndash;U10)</td><td>Select Sundays (festivals)</td><td>TBD</td><td>Home / Away per festival</td></tr>
        <tr><td class="team">U12 Boys &amp; Girls</td><td>Sunday</td><td>TBD</td><td>Home / Away per fixture</td></tr>
        <tr><td class="team">U14 &amp; U16 Boys &amp; Girls</td><td>Saturday</td><td>TBD</td><td>Home / Away per fixture</td></tr>
        <tr><td class="team">U18 Girls</td><td>Wednesday</td><td>TBD</td><td>Home / Away per fixture</td></tr>
        <tr><td class="team">U18 Boys</td><td>Wednesday</td><td>TBD</td><td>Home / Away per fixture</td></tr>
        <tr><td class="team">Senior Men's &amp; Women's</td><td>Saturday</td><td>TBD</td><td>Jim Hamilton Field (Home)</td></tr>
      </table>
    </div>
    <p class="sched-note">Kickoff times vary week to week and are confirmed by coaches ahead of each fixture. U12s occasionally play a festival format of two 30-minute games in place of a single match. Full fixture list, including away matches, runs on the <a href="https://www.rugbyontario.com/fixtures/" target="_blank" rel="noopener" style="color:var(--sky-deep); font-weight:700;">Rugby Ontario schedule &rarr;</a></p>
  </div>
</section>

<section style="background:#fff; border-top:1px solid var(--line); padding-top:60px; padding-bottom:100px;">
  <div class="wrap" style="text-align:center;">
    <span class="eyebrow" style="color:var(--sky-deep); justify-content:center;">Ready To Play?</span>
    <h2 style="font-size:clamp(26px,3.4vw,36px); color:var(--navy); margin-top:14px; margin-bottom:26px;">Registration for the 2026 season is open.</h2>
    <a class="cta-btn" style="display:inline-block; background:var(--navy); color:#fff !important;" href="https://www.playhq.com/ca/rugby-canada/register/c4290e">Register Now &rarr;</a>
  </div>
</section>

{CONTACT_SECTION}
"""

# ---------------------------------------------------------------------------
# ALUMNI.HTML
# ---------------------------------------------------------------------------
alumni_body = f"""
<section class="pagehero">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap pagehero-inner">
    <span class="eyebrow">Since 1967</span>
    <h1>The Alumni Network.</h1>
    <p>Barrie Rugby's roots run through Simcoe County high schools, three generations of playing families, and players who've gone on to represent Canada. This is where old teammates find each other again.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Notable Names</span>
      <h2>A few from the honour roll.</h2>
      <p class="lede">Pulled from the club's own written history &mdash; a small sample of the players who wore the crest before you.</p>
    </div>
    <div class="alumni-grid">
      <div class="alum-card">
        <div class="mono">01</div>
        <div><h3>Jim Corrigal</h3><p>Canadian Sports Hall-of-Famer who played as a schoolboy in the club's earliest years, before its 1967 founding as the Barrie Huronia Rugby Club.</p></div>
      </div>
      <div class="alum-card">
        <div class="mono">02</div>
        <div><h3>Ian Cathery</h3><p>Selected to Canada's National Team in the late 1980s &mdash; part of the Cathery family that shaped the club through the 1970s and '80s.</p></div>
      </div>
      <div class="alum-card">
        <div class="mono">03</div>
        <div><h3>Michael Cathery</h3><p>Went on to captain English Universities before continuing his playing career at Exeter.</p></div>
      </div>
      <div class="alum-card">
        <div class="mono">04</div>
        <div><h3>Bernie LeSage</h3><p>Played extensively across Ontario, Western Canada, and Europe, including an invitational side alongside the Belgian RFU President's Select.</p></div>
      </div>
      <div class="alum-card">
        <div class="mono">05</div>
        <div><h3>Rob Avery</h3><p>The club's longest-serving player, joining in the early 1970s and playing prop for the better part of two decades.</p></div>
      </div>
      <div class="alum-card">
        <div class="mono">06</div>
        <div><h3>Jack LeSage</h3><p>Club co-founder who introduced rugby to Barrie's high schools, planting the seed for the youth pathway the club still runs today.</p></div>
      </div>
    </div>

    <div class="alum-note">
      Are you a Barrie Rugby alum, or do you have a name, photo, or story that belongs on this page? We're building out the full alumni archive &mdash; get in touch at <a href="mailto:info@barrierugbyclub.com" style="color:var(--sky-deep); font-weight:700;">info@barrierugbyclub.com</a> and help us fill in the gaps.
    </div>
  </div>
</section>

<section class="programs" style="border-top:1px solid var(--line);">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Stay Connected</span>
      <h2>Come back for a match.</h2>
      <p class="lede">Alumni are always welcome on Jim Hamilton Field &mdash; for a home game, a tour reunion, or just to see how the youth pathway you helped build has grown.</p>
    </div>
    <div class="card-grid">
      <div class="card"><span class="tag">Reconnect</span><h3>Old Boys &amp; Girls</h3><p>Let us know you played &mdash; we're building a proper alumni contact list for reunions and season updates.</p></div>
      <div class="card"><span class="tag">Give Back</span><h3>Coach or Mentor</h3><p>Alumni are a big part of the club's coaching bench. If you're local and want in, reach out.</p></div>
      <div class="card"><span class="tag">Support</span><h3>Sponsor or Donate</h3><p>Many of our sponsors are alumni-owned businesses &mdash; and the Memorial &amp; Development Fund takes tax-receipted donations through the National Sport Trust Fund. <a href="index.html#donate" style="color:var(--sky-deep); font-weight:700;">Sponsor or donate &rarr;</a></p></div>
    </div>
  </div>
</section>

{CONTACT_SECTION}
"""

# ---------------------------------------------------------------------------
# RESOURCES.HTML
# ---------------------------------------------------------------------------
resources_body = f"""
<section class="pagehero">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap pagehero-inner">
    <span class="eyebrow">Resources</span>
    <h1>Rules, safety &amp; governance.</h1>
    <p>Official Rugby Ontario links, club governance documents, and the World Rugby resources every player, parent, and coach should know.</p>
  </div>
</section>

<section>
  <div class="wrap">

    <div class="res-group-label">Rugby Ontario</div>
    <div class="res-grid">
      <a class="res-link" href="https://www.rugbyontario.com" target="_blank" rel="noopener">
        <div><div class="t">Rugby Ontario &mdash; Home</div><div class="d">Provincial governing body for rugby in Ontario</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="https://www.rugbyontario.com/fixtures/" target="_blank" rel="noopener">
        <div><div class="t">Rugby Ontario Schedule</div><div class="d">Full fixture list across all divisions</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="https://www.rugbyontario.com/governance-policies/#Manuals" target="_blank" rel="noopener">
        <div><div class="t">Rugby Ontario Ops Manual</div><div class="d">Governance policies &amp; operations manual</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="https://www.playhq.com/ca/rugby-canada/register/c4290e" target="_blank" rel="noopener">
        <div><div class="t">Registration (PlayHQ)</div><div class="d">Register for the current season</div></div>
        <span class="arrow">&rarr;</span>
      </a>
    </div>

    <div class="res-group-label">Player Safety</div>
    <div class="res-grid">
      <a class="res-link" href="https://www.world.rugby/the-game/player-welfare" target="_blank" rel="noopener">
        <div><div class="t">Player Welfare</div><div class="d">World Rugby's player safety resources</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="https://www.world.rugby/the-game/laws/home" target="_blank" rel="noopener">
        <div><div class="t">Laws of the Game</div><div class="d">Official World Rugby law book</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="https://www.world.rugby/the-game/beginners-guide/safety" target="_blank" rel="noopener">
        <div><div class="t">Beginner's Guide</div><div class="d">New to rugby? Start here</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="programs.html#matrix">
        <div><div class="t">Age Grade Matrix</div><div class="d">Which age group your player belongs in</div></div>
        <span class="arrow">&rarr;</span>
      </a>
    </div>

    <div class="res-group-label">The Club</div>
    <div class="res-grid">
      <a class="res-link" href="index.html#about">
        <div><div class="t">About Us</div><div class="d">Club history &amp; leadership</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="index.html#contact">
        <div><div class="t">Volunteering</div><div class="d">Get involved off the pitch</div></div>
        <span class="arrow">&rarr;</span>
      </a>
    </div>

  </div>
</section>

{CONTACT_SECTION}
"""

def page(title, active, body):
    return f"""<!DOCTYPE html>
<html lang="en">
{HEAD.format(title=title, css=CSS)}
<body>
{nav(active)}
{body}
{FOOTER}
</body>
</html>"""

out_dir = '/mnt/user-data/outputs'
os.makedirs(out_dir, exist_ok=True)

with open(f'{out_dir}/index.html', 'w') as f:
    f.write(page("Barrie Rugby Club", "home", index_body))

with open(f'{out_dir}/programs.html', 'w') as f:
    f.write(page("Programs | Barrie Rugby Club", "programs", programs_body))

with open(f'{out_dir}/alumni.html', 'w') as f:
    f.write(page("Alumni | Barrie Rugby Club", "alumni", alumni_body))

with open(f'{out_dir}/resources.html', 'w') as f:
    f.write(page("Resources | Barrie Rugby Club", "resources", resources_body))

print("Built index.html, programs.html, alumni.html, resources.html")
for fn in ['index.html','programs.html','alumni.html','resources.html']:
    p = f'{out_dir}/{fn}'
    print(fn, round(os.path.getsize(p)/1024,1), 'KB')
