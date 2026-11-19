"""Build the static portfolio.  Run:  python3 build.py
Outputs ../dist (hosted site) and ../artifact_index.html (fragment used for the Claude artifact publish)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import *
import home, cases

ROOT = pathlib.Path(__file__).parent.parent
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

T_HOME = "Digital Forensics & Cyber Investigations Portfolio"
D_HOME = ("Digital forensics portfolio: computer, Windows, mobile, browser, IoT and cloud investigations using Magnet AXIOM, "
          "Cellebrite, X-Ways and Python. Academic forensic case studies.")
body = home.home_body()
(DIST / "index.html").write_text(full_page(T_HOME, D_HOME, "index.html", body, prefix=""))
(ROOT / "artifact_index.html").write_text(fragment_page(T_HOME, D_HOME, "index.html", body))

pages = ["index.html"]
for fn in cases.ALL:
    slug, short, desc, b = fn()
    (DIST / f"{slug}.html").write_text(full_page(f"{short} | Digital Forensics Portfolio", desc, f"{slug}.html", b))
    pages.append(f"{slug}.html")

(DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"<url><loc>{DOMAIN}/{p if p != 'index.html' else ''}</loc></url>\n" for p in pages) + "</urlset>\n")
(DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print("built", pages)
