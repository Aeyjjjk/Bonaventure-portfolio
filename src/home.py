import json
from lib import *
import svgs

ICON = {
 "disk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="1"/><path d="M8 20h8M12 16v4"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg>',
 "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.500 0 18M12 3c-3 3.5-3 14.500 0 18"/></svg>',
 "chip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="6" y="6" width="12" height="12"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
 "cloud": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M7 18a4 4 0 010-8 5.500 5.500 0 0110.500 1.500A3.300 3.300 0 0117 18z"/></svg>',
 "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M13 2L5 14h6l-1 8 8-12h-6z"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M6 2h9l4 4v16H6zM14 2v5h5M9 12h7M9 16h7"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 2l8 3v6c0 5-3.500 9-8 11-4.500-2-8-6-8-11V5z"/><path d="M9 12l2 2 4-4"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3" y="5" width="18" height="14"/><path d="M3 6l9 7 9-7"/></svg>',
 "plan": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="4" y="4" width="16" height="16"/><path d="M4 10h16M10 4v16"/></svg>',
 "wrench": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M14 6a4 4 0 005 5l-9 9a2.500 2.500 0 01-4-4l9-9z"/></svg>',
 "lens": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="10.500" cy="10.500" r="6.500"/><path d="M16 16l5 5"/></svg>',
}

METHOD = [
 ("Identify", "Define the question and the likely sources of evidence: which devices, accounts, applications or cloud services could hold relevant data, and what the scenario allows."),
 ("Preserve", "Protect the evidence before touching it. Keep originals unaltered, record provenance, and work on copies so the original remains available for checking."),
 ("Acquire", "Collect the data through a method suited to the source: disk imaging, a full file system extraction, or an official data access request. Record hash values where the method supports them."),
 ("Examine", "Parse and locate artefacts with forensic tools, then confirm important items by hand, for example in hexadecimal or directly in the database."),
 ("Analyse", "Correlate artefacts across tools and sources, separate recovered evidence from interpretation, and test whether more than one artefact supports the same reading."),
 ("Report", "State what was found, how, and with what limits. Keep confirmed findings, potential artefacts and interpretation clearly apart."),
]

SOC_METHOD = [
 ("Triage", "Establish what the artefact is: read email headers and authentication results, or identify a file by hash and detection ratio."),
 ("Analyse", "Inspect structure and behaviour: MIME parts and attachment hashes, PE sections and entropy, and sandbox runs."),
 ("Correlate", "Map findings to known intelligence and ATT&CK, and keep what the sample shows apart from what published reports say."),
 ("Detect", "Turn findings into defanged indicators and detection logic such as a YARA rule, and record where testing is still outstanding."),
 ("Remediate", "Apply fixes in a repeatable, reversible way: a dry run first, a backup before changes and a tested rollback."),
 ("Verify and report", "Re-scan, confirm the result, and report with confidence levels, scope limits and open items."),
]


def D(roles, inner, tag="div", cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag} data-for="{roles}"{c}>{inner}</{tag}>'

