"""Builds the three role CVs (assets/downloads/CV-*.pdf) and assets/img/og.png with Chromium (Playwright)."""
import pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent.parent
OUT = ROOT / "dist" / "assets"
CSS = "<style>\n@page{size:A4;margin:0}\n*{box-sizing:border-box}\nbody{margin:0;font:400 9.6pt/1.5 Inter,'Helvetica Neue',Arial,sans-serif;color:#1a2233;-webkit-print-color-adjust:exact;print-color-adjust:exact}\n.page{width:210mm;height:297mm;padding:14mm 16mm 12mm;position:relative;overflow:hidden;page-break-after:always}\n.page:last-child{page-break-after:auto}\n.top{background:#0B1020;color:#F4F5F7;margin:-14mm -16mm 8mm;padding:13mm 16mm 9mm;border-bottom:3px solid #27C6B0}\nh1{font:700 22pt/1.1 Inter,sans-serif;margin:0 0 3px;letter-spacing:-.01em}\n.role{font:500 9pt/1.4 'DejaVu Sans Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#27C6B0}\n.contact{margin-top:8px;font:400 8.6pt/1.5 'DejaVu Sans Mono',monospace;color:#A5AFBF}\n.ph{color:#F0A45D}\n.ph.d{color:#b8680f}\nh2{font:600 8.4pt/1 'DejaVu Sans Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:#0e8a7a;margin:0 0 7px;padding-bottom:5px;border-bottom:1px solid #d5dbe5}\nsection{margin-bottom:9mm}\np{margin:0 0 5px}\n.row{display:flex;justify-content:space-between;gap:10px;align-items:baseline}\n.row b{font-weight:600;font-size:10.2pt}\n.row span{font:400 8.3pt/1.4 'DejaVu Sans Mono',monospace;color:#5b6678;white-space:nowrap}\n.sub{color:#5b6678;font-size:9pt;margin-bottom:3px}\nul{margin:3px 0 7px;padding-left:15px}li{margin:1.6px 0}\n.grid{display:grid;grid-template-columns:1fr 1fr;gap:6mm 9mm}\n.tag{display:inline-block;font:500 7.6pt/1 'DejaVu Sans Mono',monospace;border:1px solid #c9d1dd;padding:3px 5px;margin:0 3px 4px 0;color:#2a3548}\n.note{font-size:8.2pt;color:#5b6678;border-left:2px solid #F0A45D;padding-left:8px;margin-top:6px}\n.foot{position:absolute;left:16mm;right:16mm;bottom:8mm;display:flex;justify-content:space-between;font:400 7.6pt 'DejaVu Sans Mono',monospace;color:#8a94a6}\n</style>"
FORENSIC_PROJ = '<div class="row"><b>Forensic investigation of Amazon Alexa-enabled IoT devices</b><span>MSc research project</span></div>\n<ul><li>Acquired cloud-hosted evidence from an Echo Dot and an Echo Show through an Amazon GDPR Subject Access Request, then analysed it in Python (Google Colaboratory) and cross-checked it in Magnet AXIOM.</li>\n<li>Found that the Echo Dot held human-behaviour artefacts (voice utterances, Drop-In logs, music history, temperature readings) and the Echo Show held device telemetry, including a 16-second connectivity anomaly. Cross-device analysis gave a fuller picture than either device alone.</li>\n<li>Reported limitations: limited data scope, no hash verification and no standardised tooling for Amazon GDPR data.</li></ul>\n\n<div class="row"><b>RAID reconstruction and Windows digital forensics</b><span>Advanced Forensic Computing</span></div>\n<ul><li>Rebuilt four disk images (BEF2-1 to BEF2-4) into one image in X-Ways using the JBOD/Linear option.</li>\n<li>Examined registry hives, shellbags, jump lists, LNK files and the Recycle Bin, validated key artefacts in hexadecimal, and compared SHA-256 values for nine recovered images.</li></ul>\n\n<div class="row"><b>Snapchat mobile application forensics</b><span>Advanced Mobile Forensics</span></div>\n<ul><li>Compared Snapchat artefacts on a Samsung Galaxy S20+ and an iPhone with Cellebrite Physical Analyzer. Android held Memories, My Eyes Only and Journal databases. iOS gave more device-level metadata.</li>\n<li>Recorded hash values before and after examination, with no change.</li></ul>\n\n<div class="row"><b>Browser forensics of UC Browser</b><span>Internet forensics</span></div>\n<ul><li>Built a Windows 10 VirtualBox lab (8 GB RAM, 4 cores, 30 GB disk), ran normal and incognito sessions, imaged with FTK Imager and examined with X-Ways, DB Browser for SQLite and Magnet AXIOM.</li>\n<li>Separated recovered artefacts (12 cookie results) from potential browser activity (323 items) among 89,345 items analysed.</li></ul>'
SKILLS_F = '<section><h2>Technical skills</h2>\n<div class="grid">\n<div><p style="font-weight:600;margin-bottom:4px">Computer forensics</p><span class="tag">X-Ways Forensics</span><span class="tag">Magnet AXIOM</span><span class="tag">FTK Imager</span><span class="tag">Windows Registry Recovery</span><span class="tag">RegRipper</span><span class="tag">MFT Stampede</span></div>\n<div><p style="font-weight:600;margin-bottom:4px">Mobile forensics</p><span class="tag">Cellebrite Physical Analyzer</span><span class="tag">Magnet AXIOM</span><span class="tag">Android artefacts</span><span class="tag">iOS artefacts</span></div>\n<div><p style="font-weight:600;margin-bottom:4px">Browser and internet forensics</p><span class="tag">SQLite</span><span class="tag">DB Browser for SQLite</span><span class="tag">History, cache and cookie analysis</span></div>\n<div><p style="font-weight:600;margin-bottom:4px">IoT and cloud forensics</p><span class="tag">Amazon GDPR SAR</span><span class="tag">Alexa artefact analysis</span><span class="tag">Python</span><span class="tag">Google Colaboratory</span></div></div>\n<p style="font-weight:600;margin:8px 0 4px">Methods</p><span class="tag">Disk imaging</span><span class="tag">Evidence preservation</span><span class="tag">Hash verification</span><span class="tag">RAID reconstruction</span><span class="tag">Registry examination</span><span class="tag">Database analysis</span><span class="tag">Timeline reconstruction</span><span class="tag">Artefact correlation</span><span class="tag">Data visualisation</span>\n<p class="note">Tools are listed where they were used in the projects above. No proficiency levels are claimed.</p></section>\n\n'
PREV = '<section><h2>Previous experience</h2>\n<div class="row"><b>Transmission Company of Nigeria</b><span>Dec 2022 – Jun 2024</span></div><div class="sub">Role: <span class="ph d">[JOB TITLE]</span> · High-voltage transmission</div>\n<ul><li>Diagnosed faults on transmission lines and transformers using grounding cables, thermal cameras and fault locators.</li>\n<li>Wrote detailed technical reports on maintenance and repairs, documenting what was done and why.</li>\n<li>Contributed to planning and execution of new transmission line projects, including budgeting and scheduling, and to site surveys and equipment selection.</li>\n<li>Carried out routine maintenance checks and enforced safety regulations and protective equipment use on site.</li></ul>\n<div class="row"><b>Vitek Engineering Company</b><span>Dec 2019 – Nov 2022</span></div><div class="sub">Role: <span class="ph d">[JOB TITLE]</span> · Electrical installations</div>\n<ul><li>Worked with contractors and senior engineers to plan and carry out electrical installations safely and on schedule.</li>\n<li>Assisted on residential wiring projects and gained hands-on experience installing, maintaining and repairing electrical systems, including a 500 kVA transformer.</li></ul></section>\n\n'

