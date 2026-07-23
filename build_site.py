import os
import sys

_BASE = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = '/home/claude' if os.path.exists('/home/claude/sponsor_b64.py') else _BASE
sys.path.insert(0, ASSET_DIR)
from sponsor_b64 import DONALEIGHS, WESTERN, MITSUBISHI, TODDSMITH

with open(os.path.join(ASSET_DIR, 'logo_transparent_b64.txt')) as f:
    LOGO = 'data:image/png;base64,' + f.read().strip()

# ---------------------------------------------------------------------------
# ANNOUNCEMENT BANNER — edit these 4 lines and rerun the script to update
# ---------------------------------------------------------------------------
from string import Template

ANNOUNCE_ENABLED = True
ANNOUNCE_TEXT = "Download the official Rugby Canada app to follow Barrie Rugby Club scores, schedules, and news."
ANNOUNCE_LINK = "https://get.playhq.com/apps/rugbycanada"
ANNOUNCE_LINK_TEXT = "Download The App"
ANNOUNCE_PAGES = {"home"}  # which page(s) show it: any of "home", "programs", "alumni", "resources"

_ANNOUNCE_TEMPLATE = Template("""
<div class="announce-bar" id="announceBar">
  <div class="wrap">
    <span class="msg">$TEXT</span>
    <a class="cta" href="$LINK" target="_blank" rel="noopener">$LINK_TEXT &rarr;</a>
    <button class="close" id="announceClose" aria-label="Dismiss announcement">&times;</button>
  </div>
</div>
<script>
(function(){
  var KEY = 'barrieAnnounceDismissed_v2';
  var bar = document.getElementById('announceBar');
  if(!bar) return;
  try{
    if(localStorage.getItem(KEY) === '1'){ bar.style.display = 'none'; return; }
  }catch(e){}
  var btn = document.getElementById('announceClose');
  btn.addEventListener('click', function(){
    bar.style.display = 'none';
    try{ localStorage.setItem(KEY, '1'); }catch(e){}
  });
})();
</script>
""")

ANNOUNCE_BAR = _ANNOUNCE_TEMPLATE.substitute(
    TEXT=ANNOUNCE_TEXT, LINK=ANNOUNCE_LINK, LINK_TEXT=ANNOUNCE_LINK_TEXT
) if ANNOUNCE_ENABLED else ""

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
.navlinks{display:flex; align-items:center; gap:24px;}
.navlinks a{color:rgba(255,255,255,0.82); font-size:13px; font-weight:700; letter-spacing:0.05em; text-transform:uppercase; transition:color .15s ease; white-space:nowrap;}
.navlinks a:hover, .navlinks a.active{color:var(--sky);}
.navlinks a.donate-link{color:var(--gold);}
.navlinks a.donate-link:hover{color:#fff;}
.cta-btn{background:var(--sky); color:var(--navy-deep) !important; font-family:'Anton', sans-serif; letter-spacing:0.05em; font-size:13px; padding:12px 22px; border-radius:3px; text-transform:uppercase; transition:background .15s ease, transform .15s ease; white-space:nowrap;}
.cta-btn:hover{background:#fff; transform:translateY(-1px);}
@media (max-width:1080px){ .navlinks{display:none;} }

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
      <a href="index.html#shop"{cls('shop')}>Shop</a>
      <a href="resources.html"{cls('resources')}>Resources</a>
      <a href="index.html#contact"{cls('contact')}>Contact</a>
      <a class="donate-link" href="index.html#donate"{cls('donate')}>Donate</a>
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
      <a href="index.html#shop">Shop</a>
      <a href="resources.html">Resources</a>
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
    if(!greeted){greeted=true; add('bot',"Hi! I'm the Barrie Rugby Club assistant. Ask me about programs, practice times, registration, donations, or anything else about the club.");}}
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
    banner = ANNOUNCE_BAR if active in ANNOUNCE_PAGES else ""
    return f"""<!DOCTYPE html>
<html lang="en">
{HEAD.format(title=title, css=CSS)}
<body>
{banner}
{nav(active)}
{body}
{FOOTER}
{CHAT_WIDGET}
</body>
</html>"""

out_dir = '/mnt/user-data/outputs' if os.path.isdir('/mnt/user-data') else os.path.join(_BASE, 'out')
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