def hero():
    def block(r, label, h1, lede, primary, meta):
        return D(r, f'''<p class="label t">{label}</p><h1>{h1}</h1><p class="lede">{lede}</p>
<div class="cta-row"><a class="btn" href="#investigations">{primary} {ARROW}</a>{cvlinks("btn ghost")}</div>
<div class="hero-meta">{meta}</div>''')
    copy = (block("forensics", "Digital Forensics &amp; Cyber Investigations", "Digital evidence.<br><em>Beyond the surface.</em>",
        "Exploring the intersection of digital forensics, cyber investigations and emerging connected technologies through structured investigation and evidence-led research.",
        "Explore investigations", "<span><b>04</b> investigations</span><span><b>05</b> evidence domains</span><span>Academic forensic case studies</span>")
      + block("soc", "SOC Analyst · Threat intelligence &amp; vulnerability management", "Detect. Triage.<br><em>Respond.</em>",
        "Threat profiling, phishing analysis and vulnerability remediation, written up with evidence, confidence levels and clear next steps.",
        "Explore projects", "<span><b>03</b> projects</span><span>ATT&amp;CK · YARA · OpenVAS · Ansible</span><span>Training exercises</span>")
      + block("electrical", "Electrical Engineering · High-voltage systems", "Power systems.<br><em>Built safely.</em>",
        "Electrical engineer with over three years in high-voltage transmission: design and installation, fault diagnosis, technical reporting and safety compliance.",
        "See experience", "<span><b>3+</b> years in high voltage</span><span><b>02</b> employers</span><span>BEng Electrical/Electronics</span>"))
    sil = '<svg class="sil" viewBox="0 0 120 150" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="60" cy="52" r="24"/><path d="M14 148c2-36 22-56 46-56s44 20 46 56"/></svg>'
    return f'''<section class="hero grid-fade" id="top" aria-labelledby="h1" style="padding-block:clamp(40px,6vw,88px)"><div class="wrap hero-grid">
<div class="hero-copy">
<div class="rs-wrap"><span class="label">View this portfolio as</span>{switcher("rs rs-hero")}</div>
<div class="hero-roles" id="h1" role="heading" aria-level="1">{copy}</div>
</div>
<div class="hero-vis"><div class="pscene" role="group" aria-label="Profile photograph">
<div class="pframe"><div class="pmsg">{sil}<span>Profile photo</span><small data-for="electrical">Add assets/img/profile-electrical.webp</small><small data-for="forensics">Add assets/img/profile-forensics.webp</small><small data-for="soc">Add assets/img/profile-soc.webp</small></div>
<img class="pimg" data-for="electrical" data-fb="assets/img/profile.webp" src="assets/img/profile-electrical.webp" alt="Portrait photograph, Electrical view" width="800" height="1000" decoding="async" hidden><img class="pimg" data-for="forensics" data-fb="assets/img/profile.webp" src="assets/img/profile-forensics.webp" alt="Portrait photograph, Forensics view" width="800" height="1000" decoding="async" hidden><img class="pimg" data-for="soc" data-fb="assets/img/profile.webp" src="assets/img/profile-soc.webp" alt="Portrait photograph, SOC view" width="800" height="1000" decoding="async" hidden></div>
<i class="cm a"></i><i class="cm b"></i><i class="cm c"></i><i class="cm d"></i>
<span class="tag am" data-for="forensics" style="left:6%;top:4%">Exhibit PRF-01</span><span class="tag te" data-for="forensics" style="right:6%;bottom:4%">Digital forensics</span>
<span class="tag am" data-for="soc" style="left:6%;top:4%">Case file · SOC</span><span class="tag te" data-for="soc" style="right:6%;bottom:4%">Threat &amp; vulnerability</span>
<span class="tag am" data-for="electrical" style="left:6%;top:4%">Field engineer</span><span class="tag te" data-for="electrical" style="right:6%;bottom:4%">High voltage</span>
</div></div></div></section>'''

def intro():
    def pill(items):
        return '<div class="pillars">' + "".join(f'<div><span class="label a">{a}</span><b>{b}</b><span>{c}</span></div>' for a, b, c in items) + '</div>'
    F = ('<h2 id="intro-h">Understanding the evidence behind digital activity.</h2>'
      '<div class="body"><p>This portfolio collects four practical investigations carried out as academic forensic case studies. Each starts from a question, works through acquisition and examination, and ends with what the evidence supports and where it stops.</p>'
      '<p>The work spans a seized-computer scenario with a reconstructed RAID set, a comparison of Snapchat artefacts on Android and iOS, residual traces left by a private-browsing session, and cloud-hosted evidence from Amazon Echo devices obtained through a GDPR Subject Access Request.</p>'
      '<p>Throughout, findings are labelled by how strongly the evidence supports them, and limitations are stated next to the results they affect.</p></div>'
      + pill([("Computers", "Windows &amp; disks", "RAID reconstruction, registry hives, shellbags, LNK and jump lists."), ("Mobile", "Android &amp; iOS", "Snapchat databases and device metadata across two platforms."),
              ("Browsers", "Residual traces", "History, cookies, cache and carved fragments from a private session."), ("IoT &amp; cloud", "Connected devices", "Alexa telemetry and behavioural artefacts from official data exports.")]))
    S = ('<h2>Turning alerts and artefacts into decisions.</h2>'
      '<div class="body"><p>Three training projects cover the day-to-day questions of a SOC: what is this file, is this email malicious, and did the fix actually work.</p>'
      '<p>One is a threat profile of a ransomware sample, with indicators, ATT&amp;CK mapping and a detection rule. One is the triage of an invoice-fraud email. One is a vulnerability fix on a lab server, done with a tested Ansible playbook and proved with a re-scan.</p>'
      '<p>Each states its confidence, separates what was seen from what was reported, and lists what is still open.</p></div>'
      + pill([("Intelligence", "Threat profiling", "Classification, lifecycle, indicators and ATT&amp;CK for a DarkSide DLL."), ("Email", "Phishing triage", "Headers, SPF, DKIM and DMARC, links, tracking pixel and attachment."),
              ("Vulnerabilities", "Patch and verify", "OpenVAS baseline, Ansible upgrade, rollback and re-scan."), ("Detection", "Rules and hunts", "A structural YARA rule and hunting ideas tied to observed behaviour.")]))
    E = ('<h2>Safe, reliable high-voltage systems.</h2>'
      '<div class="body"><p>Over three years of work on high-voltage transmission lines and transformers, from planning and installation to fault diagnosis and routine inspection.</p>'
      '<p>Earlier work with a contractor and senior engineers covered electrical installations and residential wiring, including hands-on experience with a 500 kVA transformer.</p>'
      '<p>Across both roles the emphasis was the same: work that meets the project need, follows safety regulations and is documented clearly.</p></div>'
      + pill([("Transmission", "Lines and sites", "Design and installation of new lines, site surveys and equipment selection."), ("Diagnostics", "Fault finding", "Grounding cables, thermal cameras and fault locators to restore service."),
              ("Reporting", "Technical reports", "Maintenance and repair work documented so others can follow it."), ("Safety", "Compliance", "Regulations followed and protective equipment worn on site.")]))
    return f'<section class="alt" aria-labelledby="intro-h"><div class="wrap">{D("forensics", F, cls="intro")}{D("soc", S, cls="intro")}{D("electrical", E, cls="intro")}</div></section>'