EDU_MSC = '<div class="row"><b>MSc Digital Forensics and Cyber Investigations</b><span>Sept 2024 – present</span></div><div class="sub">Teesside University, Middlesbrough</div>'
EDU_BENG = '<div class="row" style="margin-top:6px"><b>BEng Electrical/Electronics</b><span>2017 – 2022</span></div><div class="sub">Afe Babalola University, Ado-Ekiti, Nigeria</div>'

def top(role_line):
    return ('<div class="top"><h1><span class="ph">[YOUR FULL PROFESSIONAL NAME]</span></h1>'
            f'<div class="role">{role_line}</div>'
            '<div class="contact"><span class="ph">[PROFESSIONAL EMAIL]</span> &nbsp;·&nbsp; <span class="ph">[LINKEDIN URL]</span> &nbsp;·&nbsp; <span class="ph">[GITHUB URL]</span> &nbsp;·&nbsp; <span class="ph">[LOCATION]</span></div></div>')

def foot(n, t): return f'<div class="foot"><span>Curriculum vitae</span><span>{n} / {t}</span></div>'

SOC_PROJ = """<div class="row"><b>DarkSide ransomware threat profile</b><span>CTI training exercise · draft v1.0</span></div>
<ul><li>Profiled a 32-bit Windows DLL (54 of 62 engines detect it as DarkSide) from VirusTotal metadata, sandbox data and published reporting, with High confidence in the classification and Moderate overall confidence.</li>
<li>Mapped behaviour to MITRE ATT&amp;CK, keeping rows evidenced by the sample apart from rows taken from published reports. Wrote a structural YARA rule, tabulated defanged indicators and made six prioritised recommendations.</li>
<li>Listed unfinished items openly: MISP search, MalwareBazaar check and YARA test results.</li></ul>
<div class="row"><b>Remediating nginx 1.15.5 with Ansible</b><span>Vulnerability management lab</span></div>
<ul><li>Upgraded a source-built nginx to 1.30.4 with a playbook that checks the version, was syntax-checked and dry-run first, and finished with ok=19, changed=5, failed=0.</li>
<li>Wrote and ran a rollback playbook that restores a backup, and verified the result with nginx -v, curl headers and an OpenVAS re-scan.</li>
<li>Traced the remaining 9.8 (Critical) result to Apache Tomcat (Ghostcat) on another port, outside the assigned scope.</li></ul>
<div class="row"><b>Invoice fraud phishing analysis</b><span>SOC case-study exercise</span></div>
<ul><li>Triaged a suspected business email compromise message: a private originating IP, SPF fail, no DKIM, DMARC fail, three sender identities, two credential-harvesting links, a tracking pixel and an HTML attachment presented as a PDF.</li>
<li>Extracted and defanged indicators, hashed the attachment, and recommended payment, email-security, attachment, training and response controls.</li>
<li>Noted that the headers do not confirm what the gateway did, so the message trace needs checking.</li></ul>"""

