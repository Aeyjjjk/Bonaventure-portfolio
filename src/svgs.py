"""Vector illustrations. Every one is an explanatory reconstruction, never a device screenshot."""
T, A, L, BG, CARD, FG, F2 = "#27C6B0", "#F0A45D", "#26344B", "#0B1020", "#172238", "#F4F5F7", "#A5AFBF"
FONT = "font-family=\"IBM Plex Mono,monospace\""

def _svg(w, h, inner, label, cls="diagram"):
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>')

def txt(x, y, s, size=12, fill=F2, anchor="start", weight=400, ls=0):
    return (f'<text x="{x}" y="{y}" {FONT} font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}" letter-spacing="{ls}">{s}</text>')

def rect(x, y, w, h, stroke=L, fill="none", sw=1, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" stroke="{stroke}" fill="{fill}" stroke-width="{sw}" {extra}/>'

def line(x1, y1, x2, y2, stroke=L, sw=1, dash=""):
    d = f'stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" {d}/>'

def arrow(x1, y1, x2, y2, c=T):
    return line(x1, y1, x2, y2, c, 1.5) + f'<path d="M{x2} {y2} l-7 -4 v8z" fill="{c}" transform="rotate(0)"/>'

def grid(w, h, step=40):
    g = "".join(line(x, 0, x, h, "#1D2B40") for x in range(0, w, step)) + "".join(line(0, y, w, y, "#1D2B40") for y in range(0, h, step))
    return g

# ---------- card art ----------
def raid_card():
    inner = grid(480, 300) + ""
    for i in range(4):
        y = 50 + i * 52
        inner += rect(40, y, 120, 36, T, CARD) + txt(100, y + 22, f"BEF2-{i+1}", 12, FG, "middle", 500) + arrow(160, y + 18, 250, 150)
    inner += rect(256, 120, 170, 60, A, CARD, 1.5) + txt(341, 148, "BEF2-REBUILT", 13, A, "middle", 500) + txt(341, 166, "JBOD / LINEAR", 10.5, F2, "middle")
    inner += txt(24, 285, "ILLUSTRATION · RECONSTRUCTION", 10, F2, "start", 500, 1.5)
    return _svg(480, 300, inner, "Illustration: four disk images combined into one rebuilt image", "")

def snap_card():
    inner = grid(480, 300)
    for x, lab, c in ((90, "ANDROID", T), (270, "iOS", A)):
        inner += rect(x, 40, 120, 210, c, CARD, 1.5, 'rx="14"') + rect(x + 10, 56, 100, 160, L, BG)
        inner += txt(x + 60, 236, lab, 12, c, "middle", 500, 1.5)
        for j in range(3):
            inner += rect(x + 20, 70 + j * 44, 80, 32, L, CARD)
            inner += txt(x + 60, 91 + j * 44, ("arroyo.db", "contacts", "media")[j], 10, F2, "middle")
    inner += line(222, 145, 258, 145, F2, 1, "3 3") + txt(240, 283, "ILLUSTRATION · NOT A DEVICE SCREENSHOT", 10, F2, "middle", 500, 1.5)
    return _svg(480, 300, inner, "Illustration: Android and iOS handsets compared", "")

def uc_card():
    inner = grid(480, 300)
    inner += rect(50, 40, 380, 200, T, CARD, 1.5) + line(50, 70, 430, 70, L)
    inner += rect(62, 48, 110, 22, A, BG) + txt(117, 63, "NORMAL", 10, A, "middle", 500, 1.2)
    inner += rect(176, 48, 110, 22, F2, BG) + txt(231, 63, "PRIVATE", 10, F2, "middle", 500, 1.2)
    for j, lab in enumerate(("History", "Cookies", "Cache", "Search hits")):
        inner += rect(70 + (j % 2) * 175, 92 + (j // 2) * 62, 160, 46, L, BG) + txt(150 + (j % 2) * 175, 120 + (j // 2) * 62, lab, 12, FG, "middle", 500)
    inner += txt(240, 283, "ILLUSTRATION · RESIDUAL BROWSER ARTEFACTS", 10, F2, "middle", 500, 1.5)
    return _svg(480, 300, inner, "Illustration: browser window with normal and private tabs and artefact stores", "")

# ---------- hero scene overlay ----------
def hero_overlay():
    s = grid(400, 500)
    s += f'<g stroke="{T}" stroke-width="1.2" fill="none"><path d="M20 40V20h20M360 20h20v20M380 460v20h-20M40 480H20v-20"/></g>'
    s += line(200, 0, 200, 500, "#2a4a5c", 1, "2 6") + line(0, 250, 400, 250, "#2a4a5c", 1, "2 6")
    s += f'<circle cx="200" cy="250" r="86" stroke="{T}" stroke-width="1" fill="none" opacity=".35"/><circle cx="200" cy="250" r="140" stroke="{T}" stroke-width="1" fill="none" opacity=".18"/>'
    for i in range(0, 400, 20):
        h = 8 if i % 100 == 0 else 4
        s += line(i, 0, i, h, F2, 1) + line(i, 500, i, 500 - h, F2, 1)
    return f'<svg class="ov" viewBox="0 0 400 500" preserveAspectRatio="none" aria-hidden="true">{s}</svg>'

# ---------- ALEXA ----------
def alexa_timeline():
    # Real dates. Day offsets from 2025-08-10; Echo Show to 2026-01-16 (160 days), Echo Dot 2026-02-11 to 2026-03-06.
    W, H = 960, 300
    d0 = 0
    total = 209  # 2025-08-10 -> 2026-03-07
    x = lambda d: 60 + d / total * 860
    s = grid(W, H, 40)
    months = [("Aug 25", 0), ("Sep", 22), ("Oct", 52), ("Nov", 83), ("Dec", 113), ("Jan 26", 144), ("Feb", 175), ("Mar", 203)]
    s += line(60, 230, 920, 230, F2, 1)
    for m, d in months:
        s += line(x(d), 226, x(d), 238, F2) + txt(x(d), 256, m, 11, F2, "middle")
    s += rect(x(0), 70, x(160) - x(0), 44, A, "rgba(240,164,93,.14)", 1.5) + txt(x(0) + 10, 97, "ECHO SHOW · 160 days · 1,296 log entries", 12, A, "start", 500)
    s += rect(x(185), 150, x(208) - x(185), 44, T, "rgba(39,198,176,.14)", 1.5) + txt(x(185) - 10, 177, "ECHO DOT · 23 days", 12, T, "end", 500)
    s += line(x(0), 50, x(0), 230, A, 1.5, "4 3") + txt(x(0) + 8, 44, "2025-08-10 · 21:54:04Z to 21:54:20Z · 16 s connectivity anomaly", 11.5, A, "start", 500)
    s += f'<circle cx="{x(0)}" cy="92" r="5" fill="{A}"/>'
    s += txt(x(160), 134, "capture ends 2026-01-16", 10.5, F2, "middle") + txt(x(185), 212, "2026-02-11", 10.5, F2, "middle") + txt(x(208), 212, "03-06", 10.5, F2, "middle")
    s += txt(x(166), 78, "No overlap between", 10.5, F2, "start") + txt(x(166), 92, "the two capture windows", 10.5, F2, "start")
    s += txt(60, 290, "Dates from the dissertation. Axis is calendar time, spans are drawn to scale.", 10.5, F2)
    return _svg(W, H, s, "Timeline of the Echo Show capture window and the Echo Dot capture window with the 16 second anomaly marked on 10 August 2025")

def alexa_conn():
    W, H = 560, 230
    s = ""
    tot = 127; ok = 60; un = 67
    bw = 480
    s += txt(0, 18, "Echo Dot · EndpointHealth.connectivity · 127 entries", 12, F2, "start", 500)
    s += rect(0, 40, bw * ok / tot, 44, T, "rgba(39,198,176,.25)", 1.5) + rect(bw * ok / tot, 40, bw * un / tot, 44, A, "rgba(240,164,93,.25)", 1.5)
    s += txt(bw * ok / tot / 2, 68, "OK · 60", 15, T, "middle", 500) + txt(bw * ok / tot + bw * un / tot / 2, 68, "UNREACHABLE · 67", 15, A, "middle", 500)
    s += txt(bw * ok / tot + bw * un / tot / 2, 106, "52.8%", 13, A, "middle")
    s += txt(0, 150, "Each power cycle between scheduled sessions produced an UNREACHABLE", 12.5, FG) + txt(0, 170, "transition. The count reflects the test design, not interference.", 12.5, FG)
    s += txt(0, 204, "Source: dissertation section 4.2.2. Bar drawn to scale.", 10.5, F2)
    return _svg(W, H, s, "Bar showing 60 OK and 67 UNREACHABLE connectivity entries out of 127")

def alexa_axiom():
    W, H = 560, 250
    data = [("Media", 728, T), ("Documents (CSV)", 110, A), ("Communication", 5, F2), ("Operating system", 1, F2)]
    s = txt(0, 18, "Magnet AXIOM · 844 evidence items", 12, F2, "start", 500)
    mx = 728
    for i, (n, v, c) in enumerate(data):
        y = 44 + i * 48
        bw = max(3, 330 * v / mx)
        s += txt(0, y + 20, n, 13, FG) + rect(150, y, bw, 28, c, "rgba(255,255,255,.04)", 1.5) + txt(150 + bw + 10, y + 20, f"{v:,}", 14, c if c != F2 else FG, "start", 500)
    s += txt(0, 240, "Source: dissertation section 4.5. Bars drawn to scale.", 10.5, F2)
    return _svg(W, H, s, "Bar chart of Magnet AXIOM evidence items: media 728, documents 110, communication 5, operating system 1")

def alexa_workflow():
    W, H = 960, 170
    steps = ["Scenario", "SAR request", "Archive received", "Copy & organise", "Colab analysis", "AXIOM check"]
    s = ""
    for i, t in enumerate(steps):
        x = 10 + i * 156
        s += rect(x, 40, 136, 70, T if i != 1 else A, CARD, 1.4) + txt(x + 68, 70, f"{i+1:02d}", 11, A, "middle", 500, 1.5) + txt(x + 68, 94, t, 13, FG, "middle", 500)
        if i < 5:
            s += arrow(x + 136, 75, x + 156, 75)
    s += txt(10, 150, "Original ZIP preserved unaltered. All analysis performed on working copies. No hash verification was possible (see limitations).", 11.5, F2)
    return _svg(W, H, s, "Acquisition workflow from scenario through SAR request to analysis and cross-tool check")

# ---------- RAID ----------
def raid_process():
    W, H = 960, 300
    s = grid(W, H)
    for i in range(4):
        y = 40 + i * 58
        s += rect(40, y, 190, 42, T, CARD, 1.4) + txt(135, y + 26, f"BEF2-{i+1}  (image)", 13, FG, "middle", 500) + arrow(230, y + 21, 380, 150)
    s += rect(60, 262, 150, 26, L, BG) + txt(135, 280, "order: 1 → 2 → 3 → 4", 11, F2, "middle")
    s += rect(380, 105, 230, 90, A, CARD, 1.6) + txt(495, 136, "X-Ways", 12, F2, "middle", 500, 2) + txt(495, 158, "Specialist &gt; Reconstruct", 12.5, FG, "middle") + txt(495, 176, "RAID System · JBOD / Linear", 12.5, FG, "middle")
    s += arrow(610, 150, 700, 150, A)
    s += rect(700, 105, 220, 90, T, CARD, 1.6) + txt(810, 140, "BEF2-REBUILT", 15, T, "middle", 500) + txt(810, 162, "single image, ALT+C", 12, F2, "middle") + txt(810, 180, "added as directory", 12, F2, "middle")
    s += txt(700, 240, "BEF1 (OS drive) examined separately.", 11.5, F2) + txt(700, 262, "ILLUSTRATION · RECONSTRUCTION OF THE PROCESS", 10.5, T, "start", 500, 1)
    return _svg(W, H, s, "Illustration: four disk images combined via X-Ways JBOD Linear option into one rebuilt image")

def raid_activity():
    W, H = 960, 380
    s = grid(W, H)
    srcs = [("NTUSER.DAT", "RecentDocs: 8 recent .jpg", 40), ("USRCLASS.DAT", "Shellbags: art, furniture folders", 110),
            ("Jump Lists", "Photos app: 4 pinned images", 180), ("LNK files", "Recent folder shortcuts", 250)]
    for n, d, y in srcs:
        s += rect(30, y, 300, 56, T, CARD, 1.4) + txt(46, y + 24, n, 13.5, T, "start", 500) + txt(46, y + 43, d, 11.5, F2) + arrow(330, y + 28, 470, 170)
    s += rect(470, 120, 210, 100, A, CARD, 1.6) + txt(575, 156, "CORRELATE", 12, A, "middle", 500, 2)
    s += txt(575, 180, "same folders, same files,", 12, FG, "middle") + txt(575, 198, "consistent timestamps", 12, FG, "middle")
    s += arrow(680, 170, 760, 170, A)
    s += rect(760, 110, 170, 120, L, BG, 1.4) + txt(845, 140, "READING", 11, F2, "middle", 500, 2) + txt(845, 166, "User account opened", 12, FG, "middle") + txt(845, 184, "the antique images", 12, FG, "middle") + txt(845, 206, "(interpretation)", 11, F2, "middle")
    s += txt(30, 340, "ILLUSTRATION · HOW INDEPENDENT ARTEFACTS SUPPORT ONE ANOTHER. Not an original screenshot.", 10.5, T, "start", 500, 0.5)
    return _svg(W, H, s, "Illustration: registry hives, shellbags, jump lists and LNK files feeding a correlated reading of user activity")

# ---------- SNAPCHAT ----------
def snap_workflow():
    W, H = 960, 150
    steps = [("Device", "S20+ 5G / iPhone"), ("Hash noted", "before extraction"), ("Full file system", "extraction"), ("Examine", "Physical Analyzer"), ("Hash compared", "after analysis")]
    s = ""
    for i, (a, b) in enumerate(steps):
        x = 10 + i * 188
        s += rect(x, 30, 164, 76, T if i != 1 and i != 4 else A, CARD, 1.4) + txt(x + 82, 62, a, 13.5, FG, "middle", 500) + txt(x + 82, 82, b, 11.5, F2, "middle")
        if i < 4:
            s += arrow(x + 164, 68, x + 188, 68)
    return _svg(W, H, s, "Extraction workflow: hash recorded, full file system extraction, examination, hash compared")

def snap_db():
    W, H = 960, 360
    s = grid(W, H)
    s += rect(310, 20, 340, 320, T, "rgba(39,198,176,.05)", 1.5) + txt(480, 50, "arroyo.db  (main Snapchat store)", 14, T, "middle", 500)
    items = [("Messages", "26 conversation rows", "both", 80), ("Memories", "saved snaps", "android", 140), ("My Eyes Only", "private store", "android", 200), ("Journal", "entries, log", "android", 260)]
    for n, d, p, y in items:
        c = T if p == "both" else A
        s += rect(340, y, 280, 46, c, CARD, 1.3) + txt(354, y + 20, n, 13.5, FG, "start", 500) + txt(354, y + 37, d, 11, F2)
        s += txt(606, y + 28, "ANDROID + iOS" if p == "both" else "ANDROID ONLY", 10, c, "end", 500, 1)
    s += rect(40, 120, 220, 110, L, BG) + txt(150, 150, "Write-ahead log", 13.5, FG, "middle", 500) + txt(150, 172, "Android ≈ 4 MB", 12, F2, "middle") + txt(150, 190, "iOS ≈ 2 MB", 12, F2, "middle") + txt(150, 212, "(arroyo.db-wal)", 11, F2, "middle")
    s += arrow(260, 175, 310, 175)
    s += txt(700, 120, "Where each store was seen", 12, FG, "start", 500)
    s += txt(700, 146, "Messages: both platforms", 12, T) + txt(700, 168, "Memories: Android only", 12, A) + txt(700, 190, "My Eyes Only: Android only", 12, A) + txt(700, 212, "Journal: Android only", 12, A)
    s += txt(30, 346, "ILLUSTRATION · SIMPLIFIED STRUCTURE, NOT A DATABASE SCREENSHOT", 10.5, T, "start", 500, 1)
    return _svg(W, H, s, "Illustration of the arroyo.db database and which stores were seen on Android and iOS")

def snap_hash():
    W, H = 720, 200
    s = rect(20, 30, 250, 80, A, CARD, 1.4) + txt(145, 60, "HASH BEFORE", 11, A, "middle", 500, 2) + txt(145, 88, "recorded at extraction", 12.5, FG, "middle")
    s += rect(450, 30, 250, 80, A, CARD, 1.4) + txt(575, 60, "HASH AFTER", 11, A, "middle", 500, 2) + txt(575, 88, "recorded after analysis", 12.5, FG, "middle")
    s += f'<circle cx="360" cy="70" r="30" fill="rgba(39,198,176,.12)" stroke="{T}" stroke-width="1.5"/><path d="M345 70l10 10 20-22" stroke="{T}" stroke-width="3" fill="none"/>'
    s += line(270, 70, 330, 70, T, 1.5) + line(390, 70, 450, 70, T, 1.5)
    s += txt(360, 140, "No hash value changed on either device (report conclusion).", 12.5, FG, "middle")
    s += txt(360, 166, "Hash values are not published here.", 11.5, F2, "middle")
    return _svg(W, H, s, "Hash recorded before extraction matches hash recorded after analysis")

# ---------- UC BROWSER ----------
def uc_vm():
    W, H = 720, 280
    s = rect(20, 20, 680, 240, L, BG, 1.2) + txt(40, 46, "HOST · Oracle VM VirtualBox", 12, F2, "start", 500, 1.2)
    s += rect(60, 66, 420, 170, T, CARD, 1.6) + txt(80, 94, "GUEST · Windows 10", 13, T, "start", 500)
    for i, (a, b) in enumerate((("8 GB", "RAM"), ("4", "processor cores"), ("30 GB", "virtual hard disk"))):
        x = 80 + i * 134
        s += rect(x, 120, 122, 80, L, BG) + txt(x + 61, 156, a, 24, FG, "middle", 500) + txt(x + 61, 180, b, 10.5, F2, "middle")
    s += txt(80, 224, "UC Browser installed · normal and incognito sessions run here", 11, F2)
    s += arrow(480, 150, 540, 150, A) + rect(540, 106, 140, 88, A, CARD, 1.4) + txt(610, 142, "FTK Imager", 13, FG, "middle", 500) + txt(610, 162, "raw .dd image", 11.5, F2, "middle") + txt(610, 180, "→ X-Ways, AXIOM", 11.5, F2, "middle")
    s += txt(20, 275, "ILLUSTRATION · CONFIGURATION AS STATED IN THE REPORT", 10, T, "start", 500, 1)
    return _svg(W, H + 10, s, "Illustration of the VirtualBox host, the Windows 10 guest with 8 GB RAM, 4 cores and 30 GB disk, and the imaging step")

def uc_sqlite():
    W, H = 720, 300
    s = rect(20, 20, 330, 260, T, CARD, 1.4) + txt(36, 46, "History  (SQLite)", 14, T, "start", 500) + txt(36, 66, "12 tables · 14 indexes", 11.5, F2)
    cols = [("url", "visited address"), ("title", "page title"), ("visit_count", "times visited"), ("typed_count", "times typed"), ("last_visit_time", "WebKit timestamp"), ("hidden", "0 = visible"), ("favicon_id", "icon reference")]
    for i, (a, b) in enumerate(cols):
        y = 82 + i * 28
        s += line(36, y + 20, 334, y + 20, L) + txt(40, y + 14, a, 12, FG, "start", 500) + txt(334, y + 14, b, 10.5, F2, "end")
    s += arrow(350, 150, 400, 150, A)
    s += rect(400, 100, 300, 100, A, CARD, 1.4) + txt(550, 130, "last_visit_time", 12, A, "middle", 500) + txt(550, 152, "WebKit epoch value", 12, FG, "middle") + txt(550, 174, "converted to date/time", 12, FG, "middle") + txt(550, 192, "with a timestamp tool", 11, F2, "middle")
    s += rect(400, 220, 300, 60, L, BG) + txt(550, 246, "Cookies, bookmarks, login data", 11.5, FG, "middle") + txt(550, 264, "encrypted: not readable here", 11.5, A, "middle")
    return _svg(W, H, s, "Illustration of the UC Browser History database table fields and timestamp conversion")

def uc_activity():
    W, H = 960, 200
    s = line(60, 100, 900, 100, F2, 1)
    pts = [("google.co.uk", "normal"), ("sky.com", "normal"), ("bbc.co.uk", "normal"), ("google.com", "normal"), ("sleuth", "normal"), ("bing.com", "normal"), ("netclean", "normal"), ("search in incognito", "private")]
    for i, (a, k) in enumerate(pts):
        x = 90 + i * 112
        c = A if k == "private" else T
        s += f'<circle cx="{x}" cy="100" r="7" fill="{BG}" stroke="{c}" stroke-width="2"/>' + txt(x, 80 if i % 2 == 0 else 134, a, 11.5, FG, "middle", 500)
    s += txt(60, 180, "Order of the scripted session as described in the report. These are scenario steps, not recovered timestamps.", 11, A, "start", 500)
    return _svg(W, H, s, "Scripted browsing sequence: seven normal-mode sites followed by one private-mode search")

# ---------- SOC projects: card art ----------
def dark_card():
    inner = grid(480, 300)
    inner += rect(60, 40, 170, 200, T, CARD, 1.5) + txt(145, 62, "32-bit DLL", 11, T, "middle", 500, 1.2)
    for j, (n, e, c) in enumerate((( ".text", 6.09, L), (".text1", 5.13, L), (".rdata", 3.22, L), (".data", 7.71, A), (".ndata", 7.94, A))):
        y = 76 + j * 30
        inner += rect(72, y, 146, 22, c, BG) + txt(80, y + 15, n, 10.5, FG, "start", 500) + txt(210, y + 15, f"{e:.2f}", 10, c if c == A else F2, "end")
    inner += txt(145, 232, "SECTION ENTROPY", 9, F2, "middle", 400, 1.2)
    inner += arrow(232, 140, 290, 140, A)
    inner += rect(296, 96, 130, 88, A, CARD, 1.5) + txt(361, 126, "README.[ID].TXT", 10.5, A, "middle", 500) + txt(361, 146, "file.[ID]", 10.5, F2, "middle") + txt(361, 166, "T1486", 10.5, T, "middle", 500)
    inner += txt(24, 285, "ILLUSTRATION · NOT A SAMPLE VIEW", 10, F2, "start", 500, 1.5)
    return _svg(480, 300, inner, "Illustration: a packed DLL with high-entropy sections leading to a ransom note and renamed files", "")

def vuln_card():
    inner = grid(480, 300)
    inner += rect(40, 50, 150, 70, A, CARD, 1.5) + txt(115, 78, "nginx", 11, F2, "middle") + txt(115, 104, "1.15.5", 22, A, "middle", 600)
    inner += rect(290, 50, 150, 70, T, CARD, 1.5) + txt(365, 78, "nginx", 11, F2, "middle") + txt(365, 104, "1.30.4", 22, T, "middle", 600)
    inner += arrow(192, 85, 288, 85, T) + txt(240, 76, "Ansible", 10, T, "middle", 500)
    inner += line(290, 112, 192, 112, F2, 1, "3 3") + txt(240, 128, "rollback", 9.5, F2, "middle")
    inner += txt(40, 168, "OPENVAS · HIGHEST FINDING", 9.5, F2, "start", 500, 1.2)
    inner += rect(40, 176, 400, 16, L, BG) + rect(40, 176, 392, 16, A, A) 
    inner += txt(40, 214, "BASELINE  9.8", 10.5, A, "start", 500) 
    inner += rect(40, 226, 400, 16, L, BG) + rect(40, 226, 3, 16, T, T) 
    inner += txt(40, 262, "nginx 1.30.4  0.0 (Log)", 10.5, T, "start", 500)
    inner += txt(456, 283, "ILLUSTRATION", 9.5, F2, "end", 500, 1.5)
    return _svg(480, 300, inner, "Illustration: nginx upgraded from 1.15.5 to 1.30.4 with a rollback path, and the severity falling from 9.8 to 0.0 for nginx", "")

def phish_card():
    inner = grid(480, 300)
    inner += rect(60, 40, 360, 190, T, CARD, 1.5) + line(60, 40, 240, 150, L) + line(420, 40, 240, 150, L)
    for j, (k, v, c) in enumerate((("From", "medequip-solutions", F2), ("Return-Path", "medequip-invoices", A), ("Reply-To", "free-mail address", A))):
        y = 160 + j * 22
        inner += txt(80, y, k, 10.5, F2, "start", 500, 1) + txt(400, y, v, 10.5, c, "end", 500)
    for j, (k, c) in enumerate((("SPF fail", A), ("DKIM none", A), ("DMARC fail", A))):
        inner += rect(88 + j * 110, 244, 100, 22, c, BG) + txt(138 + j * 110, 259, k, 10, c, "middle", 500)
    inner += txt(24, 289, "ILLUSTRATION · THREE SENDER IDENTITIES", 10, F2, "start", 500, 1.5)
    return _svg(480, 300, inner, "Illustration: an envelope with three different sender identities and failed SPF, DKIM and DMARC checks", "")

# ---------- SOC projects: case diagrams ----------
def dark_lifecycle():
    stages = [("Initial access", "Varies by affiliate", "Reported", F2), ("Execution", "rundll32.exe loads DLL", "Observed", T), ("Persistence", "None seen in sandbox", "Not seen", F2),
              ("Command & control", "2 domains (Moderate)", "Rule-based", A), ("Impact", "Encrypt, rename, note", "Observed", T)]
    inner = ""
    for i, (a, b, c, col) in enumerate(stages):
        x = 12 + i * 150
        inner += rect(x, 40, 134, 96, col, CARD, 1.5) + txt(x + 67, 66, a, 11.5, FG, "middle", 600) + txt(x + 67, 92, b, 9.5, F2, "middle") + txt(x + 67, 122, c.upper(), 9.5, col, "middle", 500, 1.2)
        if i < 4: inner += arrow(x + 134, 88, x + 150, 88, F2)
    inner += txt(12, 24, "ATTACK LIFECYCLE · STAGES AS EVIDENCED IN THE REPORT", 10, F2, "start", 500, 1.2)
    inner += txt(12, 166, "Reported = from published reports on DarkSide, not visible in this sample.", 10, F2) + txt(12, 184, "Observed = seen in sandbox data for the assigned sample.", 10, F2)
    return _svg(760, 200, inner, "Diagram: DarkSide attack lifecycle stages and how each is evidenced")

def ansible_flow():
    steps = [("Baseline", "OpenVAS scan"), ("Syntax check", "no errors"), ("Dry run", "--check"), ("Backup", "old binary kept"), ("Patch", "1.15.5 to 1.30.4"), ("Verify", "curl + version"), ("Re-scan", "Greenbone")]
    inner = ""
    for i, (a, b) in enumerate(steps):
        x = 8 + i * 106
        col = A if i in (0,) else (T if i >= 4 else F2)
        inner += rect(x, 40, 94, 70, col, CARD, 1.5) + txt(x + 47, 68, a, 11, FG, "middle", 600) + txt(x + 47, 90, b, 9, F2, "middle")
        if i < 6: inner += arrow(x + 94, 75, x + 106, 75, F2)
    inner += line(8 + 4 * 106 + 47, 112, 8 + 4 * 106 + 47, 146, A, 1.2, "4 3") + line(8 + 3 * 106 + 47, 146, 8 + 4 * 106 + 47, 146, A, 1.2, "4 3") + line(8 + 3 * 106 + 47, 146, 8 + 3 * 106 + 47, 112, A, 1.2, "4 3")
    inner += txt(8 + 3 * 106 + 47, 166, "rollback_nginx.yml restores the backup", 10, A, "middle", 500)
    inner += txt(8, 24, "REMEDIATION WORKFLOW · RECONSTRUCTED FROM THE REPORT", 10, F2, "start", 500, 1.2)
    return _svg(760, 184, inner, "Diagram: remediation workflow from baseline scan through dry run, backup, patch, verification and re-scan, with a rollback path")

def phish_flow():
    inner = txt(8, 20, "WHAT THE READER SEES VS WHAT SENT IT", 10, F2, "start", 500, 1.2)
    inner += rect(8, 34, 220, 90, F2, CARD, 1.2) + txt(118, 56, "Visible sender", 10, F2, "middle", 500, 1) + txt(118, 84, "billing@", 11.5, FG, "middle", 500) + txt(118, 102, "medequip-solutions.com", 11.5, FG, "middle", 500)
    inner += rect(270, 34, 220, 90, A, CARD, 1.5) + txt(380, 56, "Actual sending domain", 10, A, "middle", 500, 1) + txt(380, 84, "Return-Path, Message-ID:", 10.5, F2, "middle") + txt(380, 102, "medequip-invoices.com", 11.5, A, "middle", 500)
    inner += rect(532, 34, 220, 90, A, CARD, 1.5) + txt(642, 56, "Replies go to", 10, A, "middle", 500, 1) + txt(642, 84, "free-mail address", 11.5, A, "middle", 500) + txt(642, 102, "(not the vendor domain)", 10, F2, "middle")
    inner += arrow(228, 79, 268, 79, F2) + arrow(490, 79, 530, 79, F2)
    inner += txt(8, 150, "Both links place the vendor name in a subdomain of an unrelated registrable domain, and the two links differ from each other.", 10.5, F2)
    return _svg(760, 170, inner, "Diagram: the visible sender, the actual sending domain and the reply address are three different identities")

# ---------- electrical experience card art ----------
def tower_card():
    inner = grid(480, 300)
    inner += line(240, 40, 150, 250, T, 1.5) + line(240, 40, 330, 250, T, 1.5) + line(190, 150, 290, 150, T, 1.2) + line(205, 110, 275, 110, T, 1.2) + line(170, 200, 310, 200, T, 1.2)
    inner += line(150, 250, 330, 250, T, 1.5) + line(190, 150, 290, 250, L) + line(290, 150, 190, 250, L)
    for y in (110, 150):
        inner += line(205 if y == 110 else 190, y, 20, y + 30, A, 1) + line(275 if y == 110 else 290, y, 460, y + 30, A, 1)
    inner += txt(24, 285, "ILLUSTRATION · TRANSMISSION LINE", 10, F2, "start", 500, 1.5)
    return _svg(480, 300, inner, "Illustration: a transmission tower with conductors", "")

def wiring_card():
    inner = grid(480, 300)
    inner += rect(60, 60, 110, 70, T, CARD, 1.5) + txt(115, 100, "Supply", 11, FG, "middle", 500)
    inner += rect(190, 60, 110, 70, A, CARD, 1.5) + txt(245, 90, "Transformer", 11, FG, "middle", 500) + txt(245, 108, "500 kVA", 10, A, "middle")
    inner += rect(320, 60, 110, 70, T, CARD, 1.5) + txt(375, 100, "Distribution", 11, FG, "middle", 500)
    inner += arrow(170, 95, 188, 95, F2) + arrow(300, 95, 318, 95, F2)
    for j in range(4):
        inner += line(375, 130, 90 + j * 100, 200, L) + rect(60 + j * 100, 200, 60, 34, L, BG) + txt(90 + j * 100, 221, ("Circuit", "Circuit", "Circuit", "Circuit")[j], 9.5, F2, "middle")
    inner += txt(24, 285, "ILLUSTRATION · INSTALLATION", 10, F2, "start", 500, 1.5)
    return _svg(480, 300, inner, "Illustration: supply, transformer and distribution to circuits", "")