def projects():
    def card(cls, d, href, ref, title, cat, desc, tools, thumb, big=False):
        t = "".join(f"<span>{x}</span>" for x in tools)
        da = f' data-d="{d}"' if d else ""
        return f'''<a class="card {cls}"{da} href="{href}"><div class="thumb{'' if big else ' art'}"><span class="tag am ref">{ref}</span>{thumb}</div>
<div class="txt"><span class="cat">{cat}</span><h3>{title}</h3><p>{desc}</p><div class="tools">{t}</div><span class="view">View case study {ARROW}</span></div></a>'''
    alexa_thumb = '<div style="position:absolute;inset:0;display:grid;place-items:center;background:#0a1224"><div style="width:min(78%,560px);border:1px solid #F0A45D;position:relative"><img src="assets/img/alexa-echo-devices.webp" alt="Project photograph of an Echo Dot and an Echo Show" loading="lazy" width="629" height="481"></div></div>'
    F = f'''<div class="sec-head"><span class="label t">Selected investigations</span><h2 id="inv-h">Four investigations, one method.</h2><p>Filter by discipline. Each case study follows the same structure, from the original question to limitations.</p></div>
<div class="filters" role="group" aria-label="Filter investigations by discipline">
<button class="chip" type="button" data-f="all" aria-pressed="true">All</button><button class="chip" type="button" data-f="computer" aria-pressed="false">Computer</button><button class="chip" type="button" data-f="mobile" aria-pressed="false">Mobile</button><button class="chip" type="button" data-f="browser" aria-pressed="false">Browser</button><button class="chip" type="button" data-f="iot" aria-pressed="false">IoT &amp; cloud</button></div>
<p class="label" id="filter-status" aria-live="polite" style="margin:-8px 0 20px">4 investigations shown</p>
<div class="cards">
{card("c1","iot cloud","alexa-iot-forensics.html","ALX-01 · Flagship research","Amazon Alexa IoT Forensics","IoT Forensics / Cloud Forensics","Cloud-based evidence acquisition and artefact interpretation across an Echo Dot and an Echo Show, using Amazon's GDPR Subject Access Request. The comparison shows that cross-device analysis gives a fuller picture than either device alone.",["GDPR SAR","Python / Colab","Magnet AXIOM"],alexa_thumb,True)}
{card("c2","computer","raid-windows-forensics.html","RDW-02","Advanced Forensic Computing","Disk Forensics / Windows Artefacts / RAID Reconstruction","Four disk images rebuilt into one, then a Windows drive examined through registry hives, shellbags, LNK files and jump lists, with key items checked in hexadecimal.",["X-Ways","Magnet AXIOM","RegRipper","MFT Stampede"],svgs.raid_card())}
{card("c3","mobile","snapchat-mobile-forensics.html","SNP-03","Mobile Application Forensics","Android / iOS / Snapchat","A comparison of Snapchat artefacts on a Samsung Galaxy S20+ and an iPhone, with hash checks before and after examination.",["Cellebrite Physical Analyzer","Magnet AXIOM"],svgs.snap_card())}
{card("c4","browser","uc-browser-forensics.html","UCB-04","UC Browser Forensics","Internet Forensics / Browser Artefacts","Normal and incognito browsing in a controlled Windows 10 virtual machine, then imaged and examined for history, cookies, cache and carved fragments.",["FTK Imager","X-Ways","DB Browser for SQLite","Magnet AXIOM"],svgs.uc_card())}
</div>'''
    S = f'''<div class="sec-head"><span class="label t">Selected projects</span><h2>Three projects, one habit: show the evidence.</h2><p>Training exercises in threat intelligence, email analysis and vulnerability management. Each lists its limits and open items.</p></div>
<div class="cards">
{card("c2","","darkside-threat-profile.html","SOC-01","DarkSide Ransomware Threat Profile","Threat Intelligence / Malware Triage","A 32-bit Windows DLL profiled from detection, sandbox and published data: lifecycle, indicators, ATT&amp;CK mapping, a YARA rule and six actions. Draft v1.0.",["VirusTotal","ATT&amp;CK","YARA"],svgs.dark_card())}
{card("c3","","nginx-ansible-remediation.html","SOC-02","nginx Remediation with Ansible","Vulnerability Management","A source-built nginx upgraded from 1.15.5 to 1.30.4 with a dry-run-first playbook and a tested rollback, then checked with an OpenVAS re-scan.",["Ansible","OpenVAS / Greenbone","nginx"],svgs.vuln_card())}
{card("c4","","invoice-fraud-phishing-analysis.html","SOC-03","Invoice Fraud Phishing Analysis","Email Analysis / BEC","A suspected invoice-fraud email triaged through headers, SPF, DKIM and DMARC, sender identity, links, tracking pixel and a disguised attachment.",["Raw .eml","SHA-256","IOC defanging"],svgs.phish_card())}
</div>'''
    def ec(ref, title, cat, when, bullets, art):
        li = "".join(f"<li>{b}</li>" for b in bullets)
        return f'''<div class="card ec"><div class="thumb art"><span class="tag am ref">{ref}</span>{art}</div><div class="txt"><span class="cat">{cat}</span><h3>{title}</h3><p class="when">{when} · <span class="ph">[JOB TITLE]</span></p><ul class="ecl">{li}</ul></div></div>'''
    E = f'''<div class="sec-head"><span class="label t">Experience</span><h2>Two employers, one discipline.</h2><p>Work on transmission lines, transformers and electrical installations.</p></div>
<div class="cards">
{ec("EXP-01","Transmission Company of Nigeria","High-voltage transmission","December 2022 to June 2024",["Worked with engineering teams on new transmission lines: material and equipment selection, site surveys and route choice.","Diagnosed faults on lines and transformers with grounding cables, thermal cameras and fault locators.","Wrote technical reports on maintenance and repairs, and helped plan budgets and schedules for new projects.","Enforced safety regulations and protective equipment use, and carried out routine inspections of lines and transformers."],svgs.tower_card())}
{ec("EXP-02","Vitek Engineering Company","Electrical installations","December 2019 to November 2022",["Planned and carried out installations with contractors and senior engineers, safely and on schedule.","Assisted a licensed electrical company with residential wiring, to code.","Installed, maintained and repaired electrical systems, including a 500 kVA transformer."],svgs.wiring_card())}
</div>
<div class="note-box" style="margin-top:20px"><b>Next step</b>MSc Digital Forensics and Cyber Investigations graduate (Teesside University, Merit), building on an electrical background of fault diagnosis and written technical reporting. Switch to Digital Forensics or SOC Analyst to see that work.</div>'''
    return f'<section id="investigations" aria-labelledby="inv-h"><div class="wrap">{D("forensics", F)}{D("soc", S)}{D("electrical", E)}</div></section>'

