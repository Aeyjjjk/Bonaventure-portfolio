"""Shared layout, helpers and SVG illustrations for the portfolio build."""
import html, pathlib

SRC = pathlib.Path(__file__).parent
CSS = (SRC / "site.css").read_text()
CSS += """
header.site{top:env(safe-area-inset-top,0px)}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:70;background:var(--bg)}
"""
JS = (SRC / "site.js").read_text()
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&display=swap">')

NAME = '<span class="ph">[YOUR FULL PROFESSIONAL NAME]</span>'
DOMAIN = "https://YOUR-DOMAIN.example"

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 12h16M14 6l6 6-6 6"/></svg>'
DL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>'

MONO = ('<svg width="40" height="40" viewBox="0 0 40 40" fill="none" aria-hidden="true">'
        '<path d="M2 12V2h10M28 2h10v10M38 28v10H28M12 38H2V28" stroke="#F0A45D" stroke-width="2"/>'
        '<text x="20" y="25.5" text-anchor="middle" font-family="IBM Plex Mono,monospace" font-weight="500" font-size="14" fill="#27C6B0">DF</text></svg>')

STATUS = {
    "conf": ("s-conf", "Confirmed"), "rec": ("s-rec", "Recovered"), "pot": ("s-pot", "Potential"),
    "int": ("s-int", "Interpretation"), "hyp": ("s-hyp", "Hypothesis"), "lim": ("s-lim", "Limitation"),
}

def st(k):
    c, t = STATUS[k]
    return f'<span class="status {c}">{t}</span>'

LEGEND = ('<div class="legend" role="note" aria-label="Evidence status key">'
          + st("conf") + 'verified directly in the investigation output'
          + st("rec") + 'artefact recovered from the evidence'
          + st("pot") + 'present but not shown to be user-initiated'
          + st("int") + 'analytical reading'
          + st("hyp") + 'working idea, untested'
          + st("lim") + 'constraint on what can be claimed</div>')

def esc(s):
    return html.escape(s, quote=True)

def nav(prefix, current=None):
    p = prefix
    items = [("Home", p + "#top" if p else "#top"), ("About", p + "#about"), ("Investigations", p + "#investigations"),
             ("Skills", p + "#skills"), ("Contact", p + "#contact")]
    li = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in items)
    li += f'<li class="cv-m"><a href="assets/downloads/CV.pdf" target="_blank" rel="noopener">Download CV</a></li>'
    home = (p or "") + "#top" if p else "#top"
    return f'''<a class="skip" href="#main">Skip to content</a><div class="progress" aria-hidden="true"></div>
<header class="site"><div class="wrap nav">
<a class="brand" href="{p + '#top' if p else '#top'}" aria-label="Digital Forensics and Cyber Investigations, home">{MONO}<span><b>Digital Forensics</b><i>&amp; Cyber Investigations</i></span></a>
<ul id="navlist">{li}</ul>
<a class="btn sm cv" href="assets/downloads/CV.pdf" target="_blank" rel="noopener">{DL}Download CV</a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="navlist" aria-label="Menu"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h18M3 12h18M3 17h18"/></svg></button>
</div></header>'''

PROJECTS = [
    ("alexa-iot-forensics.html", "Amazon Alexa IoT Forensics"),
    ("raid-windows-forensics.html", "RAID Reconstruction & Windows Forensics"),
    ("snapchat-mobile-forensics.html", "Snapchat Mobile Forensics"),
    ("uc-browser-forensics.html", "UC Browser Forensics"),
]

def footer(prefix):
    p = prefix
    pl = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in PROJECTS)
    return f'''<footer class="site"><div class="wrap">
<div class="foot">
<div class="about-f"><p class="big">{NAME}</p><p style="color:var(--fg2);margin:8px 0 0">Digital Forensics &amp; Cyber Investigations.</p>
<p style="color:var(--fg2);font-size:14px;margin-top:18px">Academic forensic case studies. Scenarios are simulations built for research and assessment, not live prosecutions.</p></div>
<div class="col"><h4>Navigate</h4><ul><li><a href="{p}#about">About</a></li><li><a href="{p}#investigations">Investigations</a></li><li><a href="{p}#skills">Skills</a></li><li><a href="{p}#contact">Contact</a></li></ul></div>
<div class="col"><h4>Investigations</h4><ul>{pl}</ul></div>
<div class="col"><h4>Contact</h4><ul><li><span class="ph">[PROFESSIONAL EMAIL]</span></li><li><a href="#" data-soon="LinkedIn link not set yet. Replace [LINKEDIN URL] in the source.">LinkedIn</a></li><li><a href="#" data-soon="GitHub link not set yet. Replace [GITHUB URL] in the source.">GitHub</a></li><li><a href="assets/downloads/CV.pdf" target="_blank" rel="noopener">Download CV</a></li></ul></div>
</div>
<div class="foot-bot"><span>&copy; <span class="yr">2026</span> {NAME}</span><em>Investigate. Analyse. Understand.</em></div>
</div></footer><div class="toast" role="status" aria-live="polite"></div>'''