SKILLS_S = """<section><h2>Technical skills</h2><div class="grid">
<div><p style="font-weight:600;margin-bottom:4px">Threat intelligence</p><span class="tag">VirusTotal (GUI and API)</span><span class="tag">MITRE ATT&amp;CK</span><span class="tag">YARA</span><span class="tag">IOC handling</span><span class="tag">Confidence language</span></div>
<div><p style="font-weight:600;margin-bottom:4px">Email and phishing analysis</p><span class="tag">Raw .eml headers</span><span class="tag">SPF / DKIM / DMARC</span><span class="tag">MIME and base64</span><span class="tag">SHA-256</span></div>
<div><p style="font-weight:600;margin-bottom:4px">Vulnerability management</p><span class="tag">OpenVAS / Greenbone</span><span class="tag">Ansible</span><span class="tag">nginx</span><span class="tag">Rollback planning</span></div>
<div><p style="font-weight:600;margin-bottom:4px">Digital forensics (MSc)</p><span class="tag">Magnet AXIOM</span><span class="tag">X-Ways</span><span class="tag">Cellebrite</span><span class="tag">Python</span></div></div>
<p class="note">Tools are listed where they were used in the projects above. No proficiency levels are claimed.</p></section>"""

EL_EXP = """<section><h2>Work experience</h2>
<div class="row"><b>Transmission Company of Nigeria</b><span>Dec 2022 – Jun 2024</span></div><div class="sub">Role: <span class="ph d">[JOB TITLE]</span> · High-voltage transmission</div>
<ul><li>Design and installation of new transmission lines: worked with engineering teams, helped select materials and equipment, and contributed to site surveys that found the best routes.</li>
<li>Fault diagnosis and repairs: diagnosed faults on transmission lines and transformers with grounding cables, thermal cameras and fault locators, and helped restore power in high-pressure situations.</li>
<li>Technical reports: wrote detailed reports on maintenance and repairs, documenting what was done and why.</li>
<li>Planning and execution: helped plan new transmission projects, from budgeting to scheduling of works.</li>
<li>Safety: made sure workers followed safety regulations and wore complete personal protective equipment on site.</li>
<li>Routine maintenance checks on high-voltage transmission lines and transformers to catch problems before they became disruptions.</li></ul>
<div class="row"><b>Vitek Engineering Company</b><span>Dec 2019 – Nov 2022</span></div><div class="sub">Role: <span class="ph d">[JOB TITLE]</span> · Electrical installations</div>
<ul><li>Worked with contractors and senior engineers to plan and carry out electrical installations safely and on schedule.</li>
<li>Assisted a licensed electrical company with residential wiring projects, making sure systems were functional and up to code.</li>
<li>Gained hands-on experience installing, maintaining and repairing electrical systems, including a 500 kVA transformer.</li></ul></section>"""