def competencies():
    def grid(items):
        return '<div class="comp">' + "".join(f'<div>{ICON[i]}<h3>{t}</h3><p>{d}</p></div>' for i, t, d in items) + '</div>'
    F = grid([("disk", "Computer Forensics", "Disk imaging, RAID reconstruction, registry hives and Windows user-activity artefacts."),
             ("phone", "Mobile Forensics", "Full file system examination of Android and iOS, and Snapchat application databases."),
             ("globe", "Browser Forensics", "History databases, cookies, cache, and carved URL fragments in a private-browsing scenario."),
             ("chip", "IoT Forensics", "Telemetry and behavioural artefacts from consumer smart-home devices."),
             ("cloud", "Cloud Forensics", "Evidence obtained through official data access requests, and the limits of that route."),
             ("lens", "Digital Evidence Analysis", "Cross-tool verification, artefact correlation and separating findings from interpretation.")])
    S = grid([("lens", "Threat Intelligence", "Classifying a sample, mapping it to ATT&amp;CK and stating confidence in each judgement."),
             ("mail", "Phishing Analysis", "Headers, SPF, DKIM and DMARC, sender identity, links, pixels and attachments."),
             ("shield", "Vulnerability Management", "Baseline scans, patching with Ansible, rollback planning and re-scan verification."),
             ("chip", "Malware Triage", "Static metadata, section entropy, sandbox behaviour and indicators from a ransomware DLL."),
             ("doc", "Detection Logic", "A structural YARA rule built where verified strings were not available."),
             ("plan", "Incident Reporting", "Prioritised recommendations, defanged IOCs and open items stated openly.")])
    E = grid([("bolt", "Transmission Lines", "Design and installation of new high-voltage lines, including material selection and site surveys."),
             ("wrench", "Fault Diagnosis", "Locating faults on lines and transformers using grounding cables, thermal cameras and fault locators."),
             ("doc", "Technical Reporting", "Detailed reports on maintenance and repairs that explain what was done and why."),
             ("plan", "Project Planning", "Budgeting and scheduling for new transmission projects."),
             ("shield", "Safety Compliance", "Regulations followed and protective equipment required for everyone on site."),
             ("disk", "Routine Maintenance", "Regular inspection of high-voltage lines and transformers to catch problems early.")])
    head = lambda t, p: f'<div class="sec-head"><span class="label t">{t}</span><h2>Disciplines practised.</h2><p>{p}</p></div>'
    return (f'<section class="alt" data-fold aria-labelledby="comp-h"><div class="wrap" id="comp-h">'
            + D("forensics", head("Technical competencies", "Each area is backed by an investigation in this portfolio. See Skills for the tools involved.") + F)
            + D("soc", head("Technical competencies", "Each area is backed by one of the three SOC projects. See Skills for the tools involved.") + S)
            + D("electrical", head("Core competencies", "Drawn from work on transmission lines, transformers and installations.") + E) + '</div></section>')

