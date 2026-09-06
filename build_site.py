import os
import sys
import json

_BASE = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = '/home/claude' if os.path.exists('/home/claude/sponsor_b64.py') else _BASE
sys.path.insert(0, ASSET_DIR)
from sponsor_b64 import DONALEIGHS, WESTERN, MITSUBISHI, TODDSMITH, JONES, MINDTOMUSCLE

with open(os.path.join(ASSET_DIR, 'logo_transparent_b64.txt')) as f:
    LOGO = 'data:image/png;base64,' + f.read().strip()


def _load_b64(fname):
    path = os.path.join(ASSET_DIR, fname)
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return ''

# background photos (pagehero) + hero video poster frame
BG_PROGRAMS_B64 = _load_b64('bg_programs_b64.txt')
BG_ALUMNI_B64 = _load_b64('bg_alumni_b64.txt')
BG_RESOURCES_B64 = _load_b64('bg_resources_b64.txt')
BG_HERO_POSTER_B64 = _load_b64('bg_hero_poster_b64.txt')


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
[id]{scroll-margin-top:96px;} /* keep anchor targets clear of the sticky header */
body{font-family:'Public Sans', sans-serif; color:var(--ink); background:var(--paper); -webkit-font-smoothing:antialiased;}
img{max-width:100%;display:block;}
a{color:inherit;text-decoration:none;}
.display{font-family:'Anton', sans-serif; text-transform:uppercase; letter-spacing:0.01em;}
.eyebrow{font-family:'Anton', sans-serif; font-size:12.5px; letter-spacing:0.22em; text-transform:uppercase; display:inline-flex; align-items:center; gap:10px;}
.eyebrow::before{content:""; width:22px;height:2px;background:currentColor;display:inline-block;}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px;}
@media (max-width:640px){.wrap{padding:0 20px;}}