EL_SKILLS = """<section><h2>Key skills</h2><div class="grid">
<div><p style="font-weight:600;margin-bottom:4px">Electrical work</p><span class="tag">Wiring, installations and repairs</span><span class="tag">Electrical systems and codes</span><span class="tag">High-voltage lines and transformers</span></div>
<div><p style="font-weight:600;margin-bottom:4px">Diagnostics and tools</p><span class="tag">Troubleshooting</span><span class="tag">Fault locators</span><span class="tag">Thermal cameras</span><span class="tag">Power tools and testing equipment</span></div>
<div><p style="font-weight:600;margin-bottom:4px">Delivery</p><span class="tag">Technical reporting</span><span class="tag">Budgeting and scheduling</span><span class="tag">Safety compliance</span></div>
<div><p style="font-weight:600;margin-bottom:4px">Working style</p><span class="tag">Communication</span><span class="tag">Teamwork</span></div></div></section>"""

MEM = '<section><h2>Memberships</h2><p>Nigerian Society of Engineers (NSE) · International Association of Engineers (IAENG)</p></section><section><h2>References</h2><p>Available on request.</p></section>'

def doc(pages): return '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CV</title>' + CSS + '</head><body>' + pages + '</body></html>'

CVS = {}
CVS["digital-forensics"] = doc(
 '<div class="page">' + top("Digital Forensics &amp; Cyber Investigations") +
 '<section><h2>Profile</h2><p>Digital forensics postgraduate with practical academic investigation experience across computer, mobile, browser and IoT forensics. Work to date covers evidence acquisition, artefact examination, cross-tool verification and clear reporting of findings and limitations. Previous career in electrical engineering, including fault diagnosis and technical reporting on high-voltage transmission systems.</p></section>'
 '<section><h2>Education</h2>' + EDU_MSC + EDU_BENG + '</section><section><h2>Forensic projects (academic case studies)</h2>' + FORENSIC_PROJ + '</section>' + foot(1, 2) + '</div>'
 '<div class="page">' + SKILLS_F + PREV + MEM + foot(2, 2) + '</div>')
CVS["soc-analyst"] = doc(
 '<div class="page">' + top("SOC Analyst · Threat Intelligence &amp; Vulnerability Management") +
 '<section><h2>Profile</h2><p>Digital forensics postgraduate building a SOC analyst profile through three training projects: a ransomware threat profile, an invoice-fraud email triage and a vulnerability fix with a tested rollback. Each project states its confidence, separates observed evidence from reported intelligence and lists open items. Previous career in high-voltage electrical engineering, including fault diagnosis and written technical reporting.</p></section>'
 '<section><h2>Education</h2>' + EDU_MSC + EDU_BENG + '</section><section><h2>SOC projects (training exercises)</h2>' + SOC_PROJ + '</section>' + foot(1, 2) + '</div>'
 '<div class="page">' + SKILLS_S + PREV.replace("Previous experience", "Previous experience") + MEM + foot(2, 2) + '</div>')
CVS["electrical-engineering"] = doc(
 '<div class="page">' + top("Electrical Engineering · High-voltage Systems") +
 '<section><h2>Career objective</h2><p>Meticulous electrical engineer with over three years of experience in high-voltage electrical systems, seeking to expand technical expertise and gain international experience in problem-solving in an electrician role. Committed to high-quality work while ensuring safety and compliance with regulations. Also studying Digital Forensics and Cyber Investigations.</p></section>'
 + EL_EXP + foot(1, 2) + '</div>'
 '<div class="page">' + EL_SKILLS + '<section><h2>Education</h2>' + EDU_BENG.replace(' style="margin-top:6px"', '') + EDU_MSC + '</section>' + MEM + foot(2, 2) + '</div>')

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
    for k, h in CVS.items():
        pg = b.new_page()
        pg.set_content(h)
        pg.pdf(path=str(OUT / "downloads" / f"CV-{k}.pdf"), format="A4", print_background=True, prefer_css_page_size=True)
    pg2 = b.new_page(viewport={"width": 1200, "height": 630})
    pg2.set_content(OG)
    pg2.screenshot(path=str(OUT / "img" / "og.png"))
    b.close()
print("ok")