YEAR_JS = "document.querySelectorAll('.yr').forEach(function(e){e.textContent=new Date().getFullYear()});"

def head_meta(title, desc, page, og="assets/img/og.png"):
    return (f'<title>{esc(title)}</title>\n<meta name="description" content="{esc(desc)}">\n'
            f'<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">'
            f'<meta property="og:type" content="website"><meta property="og:image" content="{DOMAIN}/{og}">'
            f'<meta property="og:url" content="{DOMAIN}/{page}"><meta name="twitter:card" content="summary_large_image">'
            f'<link rel="canonical" href="{DOMAIN}/{page}"><meta name="theme-color" content="#0B1020">')

def full_page(title, desc, page, body, prefix="index.html"):
    """A complete HTML document (used for case studies and the hosted index)."""
    return (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            f'{head_meta(title, desc, page)}\n{FONTS}\n<style>{CSS}</style></head><body>\n'
            f'{nav(prefix)}<main id="main">{body}</main>{footer(prefix)}\n<script>{JS}\n{YEAR_JS}</script></body></html>')

def fragment_page(title, desc, page, body):
    """The artifact host wraps this in its own skeleton, so no html/head/body tags."""
    return (f'{head_meta(title, desc, page)}\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n'
            f'<style>{CSS}</style>\n{nav("")}<main id="main">{body}</main>{footer("")}\n<script>{JS}\n{YEAR_JS}</script>')

# ---------- case-study helpers ----------
def shot(img, label, cap, alt, w=None):
    src = f"assets/img/{img}.webp"
    return (f'<figure class="shot"><button type="button" data-lb="{src}" data-alt="{esc(alt)}" data-cap="{esc(label + ". " + cap)}">'
            f'<img src="{src}" alt="{esc(alt)}" loading="lazy" decoding="async"></button>'
            f'<figcaption><b>{esc(label)}</b>{esc(cap)}</figcaption></figure>')

def gallery(items, wide=False):
    return f'<div class="gallery{" wide" if wide else ""}">' + "".join(shot(*i) for i in items) + "</div>"

def panel(label, ref, inner, cap="", recon=False):
    c = f'<div class="cap{" reconstruction" if recon else ""}">{cap}</div>' if cap else ""
    return f'<figure class="panel" style="margin-inline:0"><div class="ph-bar"><span>{label}</span><b>{ref}</b></div><div class="pb">{inner}</div>{c}</figure>'

def kv(pairs):
    return '<dl class="kv">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in pairs) + "</dl>"

def flow(steps):
    return '<ol class="flow">' + "".join(f"<li><b>{t}</b>{d}</li>" for t, d in steps) + "</ol>"

def stats(items):
    return '<div class="stats">' + "".join(f'<div class="{c}"><b>{n}</b><span>{l}</span></div>' for n, l, c in items) + "</div>"

def findings(rows):
    return '<ul class="findlist">' + "".join(f"<li>{st(k)}<span>{t}</span></li>" for k, t in rows) + "</ul>"

def details(summary, body):
    return f'<details class="x"><summary>{summary}</summary><div class="xb">{body}</div></details>'

def table(head, rows, cls=None):
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in head)
    out = ""
    for r in rows:
        tds = ""
        for i, c in enumerate(r):
            k = ""
            if isinstance(c, tuple):
                c, k = c
            tds += f'<td class="{k}">{c}</td>'
        out += f"<tr>{tds}</tr>"
    return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{out}</tbody></table></div>'

def case_page(slug, title, short, desc, eyebrow, sub, badges, hero_html, sections, idx):
    toc = "".join(f'<li><a href="#{s[0]}"><span>{i + 1:02d}</span>{s[1]}</a></li>' for i, s in enumerate(sections))
    secs = ""
    for i, (sid, stitle, shtml) in enumerate(sections):
        secs += (f'<section class="cs-sec" id="{sid}" aria-labelledby="{sid}-h"><header><span class="label t">{i + 1:02d}</span>'
                 f'<h2 id="{sid}-h">{stitle}</h2></header>{shtml}</section>')
    prev = PROJECTS[(idx - 1) % 4]; nxt = PROJECTS[(idx + 1) % 4]
    body = f'''<div class="cs-hero grid-fade"><div class="wrap">
<div class="crumbs label"><a href="index.html#investigations">Investigations</a><span>/</span><span class="a">{eyebrow}</span></div>
<div class="cs-hero-grid"><div><h1>{title}</h1><p class="sub">{sub}</p><div class="badge-row">{badges}</div></div><div>{hero_html}</div></div>
</div></div>
<div class="wrap cs"><nav class="toc" aria-label="Case study sections"><ol>{toc}</ol></nav><div>{secs}
<nav class="next" aria-label="Case study navigation"><a href="{prev[0]}"><span class="label">&larr; Previous investigation</span><b>{prev[1]}</b></a><a href="{nxt[0]}"><span class="label">Next investigation &rarr;</span><b>{nxt[1]}</b></a></nav>
</div></div>'''
    return slug, short, desc, body