def method():
    def one(key, title, steps, lead, note):
        tabs = "".join(f'<button type="button" role="tab" aria-selected="false" tabindex="-1"><span class="n">{i+1:02d}</span><b>{t}</b></button>' for i, (t, d) in enumerate(steps))
        data = json.dumps([{"t": t, "d": d} for t, d in steps])
        return D(key, f'''<div class="mw"><div class="sec-head"><span class="label t">Methodology</span><h2>{title}</h2><p>{lead}</p></div>
<div class="method" role="tablist" aria-label="Stages">{tabs}</div>
<div class="method-panel" role="tabpanel" aria-live="polite"></div>
<p class="note">{note}</p>
<script type="application/json" class="mdata">{data}</script></div>''')
    return ('<section id="method" data-fold aria-labelledby="m-h"><div class="wrap" id="m-h">'
        + one("forensics", "Evidence requires process.", METHOD, "Select a stage to read how it is approached.", "A general investigative framework. It describes the approach across this portfolio, and does not claim that every project followed identical procedures. For example, the Alexa data came from a data access request, so no disk image or hash could be made.")
        + one("soc", "From a raw artefact to a verified outcome.", SOC_METHOD, "Select a stage to read how the three SOC projects were approached.", "A summary of the approach across the three training projects. It does not claim to describe a production SOC workflow.")
        + '</div></section>')

