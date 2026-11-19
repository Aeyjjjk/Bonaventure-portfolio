"""Builds assets/downloads/CV.pdf and assets/img/og.png with Chromium (Playwright)."""
import pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent.parent
OUT = ROOT / "dist" / "assets"

CV = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CV | Digital Forensics &amp; Cyber Investigations</title>
<style>
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font:400 9.6pt/1.5 Inter,'Helvetica Neue',Arial,sans-serif;color:#1a2233;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;padding:14mm 16mm 12mm;position:relative;overflow:hidden;page-break-after:always}
.page:last-child{page-break-after:auto}
.top{background:#0B1020;color:#F4F5F7;margin:-14mm -16mm 8mm;padding:13mm 16mm 9mm;border-bottom:3px solid #27C6B0}
h1{font:700 22pt/1.1 Inter,sans-serif;margin:0 0 3px;letter-spacing:-.01em}
.role{font:500 9pt/1.4 'DejaVu Sans Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#27C6B0}
.contact{margin-top:8px;font:400 8.6pt/1.5 'DejaVu Sans Mono',monospace;color:#A5AFBF}
.ph{color:#F0A45D}
.ph.d{color:#b8680f}
h2{font:600 8.4pt/1 'DejaVu Sans Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:#0e8a7a;margin:0 0 7px;padding-bottom:5px;border-bottom:1px solid #d5dbe5}
section{margin-bottom:9mm}
p{margin:0 0 5px}
.row{display:flex;justify-content:space-between;gap:10px;align-items:baseline}
.row b{font-weight:600;font-size:10.2pt}
.row span{font:400 8.3pt/1.4 'DejaVu Sans Mono',monospace;color:#5b6678;white-space:nowrap}
.sub{color:#5b6678;font-size:9pt;margin-bottom:3px}
ul{margin:3px 0 7px;padding-left:15px}li{margin:1.6px 0}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:6mm 9mm}
.tag{display:inline-block;font:500 7.6pt/1 'DejaVu Sans Mono',monospace;border:1px solid #c9d1dd;padding:3px 5px;margin:0 3px 4px 0;color:#2a3548}
.note{font-size:8.2pt;color:#5b6678;border-left:2px solid #F0A45D;padding-left:8px;margin-top:6px}
.foot{position:absolute;left:16mm;right:16mm;bottom:8mm;display:flex;justify-content:space-between;font:400 7.6pt 'DejaVu Sans Mono',monospace;color:#8a94a6}
</style></head><body>

<div class="page">
<div class="top"><h1><span class="ph">[YOUR FULL PROFESSIONAL NAME]</span></h1>
<div class="role">Digital Forensics &amp; Cyber Investigations</div>
<div class="contact"><span class="ph">[PROFESSIONAL EMAIL]</span> &nbsp;·&nbsp; <span class="ph">[LINKEDIN URL]</span> &nbsp;·&nbsp; <span class="ph">[GITHUB URL]</span> &nbsp;·&nbsp; <span class="ph">[LOCATION]</span></div></div>

<section><h2>Profile</h2>
<p>Digital forensics postgraduate with practical academic investigation experience across computer, mobile, browser and IoT forensics. Work to date covers evidence acquisition, artefact examination, cross-tool verification and clear reporting of findings and limitations. Previous career in electrical engineering, including fault diagnosis and technical reporting on high-voltage transmission systems.</p></section>

<section><h2>Education</h2>
<div class="row"><b>MSc Digital Forensics and Cyber Investigations</b><span>Sept 2024 – present</span></div><div class="sub">Teesside University, Middlesbrough</div>
<div class="row" style="margin-top:6px"><b>BEng Electrical/Electronics</b><span>2017 – 2022</span></div><div class="sub">Afe Babalola University, Ado-Ekiti, Nigeria</div></section>

<section><h2>Forensic projects (academic case studies)</h2>
<div class="row"><b>Forensic investigation of Amazon Alexa-enabled IoT devices</b><span>MSc research project</span></div>
<ul><li>Acquired cloud-hosted evidence from an Echo Dot and an Echo Show through an Amazon GDPR Subject Access Request, then analysed it in Python (Google Colaboratory) and cross-checked it in Magnet AXIOM.</li>
<li>Found that the Echo Dot held human-behaviour artefacts (voice utterances, Drop-In logs, music history, temperature readings) and the Echo Show held device telemetry, including a 16-second connectivity anomaly. Cross-device analysis gave a fuller picture than either device alone.</li>
<li>Reported limitations: limited data scope, no hash verification and no standardised tooling for Amazon GDPR data.</li></ul>

<div class="row"><b>RAID reconstruction and Windows digital forensics</b><span>Advanced Forensic Computing</span></div>
<ul><li>Rebuilt four disk images (BEF2-1 to BEF2-4) into one image in X-Ways using the JBOD/Linear option.</li>
<li>Examined registry hives, shellbags, jump lists, LNK files and the Recycle Bin, validated key artefacts in hexadecimal, and compared SHA-256 values for nine recovered images.</li></ul>

<div class="row"><b>Snapchat mobile application forensics</b><span>Advanced Mobile Forensics</span></div>
<ul><li>Compared Snapchat artefacts on a Samsung Galaxy S20+ and an iPhone with Cellebrite Physical Analyzer. Android held Memories, My Eyes Only and Journal databases. iOS gave more device-level metadata.</li>
<li>Recorded hash values before and after examination, with no change.</li></ul>

<div class="row"><b>Browser forensics of UC Browser</b><span>Internet forensics</span></div>
<ul><li>Built a Windows 10 VirtualBox lab (8 GB RAM, 4 cores, 30 GB disk), ran normal and incognito sessions, imaged with FTK Imager and examined with X-Ways, DB Browser for SQLite and Magnet AXIOM.</li>
<li>Separated recovered artefacts (12 cookie results) from potential browser activity (323 items) among 89,345 items analysed.</li></ul></section>
<div class="foot"><span>Curriculum vitae</span><span>1 / 2</span></div></div>

<div class="page">
<section><h2>Technical skills</h2>
<div class="grid">
<div><p style="font-weight:600;margin-bottom:4px">Computer forensics</p><span class="tag">X-Ways Forensics</span><span class="tag">Magnet AXIOM</span><span class="tag">FTK Imager</span><span class="tag">Windows Registry Recovery</span><span class="tag">RegRipper</span><span class="tag">MFT Stampede</span></div>
<div><p style="font-weight:600;margin-bottom:4px">Mobile forensics</p><span class="tag">Cellebrite Physical Analyzer</span><span class="tag">Magnet AXIOM</span><span class="tag">Android artefacts</span><span class="tag">iOS artefacts</span></div>
<div><p style="font-weight:600;margin-bottom:4px">Browser and internet forensics</p><span class="tag">SQLite</span><span class="tag">DB Browser for SQLite</span><span class="tag">History, cache and cookie analysis</span></div>
<div><p style="font-weight:600;margin-bottom:4px">IoT and cloud forensics</p><span class="tag">Amazon GDPR SAR</span><span class="tag">Alexa artefact analysis</span><span class="tag">Python</span><span class="tag">Google Colaboratory</span></div></div>
<p style="font-weight:600;margin:8px 0 4px">Methods</p><span class="tag">Disk imaging</span><span class="tag">Evidence preservation</span><span class="tag">Hash verification</span><span class="tag">RAID reconstruction</span><span class="tag">Registry examination</span><span class="tag">Database analysis</span><span class="tag">Timeline reconstruction</span><span class="tag">Artefact correlation</span><span class="tag">Data visualisation</span>
<p class="note">Tools are listed where they were used in the projects above. No proficiency levels are claimed.</p></section>

<section><h2>Previous experience</h2>
<div class="row"><b>Transmission Company of Nigeria</b><span>Dec 2022 – Jun 2024</span></div><div class="sub">Role: <span class="ph d">[JOB TITLE]</span> · High-voltage transmission</div>
<ul><li>Diagnosed faults on transmission lines and transformers using grounding cables, thermal cameras and fault locators.</li>
<li>Wrote detailed technical reports on maintenance and repairs, documenting what was done and why.</li>
<li>Contributed to planning and execution of new transmission line projects, including budgeting and scheduling, and to site surveys and equipment selection.</li>
<li>Carried out routine maintenance checks and enforced safety regulations and protective equipment use on site.</li></ul>
<div class="row"><b>Vitek Engineering Company</b><span>Dec 2019 – Nov 2022</span></div><div class="sub">Role: <span class="ph d">[JOB TITLE]</span> · Electrical installations</div>
<ul><li>Worked with contractors and senior engineers to plan and carry out electrical installations safely and on schedule.</li>
<li>Assisted on residential wiring projects and gained hands-on experience installing, maintaining and repairing electrical systems, including a 500 kVA transformer.</li></ul></section>

<section><h2>Memberships</h2><p>Nigerian Society of Engineers (NSE) · International Association of Engineers (IAENG)</p></section>
<section><h2>References</h2><p>Available on request.</p></section>
<div class="foot"><span>Curriculum vitae</span><span>2 / 2</span></div></div>
</body></html>"""

OG = """<!doctype html><html><head><meta charset="utf-8"><style>
body{margin:0;width:1200px;height:630px;background:#0B1020;color:#F4F5F7;font-family:Inter,sans-serif;position:relative;overflow:hidden}
.g{position:absolute;inset:0;background-image:linear-gradient(#1D2B40 1px,transparent 1px),linear-gradient(90deg,#1D2B40 1px,transparent 1px);background-size:56px 56px;opacity:.7}
.c{position:absolute;left:72px;right:72px;top:72px;bottom:72px;border:1px solid #26344B}
h1{position:absolute;left:112px;top:190px;margin:0;font:700 88px/0.98 Inter,sans-serif;letter-spacing:-.03em;text-transform:uppercase}
h1 em{font-style:normal;color:#27C6B0}
.l{position:absolute;left:112px;top:120px;font:500 20px 'DejaVu Sans Mono',monospace;letter-spacing:.16em;color:#27C6B0;text-transform:uppercase}
.f{position:absolute;left:112px;bottom:112px;font:500 22px 'DejaVu Sans Mono',monospace;color:#F0A45D;letter-spacing:.1em}
</style></head><body><div class="g"></div><div class="c"></div><div class="l">Digital Forensics &amp; Cyber Investigations</div>
<h1>Digital evidence.<br><em>Beyond the surface.</em></h1><div class="f">Investigate. Analyse. Understand.</div></body></html>"""

(OUT / "downloads").mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.set_content(CV)
    pg.pdf(path=str(OUT / "downloads" / "CV.pdf"), format="A4", print_background=True, prefer_css_page_size=True)
    pg2 = b.new_page(viewport={"width": 1200, "height": 630})
    pg2.set_content(OG)
    pg2.screenshot(path=str(OUT / "img" / "og.png"))
    b.close()
print("ok")
