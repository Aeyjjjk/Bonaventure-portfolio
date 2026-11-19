import json
from lib import *
import svgs

ICON = {
 "disk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="1"/><path d="M8 20h8M12 16v4"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg>',
 "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.500 0 18M12 3c-3 3.5-3 14.500 0 18"/></svg>',
 "chip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="6" y="6" width="12" height="12"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
 "cloud": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M7 18a4 4 0 010-8 5.500 5.500 0 0110.500 1.500A3.300 3.300 0 0117 18z"/></svg>',
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

def hero():
    return f'''<section class="hero grid-fade" id="top" aria-labelledby="h1" style="padding-block:clamp(48px,7vw,96px)"><div class="wrap hero-grid">
<div class="hero-copy">
<p class="label t">Digital Forensics &amp; Cyber Investigations</p>
<h1 id="h1">Digital evidence.<br><em>Beyond the surface.</em></h1>
<p class="lede">Exploring the intersection of digital forensics, cyber investigations and emerging connected technologies through structured investigation and evidence-led research.</p>
<div class="cta-row"><a class="btn" href="#investigations">Explore investigations {ARROW}</a><a class="btn ghost" href="#" data-soon="The portfolio PDF is not exported yet. It will be linked here once supplied.">Download portfolio</a></div>
<div class="hero-meta"><span><b>04</b> investigations</span><span><b>05</b> evidence domains</span><span>Academic forensic case studies</span></div>
</div>
<div class="hero-vis"><div class="scene" role="group" aria-label="Evidence composition with a project photograph of an Echo Dot and an Echo Show">
{svgs.hero_overlay()}
<div class="photo"><img src="assets/img/alexa-echo-devices.webp" alt="Project photograph of an Amazon Echo Dot and an Echo Show on a surface" width="629" height="481" decoding="async"></div>
<span class="tag am" style="left:11%;top:11%">Exhibit ALX-01</span>
<span class="tag" style="right:11%;top:11%">UTC+0</span>
<span class="tag te" style="left:11%;bottom:20%">Source · SAR archive</span>
<span class="tag am" style="right:11%;bottom:20%">21:54:04Z → 21:54:20Z</span>
<span class="tag" style="left:11%;bottom:11%">Project photograph</span>
<span class="tag te" style="right:11%;bottom:11%">16 s anomaly</span>
</div></div></div></section>'''

def intro():
    return f'''<section class="alt" aria-labelledby="intro-h"><div class="wrap"><div class="intro">
<h2 id="intro-h">Understanding the evidence behind digital activity.</h2>
<div class="body"><p>This portfolio collects four practical investigations carried out as academic forensic case studies. Each starts from a question, works through acquisition and examination, and ends with what the evidence supports and where it stops.</p>
<p>The work spans a seized-computer scenario with a reconstructed RAID set, a comparison of Snapchat artefacts on Android and iOS, residual traces left by a private-browsing session, and cloud-hosted evidence from Amazon Echo devices obtained through a GDPR Subject Access Request.</p>
<p>Throughout, findings are labelled by how strongly the evidence supports them, and limitations are stated next to the results they affect.</p></div>
<div class="pillars">
<div><span class="label a">Computers</span><b>Windows &amp; disks</b><span>RAID reconstruction, registry hives, shellbags, LNK and jump lists.</span></div>
<div><span class="label a">Mobile</span><b>Android &amp; iOS</b><span>Snapchat databases and device metadata across two platforms.</span></div>
<div><span class="label a">Browsers</span><b>Residual traces</b><span>History, cookies, cache and carved fragments from a private session.</span></div>
<div><span class="label a">IoT &amp; cloud</span><b>Connected devices</b><span>Alexa telemetry and behavioural artefacts from official data exports.</span></div>
</div></div></div></section>'''

def projects():
    def card(cls, d, href, ref, title, cat, desc, tools, thumb, big=False):
        t = "".join(f"<span>{x}</span>" for x in tools)
        return f'''<a class="card {cls}" data-d="{d}" href="{href}"><div class="thumb{'' if big else ' art'}"><span class="tag am ref">{ref}</span>{thumb}</div>
<div class="txt"><span class="cat">{cat}</span><h3>{title}</h3><p>{desc}</p><div class="tools">{t}</div><span class="view">View case study {ARROW}</span></div></a>'''
    alexa_thumb = '<div style="position:absolute;inset:0;display:grid;place-items:center;background:#0a1224"><div style="width:min(78%,560px);border:1px solid #F0A45D;position:relative"><img src="assets/img/alexa-echo-devices.webp" alt="Project photograph of an Echo Dot and an Echo Show" loading="lazy" width="629" height="481"></div></div>'
    return f'''<section id="investigations" aria-labelledby="inv-h"><div class="wrap">
<div class="sec-head"><span class="label t">Selected investigations</span><h2 id="inv-h">Four investigations, one method.</h2><p>Filter by discipline. Each case study follows the same structure, from the original question to limitations.</p></div>
<div class="filters" role="group" aria-label="Filter investigations by discipline">
<button class="chip" type="button" data-f="all" aria-pressed="true">All</button><button class="chip" type="button" data-f="computer" aria-pressed="false">Computer</button><button class="chip" type="button" data-f="mobile" aria-pressed="false">Mobile</button><button class="chip" type="button" data-f="browser" aria-pressed="false">Browser</button><button class="chip" type="button" data-f="iot" aria-pressed="false">IoT &amp; cloud</button></div>
<p class="label" id="filter-status" aria-live="polite" style="margin:-8px 0 20px">4 investigations shown</p>
<div class="cards">
{card("c1","iot cloud","alexa-iot-forensics.html","ALX-01 · Flagship research","Amazon Alexa IoT Forensics","IoT Forensics / Cloud Forensics","Cloud-based evidence acquisition and artefact interpretation across an Echo Dot and an Echo Show, using Amazon's GDPR Subject Access Request. The comparison shows that cross-device analysis gives a fuller picture than either device alone.",["GDPR SAR","Python / Colab","Magnet AXIOM"],alexa_thumb,True)}
{card("c2","computer","raid-windows-forensics.html","RDW-02","Advanced Forensic Computing","Disk Forensics / Windows Artefacts / RAID Reconstruction","Four disk images rebuilt into one, then a Windows drive examined through registry hives, shellbags, LNK files and jump lists, with key items checked in hexadecimal.",["X-Ways","Magnet AXIOM","RegRipper","MFT Stampede"],svgs.raid_card())}
{card("c3","mobile","snapchat-mobile-forensics.html","SNP-03","Mobile Application Forensics","Android / iOS / Snapchat","A comparison of Snapchat artefacts on a Samsung Galaxy S20+ and an iPhone, with hash checks before and after examination.",["Cellebrite Physical Analyzer","Magnet AXIOM"],svgs.snap_card())}
{card("c4","browser","uc-browser-forensics.html","UCB-04","UC Browser Forensics","Internet Forensics / Browser Artefacts","Normal and incognito browsing in a controlled Windows 10 virtual machine, then imaged and examined for history, cookies, cache and carved fragments.",["FTK Imager","X-Ways","DB Browser for SQLite","Magnet AXIOM"],svgs.uc_card())}
</div></div></section>'''

def competencies():
    items = [("disk", "Computer Forensics", "Disk imaging, RAID reconstruction, registry hives and Windows user-activity artefacts."),
             ("phone", "Mobile Forensics", "Full file system examination of Android and iOS, and Snapchat application databases."),
             ("globe", "Browser Forensics", "History databases, cookies, cache, and carved URL fragments in a private-browsing scenario."),
             ("chip", "IoT Forensics", "Telemetry and behavioural artefacts from consumer smart-home devices."),
             ("cloud", "Cloud Forensics", "Evidence obtained through official data access requests, and the limits of that route."),
             ("lens", "Digital Evidence Analysis", "Cross-tool verification, artefact correlation and separating findings from interpretation.")]
    c = "".join(f'<div>{ICON[i]}<h3>{t}</h3><p>{d}</p></div>' for i, t, d in items)
    return f'''<section class="alt" aria-labelledby="comp-h"><div class="wrap"><div class="sec-head"><span class="label t">Technical competencies</span><h2 id="comp-h">Disciplines practised.</h2><p>Each area is backed by an investigation in this portfolio. See Skills for the tools involved.</p></div><div class="comp">{c}</div></div></section>'''

def method():
    tabs = "".join(f'<button type="button" role="tab" id="mt{i}" aria-selected="false" aria-controls="method-panel" tabindex="-1"><span class="n">{i+1:02d}</span><b>{t}</b></button>' for i, (t, d) in enumerate(METHOD))
    data = json.dumps([{"t": t, "d": d} for t, d in METHOD])
    return f'''<section id="method" aria-labelledby="m-h"><div class="wrap"><div class="sec-head"><span class="label t">Methodology</span><h2 id="m-h">Evidence requires process.</h2><p>Select a stage to read how it is approached.</p></div>
<div class="method" role="tablist" aria-label="Investigation stages">{tabs}</div>
<div class="method-panel" id="method-panel" role="tabpanel" aria-live="polite"></div>
<p class="note">A general investigative framework. It describes the approach across this portfolio, and does not claim that every project followed identical procedures. For example, the Alexa data came from a data access request, so no disk image or hash could be made.</p>
<script type="application/json" id="method-data">{data}</script></div></section>'''

def about():
    return f'''<section class="alt" id="about" aria-labelledby="ab-h"><div class="wrap"><div class="sec-head"><span class="label t">About</span><h2 id="ab-h">How digital activity leaves a trace.</h2><p>Name and background details are placeholders to complete.</p></div>
<div class="about"><div class="portrait"><div class="frame"><span>Professional portrait<br>placeholder</span></div><p class="label" style="margin-top:12px">{NAME}</p></div>
<div class="about-copy"><div class="open"><p>I am interested in understanding how digital activity can be reconstructed from the traces left across devices, applications and connected environments.</p>
<p>My work explores computer, mobile, browser and IoT forensics, with an emphasis on evidence acquisition, artefact examination and structured investigative analysis.</p>
<p>Through research and practical forensic investigations, I explore the relationship between digital evidence, technology and investigative decision-making.</p></div>
<div class="dl"><div><h4>Areas of interest</h4><ul><li>IoT and cloud evidence</li><li>Windows user-activity artefacts</li><li>Mobile application databases</li><li>Evidence interpretation and limits</li></ul></div>
<div><h4>Investigation domains</h4><ul><li>Computer and Windows forensics</li><li>Mobile device forensics</li><li>Browser and internet forensics</li><li>IoT and cloud forensics</li></ul></div>
<div><h4>Academic background</h4><ul><li>MSc Digital Forensics and Cyber Investigations <span class="ph">[INSTITUTION · DATES]</span></li><li>BEng Electrical/Electronics <span class="ph">[INSTITUTION · YEAR]</span></li></ul></div>
<div><h4>Location</h4><ul><li><span class="ph">[LOCATION]</span></li></ul></div></div>
<p>The case studies here were completed as academic work. They are presented as research and assessment exercises with simulated scenarios.</p>
<div class="cta-row"><a class="btn" href="assets/downloads/CV.pdf" target="_blank" rel="noopener">{DL}Download CV</a><a class="btn ghost" href="#contact">Get in touch</a></div></div></div></div></section>'''

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

def skills():
    cats = ""
    for name, (blurb, tools) in TOOLS.items():
        t = "".join(f'<button type="button" class="tool" aria-expanded="false" data-how="{esc(h)}">{n}</button>' for n, h in tools)
        cats += f'<div class="skillcat"><span class="label t">{name}</span><h3>{name}</h3><p>{blurb}</p><div class="tl">{t}</div><div class="tooldesc" aria-live="polite"></div></div>'
    return f'''<section id="skills" aria-labelledby="sk-h"><div class="wrap"><div class="sec-head"><span class="label t">Skills and tools</span><h2 id="sk-h">What was used, and how.</h2><p>Select a tool to see how it was applied in these investigations. No proficiency ratings are claimed.</p></div><div class="skillgrid">{cats}</div></div></section>'''

def contact():
    return f'''<section class="alt" id="contact" aria-labelledby="c-h"><div class="wrap"><div class="contact">
<h2 id="c-h">Have an investigation, research opportunity or technical collaboration in mind?</h2>
<div class="ways"><dl><div><dt>Email</dt><dd><span class="ph">[PROFESSIONAL EMAIL]</span></dd></div><div><dt>LinkedIn</dt><dd><a href="#" data-soon="Add your LinkedIn URL in place of [LINKEDIN URL].">[LINKEDIN URL]</a></dd></div><div><dt>GitHub</dt><dd><a href="#" data-soon="Add your GitHub URL in place of [GITHUB URL].">[GITHUB URL]</a></dd></div><div><dt>Location</dt><dd>[LOCATION]</dd></div><div><dt>CV</dt><dd><a href="assets/downloads/CV.pdf" target="_blank" rel="noopener">Download CV (PDF)</a></dd></div></dl></div>
<form id="contact-form" novalidate aria-label="Contact form">
<div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name"><span class="err">Enter your name.</span></div>
<div class="field"><label for="f-mail">Email</label><input id="f-mail" name="email" type="email" autocomplete="email"><span class="err">Enter a valid email address.</span></div>
<div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message"></textarea><span class="err">Write at least 10 characters.</span></div>
<button class="btn" type="submit">Send message</button>
<p class="formnote">Demo form: it checks your input but does not send anything yet. Connect it to a form service before publishing.</p></form>
<div class="confirm" id="form-ok" tabindex="-1" role="status"><p style="color:var(--fg);margin:0 0 10px"><strong>Form checked. Nothing was sent.</strong></p><p style="margin:0 0 16px;color:var(--fg2)">This form is not connected to a submission service yet. Use the email address above in the meantime.</p><button class="btn ghost sm" type="button" id="form-again">Edit message</button></div>
</div></div></section>'''

def home_body():
    return hero() + intro() + projects() + competencies() + method() + about() + skills() + contact()