def about():
    F = ('<div class="open"><p>I am interested in understanding how digital activity can be reconstructed from the traces left across devices, applications and connected environments.</p>'
         '<p>My work explores computer, mobile, browser and IoT forensics, with an emphasis on evidence acquisition, artefact examination and structured investigative analysis.</p>'
         '<p>Through research and practical forensic investigations, I explore the relationship between digital evidence, technology and investigative decision-making.</p></div>')
    S = ('<div class="open"><p>I approach security analysis the way I approach fault-finding: establish what is actually happening, check it against a second source, and write it down so someone else can follow.</p>'
         '<p>My SOC-focused work so far covers threat intelligence, phishing triage and vulnerability remediation, all as training exercises, each with confidence levels and open items stated.</p>'
         '<p>I am an MSc Digital Forensics and Cyber Investigations graduate, currently completing a SOC simulation with Amdari that covers Windows, macOS and Linux log analysis in Splunk and alert investigation. My engineering background in fault diagnosis on live transmission systems supports a methodical, root-cause approach.</p></div>')
    E = ('<div class="open"><p>I am a meticulous electrical engineer with over three years of experience in high-voltage electrical systems, committed to high-quality work that is safe and meets regulations.</p>'
         '<p>I want to expand my technical expertise and gain international experience in problem-solving as an electrician or engineer.</p>'
         '<p>Alongside this I have completed an MSc in digital forensics and cyber investigation, which is covered in the other views of this portfolio.</p></div>')
    cell = lambda r, h, li: f'<div data-for="{r}"><h4>{h}</h4><ul>' + "".join(f"<li>{x}</li>" for x in li) + '</ul></div>'
    dl = (cell("forensics", "Areas of interest", ["IoT and cloud evidence", "Windows user-activity artefacts", "Mobile application databases", "Evidence interpretation and limits"])
        + cell("forensics", "Investigation domains", ["Computer and Windows forensics", "Mobile device forensics", "Browser and internet forensics", "IoT and cloud forensics"])
        + cell("soc", "Areas of interest", ["Threat intelligence", "Phishing and BEC triage", "Vulnerability remediation", "Detection logic"])
        + cell("soc", "Project domains", ["Malware triage", "Email analysis", "Patch management with Ansible", "ATT&amp;CK mapping"])
        + cell("electrical", "Areas of strength", ["High-voltage transmission", "Fault diagnosis and repair", "Installations and wiring", "Technical reports"])
        + cell("electrical", "Memberships", ["Nigerian Society of Engineers (NSE)", "International Association of Engineers (IAENG)"])
        + '<div><h4>Academic background</h4><ul><li>MSc Digital Forensics and Cyber Investigations, Teesside University (2024 – 2026, Merit)</li><li>BEng Electrical/Electronics, Afe Babalola University (2017 – 2022)</li></ul></div>'
        + '<div><h4>Location</h4><ul><li>UK</li></ul></div>')
    acad = ('<p data-for="forensics soc">The case studies here were completed as academic or training work. They are presented as research and assessment exercises with simulated scenarios.</p>')
    return f'''<section class="alt" id="about" data-fold aria-labelledby="ab-h"><div class="wrap"><div class="sec-head"><span class="label t">About</span><h2 id="ab-h">{D("forensics", "How digital activity leaves a trace.", "span")}{D("soc", "Evidence first, then the call.", "span")}{D("electrical", "Engineering that keeps the lights on.", "span")}</h2></div>
<div class="about"><div class="portrait"><div class="frame"><span>Professional portrait<br>placeholder</span><img class="pimg" src="assets/img/profile-electrical.webp" alt="Portrait of {NAME}" width="800" height="1000" loading="lazy" decoding="async" hidden></div><p class="label" style="margin-top:12px">{NAME}</p></div>
<div class="about-copy">{D("forensics", F)}{D("soc", S)}{D("electrical", E)}
<div class="dl">{dl}</div>
{acad}
<div class="cta-row"><span style="display:contents">{cvlinks("btn")}</span><a class="btn ghost" href="#contact">Get in touch</a></div></div></div></div></section>'''