header{position:sticky; top:0; z-index:100; background:rgba(20,38,69,0.96); backdrop-filter:blur(6px); border-bottom:1px solid rgba(255,255,255,0.08);}
nav.wrap{position:relative; display:flex; align-items:center; justify-content:space-between; height:76px; gap:14px;}
.brand{display:flex; align-items:center; gap:12px; min-width:0;}
.brand img{height:46px; width:46px; flex-shrink:0;}
.brand .word{font-family:'Anton', sans-serif; color:#fff; font-size:16px; letter-spacing:0.06em; line-height:1.15;}
.brand .word span{display:block; color:var(--sky); font-size:11px; letter-spacing:0.28em; margin-top:2px;}
.navlinks{display:flex; align-items:center; gap:20px;}
.navlinks a{color:rgba(255,255,255,0.82); font-size:12.5px; font-weight:700; letter-spacing:0.05em; text-transform:uppercase; transition:color .15s ease; white-space:nowrap;}
.navlinks a:hover, .navlinks a.active{color:var(--sky);}
.navlinks a.donate-link{color:var(--gold);}
.navlinks a.donate-link:hover{color:#fff;}
.cta-btn{background:var(--sky); color:var(--navy-deep) !important; font-family:'Anton', sans-serif; letter-spacing:0.05em; font-size:13px; padding:12px 22px; border-radius:3px; text-transform:uppercase; transition:background .15s ease, transform .15s ease; white-space:nowrap; flex-shrink:0;}
.cta-btn:hover{background:#fff; transform:translateY(-1px);}
.nav-toggle{display:none; background:none; border:0; color:#fff; cursor:pointer; padding:6px; width:38px; height:38px; align-items:center; justify-content:center; flex-shrink:0; -webkit-tap-highlight-color:transparent;}
.nav-toggle svg{width:24px; height:24px;}
.nav-toggle .icon-close{display:none;}
.nav-toggle[aria-expanded="true"] .icon-open{display:none;}
.nav-toggle[aria-expanded="true"] .icon-close{display:block;}
@media (max-width:1120px){
  .nav-toggle{display:flex;}
  .navlinks{
    display:none; position:absolute; top:100%; left:0; right:0; z-index:99;
    flex-direction:column; align-items:stretch; gap:0;
    background:var(--navy-deep); border-top:1px solid rgba(255,255,255,0.1);
    box-shadow:0 16px 30px rgba(12,26,48,0.4); max-height:calc(100vh - 76px); overflow-y:auto;
  }
  .navlinks.open{display:flex;}
  .navlinks a{padding:16px 32px; border-bottom:1px solid rgba(255,255,255,0.08); width:100%;}
}
@media (max-width:480px){
  nav.wrap{height:64px;}
  .brand img{height:36px; width:36px;}
  .brand .word{font-size:12.5px;}
  .brand .word span{font-size:8.5px; letter-spacing:0.22em;}
  .cta-btn{padding:9px 14px; font-size:11px;}
  .navlinks{top:64px; max-height:calc(100vh - 64px);}
}

.pagehero{
  position:relative; overflow:hidden; padding:88px 0 68px;
  background-color:var(--navy-deep);
  background-image: linear-gradient(180deg, rgba(12,26,48,0.58) 0%, rgba(12,26,48,0.38) 45%, rgba(12,26,48,0.84) 100%), var(--section-bg, linear-gradient(180deg, var(--navy) 0%, var(--navy-deep) 100%));
  background-size: cover, cover;
  background-position: center, center;
  background-repeat: no-repeat, no-repeat;
}
@media (max-width:640px){ .pagehero{padding:64px 0 52px;} }
.pagehero .sash{position:absolute; inset:0; z-index:0; pointer-events:none;}
.pagehero .sash span{position:absolute; background:linear-gradient(90deg, var(--sky) 0%, var(--sky-deep) 100%); opacity:0.12; width:180%; height:120px; transform:rotate(-9deg); left:-40%;}
.pagehero .sash span:nth-child(2){top:220px; opacity:0.07; left:-60%;}
.pagehero-inner{position:relative; z-index:1;}
.pagehero .eyebrow{color:var(--sky); text-shadow:0 1px 6px rgba(0,0,0,0.45);}
.pagehero h1{color:#fff; font-size:clamp(34px,5.4vw,58px); line-height:1; margin:16px 0 16px; text-shadow:0 2px 18px rgba(0,0,0,0.5), 0 1px 4px rgba(0,0,0,0.35);}
.pagehero p{color:rgba(255,255,255,0.85); font-size:16.5px; line-height:1.6; max-width:600px; text-shadow:0 1px 10px rgba(0,0,0,0.4);}

.hero{position:relative; overflow:hidden; background:var(--navy-deep); padding:110px 0 90px;}
@media (max-width:800px){ .hero{padding:80px 0 60px;} }
.hero-video{position:absolute; inset:0; z-index:0; width:100%; height:100%; object-fit:cover;}
@media (prefers-reduced-motion: reduce){ .hero-video{display:none;} }
.hero-scrim{
  position:absolute; inset:0; z-index:1;
  background: linear-gradient(100deg, rgba(12,26,48,0.05) 0%, rgba(12,26,48,0.12) 30%, rgba(12,26,48,0.28) 60%, rgba(12,26,48,0.34) 100%);
}
@media (max-width:800px){
  .hero-scrim{ background: linear-gradient(180deg, rgba(12,26,48,0.1) 0%, rgba(12,26,48,0.22) 55%, rgba(12,26,48,0.4) 100%); }
}
.hero .sash{position:absolute; inset:0; z-index:2; pointer-events:none;}
.hero .sash span{position:absolute; background:linear-gradient(90deg, var(--sky) 0%, var(--sky-deep) 100%); opacity:0.14; width:180%; height:130px; transform:rotate(-9deg);}
.hero .sash span:nth-child(1){ top:-20px; left:-40%; }
.hero .sash span:nth-child(2){ top:280px; left:-60%; opacity:0.08; height:90px;}
.hero-inner{position:relative; z-index:3; display:grid; grid-template-columns:auto 1fr; gap:56px; align-items:center;}
@media (max-width:800px){ .hero-inner{grid-template-columns:1fr; text-align:center; justify-items:center;} }
.hero-crest img{width:190px; height:190px; filter:drop-shadow(0 4px 18px rgba(0,0,0,0.4));}
@media (max-width:800px){ .hero-crest img{width:130px;height:130px;} }
.hero-copy .eyebrow{color:var(--sky); text-shadow:0 2px 10px rgba(0,0,0,0.75), 0 1px 2px rgba(0,0,0,0.6);}
.hero-copy h1{color:#fff; font-size:clamp(38px, 6vw, 68px); line-height:0.98; margin:18px 0 22px; text-shadow:0 4px 30px rgba(0,0,0,0.75), 0 2px 8px rgba(0,0,0,0.65), 0 1px 2px rgba(0,0,0,0.5);}
.hero-copy h1 em{color:var(--sky); font-style:normal;}
.hero-copy p{color:#fff; font-size:17px; line-height:1.6; max-width:520px; margin-bottom:34px; text-shadow:0 2px 16px rgba(0,0,0,0.75), 0 1px 3px rgba(0,0,0,0.6);}
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
.badge.title{background:var(--navy);}
.badge.direct{background:var(--sky-deep);}
.badge.open{background:transparent; color:var(--navy); border:1.5px dashed var(--line);}
.tier-label .line{flex:1; height:1px; background:var(--line);}
.sponsor-grid{display:grid; grid-template-columns:repeat(3,1fr); gap:18px;}
@media (max-width:760px){ .sponsor-grid{grid-template-columns:1fr 1fr;} }
@media (max-width:480px){ .sponsor-grid{grid-template-columns:1fr;} }
.sponsor-grid.wide{grid-template-columns:repeat(4,1fr);}
@media (max-width:900px){ .sponsor-grid.wide{grid-template-columns:1fr 1fr;} }
@media (max-width:480px){ .sponsor-grid.wide{grid-template-columns:1fr;} }
.sponsor-card{background:#fff; border:1px solid var(--line); border-radius:4px; padding:26px 22px; display:flex; flex-direction:column; gap:6px; justify-content:center; min-height:96px;}
.sponsor-card.logo{align-items:center; justify-content:center; padding:22px;}
.sponsor-card.logo img{max-height:56px; max-width:100%; width:auto; object-fit:contain;}
.sponsor-card .sname{font-family:'Anton', sans-serif; font-size:17px; color:var(--navy); letter-spacing:0.01em;}
.sponsor-card .sdesc{font-size:13px; color:#6b7284;}
.sponsor-card.cta{border-style:dashed; align-items:flex-start; justify-content:center;}
.sponsor-card.cta a{font-size:13px; font-weight:700; color:var(--sky-deep); text-decoration:underline;}

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

/* donate */
.donate{background:var(--navy); color:#fff; border-top:4px solid var(--gold); position:relative; overflow:hidden;}
.donate .sash{position:absolute; inset:0; pointer-events:none;}
.donate .sash span{position:absolute; width:180%; height:110px; left:-45%; background:linear-gradient(90deg, var(--gold), var(--sky)); opacity:0.07; transform:rotate(-9deg);}
.donate .sash span:nth-child(1){top:-10px;}
.donate .sash span:nth-child(2){bottom:10px; opacity:0.05;}
.donate-inner{position:relative; z-index:1;}
.donate .sec-head h2{color:#fff;}
.donate .sec-head .eyebrow{color:var(--gold);}
.donate .sec-head p.lede{color:rgba(255,255,255,0.7);}
.donate-grid{display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin:36px 0 40px;}
@media (max-width:860px){ .donate-grid{grid-template-columns:1fr 1fr;} }
@media (max-width:560px){ .donate-grid{grid-template-columns:1fr;} }
.donate-card{background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.14); border-radius:4px; padding:22px 20px;}
.donate-card .n{font-family:'Anton', sans-serif; font-size:12px; color:var(--gold); letter-spacing:0.08em; text-transform:uppercase;}
.donate-card p{font-size:13.5px; line-height:1.6; color:rgba(255,255,255,0.78); margin-top:8px;}
.donate-actions{display:flex; align-items:center; gap:22px; flex-wrap:wrap; padding-top:28px; border-top:1px solid rgba(255,255,255,0.14);}
.donate-btn{background:var(--gold); color:var(--navy-deep) !important; font-family:'Anton', sans-serif; letter-spacing:0.05em; font-size:13px; padding:15px 28px; border-radius:3px; text-transform:uppercase; transition:background .15s ease, transform .15s ease; white-space:nowrap;}
.donate-btn:hover{background:#fff; transform:translateY(-1px);}
.donate-alt{font-size:13.5px; color:rgba(255,255,255,0.75); line-height:1.6; max-width:420px;}
.donate-alt a{color:var(--sky); font-weight:700; text-decoration:underline;}
.donate-note{font-size:12.5px; color:rgba(255,255,255,0.5); margin-top:20px; line-height:1.6; max-width:640px;}

/* instagram banner */
.ig-banner{background:linear-gradient(135deg, var(--navy) 0%, var(--navy-deep) 100%); position:relative; overflow:hidden; padding:96px 0;}
.ig-banner .sash{position:absolute; inset:0; pointer-events:none;}
.ig-banner .sash span{position:absolute; width:180%; height:130px; left:-40%; background:linear-gradient(90deg, var(--sky), var(--gold)); opacity:0.09; transform:rotate(-9deg);}
.ig-banner .sash span:nth-child(1){top:-30px;}
.ig-banner .sash span:nth-child(2){bottom:-10px; opacity:0.05;}
.ig-banner-inner{position:relative; z-index:1; display:grid; grid-template-columns:1.15fr 0.85fr; gap:60px; align-items:center;}
@media (max-width:860px){ .ig-banner-inner{grid-template-columns:1fr; text-align:center;} }
.ig-banner .eyebrow{color:var(--gold);}
.ig-banner h2{color:#fff; font-size:clamp(30px,4vw,44px); margin:16px 0 18px; line-height:1.05;}
.ig-banner p.lede{color:rgba(255,255,255,0.72); font-size:16.5px; line-height:1.6; max-width:440px; margin-bottom:30px;}
@media (max-width:860px){ .ig-banner p.lede{margin-left:auto;margin-right:auto;} }
.ig-banner .go{display:inline-flex; align-items:center; gap:10px; background:var(--gold); color:var(--navy-deep) !important; font-family:'Anton', sans-serif; font-size:13px; letter-spacing:0.05em; text-transform:uppercase; padding:15px 30px; border-radius:3px; transition:background .15s ease, transform .15s ease;}
.ig-banner .go:hover{background:#fff; transform:translateY(-1px);}
.ig-badge-wrap{display:flex; justify-content:center;}
.ig-badge{width:230px; height:230px; border-radius:50%; background:radial-gradient(circle at 32% 28%, rgba(124,197,234,0.28), rgba(12,26,48,0) 68%); border:1.5px dashed rgba(255,255,255,0.28); display:flex; align-items:center; justify-content:center; position:relative;}
.ig-badge::before{content:""; position:absolute; inset:16px; border-radius:50%; border:1px solid rgba(255,255,255,0.14);}
.ig-badge .glyph{position:relative; z-index:1; display:flex; flex-direction:column; align-items:center; gap:10px;}
.ig-badge .glyph svg{width:52px; height:52px; color:#fff;}
.ig-badge .glyph span{font-family:'Anton', sans-serif; font-size:13px; letter-spacing:0.08em; color:var(--sky); text-transform:none;}

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
.matrix-callout .back{position:relative; z-index:1; display:inline-flex; align-items:center; gap:6px; margin-top:14px; font-size:12px; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--sky); opacity:0.8; transition:opacity .15s ease, color .15s ease;}
.matrix-callout .back:hover{opacity:1; color:#fff;}
.matrix-callout:target{box-shadow:0 0 0 3px var(--sky);} /* confirm arrival when jumped to from Resources */

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

/* chat widget */
.bchat-fab{position:fixed; right:22px; bottom:22px; z-index:200; width:58px; height:58px; border-radius:50%; background:var(--navy); border:2px solid var(--sky); color:var(--sky); display:flex; align-items:center; justify-content:center; cursor:pointer; box-shadow:0 6px 18px rgba(12,26,48,0.35); transition:transform .15s ease, background .15s ease;}
.bchat-fab:hover{transform:translateY(-2px); background:var(--navy-deep);}
.bchat-panel{position:fixed; right:22px; bottom:92px; z-index:201; width:370px; max-width:calc(100vw - 24px); height:540px; max-height:calc(100vh - 120px); background:#fff; border:1px solid var(--line); border-radius:8px; box-shadow:0 18px 48px rgba(12,26,48,0.28); display:none; flex-direction:column; overflow:hidden;}
.bchat-panel.open{display:flex;}
@media (max-width:480px){ .bchat-panel{right:12px; left:12px; width:auto;} }
.bchat-head{background:var(--navy); color:#fff; padding:16px 18px; display:flex; align-items:center; gap:12px;}
.bchat-head img{width:34px; height:34px;}
.bchat-head .t{font-family:'Anton', sans-serif; font-size:15px; letter-spacing:0.05em; text-transform:uppercase;}
.bchat-head .s{font-size:11px; color:rgba(255,255,255,0.6); margin-top:2px; line-height:1.4;}
.bchat-close{margin-left:auto; background:none; border:0; color:rgba(255,255,255,0.7); font-size:22px; line-height:1; cursor:pointer; padding:4px;}
.bchat-close:hover{color:#fff;}
.bchat-msgs{flex:1; overflow-y:auto; padding:16px; display:flex; flex-direction:column; gap:10px; background:var(--paper);}
.bchat-msg{max-width:85%; padding:10px 14px; border-radius:12px; font-size:14px; line-height:1.55; white-space:pre-wrap; word-wrap:break-word;}
.bchat-msg.bot{background:#fff; border:1px solid var(--line); color:var(--ink); border-bottom-left-radius:3px; align-self:flex-start;}
.bchat-msg.user{background:var(--sky); color:var(--navy-deep); border-bottom-right-radius:3px; align-self:flex-end; font-weight:500;}
.bchat-msg.bot a{color:var(--sky-deep); font-weight:700; text-decoration:underline;}
.bchat-typing{align-self:flex-start; background:#fff; border:1px solid var(--line); border-radius:12px; border-bottom-left-radius:3px; padding:12px 16px; display:flex; gap:5px;}
.bchat-typing span{width:7px; height:7px; border-radius:50%; background:var(--sky-deep); opacity:0.4; animation:bchatBlink 1.2s infinite;}
.bchat-typing span:nth-child(2){animation-delay:.2s;}
.bchat-typing span:nth-child(3){animation-delay:.4s;}
@keyframes bchatBlink{0%,80%,100%{opacity:0.25;}40%{opacity:1;}}
.bchat-chips{display:flex; gap:8px; flex-wrap:wrap; padding:0 16px 10px; background:var(--paper);}
.bchat-chips button{background:#fff; border:1px solid var(--line); border-radius:20px; padding:7px 13px; font-size:12.5px; color:var(--navy); font-weight:600; cursor:pointer; transition:border-color .15s ease, color .15s ease; font-family:'Public Sans', sans-serif;}
.bchat-chips button:hover{border-color:var(--sky-deep); color:var(--sky-deep);}
.bchat-inputrow{display:flex; gap:10px; padding:12px 14px; border-top:1px solid var(--line); background:#fff;}
.bchat-inputrow input{flex:1; border:1px solid var(--line); border-radius:6px; padding:11px 13px; font-family:'Public Sans', sans-serif; font-size:14px; color:var(--ink); outline:none;}
.bchat-inputrow input:focus{border-color:var(--sky-deep);}
.bchat-send{background:var(--navy); color:#fff; border:0; border-radius:6px; padding:0 16px; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:background .15s ease;}
.bchat-send:hover{background:var(--sky-deep);}
.bchat-send:disabled{opacity:0.5; cursor:default;}

/* announcement bar */
.announce-bar{background:var(--gold); color:var(--navy-deep); position:relative; z-index:150;}
.announce-bar .wrap{display:flex; align-items:center; justify-content:center; gap:18px; padding:11px 46px; flex-wrap:wrap; text-align:center; position:relative;}
.announce-bar .msg{font-size:13.5px; font-weight:700; letter-spacing:0.01em;}
.announce-bar .cta{font-family:'Anton', sans-serif; font-size:12px; letter-spacing:0.05em; text-transform:uppercase; text-decoration:underline; white-space:nowrap; color:var(--navy-deep) !important;}
.announce-bar .close{position:absolute; right:12px; top:50%; transform:translateY(-50%); background:none; border:0; cursor:pointer; color:var(--navy-deep); font-size:20px; line-height:1; padding:4px 6px; opacity:0.65;}
.announce-bar .close:hover{opacity:1;}
@media (max-width:640px){ .announce-bar .wrap{padding:10px 40px 10px 16px; gap:10px;} .announce-bar .msg{font-size:12.5px;} }

/* ---- RUGBYCAN app band ---- */
.hero-actions .btn-app{display:inline-flex; align-items:center; gap:9px; background:rgba(255,255,255,0.10); color:#fff !important; font-family:'Anton', sans-serif; letter-spacing:0.05em; font-size:13px; padding:12px 20px; border-radius:3px; text-transform:uppercase; transition:background .15s ease, transform .15s ease;}
.hero-actions .btn-app:hover{background:rgba(255,255,255,0.2); transform:translateY(-1px);}
.hero-actions .btn-app svg{width:15px; height:15px; flex-shrink:0;}

.appband{background:var(--navy); position:relative; overflow:hidden; padding:96px 0; border-top:1px solid var(--line);}
.appband .sash{position:absolute; inset:0; pointer-events:none;}
.appband .sash span{position:absolute; width:180%; height:150px; left:-40%; background:linear-gradient(90deg, var(--sky), var(--sky-deep)); opacity:0.10; transform:rotate(-9deg);}
.appband .sash span:nth-child(1){top:-40px;}
.appband .sash span:nth-child(2){bottom:-30px; opacity:0.05;}
.appband-inner{position:relative; z-index:1; display:grid; grid-template-columns:1.1fr 0.9fr; gap:64px; align-items:center;}
@media (max-width:900px){ .appband-inner{grid-template-columns:1fr; gap:52px;} }
.appband .eyebrow{color:var(--sky);}
.appband h2{font-family:'Anton', sans-serif; text-transform:uppercase; color:#fff; font-size:clamp(30px,4vw,46px); line-height:1.03; margin:16px 0 18px;}
.appband h2 em{font-style:normal; color:var(--sky);}
.appband p.lede{color:rgba(255,255,255,0.74); font-size:16.5px; line-height:1.62; max-width:470px;}
.appband .fine{margin-top:26px; font-size:12.5px; color:rgba(255,255,255,0.5); letter-spacing:0.04em;}
.appband .fine a{color:var(--sky); text-decoration:underline;}

.store-row{display:flex; gap:14px; flex-wrap:wrap; margin-top:30px;}
.store-btn{display:inline-flex; align-items:center; gap:12px; background:#fff; color:var(--navy-deep) !important; border-radius:5px; padding:11px 20px 11px 17px; transition:transform .15s ease, box-shadow .15s ease;}
.store-btn:hover{transform:translateY(-2px); box-shadow:0 10px 22px rgba(0,0,0,0.28);}
.store-btn svg{width:24px; height:24px; flex-shrink:0;}
.store-btn .lbl{display:flex; flex-direction:column; line-height:1.15;}
.store-btn .lbl small{font-size:9.5px; letter-spacing:0.14em; text-transform:uppercase; color:#5a6274;}
.store-btn .lbl strong{font-family:'Anton', sans-serif; font-size:16px; letter-spacing:0.02em; font-weight:400;}
.store-btn:focus-visible, .hero-actions .btn-app:focus-visible, .appband a:focus-visible{outline:2px solid var(--sky); outline-offset:3px;}

.phone-wrap{display:flex; justify-content:center;}
.phone{width:250px; border-radius:30px; background:linear-gradient(160deg,#1d3560,#0c1a30); border:1px solid rgba(255,255,255,0.16); padding:12px; box-shadow:0 28px 60px rgba(0,0,0,0.45); position:relative;}
.phone::before{content:""; position:absolute; top:20px; left:50%; transform:translateX(-50%); width:64px; height:5px; border-radius:3px; background:rgba(255,255,255,0.18);}
.phone-screen{background:var(--navy-deep); border-radius:22px; padding:38px 16px 18px; border:1px solid rgba(255,255,255,0.08);}
.phone-mark{text-align:center; padding-bottom:16px; border-bottom:1px solid rgba(255,255,255,0.1);}
.phone-mark b{display:block; font-family:'Anton', sans-serif; font-size:21px; letter-spacing:0.09em; color:#fff; font-weight:400;}
.phone-mark span{display:block; font-size:9px; letter-spacing:0.2em; text-transform:uppercase; color:var(--sky); margin-top:5px;}
.phone-row{display:flex; align-items:center; gap:11px; padding:13px 4px; border-bottom:1px solid rgba(255,255,255,0.06);}
.phone-row:last-child{border-bottom:0;}
.phone-row .pic{width:30px; height:30px; border-radius:7px; background:rgba(124,197,234,0.14); display:flex; align-items:center; justify-content:center; flex-shrink:0;}
.phone-row .pic svg{width:15px; height:15px; color:var(--sky);}
.phone-row .ptxt{font-size:12.5px; font-weight:600; color:rgba(255,255,255,0.88); flex:1;}
.phone-row .chev{color:rgba(255,255,255,0.3); font-size:13px;}
.phone-row .live{display:inline-flex; align-items:center; gap:5px; font-family:'Anton', sans-serif; font-size:9.5px; letter-spacing:0.12em; color:#fff; background:var(--red); padding:3px 7px; border-radius:3px;}
.phone-row .live i{width:5px; height:5px; border-radius:50%; background:#fff; display:inline-block; animation:livePulse 1.6s ease-in-out infinite;}
@keyframes livePulse{0%,100%{opacity:1;}50%{opacity:0.25;}}
@media (prefers-reduced-motion:reduce){ .phone-row .live i{animation:none;} }
@media (max-width:900px){ .phone{width:225px;} }

/* ---------------------------------------------------------------------------
   registration fees page (fees.html)
   Data colours reuse the existing brand tokens: Rugby Canada = --red,
   Rugby Ontario = --gold, Barrie Rugby Club = --sky-deep. Ink on each fill is
   picked for contrast (white on red, navy on gold and sky).
   --------------------------------------------------------------------------- */
.fee-panel{background:#fff; border:1px solid var(--line); border-radius:4px; padding:34px 32px 36px;}
@media (max-width:640px){ .fee-panel{padding:26px 20px 28px;} }
.fee-panel .lbl{font-family:'Anton', sans-serif; font-size:12px; letter-spacing:0.14em; text-transform:uppercase; color:var(--sky-deep);}
.fee-chips{display:flex; flex-wrap:wrap; gap:8px; margin-top:16px;}
.fee-chip{font-family:'Public Sans', sans-serif; font-size:13px; font-weight:700; line-height:1; cursor:pointer; padding:10px 15px; border-radius:20px; border:1px solid var(--line); background:var(--paper); color:var(--navy); transition:background .15s ease, color .15s ease, border-color .15s ease;}
.fee-chip:hover{border-color:var(--sky-deep); color:var(--sky-deep);}
.fee-chip[aria-pressed="true"]{background:var(--navy); border-color:var(--navy); color:#fff;}
.fee-chip:focus-visible{outline:3px solid var(--sky-deep); outline-offset:2px;}
.fee-readout{margin-top:28px; padding-top:26px; border-top:1px solid var(--line);}
.fee-readout .top{display:flex; flex-wrap:wrap; align-items:flex-end; justify-content:space-between; gap:6px 22px; margin-bottom:14px;}
.fee-readout .who{font-family:'Anton', sans-serif; font-size:clamp(22px,3.4vw,30px); text-transform:uppercase; color:var(--navy); line-height:1.05;}
.fee-readout .who small{display:block; font-family:'Public Sans', sans-serif; font-size:12px; font-weight:600; letter-spacing:0.1em; text-transform:uppercase; color:#6b7284; margin-top:8px;}
.fee-readout .amt{font-family:'Anton', sans-serif; font-size:clamp(30px,5.2vw,46px); line-height:0.95; color:var(--sky-deep);}
.fee-bar{display:flex; gap:2px; width:100%; height:20px; border-radius:3px; overflow:hidden;}
.fee-bar.big{height:58px; border-radius:4px;}
.fee-bar .s{display:flex; align-items:center; justify-content:center; overflow:hidden; width:var(--w); transition:width .5s cubic-bezier(.22,.7,.25,1);}
.fee-bar .s.rc{background:var(--red); color:#fff;}
.fee-bar .s.ro{background:var(--gold); color:var(--navy-deep);}
.fee-bar .s.club{background:var(--sky-deep); color:var(--navy-deep);}
.fee-bar .v{font-size:13.5px; font-weight:700; white-space:nowrap; padding:0 8px;}
.fee-bar .v.off{opacity:0;}
@media (max-width:640px){ .fee-bar.big .v{display:none;} }
@media (prefers-reduced-motion: reduce){ .fee-bar .s{transition:none;} }
.fee-legend{list-style:none; display:grid; grid-template-columns:repeat(3,1fr); gap:1px; background:var(--line); border:1px solid var(--line); margin-top:20px;}
@media (max-width:640px){ .fee-legend{grid-template-columns:1fr;} }
.fee-legend li{background:#fff; padding:16px 18px;}
.fee-legend .k{display:flex; align-items:center; gap:9px; font-family:'Anton', sans-serif; font-size:11.5px; letter-spacing:0.12em; text-transform:uppercase; color:#6b7284;}
.fee-legend .k::before{content:""; width:11px; height:11px; border-radius:2px; background:var(--c); flex-shrink:0;}
.fee-legend li:nth-child(1){--c:var(--red);}
.fee-legend li:nth-child(2){--c:var(--gold);}
.fee-legend li:nth-child(3){--c:var(--sky-deep);}
.fee-legend .n{display:block; font-family:'Anton', sans-serif; font-size:24px; color:var(--navy); margin-top:7px;}
.fee-legend .s{display:block; font-size:12.5px; color:#6b7284; margin-top:3px;}

.card.org-rc::before{background:var(--red);}
.card.org-ro::before{background:var(--gold);}
.card .amt{font-family:'Anton', sans-serif; font-size:22px; color:var(--navy); margin:12px 0 2px;}
.card .amt-l{font-size:11.5px; letter-spacing:0.1em; text-transform:uppercase; color:#6b7284; margin-bottom:12px;}

.fee-key{display:flex; flex-wrap:wrap; gap:10px 24px; font-size:13px; font-weight:700; color:#5a6274; padding-bottom:18px; border-bottom:1px solid var(--line);}
.fee-key span{display:flex; align-items:center; gap:9px;}
.fee-key span::before{content:""; width:11px; height:11px; border-radius:2px; background:var(--c); flex-shrink:0;}
.fee-key .r{--c:var(--red);} .fee-key .o{--c:var(--gold);} .fee-key .c{--c:var(--sky-deep);}
.fee-tablewrap{overflow-x:auto;}
table.fee-table{width:100%; border-collapse:collapse;}
table.fee-table th, table.fee-table td{text-align:left; vertical-align:top; padding:16px 0;}
table.fee-table tr.grp th{padding:28px 0 9px; font-family:'Anton', sans-serif; font-size:12px; letter-spacing:0.14em; text-transform:uppercase; color:var(--sky-deep); border-bottom:1px solid var(--line);}
table.fee-table tr.grp:first-child th{padding-top:8px;}
.fee-c1{width:200px; padding-right:26px !important;}
.fee-c1 .l{display:block; font-weight:700; color:var(--navy); font-size:15px;}
.fee-c1 .s{display:block; font-weight:400; font-size:12.5px; color:#6b7284; margin-top:2px;}
.fee-c3{width:140px; padding-left:26px !important; text-align:right;}
.fee-c3 .t{display:block; font-family:'Anton', sans-serif; font-size:22px; color:var(--navy); line-height:1.05;}
.fee-c3 .p{display:block; font-size:12px; color:#6b7284; margin-top:3px;}
table.fee-table tbody tr:not(.grp)+tr:not(.grp) .fee-c1,
table.fee-table tbody tr:not(.grp)+tr:not(.grp) .fee-c2,
table.fee-table tbody tr:not(.grp)+tr:not(.grp) .fee-c3{border-top:1px solid var(--line);}
.fee-vals{display:flex; flex-wrap:wrap; gap:6px 20px; margin-top:12px; font-size:13px; font-weight:700; color:#5a6274;}
.fee-vals b{display:flex; align-items:center; gap:8px; font-weight:700;}
.fee-vals b::before{content:""; width:9px; height:9px; border-radius:2px; background:var(--c); flex-shrink:0;}
.fee-vals .r{--c:var(--red);} .fee-vals .o{--c:var(--gold);} .fee-vals .c{--c:var(--sky-deep);}
.fee-vals .nm{display:none; font-weight:400; color:#6b7284; margin-right:5px;}
@media (max-width:760px){
  table.fee-table, table.fee-table tbody, table.fee-table tr, table.fee-table th, table.fee-table td{display:block; width:auto;}
  table.fee-table th, table.fee-table td{padding:0 !important; border:0 !important;}
  table.fee-table tr:not(.grp){display:flex; flex-direction:column; gap:11px; padding:20px 0;}
  table.fee-table tr:not(.grp)+tr:not(.grp){border-top:1px solid var(--line) !important;}
  table.fee-table tr.grp th{padding:26px 0 9px !important; border-bottom:1px solid var(--line) !important;}
  .fee-c1{order:1;} .fee-c3{order:2;} .fee-c2{order:3;}
  .fee-c3{text-align:left; display:flex; align-items:baseline; gap:12px;}
  .fee-c3 .t{font-size:19px;} .fee-c3 .p{margin-top:0;}
  .fee-vals b{width:100%;}
  .fee-vals .nm{display:inline;}
}
details.fee-plain{margin-top:30px; border-top:1px solid var(--line); padding-top:20px;}
details.fee-plain summary{cursor:pointer; font-family:'Anton', sans-serif; font-size:12.5px; letter-spacing:0.1em; text-transform:uppercase; color:var(--sky-deep);}
details.fee-plain summary:hover{color:var(--navy);}
details.fee-plain .sched-wrap{margin-top:18px;}
table.sched-table td.num, table.sched-table th.num{text-align:right;}

.fee-kit{display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-top:26px;}
@media (max-width:700px){ .fee-kit{grid-template-columns:1fr;} }
.fee-kit .card{display:flex; flex-direction:column;}
.fee-kit .band{font-family:'Anton', sans-serif; font-size:24px; text-transform:uppercase; color:var(--navy); line-height:1;}
.fee-kit .band em{font-style:normal; color:var(--sky-deep);}
.fee-kit ul{margin-top:16px; padding-left:18px;}
.fee-kit li{font-size:14.5px; line-height:1.8; color:#454d64;}
.fee-kit .note{margin-top:auto; padding-top:18px; font-size:12.5px; color:#6b7284;}

.fee-change{display:grid; grid-template-columns:repeat(3,1fr); gap:1px; background:var(--line); border:1px solid var(--line); margin-top:26px;}
@media (max-width:760px){ .fee-change{grid-template-columns:1fr;} }
.fee-change > div{background:#fff; padding:26px 24px 28px;}
.fee-change .t{font-family:'Anton', sans-serif; font-size:11.5px; letter-spacing:0.14em; text-transform:uppercase; color:var(--sky-deep);}
.fee-change .n{font-family:'Anton', sans-serif; font-size:clamp(30px,4.4vw,40px); line-height:1; color:var(--navy); margin-top:12px;}
.fee-change .l{font-size:14px; line-height:1.65; color:#5a6274; margin-top:10px;}
.fee-note{background:#fff; border:1px solid var(--line); border-left:4px solid var(--sky); padding:24px 26px; border-radius:2px; margin-top:26px;}
.fee-note h3{font-family:'Anton', sans-serif; font-size:12.5px; letter-spacing:0.14em; text-transform:uppercase; color:#6b7284;}
.fee-note ul{margin-top:14px; padding:0; list-style:none; display:grid; gap:10px 32px; grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));}
.fee-note li{display:flex; gap:10px; font-size:14.5px; line-height:1.6; color:#454d64;}
.fee-note li::before{content:""; flex-shrink:0; width:6px; height:6px; margin-top:9px; border-radius:50%; background:var(--sky-deep);}

.fee-close{background:var(--navy); color:#fff; position:relative; overflow:hidden; border-top:4px solid var(--sky-deep);}
.fee-close .sash{position:absolute; inset:0; pointer-events:none;}
.fee-close .sash span{position:absolute; width:180%; height:110px; left:-45%; background:linear-gradient(90deg, var(--sky), var(--sky-deep)); opacity:0.08; transform:rotate(-9deg);}
.fee-close .sash span:nth-child(1){top:-10px;}
.fee-close .sash span:nth-child(2){bottom:10px; opacity:0.05;}
.fee-close-inner{position:relative; z-index:1;}
.fee-close .sec-head h2{color:#fff;}
.fee-close .sec-head .eyebrow{color:var(--sky);}
.fee-close .sec-head p.lede{color:rgba(255,255,255,0.72);}
.fee-close .prose p{font-size:16px; line-height:1.75; color:rgba(255,255,255,0.8); max-width:70ch;}
.fee-close .prose p + p{margin-top:16px;}
.fee-close .prose strong{color:#fff;}
.fee-close .donate-card .n{color:var(--sky);}
"""

HEAD = """<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Barrie Rugby Club">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://www.barrierugby.com/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#142645">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Public+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{css}</style>
{extra}{jsonld}
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
    <div class="navlinks" id="navLinks">
      <a href="index.html#about"{cls('about')}>About</a>
      <a href="programs.html"{cls('programs')}>Programs</a>
      <a href="alumni.html"{cls('alumni')}>Alumni</a>
      <a href="index.html#sponsors"{cls('sponsors')}>Sponsors</a>
      <a href="index.html#shop"{cls('shop')}>Shop</a>
      <a href="resources.html"{cls('resources')}>Resources</a>
      <a href="index.html#app"{cls('app')}>Get The App</a>
      <a href="index.html#contact"{cls('contact')}>Contact</a>
      <a class="donate-link" href="index.html#donate"{cls('donate')}>Donate</a>
    </div>
    <a class="cta-btn" href="https://www.playhq.com/ca/rugby-canada/register/c4290e">Register</a>
    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="navLinks" aria-label="Toggle menu">
      <svg class="icon-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/></svg>
    </button>
  </nav>
</header>
<script>
(function(){{
  var t=document.getElementById('navToggle'), l=document.getElementById('navLinks');
  if(!t||!l) return;
  function close(){{ l.classList.remove('open'); t.setAttribute('aria-expanded','false'); }}
  function toggle(){{
    var open=l.classList.toggle('open');
    t.setAttribute('aria-expanded', open?'true':'false');
  }}
  t.addEventListener('click', toggle);
  l.addEventListener('click', function(e){{ if(e.target.tagName==='A'){{ close(); }} }});
  document.addEventListener('click', function(e){{
    if(l.classList.contains('open') && !l.contains(e.target) && !t.contains(e.target)){{ close(); }}
  }});
  document.addEventListener('keydown', function(e){{ if(e.key==='Escape'){{ close(); }} }});
}})();
</script>"""

FOOTER = f"""<footer>
  <div class="wrap foot-inner">
    <div class="foot-brand">
      <img src="{LOGO}" alt="Barrie Rugby crest">
      <span>&copy; 2026 Barrie Rugby Club. All rights reserved.</span>
    </div>
    <div class="foot-links">
      <a href="index.html#about">About</a>
      <a href="programs.html">Programs</a>
      <a href="fees.html">Fees</a>
      <a href="alumni.html">Alumni</a>
      <a href="index.html#sponsors">Sponsors</a>
      <a href="index.html#shop">Shop</a>
      <a href="resources.html">Resources</a>
      <a href="index.html#app">Get The App</a>
      <a href="index.html#contact">Contact</a>
      <a href="index.html#donate">Donate</a>
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

CHAT_WIDGET = """
<button class="bchat-fab" id="bchatFab" aria-label="Ask the club a question">
  <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
</button>
<div class="bchat-panel" id="bchatPanel" role="dialog" aria-label="Barrie Rugby Club chat assistant">
  <div class="bchat-head">
    <img id="bchatCrest" src="" alt="">
    <div>
      <div class="t">Ask The Club</div>
      <div class="s">AI assistant &mdash; answers can be wrong. Email us for anything official.</div>
    </div>
    <button class="bchat-close" id="bchatClose" aria-label="Close chat">&times;</button>
  </div>
  <div class="bchat-msgs" id="bchatMsgs"></div>
  <div class="bchat-chips" id="bchatChips">
    <button data-q="When are practices?">When are practices?</button>
    <button data-q="How do I register?">How do I register?</button>
    <button data-q="Where does my registration fee actually go?">Where do my fees go?</button>
    <button data-q="How can I donate to the club?">How can I donate?</button>
  </div>
  <div class="bchat-inputrow">
    <input id="bchatInput" type="text" maxlength="500" placeholder="Ask about programs, schedules&hellip;" autocomplete="off">
    <button class="bchat-send" id="bchatSend" aria-label="Send">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4 20-7z"/></svg>
    </button>
  </div>
</div>
<script>
(function(){
  var fab=document.getElementById('bchatFab'), panel=document.getElementById('bchatPanel'),
      msgs=document.getElementById('bchatMsgs'), input=document.getElementById('bchatInput'),
      sendBtn=document.getElementById('bchatSend'), chips=document.getElementById('bchatChips'),
      history=[], busy=false, greeted=false;

  var brandImg=document.querySelector('.brand img');
  if(brandImg){document.getElementById('bchatCrest').src=brandImg.src;}

  function esc(s){var d=document.createElement('div'); d.textContent=s; return d.innerHTML;}
  function linkify(s){return esc(s).replace(/(https?:\\/\\/[^\\s<]+[^\\s<.,)])/g,'<a href="$1" target="_blank" rel="noopener">$1</a>')
    .replace(/([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,})/g,'<a href="mailto:$1">$1</a>');}
  function add(role,text){var el=document.createElement('div'); el.className='bchat-msg '+role;
    el.innerHTML=role==='bot'?linkify(text):esc(text); msgs.appendChild(el); msgs.scrollTop=msgs.scrollHeight; return el;}
  function typing(on){var t=document.getElementById('bchatTyping');
    if(on&&!t){t=document.createElement('div'); t.id='bchatTyping'; t.className='bchat-typing';
      t.innerHTML='<span></span><span></span><span></span>'; msgs.appendChild(t); msgs.scrollTop=msgs.scrollHeight;}
    if(!on&&t){t.remove();}}

  function open(){panel.classList.add('open'); input.focus();
    if(!greeted){greeted=true; add('bot',"Hi! I'm the Barrie Rugby Club assistant. Ask me about programs, practice times, registration, fees, donations, or anything else about the club.");}}
  fab.addEventListener('click',function(){panel.classList.contains('open')?panel.classList.remove('open'):open();});
  document.getElementById('bchatClose').addEventListener('click',function(){panel.classList.remove('open');});
  chips.addEventListener('click',function(e){var b=e.target.closest('button'); if(b){send(b.getAttribute('data-q'));}});

  function send(text){
    text=(text||input.value).trim();
    if(!text||busy) return;
    input.value=''; chips.style.display='none';
    add('user',text); history.push({role:'user',content:text});
    busy=true; sendBtn.disabled=true; typing(true);
    fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({messages:history.slice(-10)})})
      .then(function(r){if(!r.ok) throw new Error(r.status); return r.json();})
      .then(function(d){
        typing(false);
        var reply=d.reply||"Sorry, something went wrong. Please email info@barrierugbyclub.com.";
        add('bot',reply); history.push({role:'assistant',content:reply});})
      .catch(function(){
        typing(false);
        add('bot',"Sorry, I'm having trouble connecting right now. Please email info@barrierugbyclub.com and a real human will get back to you.");})
      .finally(function(){busy=false; sendBtn.disabled=false; input.focus();});
  }
  sendBtn.addEventListener('click',function(){send();});
  input.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault(); send();}});
})();
</script>
"""

# ---------------------------------------------------------------------------
# ANNOUNCEMENT BANNER
# ---------------------------------------------------------------------------
# Content is baked in here at build time (the constants below) AND can be
# overridden at runtime by Cloudflare KV via /api/banner, edited from /admin.
#
#   - If /api/banner returns valid JSON, it wins - no rebuild needed to change
#     the text, link, on/off state, or which pages show the banner.
#   - If /api/banner is missing, erroring, or not yet wired up, the baked-in
#     values below render immediately with no network wait.
#
# So: edit these constants + rerun this script for a permanent change; use
# /admin for a quick change once the KV Function is deployed.
#
# ANNOUNCE_PAGES valid values: "home", "programs", "alumni", "resources"
# Bump ANNOUNCE_VERSION whenever the message changes, so people who already
# dismissed the previous banner are shown the new one.
# ---------------------------------------------------------------------------
ANNOUNCE_ENABLED = True
ANNOUNCE_TEXT = (
    "Junior 7s registration is now open!"
)
ANNOUNCE_LINK = "https://www.playhq.com/ca/rugby-canada/register/c4290e"
ANNOUNCE_LINK_TEXT = "Register Now"
ANNOUNCE_PAGES = {"home", "programs"}
ANNOUNCE_VERSION = "4"
# ISO datetime with Toronto offset ("-04:00" EDT / "-05:00" EST). After this
# moment the banner hides itself client-side for everyone, no redeploy needed.
# "" = never expires.
ANNOUNCE_EXPIRES = "2026-10-04T23:59:59-04:00"

_ANNOUNCE_PAYLOAD = {
    "enabled": ANNOUNCE_ENABLED,
    "text": ANNOUNCE_TEXT,
    "link": ANNOUNCE_LINK,
    "linkText": ANNOUNCE_LINK_TEXT,
    "pages": sorted(ANNOUNCE_PAGES),
    "version": ANNOUNCE_VERSION,
}
if ANNOUNCE_EXPIRES:
    _ANNOUNCE_PAYLOAD["expires"] = ANNOUNCE_EXPIRES
_ANNOUNCE_DEFAULT = json.dumps(_ANNOUNCE_PAYLOAD)


def announce_bar(page_key):
    return f"""
<div class="announce-bar" id="announceBar" style="display:none;">
  <div class="wrap">
    <span class="msg" id="announceMsg"></span>
    <a class="cta" id="announceCta" target="_blank" rel="noopener"></a>
    <button class="close" id="announceClose" aria-label="Dismiss announcement">&times;</button>
  </div>
</div>
<script>
(function(){{
  var PAGE_KEY = "{page_key}";
  var BAKED = {_ANNOUNCE_DEFAULT};
  var bar = document.getElementById('announceBar');
  var msg = document.getElementById('announceMsg');
  var cta = document.getElementById('announceCta');
  var closeBtn = document.getElementById('announceClose');
  if(!bar) return;
  var dkey = 'barrieAnnounceDismissed_1';

  function render(data){{
    if(!data || !data.enabled){{ bar.style.display = 'none'; return; }}
    if(data.expires){{
      var exp = new Date(data.expires);
      if(!isNaN(exp) && new Date() > exp){{ bar.style.display = 'none'; return; }}
    }}
    if(!data.pages || data.pages.indexOf(PAGE_KEY) === -1){{ bar.style.display = 'none'; return; }}
    dkey = 'barrieAnnounceDismissed_' + (data.version || '1');
    try{{ if(localStorage.getItem(dkey) === '1'){{ bar.style.display = 'none'; return; }} }}catch(e){{}}
    msg.textContent = data.text || '';
    if(data.link){{
      cta.href = data.link;
      cta.textContent = (data.linkText || 'Learn More') + ' →';
      cta.style.display = '';
    }} else {{
      cta.removeAttribute('href');
      cta.textContent = '';
      cta.style.display = 'none';
    }}
    bar.style.display = 'block';
  }}

  closeBtn.addEventListener('click', function(){{
    bar.style.display = 'none';
    try{{ localStorage.setItem(dkey, '1'); }}catch(e){{}}
  }});

  // Baked-in content paints immediately; KV overrides it when available.
  render(BAKED);
  fetch('/api/banner', {{cache: 'no-store'}}).then(function(r){{ return r.ok ? r.json() : null; }}).then(function(data){{
    if(data) render(data);
  }}).catch(function(){{}});
}})();
</script>
"""

# INDEX.HTML
# ---------------------------------------------------------------------------

index_body = f"""
<section class="hero">
  <video class="hero-video" autoplay muted loop playsinline poster="data:image/jpeg;base64,{BG_HERO_POSTER_B64}">
    <source src="hero-lineout.mp4" type="video/mp4">
  </video>
  <div class="hero-scrim"></div>
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
        <a class="btn-app" href="#app">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M11 18h2"/></svg>
          Get The App
        </a>
      </div>
    </div>
  </div>
</section>

<div class="strip">
  <div class="track">
    <span class="dot">EST. 1967</span><span class="dot">JIM HAMILTON FIELD</span><span class="dot">U6 &rarr; SENIOR</span><span class="dot">MEN'S &amp; WOMEN'S</span><span class="dot">BARRIE, ON</span>
    <span class="dot">EST. 1967</span><span class="dot">JIM HAMILTON FIELD</span><span class="dot">U6 &rarr; SENIOR</span><span class="dot">MEN'S &amp; WOMEN'S</span><span class="dot">BARRIE, ON</span>
  </div>
</div>

<section class="ig-banner">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap ig-banner-inner">
    <div>
      <span class="eyebrow">On The Sideline</span>
      <h2 class="display">Follow The Season.</h2>
      <p class="lede">Game days, tour recaps, and sideline moments from Jim Hamilton Field &mdash; posted every week.</p>
      <a class="go" href="https://www.instagram.com/barrierugby" target="_blank" rel="noopener">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg>
        Follow @barrierugby
      </a>
    </div>
    <div class="ig-badge-wrap">
      <div class="ig-badge">
        <div class="glyph">
          <svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg>
          <span>@BARRIERUGBY</span>
        </div>
      </div>
    </div>
  </div>
</section>

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
    <div class="card-grid">
      <div class="card"><span class="tag">Youth &amp; Minis</span><h3>Under 6 &ndash; Under 12</h3><p>First contact with the game. Instructional sessions built around fun, footwork, and the fundamentals.</p></div>
      <div class="card"><span class="tag">Junior</span><h3>U14 &middot; U16 &middot; U18 &mdash; Boys &amp; Girls</h3><p>Competitive age-grade rugby with dedicated boys' and girls' sides at every level &mdash; recent tours have taken teams to Portugal and France.</p></div>
      <div class="card"><span class="tag">Senior</span><h3>Men's &amp; Women's</h3><p>Competitive senior rugby on Jim Hamilton Field, open to new and returning players.</p></div>
      <div class="card"><span class="tag">In Schools</span><h3>Rugby Development Officers</h3><p>Our RDO program brings rugby into Barrie-area elementary and high schools.</p></div>
      <div class="card"><span class="tag">Access</span><h3>Financial Assistance</h3><p>The RUK program helps cover registration costs, because cost shouldn't decide who plays.</p></div>
      <div class="card"><span class="tag">Officiating</span><h3>Match Officials</h3><p>Rugby Ontario-registered officiating pathway for members who want to referee.</p></div>
    </div>
  </div>
</section>

<section class="appband" id="app">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap appband-inner">
    <div>
      <span class="eyebrow">Matchday</span>
      <h2>Every fixture.<br>Every result.<br><em>In your pocket.</em></h2>
      <p class="lede">Barrie Rugby Club runs its competitions on PlayHQ &mdash; and <strong style="color:#fff;">RUGBYCAN</strong> is the official free app that goes with it. Schedules, live scores, results and club communications for every team, from the minis to the senior sides.</p>
      <div class="store-row">
        <a class="store-btn" href="https://apps.apple.com/ca/app/rugbycan/id6756593343" target="_blank" rel="noopener" aria-label="Download RUGBYCAN on the App Store">
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.05 12.53c-.02-2.2 1.8-3.26 1.88-3.31-1.02-1.5-2.61-1.7-3.18-1.73-1.35-.14-2.64.8-3.33.8-.69 0-1.75-.78-2.87-.76-1.48.02-2.84.86-3.6 2.18-1.53 2.66-.39 6.6 1.1 8.76.73 1.06 1.6 2.25 2.74 2.2 1.1-.04 1.52-.71 2.85-.71s1.7.71 2.87.69c1.18-.02 1.93-1.08 2.65-2.14.83-1.23 1.18-2.42 1.2-2.48-.03-.01-2.29-.88-2.31-3.5zM14.9 5.5c.6-.74 1.01-1.76.9-2.78-.87.04-1.93.58-2.56 1.31-.56.65-1.06 1.7-.93 2.7.97.08 1.97-.49 2.59-1.23z"/></svg>
          <span class="lbl"><small>Download on the</small><strong>App Store</strong></span>
        </a>
        <a class="store-btn" href="https://play.google.com/store/apps/details?id=com.playhq.rugbycanada" target="_blank" rel="noopener" aria-label="Get RUGBYCAN on Google Play">
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3.6 2.3c-.24.26-.38.66-.38 1.18v17.04c0 .52.14.92.38 1.18l.06.06 9.55-9.55v-.22L3.66 2.44l-.06-.14zM16.6 15.4l-3.18-3.19v-.22l3.19-3.19.07.04 3.77 2.14c1.08.61 1.08 1.62 0 2.24l-3.77 2.14-.08.04zM15.9 16.1L12.64 12.85 3.03 22.46c.36.38.94.42 1.6.05l11.27-6.41M15.9 7.9L4.63 1.49c-.66-.38-1.24-.33-1.6.05l9.61 9.61L15.9 7.9z"/></svg>
          <span class="lbl"><small>Get it on</small><strong>Google Play</strong></span>
        </a>
      </div>
      <p class="fine">Free on iOS and Android &middot; Powered by PlayHQ &middot; Search <strong style="color:rgba(255,255,255,0.75);">Barrie Rugby Club</strong> once you're in. Not registered yet? <a href="https://www.playhq.com/ca/rugby-canada/register/c4290e">Start here</a>.</p>
    </div>
    <div class="phone-wrap">
      <div class="phone" aria-hidden="true">
        <div class="phone-screen">
          <div class="phone-mark"><b>RUGBYCAN</b><span>Powered by PlayHQ</span></div>
          <div class="phone-row">
            <div class="pic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 6v6l4 2"/><circle cx="12" cy="12" r="9"/></svg></div>
            <span class="ptxt">Live Scores</span>
            <span class="live"><i></i>LIVE</span>
          </div>
          <div class="phone-row">
            <div class="pic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg></div>
            <span class="ptxt">Fixtures &amp; Results</span>
            <span class="chev">&rsaquo;</span>
          </div>
          <div class="phone-row">
            <div class="pic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 4h16v12H7l-3 3V4z"/></svg></div>
            <span class="ptxt">Club Communications</span>
            <span class="chev">&rsaquo;</span>
          </div>
          <div class="phone-row">
            <div class="pic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.6 5.5 5.9.85-4.3 4.2 1.05 5.95L12 16.7l-5.25 2.8L7.8 13.55 3.5 9.35l5.9-.85L12 3z"/></svg></div>
            <span class="ptxt">Favourite Your Teams</span>
            <span class="chev">&rsaquo;</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="sponsors" style="background:#fff; border-top:1px solid var(--line); border-bottom:1px solid var(--line);">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Thank You</span>
      <h2>Our Sponsors</h2>
      <p class="lede">Barrie Rugby runs on the back of local businesses who back the club year after year.</p>
      <p class="lede"><a href="sponsorship-package-2026.pdf" target="_blank" rel="noopener" style="color:var(--sky-deep); font-weight:700;">View the 2026 Sponsorship Package (PDF) &rarr;</a></p>
    </div>

    <div class="tier-block">
      <div class="tier-label"><span class="badge platinum">Platinum</span><span class="line"></span></div>
      <div class="sponsor-grid">
        <div class="sponsor-card logo"><img src="{WESTERN}" alt="Western"></div>
      </div>
    </div>

    <div class="tier-block">
      <div class="tier-label"><span class="badge title">Title</span><span class="line"></span></div>
      <div class="sponsor-grid">
        <div class="sponsor-card logo"><img src="{DONALEIGHS}" alt="Donaleigh's"></div>
        <div class="sponsor-card logo"><img src="{MITSUBISHI}" alt="Barrie Mitsubishi"></div>
      </div>
    </div>

    <div class="tier-block">
      <div class="tier-label"><span class="badge direct">Direct</span><span class="line"></span></div>
      <div class="sponsor-grid wide">
        <div class="sponsor-card logo"><img src="{TODDSMITH}" alt="Todd Smith Mortgages"></div>
        <div class="sponsor-card logo"><img src="{MINDTOMUSCLE}" alt="Mind to Muscle Strength &amp; Conditioning Centre"></div>
        <div class="sponsor-card logo"><img src="{JONES}" alt="Jones Consulting Group Ltd."></div>
        <div class="sponsor-card cta"><div class="sname">Become a Sponsor</div><a href="mailto:info@barrierugbyclub.com">info@barrierugbyclub.com &rarr;</a></div>
      </div>
    </div>
  </div>
</section>

<section class="donate" id="donate">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap donate-inner">
    <div class="sec-head">
      <span class="eyebrow">Memorial &amp; Development Fund</span>
      <h2>Help build the next 60 years.</h2>
      <p class="lede">Donations flow through the National Sport Trust Fund (Project 391) and are eligible for a charitable tax receipt.</p>
    </div>
    <div class="donate-grid">
      <div class="donate-card"><div class="n">Equipment</div><p>Training, match-day, and safety gear for every age group.</p></div>
      <div class="donate-card"><div class="n">Coach Development</div><p>World Rugby &amp; Rugby Ontario certifications and clinics.</p></div>
      <div class="donate-card"><div class="n">Match Officials</div><p>Developing the next generation of Rugby Ontario referees.</p></div>
      <div class="donate-card"><div class="n">Club Development</div><p>Facilities, field maintenance, clubhouse, and technology.</p></div>
      <div class="donate-card"><div class="n">Training Opportunities</div><p>ID camps, rep program subsidies, strength &amp; conditioning.</p></div>
      <div class="donate-card"><div class="n">Member Assistance</div><p>Registration subsidies, kit help, and club events.</p></div>
    </div>
    <div class="donate-actions">
      <a class="donate-btn" href="https://www.ontariosportnetwork.ca/nstf-projects/391-barrie-rugby-club" target="_blank" rel="noopener">Donate Today &rarr;</a>
      <div class="donate-alt">Prefer to give directly? Use the <a href="https://forms.logiforms.com/formdata/user_forms/74769_1745267/345060/page1.html" target="_blank" rel="noopener">donation form</a> and select Barrie Rugby Club &middot; Memorial and Development Fund.</div>
    </div>
    <p class="donate-note">All donations are processed by the National Sport Trust Fund &mdash; Ontario, an independent charitable foundation, and are eligible for an official tax receipt.</p>
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
          <p>Casual fan apparel and lifestyle wear in club colours &mdash; the everyday store for supporters, alumni, and families on the sideline. Hosted by Source for Sports Barrie.</p>
          <a class="go" href="https://sfsbarrie.com/collections/barrie-rugby" target="_blank" rel="noopener">Shop Merch &rarr;</a>
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
      <div><div class="lbl">Youth &amp; Minis</div><div class="age">U6&ndash;U12</div></div>
      <div class="body">
        <h3>First touches, real fun</h3>
        <p>Instructional sessions built around ball skills, footwork, and enjoying the game &mdash; open to complete beginners. No experience needed, and no player is turned away for cost (see Financial Assistance below).</p>
        <div class="meta"><span class="pill">Instructional</span><span class="pill">Mon &amp; Wed practices</span><span class="pill">All experience levels</span></div>
      </div>
    </div>

    <div class="prog-row">
      <div><div class="lbl">Junior</div><div class="age">U14</div></div>
      <div class="body">
        <h3>U14 Boys &amp; Girls</h3>
        <p>Entry point into competitive age-grade rugby, playing a full Rugby Ontario / Toronto Rugby Union (TRU) calendar including regional qualifiers.</p>
        <div class="meta"><span class="pill">Competitive</span><span class="pill">Boys &amp; Girls sides</span><span class="pill">TRU Qualifiers</span></div>
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

    <div class="prog-row" id="ruk">
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
        <a class="back" href="resources.html">&larr; Back to Resources</a>
      </div>
      <a class="go" href="AgeGradeMatrix_2025.pdf" target="_blank" rel="noopener">View PDF &rarr;</a>
    </div>

    <div class="sec-head">
      <span class="eyebrow">Weekly Schedule</span>
      <h2>Practices &amp; game days.</h2>
      <p class="lede">Practice times below are confirmed &mdash; game kickoff times to follow once set.</p>
    </div>

    <h3 style="font-size:15px; color:var(--navy); margin-bottom:14px; font-family:'Anton', sans-serif; letter-spacing:0.04em; text-transform:uppercase;">Practices</h3>
    <div class="sched-wrap">
      <table class="sched-table">
        <tr><th>Team</th><th>Day</th><th>Time</th><th>Location</th></tr>
        <tr><td class="team">Youth &amp; Minis (U6&ndash;U12)</td><td>Monday &amp; Wednesday</td><td>6:00&ndash;8:00 PM</td><td>The Tree Nursery</td></tr>
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
        <tr><td class="team">Youth &amp; Minis (U6&ndash;U12)</td><td>Select Sundays (festivals)</td><td>TBD</td><td>Home / Away per festival</td></tr>
        <tr><td class="team">U14 &amp; U16 Boys &amp; Girls</td><td>Saturday</td><td>TBD</td><td>Home / Away per fixture</td></tr>
        <tr><td class="team">U18 Girls</td><td>Wednesday</td><td>TBD</td><td>Home / Away per fixture</td></tr>
        <tr><td class="team">U18 Boys</td><td>Wednesday</td><td>TBD</td><td>Home / Away per fixture</td></tr>
        <tr><td class="team">Senior Men's &amp; Women's</td><td>Saturday</td><td>TBD</td><td>Jim Hamilton Field (Home)</td></tr>
      </table>
    </div>
    <p class="sched-note">Kickoff times to be confirmed &mdash; send them whenever they're set and this table updates instantly. Full fixture list, including away matches, runs on the <a href="https://www.rugbyontario.com/fixtures/" target="_blank" rel="noopener" style="color:var(--sky-deep); font-weight:700;">Rugby Ontario schedule &rarr;</a></p>
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
      <div class="card"><span class="tag">Support</span><h3>Sponsor or Donate</h3><p>Many of our sponsors are alumni-owned businesses, and gifts to the Memorial &amp; Development Fund help fund the next generation. <a href="index.html#donate" style="color:var(--sky-deep); font-weight:700;">Donate or see sponsors &rarr;</a></p></div>
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
      <a class="res-link" href="index.html#app">
        <div><div class="t">RUGBYCAN App</div><div class="d">Official free app &mdash; fixtures, live scores &amp; results</div></div>
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
      <a class="res-link" href="fees.html">
        <div><div class="t">Where Your Registration Fee Goes</div><div class="d">How the 2026 fees split &mdash; and what the club's share covers</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="index.html#about">
        <div><div class="t">About Us</div><div class="d">Club history &amp; leadership</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="index.html#contact">
        <div><div class="t">Volunteering</div><div class="d">Get involved off the pitch</div></div>
        <span class="arrow">&rarr;</span>
      </a>
      <a class="res-link" href="sponsorship-package-2026.pdf" target="_blank" rel="noopener">
        <div><div class="t">2026 Sponsorship Package</div><div class="d">Tiered levels &amp; direct-item sponsorship menu (PDF)</div></div>
        <span class="arrow">&rarr;</span>
      </a>
    </div>

  </div>
</section>

{CONTACT_SECTION}
"""

# On cross-page anchor jumps (e.g. resources.html -> programs.html#matrix) the
# browser scrolls before the base64-embedded images finish decoding, so layout
# shifts under the scroll position and the target lands off-screen. After full
# load, re-snap to the hash target instantly (suppressing smooth-scroll so the
# correction isn't a visible animation).
# ---------------------------------------------------------------------------
# REGISTRATION FEES PAGE (fees.html)
#
# Every dollar figure below comes from the club's 2026 registration fee
# workbook. FEES is generated from that workbook, not typed by hand; the
# assertion under it re-checks that the three shares still add up to the
# advertised total, so a bad edit fails the build instead of shipping.
# ---------------------------------------------------------------------------
FEES = [
    dict(group='Minis & Youth', label='U6 &middot; U8 &middot; U10', sub='Flag rugby, non-contact', rc=30.00, ro=32.54, club=273.46, total=336.00),
    dict(group='Minis & Youth', label='U12', sub='Intro to contact', rc=40.00, ro=32.54, club=288.46, total=361.00),
    dict(group='Junior', label='U14', sub='Intro to contact', rc=82.50, ro=59.37, club=310.13, total=452.00),
    dict(group='Junior', label='U16 Girls', sub='Contact', rc=116.05, ro=59.37, club=274.58, total=450.00),
    dict(group='Junior', label='U16 Boys', sub='Contact', rc=116.05, ro=59.37, club=304.58, total=480.00),
    dict(group='Junior', label='U18 Girls', sub='Contact', rc=116.05, ro=59.37, club=274.58, total=450.00),
    dict(group='Junior', label='U18 Boys', sub='Contact', rc=116.05, ro=59.37, club=304.58, total=480.00),
    dict(group='Senior', label='Senior Women', sub='Contact', rc=129.50, ro=89.80, club=230.70, total=450.00),
    dict(group='Senior', label='Senior Men &mdash; student', sub='Contact', rc=129.50, ro=89.80, club=230.70, total=450.00),
    dict(group='Senior', label='Senior Men', sub='Contact', rc=129.50, ro=89.80, club=290.70, total=510.00),
    dict(group='Short-term', label='Two-week trial', sub='Junior or senior contact', rc=49.50, ro=22.72, club=52.78, total=125.00),
]

# 2025 -> 2026 movement, from the same workbook.
FEE_MINI_RISE = 1.00
FEE_TOTAL_RISE = 50.00
FEE_RO_DROP_JR = 5.89
FEE_RO_DROP_SR = 8.91
FEE_CLUB_RISE_SR = 58.91

for _f in FEES:
    assert abs(_f['rc'] + _f['ro'] + _f['club'] - _f['total']) < 0.011, \
        'fee split does not reconcile: ' + _f['label']
    _f['rc_p'] = _f['rc'] / _f['total'] * 100
    _f['ro_p'] = _f['ro'] / _f['total'] * 100
    _f['club_p'] = _f['club'] / _f['total'] * 100
    _f['club_pct'] = round(_f['club'] / _f['total'] * 100)

FEE_DEFAULT = next(i for i, f in enumerate(FEES) if f['label'] == 'U14')
FEE_MIN_CLUB = min(f['club_pct'] for f in FEES if f['label'] != 'Two-week trial')
FEE_MAX_CLUB = max(f['club_pct'] for f in FEES)
FEE_RC_MIN, FEE_RC_MAX = min(f['rc'] for f in FEES), max(f['rc'] for f in FEES)
FEE_RO_MIN, FEE_RO_MAX = min(f['ro'] for f in FEES), max(f['ro'] for f in FEES)


def _money(v):
    return '$%s' % format(v, ',.2f')


def _money0(v):
    return '$%s' % (format(int(round(v)), ',d') if abs(v - round(v)) < 0.005 else format(v, ',.2f'))


def _fee_plain(txt):
    """Strip the HTML entities we use in labels so they read correctly inside
    an aria-label attribute."""
    return txt.replace('&middot;', '-').replace('&mdash;', '-').replace('&amp;', 'and')


def _fee_row(f):
    label = _fee_plain(
        '%s total %s: Rugby Canada %s, Rugby Ontario %s, Barrie Rugby Club %s (%d per cent)'
        % (f['label'], _money0(f['total']), _money(f['rc']), _money(f['ro']),
           _money(f['club']), f['club_pct']))
    bar = ('<span class="fee-bar" role="img" aria-label="%s">'
           '<span class="s rc" style="--w:%.3f%%"></span>'
           '<span class="s ro" style="--w:%.3f%%"></span>'
           '<span class="s club" style="--w:%.3f%%"></span></span>'
           % (label, f['rc_p'], f['ro_p'], f['club_p']))
    vals = ('<span class="fee-vals" aria-hidden="true">'
            '<b class="r"><span class="nm">Rugby Canada</span>%s</b>'
            '<b class="o"><span class="nm">Rugby Ontario</span>%s</b>'
            '<b class="c"><span class="nm">Barrie Rugby Club</span>%s</b></span>'
            % (_money(f['rc']), _money(f['ro']), _money(f['club'])))
    return ('<tr>'
            '<th scope="row" class="fee-c1"><span class="l">%s</span><span class="s">%s</span></th>'
            '<td class="fee-c2">%s%s</td>'
            '<td class="fee-c3"><span class="t">%s</span><span class="p">%d%% stays here</span></td>'
            '</tr>' % (f['label'], f['sub'], bar, vals, _money0(f['total']), f['club_pct']))


_rows, _plain_rows, _last = [], [], None
for _f in FEES:
    if _f['group'] != _last:
        _rows.append('<tr class="grp"><th colspan="3" scope="colgroup">%s</th></tr>' % _f['group'])
        _plain_rows.append('<tr class="grp"><th colspan="5" scope="colgroup">%s</th></tr>' % _f['group'])
        _last = _f['group']
    _rows.append(_fee_row(_f))
    _plain_rows.append(
        '<tr><td class="team">%s</td><td class="num">%s</td><td class="num">%s</td>'
        '<td class="num">%s</td><td class="num">%s</td></tr>'
        % (_f['label'], _money(_f['rc']), _money(_f['ro']), _money(_f['club']), _money0(_f['total'])))

FEE_TABLE_ROWS = '\n        '.join(_rows)
FEE_PLAIN_ROWS = '\n          '.join(_plain_rows)

FEE_JSON = json.dumps([
    dict(label=f['label'], sub=f['sub'], total=f['total'], rc=f['rc'], ro=f['ro'], club=f['club'],
         rc_p=round(f['rc_p'], 3), ro_p=round(f['ro_p'], 3), club_p=round(f['club_p'], 3),
         club_pct=f['club_pct'], aria=_fee_plain(
             '%s total %s: Rugby Canada %s, Rugby Ontario %s, Barrie Rugby Club %s (%d per cent)'
             % (f['label'], _money0(f['total']), _money(f['rc']), _money(f['ro']),
                _money(f['club']), f['club_pct'])))
    for f in FEES], separators=(',', ':'))

FEES_SCRIPT = """
<script>
(function(){
  var DATA = __FEE_JSON__, DEF = __FEE_DEFAULT__;
  var chips = document.getElementById('feeChips');
  if(!chips) return;
  function el(id){ return document.getElementById(id); }
  function money(v){ return '$' + v.toFixed(2).replace(/\\B(?=(\\d{3})+(?!\\d))/g,','); }
  function money0(v){
    var s = Math.abs(v - Math.round(v)) < 0.005 ? String(Math.round(v)) : v.toFixed(2);
    return '$' + s.replace(/\\B(?=(\\d{3})+(?!\\d))/g,',');
  }
  var btns = DATA.map(function(d,i){
    var b = document.createElement('button');
    b.type='button'; b.className='fee-chip'; b.innerHTML=d.label;
    b.setAttribute('aria-pressed','false');
    b.addEventListener('click', function(){ select(i); });
    chips.appendChild(b);
    return b;
  });
  function seg(id, vid, pct, val){
    el(id).style.setProperty('--w', pct + '%');
    el(vid).textContent = money0(val);
    el(vid).className = 'v' + (pct < 8 ? ' off' : '');
  }
  function select(i){
    var d = DATA[i];
    btns.forEach(function(b,j){ b.setAttribute('aria-pressed', j===i ? 'true' : 'false'); });
    el('feeWho').innerHTML = d.label + '<small>' + d.sub + '</small>';
    el('feeTotal').textContent = money0(d.total);
    seg('feeSegRc','feeValRc',d.rc_p,d.rc);
    seg('feeSegRo','feeValRo',d.ro_p,d.ro);
    seg('feeSegClub','feeValClub',d.club_p,d.club);
    el('feeLegRc').textContent = money(d.rc);
    el('feeLegRo').textContent = money(d.ro);
    el('feeLegClub').textContent = money(d.club);
    el('feeSubRc').textContent = Math.round(d.rc_p) + '% \u2014 remitted in full';
    el('feeSubRo').textContent = Math.round(d.ro_p) + '% \u2014 remitted in full';
    el('feeSubClub').textContent = d.club_pct + '% \u2014 stays with the club';
    el('feeBigBar').setAttribute('aria-label', d.aria);
  }
  chips.addEventListener('keydown', function(e){
    var i = btns.indexOf(document.activeElement);
    if(i < 0) return;
    var n = null;
    if(e.key==='ArrowRight'||e.key==='ArrowDown') n = (i+1) % btns.length;
    if(e.key==='ArrowLeft'||e.key==='ArrowUp') n = (i-1+btns.length) % btns.length;
    if(n===null) return;
    e.preventDefault(); btns[n].focus(); select(n);
  });
  select(DEF);
})();
</script>"""
FEES_SCRIPT = FEES_SCRIPT.replace('__FEE_JSON__', FEE_JSON).replace('__FEE_DEFAULT__', str(FEE_DEFAULT))

fees_body = f"""
<section class="pagehero">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap pagehero-inner">
    <span class="eyebrow">Registration 2026</span>
    <h1>Where your registration fee goes.</h1>
    <p>Every registration is split three ways before a single ball is kicked. Here is exactly how the 2026 fees divide &mdash; and what the club's share has to carry once the season starts.</p>
  </div>
</section>

<section style="padding-top:64px; padding-bottom:64px;">
  <div class="wrap">
    <div class="fee-panel">
      <span class="lbl">Choose a registration</span>
      <div class="fee-chips" id="feeChips" role="group" aria-label="Choose a registration category"></div>
      <div class="fee-readout" aria-live="polite">
        <div class="top">
          <div class="who" id="feeWho">&mdash;</div>
          <div class="amt" id="feeTotal">&mdash;</div>
        </div>
        <span class="fee-bar big" role="img" id="feeBigBar" aria-label="">
          <span class="s rc" id="feeSegRc"><span class="v" id="feeValRc"></span></span>
          <span class="s ro" id="feeSegRo"><span class="v" id="feeValRo"></span></span>
          <span class="s club" id="feeSegClub"><span class="v" id="feeValClub"></span></span>
        </span>
        <ul class="fee-legend">
          <li><span class="k">Rugby Canada</span><span class="n" id="feeLegRc">&mdash;</span><span class="s" id="feeSubRc">national registration</span></li>
          <li><span class="k">Rugby Ontario</span><span class="n" id="feeLegRo">&mdash;</span><span class="s" id="feeSubRo">provincial registration</span></li>
          <li><span class="k">Barrie Rugby Club</span><span class="n" id="feeLegClub">&mdash;</span><span class="s" id="feeSubClub">stays with the club</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="about">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">The split</span>
      <h2>One payment, three organisations.</h2>
      <p class="lede">When you register a player you are paying three bodies at once. Two of the three amounts are set elsewhere and passed straight through by the club. The third is the only part Barrie Rugby Club ever sees.</p>
    </div>
    <div class="card-grid">
      <div class="card org-rc">
        <span class="tag">National</span>
        <h3>Rugby Canada</h3>
        <div class="amt">{_money(FEE_RC_MIN)} &ndash; {_money(FEE_RC_MAX)}</div>
        <div class="amt-l">per player, 2026</div>
        <p>The national registration every rugby player in Canada pays, regardless of which club they join. Barrie collects it and remits it &mdash; none of it stays here.</p>
      </div>
      <div class="card org-ro">
        <span class="tag">Provincial</span>
        <h3>Rugby Ontario</h3>
        <div class="amt">{_money(FEE_RO_MIN)} &ndash; {_money(FEE_RO_MAX)}</div>
        <div class="amt-l">per player, 2026</div>
        <p>The provincial registration that sanctions our teams to play in Ontario competition. Also collected and remitted in full &mdash; none of it stays here either.</p>
      </div>
      <div class="card org-club">
        <span class="tag">The club</span>
        <h3>Barrie Rugby Club</h3>
        <div class="amt">{FEE_MIN_CLUB}% &ndash; {FEE_MAX_CLUB}%</div>
        <div class="amt-l">of a full-season fee</div>
        <p>The club's share. This is the money that actually puts a coached, insured, officiated, medically covered team on Jim Hamilton Field every week of the season &mdash; and kit on every player.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">2026 fee schedule</span>
      <h2>Every category, broken down.</h2>
      <p class="lede">Read each bar left to right: Rugby Canada first, then Rugby Ontario, then the club's share. The club's portion is the largest part of every fee on this page &mdash; and the only part that comes back into Barrie rugby.</p>
    </div>
    <div class="fee-key">
      <span class="r">Rugby Canada</span><span class="o">Rugby Ontario</span><span class="c">Barrie Rugby Club</span>
    </div>
    <div class="fee-tablewrap">
      <table class="fee-table">
        <caption class="visually-hidden" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;">2026 Barrie Rugby Club registration fees, split between Rugby Canada, Rugby Ontario and the club</caption>
        <tbody>
        {FEE_TABLE_ROWS}
        </tbody>
      </table>
    </div>
    <details class="fee-plain">
      <summary>View the same figures as a plain table</summary>
      <div class="sched-wrap">
        <table class="sched-table">
          <thead><tr><th>Category</th><th class="num">Rugby Canada</th><th class="num">Rugby Ontario</th><th class="num">Barrie RC</th><th class="num">Total</th></tr></thead>
          <tbody>
          {FEE_PLAIN_ROWS}
          </tbody>
        </table>
      </div>
    </details>
  </div>
</section>

<section class="about">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">The club's share</span>
      <h2>What the club portion has to cover.</h2>
      <p class="lede">Registering a player is where the cost starts, not where it ends. Almost everything that makes a match happen is paid for out of club proceeds &mdash; not by the province, and not by the national body.</p>
    </div>
    <div class="card-grid">
      <div class="card">
        <span class="tag">Player safety</span>
        <h3>Athletic therapy</h3>
        <p>Qualified medical coverage on the sideline is not optional in contact rugby, and it is not funded from above. The cost of having an athletic therapist at our matches comes directly out of club proceeds.</p>
      </div>
      <div class="card">
        <span class="tag">Match day</span>
        <h3>Match officials</h3>
        <p>Every sanctioned match needs an accredited referee, and officials are paid and travelled for. Those costs sit with the club, on every home fixture, at every age grade.</p>
      </div>
      <div class="card">
        <span class="tag">Competition</span>
        <h3>Running the games</h3>
        <p>Almost all of the cost of running competition &mdash; including hosting branch qualifiers &mdash; falls to the clubs involved. When Barrie hosts, Barrie pays for it.</p>
      </div>
    </div>

    <div class="sec-head" style="margin-top:56px; margin-bottom:0;">
      <span class="eyebrow">In the kit bag</span>
      <h2 style="font-size:clamp(24px,3vw,32px);">And some of it goes home with the player.</h2>
      <p class="lede">Every registered player gets club kit as part of the fee &mdash; new, every season, at no extra charge.</p>
    </div>
    <div class="fee-kit">
      <div class="card">
        <div class="band">U6 <em>to</em> U12</div>
        <ul><li>Club shorts</li><li>Club t-shirt</li><li>Flags</li></ul>
        <p class="note">A full kit, included in the registration fee.</p>
      </div>
      <div class="card">
        <div class="band">U14 <em>and up</em></div>
        <ul><li>Premium match shorts</li><li>Warm-up t-shirt</li></ul>
        <p class="note">Issued new every year, to every registered player.</p>
      </div>
    </div>

    <div class="fee-note">
      <h3>The club's share also carries</h3>
      <ul>
        <li>Field access and pitch preparation at Jim Hamilton Field</li>
        <li>Match balls, training equipment, tackle shields and post padding</li>
        <li>First aid supplies and sideline medical kit</li>
        <li>Coach certification and match official development</li>
        <li>League and tournament entry for every team</li>
        <li>Festival and event hosting for the minis and youth programs</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Year over year</span>
      <h2>What changed for 2026.</h2>
      <p class="lede">Fees for the minis and youth program were effectively held &mdash; up {_money0(FEE_MINI_RISE)} on the year. From U14 up, registration rose {_money0(FEE_TOTAL_RISE)}. That increase did not go to the province &mdash; provincial fees actually came down &mdash; it went to the rising cost of putting teams on the field, and to kit that now goes home with every registered player.</p>
    </div>
    <div class="fee-change">
      <div>
        <div class="t">Minis &amp; youth</div>
        <div class="n">+{_money0(FEE_MINI_RISE)}</div>
        <div class="l">The whole change to a U6&ndash;U12 registration. Flag rugby and intro-to-contact were held where they were.</div>
      </div>
      <div>
        <div class="t">Provincial fee</div>
        <div class="n">&minus;{_money(FEE_RO_DROP_SR)}</div>
        <div class="l">The senior Rugby Ontario fee actually fell in 2026, and the junior provincial fee fell {_money(FEE_RO_DROP_JR)} alongside it.</div>
      </div>
      <div>
        <div class="t">Club share</div>
        <div class="n">+{_money(FEE_CLUB_RISE_SR)}</div>
        <div class="l">The rise in the club's share of a senior registration &mdash; more than the {_money0(FEE_TOTAL_RISE)} the fee itself went up, because the provincial saving was absorbed too.</div>
      </div>
    </div>
    <p style="margin-top:26px; font-size:15.5px; line-height:1.75; color:#454d64; max-width:70ch;">In other words: <strong style="color:var(--navy);">every dollar of the 2026 increase, and then some, went to club-side costs</strong> &mdash; therapy coverage, officials, competition, the day-to-day cost of a season, and club kit for every registered player. None of it went to head office.</p>
  </div>
</section>

<section class="fee-close">
  <div class="sash"><span></span><span></span></div>
  <div class="wrap fee-close-inner">
    <div class="sec-head">
      <span class="eyebrow">The gap</span>
      <h2>Why the club fundraises.</h2>
      <p class="lede">Barrie Rugby Club has been in this community since 1967, and the price of playing here has always been set with one thing in mind: a family should be able to say yes.</p>
    </div>
    <div class="prose">
      <p>That choice has a consequence. Registration is priced to keep rugby reachable, not to recover what a season actually costs. Sideline medical coverage, match officials, competition hosting, equipment, kit and field time all move with the market; the fee does not move with them. <strong>The difference between what registration brings in and what a full season costs is real, and it has to be closed somewhere.</strong></p>
      <p>It gets closed three ways.</p>
    </div>
    <div class="donate-grid">
      <div class="donate-card">
        <div class="n">Sponsors</div>
        <p>Local businesses who put their name behind the club and cover costs a registration fee was never going to reach.</p>
      </div>
      <div class="donate-card">
        <div class="n">Fundraising</div>
        <p>Club events and campaigns through the season, aimed squarely at the gap between fees collected and a season delivered.</p>
      </div>
      <div class="donate-card">
        <div class="n">Volunteers</div>
        <p>The coaches, referees, managers, canteen crew and board members who are not paid for any of it &mdash; the largest unbilled cost of all.</p>
      </div>
    </div>
    <div class="prose">
      <p>That is what fundraising is actually for. It is not an extra on top of a fee that already covers everything. It is the part of the budget registration was never going to reach &mdash; and it is the reason the number on the registration form is as low as it is.</p>
      <p style="font-size:13.5px; color:rgba(255,255,255,0.55); margin-top:22px;">Figures shown are 2026 registration fees. Questions about fees: <a href="mailto:info@barrierugbyclub.com" style="color:var(--sky); font-weight:700; text-decoration:underline;">info@barrierugbyclub.com</a></p>
    </div>
  </div>
</section>
""" + FEES_SCRIPT


ANCHOR_FIX = """<script>
(function(){
  if(!location.hash) return;
  function snap(){
    var el = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if(!el) return;
    var html = document.documentElement;
    var prev = html.style.scrollBehavior;
    html.style.scrollBehavior = 'auto';
    el.scrollIntoView({block:'start'});
    html.style.scrollBehavior = prev;
  }
  window.addEventListener('load', function(){ requestAnimationFrame(snap); setTimeout(snap, 250); });
})();
</script>"""

# ---------------------------------------------------------------------------
# SEO — canonical host is https://www.barrierugby.com (Cloudflare Pages serves
# pretty URLs, so /programs.html canonicalizes to /programs). Descriptions use
# locked club facts only. JSON-LD (SportsOrganization) goes on the homepage.
# ---------------------------------------------------------------------------
CANONICAL_HOST = 'https://www.barrierugby.com'

JSONLD_INDEX = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SportsOrganization",
  "name": "Barrie Rugby Club",
  "sport": "Rugby Union",
  "foundingDate": "1967",
  "url": "https://www.barrierugby.com/",
  "logo": "https://www.barrierugby.com/crest-512.png",
  "email": "info@barrierugbyclub.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2100 Nursery Rd",
    "addressLocality": "Barrie",
    "addressRegion": "ON",
    "addressCountry": "CA"
  },
  "location": {
    "@type": "Place",
    "name": "Jim Hamilton Field, Barrie Community Sports Complex",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "2100 Nursery Rd",
      "addressLocality": "Barrie",
      "addressRegion": "ON",
      "addressCountry": "CA"
    }
  },
  "sameAs": ["https://www.facebook.com/groups/barrierugby/"]
}
</script>"""


def page(title, active, body, bg_b64=None, description='', path='/', jsonld=''):
    extra = f'<style>:root{{--section-bg:url(data:image/jpeg;base64,{bg_b64})}}</style>' if bg_b64 else ''
    canonical = CANONICAL_HOST + path
    return f"""<!DOCTYPE html>
<html lang="en">
{HEAD.format(title=title, css=CSS, extra=extra, description=description, canonical=canonical, jsonld=jsonld)}
<body>
{announce_bar(active)}
{nav(active)}
{body}
{FOOTER}
{CHAT_WIDGET}
{ANCHOR_FIX}
</body>
</html>"""

out_dir = '/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else os.path.join(_BASE, 'out')
os.makedirs(out_dir, exist_ok=True)

with open(f'{out_dir}/index.html', 'w') as f:
    f.write(page(
        "Barrie Rugby Club | Youth & Senior Rugby in Barrie, Ontario",
        "home", index_body,
        description="Barrie Rugby Club — competitive and instructional rugby in Barrie, Ontario since 1967. Programs from U6 minis to Senior Men's and Women's at Jim Hamilton Field.",
        path='/', jsonld=JSONLD_INDEX))

with open(f'{out_dir}/programs.html', 'w') as f:
    f.write(page(
        "Programs & Teams | Barrie Rugby Club",
        "programs", programs_body, bg_b64=BG_PROGRAMS_B64,
        description="Every Barrie Rugby Club program — Youth & Minis (U6–U12), U14/U16/U18 boys and girls, and Senior Men's & Women's — plus the weekly practice and game day schedule.",
        path='/programs'))

with open(f'{out_dir}/fees.html', 'w') as f:
    f.write(page(
        "Where Your Registration Fee Goes | Barrie Rugby Club",
        "fees", fees_body,
        description="Where a Barrie Rugby Club registration fee goes \u2014 the 2026 split between Rugby Canada, Rugby Ontario and the club, what the club's share covers, and the kit included in every registration.",
        path='/fees'))

with open(f'{out_dir}/alumni.html', 'w') as f:
    f.write(page(
        "Alumni | Barrie Rugby Club",
        "alumni", alumni_body, bg_b64=BG_ALUMNI_B64,
        description="Players who wore the Barrie Rugby Club crest — alumni drawn from the club's own written history, dating back to its founding in 1967.",
        path='/alumni'))

with open(f'{out_dir}/resources.html', 'w') as f:
    f.write(page(
        "Resources & Documents | Barrie Rugby Club",
        "resources", resources_body, bg_b64=BG_RESOURCES_B64,
        description="Club documents, registration links, kit and merch stores, and key resources for Barrie Rugby Club players, parents, and supporters.",
        path='/resources'))

# hero background video is an external file (can't be base64-embedded like the
# photos without bloating every load) — copy it alongside the generated HTML.
video_src = os.path.join(ASSET_DIR, 'hero-lineout.mp4')
video_dst = os.path.join(out_dir, 'hero-lineout.mp4')
if os.path.exists(video_src):
    import shutil
    shutil.copy(video_src, video_dst)

# ---------------------------------------------------------------------------
# SEO SUPPORT FILES — 404.html, robots.txt, sitemap.xml, _redirects.
# The presence of 404.html switches Cloudflare Pages out of SPA-fallback mode,
# so unmatched URLs return a real 404 instead of serving index.html with a 200
# (the "soft 404" that made every old Wix URL look like a duplicate homepage).
# _redirects 301-maps every old Wix path Google still has indexed.
# ---------------------------------------------------------------------------

NOT_FOUND = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Page Not Found | Barrie Rugby Club</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#142645">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Public+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Public Sans',sans-serif;background:#0c1a30;color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;padding:32px;}}
.sash{{position:absolute;inset:0;pointer-events:none;}}
.sash span{{position:absolute;background:linear-gradient(90deg,#7cc5ea 0%,#4fa3d1 100%);opacity:0.1;width:180%;height:120px;transform:rotate(-9deg);left:-40%;top:18%;}}
.sash span:nth-child(2){{top:60%;opacity:0.06;left:-60%;}}
.box{{position:relative;z-index:1;text-align:center;max-width:560px;}}
.box img{{width:96px;height:96px;margin:0 auto 24px;display:block;}}
.eyebrow{{font-family:'Anton',sans-serif;font-size:13px;letter-spacing:0.24em;text-transform:uppercase;color:#7cc5ea;}}
h1{{font-family:'Anton',sans-serif;text-transform:uppercase;font-size:clamp(38px,7vw,64px);line-height:1.02;margin:14px 0 16px;}}
h1 em{{font-style:normal;color:#7cc5ea;}}
p{{color:rgba(255,255,255,0.82);font-size:16px;line-height:1.6;margin-bottom:28px;}}
.links{{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;}}
.links a{{color:#0c1a30;background:#7cc5ea;font-family:'Anton',sans-serif;text-transform:uppercase;letter-spacing:0.05em;font-size:13px;padding:11px 20px;border-radius:3px;text-decoration:none;transition:background .15s ease;}}
.links a:hover{{background:#fff;}}
.links a.ghost{{background:transparent;color:#fff;border:1px solid rgba(255,255,255,0.35);}}
.links a.ghost:hover{{border-color:#7cc5ea;color:#7cc5ea;background:transparent;}}
.links a:focus-visible{{outline:2px solid #7cc5ea;outline-offset:3px;}}
</style>
</head>
<body>
<div class="sash"><span></span><span></span></div>
<main class="box">
  <img src="{LOGO}" alt="Barrie Rugby crest">
  <span class="eyebrow">404 &middot; Page Not Found</span>
  <h1>KICKED INTO <em>TOUCH.</em></h1>
  <p>This page doesn't exist &mdash; or it moved when we rebuilt the site. The lineout below will throw you back in.</p>
  <nav class="links">
    <a href="/">Home</a>
    <a href="/programs">Programs</a>
    <a href="/alumni">Alumni</a>
    <a href="/resources">Resources</a>
    <a class="ghost" href="/#contact">Contact</a>
  </nav>
</main>
</body>
</html>"""

SITEMAP_LASTMOD = '2026-08-09'
FEES_LASTMOD = '2026-08-22'   # fees.html is new this build
SITEMAP = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{CANONICAL_HOST}/</loc><lastmod>{SITEMAP_LASTMOD}</lastmod></url>
  <url><loc>{CANONICAL_HOST}/programs</loc><lastmod>{SITEMAP_LASTMOD}</lastmod></url>
  <url><loc>{CANONICAL_HOST}/fees</loc><lastmod>{FEES_LASTMOD}</lastmod></url>
  <url><loc>{CANONICAL_HOST}/alumni</loc><lastmod>{SITEMAP_LASTMOD}</lastmod></url>
  <url><loc>{CANONICAL_HOST}/resources</loc><lastmod>{SITEMAP_LASTMOD}</lastmod></url>
</urlset>
"""

ROBOTS = f"""User-agent: *
Allow: /
Disallow: /admin
Disallow: /api/

Sitemap: {CANONICAL_HOST}/sitemap.xml
"""

# Every old Wix URL Google still has indexed (verified via site: search,
# 2026-08-09), 301-mapped to its closest new home. /alumni maps 1:1
# automatically (same path), so it needs no rule.
REDIRECTS = """# Old Wix site -> new site (301 permanent)
/home / 301
/history /alumni 301
/what-we-offer /programs 301
/teams /programs#teams 301
/u14-boys-team /programs#teams 301
/u14-girls-team /programs#teams 301
/u16-boys-team /programs#teams 301
/u16-girls-team /programs#teams 301
/u18-boys-team /programs#teams 301
/u18-girls-team /programs#teams 301
/mens-team /programs#teams 301
/womens-team /programs#teams 301
/executive /#about 301
/our-sponsors /#sponsors 301
/become-a-sponsor /#sponsors 301
/contact-us /#contact 301
/club-calendar /programs#matrix 301
/ruk /programs#ruk 301
/jaguars-festival /programs 301

# Convenience short link -> PlayHQ registration
/register https://www.playhq.com/ca/rugby-canada/register/c4290e 302
"""

with open(f'{out_dir}/404.html', 'w') as f:
    f.write(NOT_FOUND)
with open(f'{out_dir}/sitemap.xml', 'w') as f:
    f.write(SITEMAP)
with open(f'{out_dir}/robots.txt', 'w') as f:
    f.write(ROBOTS)
with open(f'{out_dir}/_redirects', 'w') as f:
    f.write(REDIRECTS)

print("Built index.html, programs.html, fees.html, alumni.html, resources.html")
print("Built 404.html, sitemap.xml, robots.txt, _redirects")
for fn in ['index.html','programs.html','fees.html','alumni.html','resources.html']:
    p = f'{out_dir}/{fn}'
    print(fn, round(os.path.getsize(p)/1024,1), 'KB')