TOOLS = {
 "Computer Forensics": ("Examining disks, registry hives and Windows artefacts.", [
   ("X-Ways Forensics", "Used to add disk images, reconstruct the four-disk RAID set (JBOD/Linear), browse file systems, view hexadecimal and take a refined volume snapshot in the browser investigation."),
   ("Magnet AXIOM", "Used across the computer, browser and Alexa investigations to parse artefacts, compare operating system details, locate media and cross-check other tools."),
   ("FTK Imager", "Used to convert a virtual machine disk into a raw image that X-Ways could load."),
   ("Windows Registry Recovery", "Used to load registry hives and read user, software and recent-document keys."),
   ("RegRipper", "Named in the Windows investigation as a registry extraction tool."),
   ("MFT Stampede", "Used to convert raw timestamp values into readable dates, for example the Windows installation time.")]),
 "Mobile Forensics": ("Android and iOS application artefacts.", [
   ("Cellebrite Physical Analyzer", "Used to examine full file system extractions from a Samsung Galaxy S20+ and an iPhone, including Snapchat databases, and to compare hash values."),
   ("Magnet AXIOM", "Named alongside Cellebrite as an analysis tool in the Snapchat report."),
   ("Android artefact analysis", "Snapchat stores found on Android: Memories, My Eyes Only, Journal, contacts and message data."),
   ("iOS artefact analysis", "Device-level metadata and Snapchat databases on iOS, which held fewer Snapchat-specific stores.")]),
 "Browser and Internet Forensics": ("Residual traces of web activity.", [
   ("SQLite / DB Browser for SQLite", "Used to open the UC Browser History database directly and read its tables and fields."),
   ("X-Ways search hits", "Used to find URL fragments in unallocated and unstructured space."),
   ("Browser history analysis", "Reading visited URLs, titles, counts and timestamps."),
   ("Cache analysis", "Reviewing cached records as evidence of content the browser retrieved."),
   ("Cookie analysis", "Reading cookie names, hosts and expiry values surfaced by AXIOM.")]),
 "IoT and Cloud Forensics": ("Evidence from consumer devices and cloud exports.", [
   ("Amazon GDPR SAR", "The acquisition route for the Alexa study: a Subject Access Request returned a ZIP of 32 files."),
   ("Alexa artefact analysis", "Telemetry from an Echo Show and behavioural artefacts from an Echo Dot, compared across devices."),
   ("Python / Google Colaboratory", "Used to parse the archive, build timelines and produce charts. It was the only viable analysis platform found for this data."),
   ("Cloud data analysis", "Working out what an export contains and, as importantly, what it does not.")]),
 "Technical Methods": ("Practices applied across investigations.", [
   ("Disk imaging", "Creating raw images of a virtual disk and loading them for examination."),
   ("Evidence preservation", "Keeping originals unaltered and analysing copies."),
   ("Hash verification", "Comparing SHA values for recovered images, and hash values recorded before and after mobile examination."),
   ("RAID reconstruction", "Combining four images into one rebuilt image."),
   ("Registry examination", "NTUSER.DAT, SAM, SECURITY, SOFTWARE, SYSTEM and UsrClass.dat."),
   ("Database analysis", "SQLite and application databases such as Snapchat's arroyo.db."),
   ("Timeline reconstruction", "Ordering timestamped artefacts across tools."),
   ("Artefact correlation", "Checking that independent artefacts support the same reading."),
   ("Data visualisation", "Charts and timelines produced in Python from the Alexa data.")]),
}


TOOLS_SOC = {
 "Threat Intelligence": ("Profiling a ransomware sample.", [
   ("VirusTotal", "Used through its web interface and API v3 (queried from a Python notebook) to retrieve detection ratios, vendor labels, file metadata, sandbox behaviour and crowdsourced rules."),
   ("MITRE ATT&CK", "Used to map observed and reported behaviour to technique IDs, keeping sample evidence apart from rows taken from published reports."),
   ("Published threat reports", "CISA/FBI advisory AA21-131A and vendor research from Trend Micro, Mandiant, Sophos and others were used for history, actors and lifecycle."),
   ("Confidence language", "Each judgement is rated High, Moderate or Low, with the reason stated.")]),
 "Detection": ("Turning findings into rules.", [
   ("YARA", "A rule with an exact-hash clause and a structural clause (imphash, a .text1 section and a high-entropy .ndata section), chosen because no verified strings were available. Testing is still outstanding."),
   ("IOC handling", "Indicators are tabulated with type, context and confidence, and network indicators are defanged."),
   ("Hunting ideas", "Suggested hunts for rundll32.exe loading DLLs from user-writable folders, ransom-note file names and mass renames.")]),
 "Email and Phishing Analysis": ("Triage of a suspected invoice-fraud message.", [
   ("Raw .eml inspection", "Read the Received, Return-Path, Reply-To, Message-ID, X-Mailer and Authentication-Results headers directly."),
   ("SPF, DKIM and DMARC", "Interpreted each result and its alignment, and noted that the headers do not show what the gateway did."),
   ("MIME and attachment analysis", "Decoded a base64 attachment and hashed it with SHA-256 to identify an HTML file presented as a PDF."),
   ("Link and pixel review", "Compared the HTML and plain-text links and identified a hidden 1x1 tracking image.")]),
 "Log Analysis and SIEM": ("From the Amdari SOC simulation.", [
   ("Splunk Enterprise", "Windows and macOS logs forwarded to dedicated indexes with the Universal Forwarder, plus Kali Linux authentication logs and Suricata alert output in a Linux index."),
   ("Suricata", "Network intrusion detection, including a custom ICMP rule written to test alerting."),
   ("Kali Linux and VirtualBox", "Lab environment used to build and test the pipeline.")]),
 "Vulnerability Management": ("Fix, prove and be able to undo.", [
   ("OpenVAS / Greenbone", "Used for the baseline scan and the post-patch re-scan, and to read the Applications tab to confirm the detected nginx version."),
   ("Ansible", "A patch playbook with a built-in version check, a syntax check and a --check dry run, plus a rollback playbook that restores a backup."),
   ("Verification", "nginx -v and a curl header check confirmed the running version before the re-scan."),
   ("Scan triage", "Traced the remaining 9.8 result to a different service and recorded it as out of scope.")]),
}

TOOLS_EL = {
 "Transmission": ("High-voltage lines and transformers.", [
   ("Line design and installation", "Worked with engineering teams on new high-voltage transmission lines, including material and equipment selection."),
   ("Site surveys", "Contributed to surveys that found the best routes, balancing efficiency with community impact."),
   ("Transformers", "Diagnosed faults and carried out routine checks on transformers, and gained hands-on experience with a 500 kVA unit.")]),
 "Diagnostics and Tools": ("Finding faults quickly.", [
   ("Fault locators", "Used to identify faults on transmission lines."),
   ("Thermal cameras", "Used to identify issues on lines and transformers."),
   ("Grounding cables", "Used as part of fault diagnosis and safe working."),
   ("Power tools and testing equipment", "Familiar with power tools and electrical testing equipment.")]),
 "Installation and Wiring": ("Safe, code-compliant installation.", [
   ("Electrical installations", "Planned and carried out installations with contractors and senior engineers."),
   ("Residential wiring", "Assisted a licensed electrical company so that clients' systems were functional and up to code."),
   ("Repairs and maintenance", "Installed, maintained and repaired electrical systems.")]),
 "Planning, Reporting and Safety": ("The work around the work.", [
   ("Technical reports", "Detailed reports on maintenance and repairs, documenting what was done and why."),
   ("Budgeting and scheduling", "Helped plan new transmission line projects."),
   ("Safety compliance", "Made sure workers followed safety regulations and wore complete protective equipment on site."),
   ("Teamwork", "Worked closely with engineers, contractors and teams.")]),
}

def skills():
    def grid(T):
        cats = ""
        for name, (blurb, tools) in T.items():
            t = "".join(f'<button type="button" class="tool" aria-expanded="false" data-how="{esc(h)}">{n}</button>' for n, h in tools)
            cats += f'<div class="skillcat"><span class="label t">{name}</span><h3>{name}</h3><p>{blurb}</p><div class="tl">{t}</div><div class="tooldesc" aria-live="polite"></div></div>'
        return f'<div class="skillgrid">{cats}</div>'
    head = lambda p: f'<div class="sec-head"><span class="label t">Skills and tools</span><h2>What was used, and how.</h2><p>{p}</p></div>'
    return ('<section id="skills" data-fold aria-labelledby="sk-h"><div class="wrap" id="sk-h">'
        + D("forensics", head("Select a tool to see how it was applied in these investigations. No proficiency ratings are claimed.") + grid(TOOLS))
        + D("soc", head("Select a tool to see how it was applied in the SOC projects. No proficiency ratings are claimed.") + grid(TOOLS_SOC))
        + D("electrical", head("Select an item to see where it was used. Drawn from the CV, with no proficiency ratings claimed.") + grid(TOOLS_EL)) + '</div></section>')

def contact():
    return f'''<section class="alt" id="contact" aria-labelledby="c-h"><div class="wrap"><div class="contact">
<h2 id="c-h">Have an investigation, research opportunity or technical collaboration in mind?</h2>
<div class="ways"><dl><div><dt>Email</dt><dd><a href="mailto:ogbonna1.ugwuja@gmail.com">ogbonna1.ugwuja@gmail.com</a></dd></div><div><dt>LinkedIn</dt><dd><a href="https://www.linkedin.com/in/ogbonna-ugwuja-bonaventure/" target="_blank" rel="noopener">linkedin.com/in/ogbonna-ugwuja-bonaventure</a></dd></div><div><dt>Location</dt><dd>UK</dd></div><div><dt>CV</dt><dd>{cvlinks("", "Download CV (PDF)", False)}</dd></div></dl></div>
</div></div></section>'''


def home_body():
    return hero() + intro() + projects() + competencies() + method() + about() + skills() + contact()
