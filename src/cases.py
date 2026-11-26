from lib import *
import svgs

SK = lambda items: '<div class="skills-demo">' + "".join(f"<span>{i}</span>" for i in items) + "</div>"
ACAD = '<span class="badge">Academic forensic case study</span>'

# =====================================================================
def alexa():
    hero = ('<figure class="hero-shot"><img src="assets/img/alexa-echo-devices.webp" alt="Project photograph of an Amazon Echo Dot and an Echo Show" width="629" height="481" decoding="async">'
            '<figcaption><span>Exhibit <b>ALX-01</b></span><span>Project photograph · UTC+0</span></figcaption></figure>')
    S = []
    S.append(("intro", "Project introduction",
      '<p>Amazon Echo devices keep little on the device itself and hold much of their evidence in the cloud. This research asked what an investigator can recover through an official route, a GDPR Subject Access Request, and how reliable and complete that evidence is.</p>'
      '<p>Two devices were studied: an Echo Show whose telemetry covered 160 days, and an Echo Dot used in a controlled test over 23 days. The two data sets turned out to hold different kinds of evidence.</p>'
      '<div class="note-box"><b>Academic research</b>The scenario is a simulated household burglary between 01:00 and 03:00. This is a research investigation, not a real-world criminal case.</div>'))
    S.append(("overview", "Investigation overview",
      kv([("Research area", "IoT and Cloud Forensics"), ("Devices", "Amazon Echo Dot (5th generation) and Echo Show"),
          ("Acquisition method", "Amazon GDPR Subject Access Request, Article 15 UK GDPR"), ("Analysis", "Python in Google Colaboratory, cross-checked in Magnet AXIOM"),
          ("Research context", "Simulated household burglary, 01:00 to 03:00"), ("Frameworks", "ACPO Principles of Digital Evidence; Zawoad and Hasan artefact taxonomy; Reith, Carr and Gunsch process model")])
      + stats([("160", "days of Echo Show telemetry", "am"), ("23", "days of Echo Dot data", "te"), ("32", "files in the SAR archive", ""), ("844", "items in AXIOM", "")])))
    S.append(("question", "Research question",
      '<p class="q">How can cloud-hosted digital evidence obtained through official data access mechanisms be acquired, examined and interpreted during an IoT forensic investigation?</p>'
      + '<h3>Objectives</h3><ul><li><strong>Literature and frameworks.</strong> Examine IoT forensic research and the difficulties it reports.</li><li><strong>Artefact analysis.</strong> Identify and examine artefacts in data obtained through the SAR process.</li><li><strong>Comparative evaluation.</strong> Compare findings with current models and literature to judge how well existing methods cope.</li></ul>'))
    S.append(("background", "Background and context",
      '<p>Echo hardware uses encryption and proprietary firmware, which makes conventional imaging impractical. Evidence is spread across the device, the companion app and Amazon\'s cloud, and no standard procedure exists for IoT forensics. The forensic value of SAR data had not been thoroughly evaluated.</p>'
      + details("What is a Subject Access Request?", "<p>Under Article 15 of the UK GDPR and the Data Protection Act 2018, an account holder can ask a company for a copy of the personal data it holds. Amazon accepted the request through its privacy portal and returned a ZIP archive about one week later. The route is read-only: it cannot alter Amazon's data.</p>")
      + details("Why a simulated burglary?", "<p>The scenario gave the data a purpose. It framed the Echo Dot as a possible exhibit and let the analysis ask what each artefact could say about the 01:00 to 03:00 window, without implying that any real offence took place.</p>")))
    S.append(("evidence", "Evidence sources",
      '<ul><li><strong>Echo Show telemetry.</strong> 1,296 log entries across 12 namespaces, 2025-08-10 to 2026-01-16. Network, system and device-state data only.</li>'
      '<li><strong>Echo Dot behavioural data.</strong> Voice utterances, call history, music activity, sensor readings, messaging and account settings, 2026-02-11 onward.</li>'
      '<li><strong>The archive.</strong> 32 files in CSV, XLSX, HTML and JSON, delivered as a single ZIP.</li></ul>'
      + gallery([("alexa-sar-request-steps", "Exhibit ALX-02", "Steps in the Amazon app to request the data and the confirmation message.", "Three phone screens showing the request for Alexa data in the Amazon app")])))
    S.append(("tools", "Tools and technologies",
      SK(["Amazon GDPR SAR", "Python", "Google Colaboratory", "Magnet AXIOM Examine v9.10", "Seaborn / Matplotlib"])
      + '<p style="margin-top:18px">No forensic tool was found that parses Amazon SAR archives in a standardised way. Google Colaboratory was the only viable analysis platform identified, and AXIOM served as a cross-check.</p>'))
    S.append(("acquisition", "Acquisition methodology",
      panel("Acquisition workflow", "Illustration", '<div class="dscroll">' + svgs.alexa_workflow() + '</div>',
            "Explanatory diagram of the process described in the dissertation. Not an original screenshot.", True)
      + flow([("Scenario", "Develop the simulated burglary and the two-device design."), ("Request", "Submit the SAR through Amazon's privacy portal using the account holder's own login."),
              ("Receive", "Archive delivered about a week after the request. Original ZIP kept unaltered."), ("Analyse copies", "All processing done on working copies, with an audit trail of dates.")])
      + '<p><strong>ACPO principles.</strong> The SAR route is read-only, so no data was altered at source. A record of request and receipt dates was kept.</p>'
      + '<p>' + st("lim") + 'Hash verification was not used, because the SAR process offers no independent source to verify against.</p>'))
    S.append(("analysis", "Examination and analysis",
      '<p>The work followed the eight stages below, using the dissertation\'s method.</p>'
      + flow([("Scenario", "Research and scenario development."), ("SAR", "Amazon GDPR Subject Access Request."), ("Organise", "Acquire and organise the data."), ("Echo Show", "Examine telemetry."),
              ("Echo Dot", "Analyse behavioural artefacts."), ("Compare", "Cross-device comparison."), ("Verify", "Cross-tool check in Magnet AXIOM."), ("Evaluate", "Findings and limitations.")])
      + gallery([("alexa-axiom-evidence-view", "Exhibit ALX-03", "Magnet AXIOM Examine showing 844 evidence items from the Echo archive.", "Magnet AXIOM evidence view listing CSV documents from the Echo archive")], True)))
    # Findings
    show = findings([
      ("conf", "<strong>Network identity.</strong> The same router identity and network were reported across all 108 Wi-Fi entries over 160 days, on WPA2-PSK. Identifiers are withheld on this page."),
      ("conf", "<strong>Firmware.</strong> Update count was 0 across 108 entries and one OS version was recorded throughout."),
      ("conf", "<strong>Uptime.</strong> The boot counter increased steadily across the 160 days, so no reboot or power cycle was recorded."),
      ("conf", "<strong>Connectivity anomaly.</strong> A 16-second outage on 2025-08-10 between 21:54:04Z and 21:54:20Z. A latency peak of 2,613 ms on the same date came from a second namespace."),
      ("rec", "<strong>Private network only.</strong> 108 captive-portal entries were blank, consistent with no public Wi-Fi use."),
      ("lim", "<strong>No user records.</strong> The Echo Show export held no voice, call or message artefacts. A separate SAR export would be needed.")])
    dot = findings([
      ("rec", "<strong>Voice utterances.</strong> The dissertation reports 110 recoverable utterances, each with a millisecond timestamp. Music and playback was the largest category."),
      ("rec", "<strong>Drop-In.</strong> Two incoming events: 2026-02-16 (63 s) and 2026-02-19 (33 s), both with audio and video streams, classed PRIVATE."),
      ("rec", "<strong>Music history.</strong> 61 tracks across Amazon Music and Apple Music, with track-level detail."),
      ("rec", "<strong>Temperature sensor.</strong> 1,025 readings, mean 21.3 °C, range 19.1 to 24.2 °C. This sensor is specific to the 5th generation Echo Dot."),
      ("rec", "<strong>Messaging.</strong> Two threads with partial content from test messages on 2026-03-06."),
      ("lim", "<strong>Speaker attribution gap.</strong> No active voice profile was shown in two snapshots, so speech cannot be tied to a speaker.")])
    S.append(("findings", "Findings",
      LEGEND
      + '<div class="dvs"><div class="show"><span class="label a">Echo Show</span><h3>Echo Show</h3><p class="big">Evidence relating primarily to technical device activity.</p><ul><li>Wi-Fi signal and network configuration</li><li>Device uptime and firmware integrity</li><li>One precisely timed connectivity anomaly</li></ul></div>'
        '<div class="dot"><span class="label t">Echo Dot</span><h3>Echo Dot</h3><p class="big">Evidence relating primarily to human behaviour.</p><ul><li>Spoken commands with timestamps</li><li>Drop-In calls, music history, sensor readings</li><li>Partial messaging content</li></ul></div></div>'
      + '<h3>Echo Show: technical device activity</h3>' + show
      + '<h3>Echo Dot: human behaviour</h3>' + dot
      + '<h3>What an unexplained status can and cannot show</h3><p>' + st("int") + 'The Echo Dot logged 127 connectivity entries: 60 OK and 67 UNREACHABLE (52.8%). In the controlled test, every power cycle between sessions produced an UNREACHABLE entry. Taken alone, such entries cannot prove interference.</p>'
      + '<h3>Cross-device comparison</h3>'
      + table(["Artefact category", "Echo Show", "Echo Dot", "Why it matters"],
          [["Device uptime and reboot history", ("Present", "y"), ("Absent", "n"), "Supports that the device was not powered off or reset."],
           ["Firmware and update history", ("Present", "y"), ("Absent", "n"), "Integrity can be assessed for the Echo Show only."],
           ["Network identity", ("Present", "y"), ("Absent", "n"), "Supports location checks from the Echo Show only."],
           ["Latency and anomaly logs", ("Present", "y"), ("Absent", "n"), "Only the Echo Show can evidence a network disturbance."],
           ["Captive portal / network type", ("Present", "y"), ("Absent", "n"), "Indicates a private network throughout."],
           ["Voice utterances with timestamps", ("Absent", "n"), ("Present", "y"), "Only the Echo Dot can show whether anyone spoke to it."],
           ["Music and media activity", ("Absent", "n"), ("Present", "y"), "Can place a person using the device at a given time."],
           ["Call and Drop-In history", ("Absent", "n"), ("Present", "y"), "Can show real-time communication."],
           ["Messaging artefacts", ("Absent", "n"), ("Present", "y"), "Partial content was recovered."]])))
    S.append(("dashboard", "Data visualisations",
      '<p>Charts below use figures stated in the dissertation. Where a source chart is shown as an image, it is the original output from the analysis.</p>'
      + panel("Device activity timeline", "Drawn to scale", '<div class="dscroll">' + svgs.alexa_timeline() + '</div>', "Echo Show and Echo Dot capture windows, with the 16-second anomaly on the first day of the Echo Show data.")
      + '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:20px">'
      + panel("Connectivity events", "Echo Dot", svgs.alexa_conn(), "60 OK entries and 67 UNREACHABLE out of 127.")
      + panel("Data category breakdown", "Magnet AXIOM", svgs.alexa_axiom(), "844 items, drawn to scale.") + '</div>'
      + gallery([("alexa-utterance-analysis", "Exhibit ALX-04 · Speech analysis", "Voice utterance categories and hours of day (UTC) from the Colab analysis.", "Bar charts of Echo Dot voice utterance categories and utterances by hour of day"),
                 ("alexa-artefact-availability", "Exhibit ALX-05 · Device comparison", "Artefact availability for Echo Show and Echo Dot.", "Bar chart comparing which artefact types are present on the Echo Show and the Echo Dot"),
                 ("alexa-connectivity-state", "Exhibit ALX-06 · Connectivity", "Device connectivity state over time, as captioned in the dissertation.", "Stacked bars of connectivity OK and UNREACHABLE events by date"),
                 ("alexa-temperature-readings", "Exhibit ALX-07 · Sensor", "1,025 Echo Dot temperature readings with the mean marked.", "Line chart of Echo Dot temperature readings with a mean of 21.3 degrees Celsius")], True)
      + '<div class="note-box"><b>Open check</b>The category bars in the source utterance figure add up to 70, while the text reports 110 utterances. The figure is shown as originally produced, and the total should be reconciled before publication.</div>'))
    S.append(("gallery", "Visual evidence gallery",
      '<p>Original project images, shown at their source resolution. Select an image to enlarge it. Identifiers have been removed or cropped.</p>'
      + gallery([("alexa-echo-devices", "Exhibit ALX-01", "Project photograph of the two devices.", "Project photograph of an Amazon Echo Dot and an Echo Show"),
                 ("alexa-sar-request-steps", "Exhibit ALX-02", "Requesting the data from the Amazon app.", "Phone screens showing the Amazon data request steps"),
                 ("alexa-axiom-evidence-view", "Exhibit ALX-03", "AXIOM evidence view of the archive.", "Magnet AXIOM evidence view of the Echo archive"),
                 ("alexa-utterance-analysis", "Exhibit ALX-04", "Utterance analysis.", "Charts of Echo Dot voice utterances"),
                 ("alexa-artefact-availability", "Exhibit ALX-05", "Device comparison.", "Chart comparing artefact availability across the two devices"),
                 ("alexa-temperature-readings", "Exhibit ALX-07", "Temperature readings.", "Line chart of temperature sensor readings")])))
    S.append(("limits", "Limitations and challenges",
      findings([("lim", "<strong>Limited data scope.</strong> One account and two devices limit how far results generalise."),
                ("lim", "<strong>No hash verification.</strong> The SAR process offers no independent source to verify against, which limits formal chain of custody."),
                ("lim", "<strong>No standard tooling.</strong> No forensic tool parses Amazon SAR data. AXIOM treated the archive as generic documents and did not reconstruct cross-file timelines or surface the connectivity warnings."),
                ("lim", "<strong>Platform choice.</strong> Google Colaboratory was the viable analytical platform, but it sends data to Google's servers, which raises chain-of-custody questions in formal settings."),
                ("lim", "<strong>No coordinates.</strong> The export held no latitude or longitude."),
                ("lim", "<strong>Deleted data and third parties.</strong> Data deleted before the request cannot be recovered, and the archive may hold other people's personal data.")])))
    S.append(("skills", "Technical skills demonstrated",
      SK(["Cloud evidence acquisition", "Data access requests", "Python analysis", "Timeline reconstruction", "Artefact taxonomy", "Cross-tool verification", "Data visualisation", "Limitation analysis"])))
    S.append(("takeaway", "Final investigative takeaway",
      '<div class="takeaway"><p>Cross-device analysis gives a more complete forensic picture than examining either device on its own.</p>'
      '<small>The Echo Dot shows what a person did. The Echo Show shows what the device and network did. The 16-second anomaly is a precisely timed lead, but this research does not claim it proves the simulated burglary. It is an academic investigation, not a criminal prosecution.</small></div>'))
    return case_page("alexa-iot-forensics", "Forensic investigation of Amazon Alexa-enabled IoT devices", "Amazon Alexa IoT Forensics",
        "Academic case study evaluating cloud-based evidence acquisition and artefact interpretation across an Amazon Echo Dot and Echo Show using a GDPR Subject Access Request.",
        "ALX-01 · Flagship", "Evaluating cloud-based evidence acquisition and forensic artefact interpretation across Amazon Echo Dot and Echo Show.",
        ACAD + '<span class="badge">IoT &amp; Cloud</span>', hero, S, 0)

# =====================================================================
def raid():
    hero = panel("Reconstruction", "Illustration", svgs.raid_card(), "Four images combined into one. Explanatory illustration.", True)
    S = []
    S.append(("intro", "Project introduction", '<p>A desktop computer was examined in a suspected antiques theft and fraud scenario. The work rebuilt a four-disk RAID set into a single image, then examined the operating system drive for evidence of user activity.</p>'
      '<div class="note-box"><b>Academic scenario</b>Names and personal details of the case subject are withheld. The scenario is a simulated assessment, not a real prosecution.</div>'))
    S.append(("overview", "Investigation overview", kv([("Subject", "Desktop computer, suspected antiques theft and fraud (scenario)"), ("Evidence", "Disk images BEF1 and BEF2-1 to BEF2-4, plus other provided artefacts"), ("Operating system", "Windows 10 Pro"), ("Primary tools", "X-Ways Forensics, Magnet AXIOM, Windows Registry Recovery")])
      + stats([("4", "images combined", "am"), ("2", "disks examined: BEF1, BEF2-REBUILT", "te"), ("9", "antique images matched", ""), ("32,438", "media items in AXIOM", "")])))
    S.append(("question", "Investigation objectives", '<ul><li>Reconstruct a suspected RAID configuration.</li><li>Examine the operating system drive.</li><li>Investigate user activity.</li><li>Identify relevant Windows Registry artefacts.</li><li>Examine file-system and application-specific evidence.</li><li>Validate important artefacts through hexadecimal analysis.</li><li>Document findings.</li></ul>'))
    S.append(("background", "Background and context", '<p>The scenario concerns suspected sale of antiques online under a false identity. A desktop was seized and imaged. The system drive was supplied as BEF1 and four further drives, thought to belong to a RAID-like set, as BEF2-1 to BEF2-4.</p>'
      + details("What is a JBOD / Linear RAID?", "<p>JBOD (just a bunch of disks) in linear mode joins disks end to end into one larger volume, without striping or parity. Choosing the correct mode and disk order is what makes the rebuilt volume readable.</p>")))
    S.append(("evidence", "Evidence sources", '<ul><li><strong>BEF1.</strong> The main drive holding Windows and the user profile.</li><li><strong>BEF2-1 to BEF2-4.</strong> Four drive images connected through a RAID adapter.</li><li>Nine supplied reference artefacts and images used for comparison.</li></ul>'))
    S.append(("tools", "Tools and technologies", SK(["X-Ways Forensics", "Magnet AXIOM", "RegRipper", "Windows Registry Recovery", "MFT Stampede"])
      + '<p style="margin-top:18px">MFT Stampede was used to convert raw timestamp values. For example, the Windows installation value converted to Monday 7 October 2019, 12:03:24 UTC, matching the date recorded in the registry and in AXIOM.</p>'
      + gallery([("raid-timestamp-conversion", "Exhibit RDW-02", "Timestamp conversion in MFT Stampede.", "Timestamp conversion tool showing a raw value converted into several date formats")])))
    S.append(("acquisition", "Acquisition methodology",
      '<p>The imaged files were copied from a read-only share to a working location and unzipped, and a case was created in X-Ways. The BEF2 series was reconstructed as follows.</p>'
      + panel("RAID reconstruction", "Illustration", '<div class="dscroll">' + svgs.raid_process() + '</div>', "The process as described in the report. Explanatory reconstruction, not a screenshot.", True)
      + flow([("Menu", "Specialist &gt; Reconstruct RAID System."), ("Order", "Arrange BEF2-1, BEF2-2, BEF2-3, BEF2-4."), ("Location", "Choose where to save the reconstructed disk."), ("Mode", "Select JBOD/Linear and confirm."), ("Image", "Press ALT+C to create the image.")])
      + gallery([("raid-xways-reconstruction", "Exhibit RDW-01", "X-Ways during image creation of the rebuilt disk (title bar cropped).", "X-Ways Forensics window showing a progress dialog while creating a disk image")])))
    S.append(("analysis", "Examination and analysis",
      flow([("Organise", "Evidence organisation."), ("Disk exam", "Disk examination in X-Ways."), ("RAID", "RAID reconstruction."), ("Windows", "Windows artefact investigation."), ("Registry", "Registry examination."), ("Deleted", "Deleted-file investigation."), ("Verify", "Manual verification."), ("Report", "Reporting.")])
      + panel("Reading user activity", "Illustration", '<div class="dscroll">' + svgs.raid_activity() + '</div>', "How independent artefacts support one another. Explanatory reconstruction.", True)
      + '<h3>Artefacts examined</h3>'
      + details("NTUSER.DAT", "<p>The recent-documents key for .jpg files listed eight items. Opening each showed they were the antique images under investigation.</p>")
      + details("SAM registry", "<p>A user account with relative identifier 0x3E9 (1001 decimal) was present, the first standard account after the default administrator. A password-hint artefact was also found and matched AXIOM.</p>")
      + details("SOFTWARE and SYSTEM registry", "<p>Windows 10 Pro, build 16299 (version 1709), installed 7 October 2019 at 12:03:24. The last shutdown was recorded as 28 October 2019 at 14:14:28. These values matched between Windows Registry Recovery and AXIOM.</p>")
      + details("SECURITY registry", "<p>The SECURITY hive was copied with the other hives for examination alongside SAM, SOFTWARE and SYSTEM.</p>")
      + details("Shellbags and UsrClass.dat", "<p>Shellbags held folder traces for the art and furniture folders, at node slots 11 and 12. The thumbnail view state indicated use of the thumbnail cache.</p>")
      + details("Jump Lists and LNK files", "<p>The antique images had been opened in the Microsoft Photos app, and four were pinned. LNK shortcut files in the Recent folder were consistent between X-Ways and AXIOM, with matching sizes and timestamps.</p>")
      + details("Deleted files and the Recycle Bin", "<p>Only one file was found in the Recycle Bin. The report suggests this may reflect permanent deletion with Shift+Delete, which is an interpretation.</p>")))
    S.append(("findings", "Findings", LEGEND + findings([
      ("rec", "<strong>Rebuilt data.</strong> The rebuilt disk held antique images in art and furniture folders, an encrypted archive, and a private folder with an encrypted document."),
      ("rec", "<strong>Media.</strong> AXIOM listed 32,438 media items, of which 32,150 were pictures. The nine antique images were located and extraction was complete for each."),
      ("conf", "<strong>SHA-256 comparison.</strong> The nine images from the online listing and the recovered images produced identical SHA-256 values."),
      ("rec", "<strong>User activity.</strong> Registry, shellbag, jump list and LNK artefacts each referred to the same antique files and folders."),
      ("conf", "<strong>Manual validation.</strong> Key artefacts were inspected in raw hexadecimal data and internal file structures."),
      ("int", "<strong>Report conclusion.</strong> The report concludes that the artefacts link the account holder to the sale. This portfolio reads the artefacts as consistent with that, within an academic scenario.")])
      + '<p style="margin-top:18px">Credentials and password material recovered in the exercise are deliberately not reproduced here.</p>'))
    S.append(("gallery", "Visual evidence gallery", '<p>The screenshots in this report are small, so only the legible ones are shown, at source resolution.</p>' + gallery([
      ("raid-xways-reconstruction", "Exhibit RDW-01", "X-Ways during image creation.", "X-Ways Forensics window with a progress dialog"),
      ("raid-timestamp-conversion", "Exhibit RDW-02", "Timestamp conversion.", "Timestamp conversion tool window")])))
    S.append(("limits", "Limitations and challenges", findings([
      ("lim", "<strong>Attribution.</strong> Artefacts tie files to an account. Tying them to a named person needs more corroboration than registry data alone."),
      ("lim", "<strong>Wording.</strong> The source report calls its evidence conclusive. Evidence strength depends on the whole record, so this page treats the report's wording as its own conclusion."),
      ("lim", "<strong>Credential handling.</strong> A credential hash was checked with an online lookup service, a practice that real casework would avoid."),
      ("lim", "<strong>No limitations section.</strong> The source report has none, so these points are reflections added for this portfolio.")])))
    S.append(("skills", "Technical skills demonstrated", SK(["RAID reconstruction", "Disk examination", "Windows Registry analysis", "Shellbags", "Jump Lists", "LNK files", "Hex verification", "SHA-256 comparison", "Timestamp conversion"])))
    S.append(("takeaway", "Final investigative takeaway", '<div class="takeaway"><p>Independent Windows artefacts that point at the same files make a stronger picture than any one of them.</p><small>Rebuilding the RAID set made the data readable. The registry, shellbags, jump lists and LNK files then agreed with one another and with the hash comparison. The result supports a reading of user activity, within an academic scenario.</small></div>'))
    return case_page("raid-windows-forensics", "RAID reconstruction &amp; Windows digital forensics", "RAID & Windows Forensics",
        "Academic case study on RAID reconstruction and Windows artefact analysis using X-Ways, Magnet AXIOM and registry tools.",
        "RDW-02", "Examining disk structures, Windows artefacts and user activity through an advanced forensic investigation.", ACAD + '<span class="badge">Disk &amp; Windows</span>', hero, S, 1)

# =====================================================================
def snap():
    hero = panel("Platforms compared", "Illustration", svgs.snap_card(), "Explanatory illustration. Not a device screenshot.", True)
    S = []
    S.append(("intro", "Project introduction", '<p>Snapchat stores its data in application databases that differ between platforms. This investigation compared what could be recovered from an Android phone and an iPhone using the same approach.</p><div class="note-box"><b>Academic case study</b>Names, usernames, emails and device identifiers from the exercise are withheld. All illustrations are labelled.</div>'))
    S.append(("overview", "Investigation overview", kv([("Android", "Samsung Galaxy S20+ 5G, full file system"), ("iOS", "iPhone, full file system"), ("Tools", "Cellebrite Physical Analyzer; Magnet AXIOM named in the analysis"), ("Integrity", "Hash recorded before extraction and compared after analysis")])
      + stats([("2", "platforms", ""), ("3", "Snapchat stores seen on Android only", "am"), ("6", "device details seen on iOS only", "te"), ("0", "hash values changed", "")])))
    S.append(("question", "Investigation objective", '<p class="q">Uncover the structure, behaviour and functionality of Snapchat on iOS and Android using Cellebrite Physical Analyzer.</p>'))
    S.append(("background", "Background and context", '<p>Snapchat is a messaging application with features aimed at privacy, such as My Eyes Only, so it is a useful case for showing how application design shapes what remains on a device.</p>'
      + details("What is a write-ahead log?", "<p>A database writes changes to a separate log before applying them to the main file. The log can hold recent changes that are not yet in the database. The Snapchat database log was about 4 MB on Android and about 2 MB on iOS.</p>")))
    S.append(("evidence", "Evidence sources", '<ul><li><strong>Android.</strong> Full file system extraction (legacy extraction type) of a Samsung SM-G986B.</li><li><strong>iOS.</strong> Full file system extraction of an iPhone.</li></ul>'
      + gallery([("snap-cellebrite-database-view", "Exhibit SNP-01", "Cellebrite Physical Analyzer database view on iOS (path bar cropped).", "Cellebrite Physical Analyzer showing a Snapchat database table on iOS")], True)))
    S.append(("tools", "Tools and technologies", SK(["Cellebrite Physical Analyzer", "Magnet AXIOM"])))
    S.append(("acquisition", "Acquisition methodology", panel("Evidence extraction workflow", "Illustration", '<div class="dscroll">' + svgs.snap_workflow() + '</div>', "Explanatory reconstruction of the process in the report.", True)
      + '<p>Hash values were noted before extraction so they could be compared after analysis. A matching hash shows the examination did not change the extracted data.</p>' + panel("Hash verification", "Illustration", svgs.snap_hash(), "The report states that no hash value changed on either device. Values are not published here.", True)))
    S.append(("analysis", "Examination and analysis", '<p>Twelve areas were examined on each device. The map below shows where the report documents results.</p>'
      + table(["Area examined", "Result documented in the report"], [
          ["Device information", ("Yes. Detailed on iOS, limited on Android", "y")], ["Application data", ("Yes. Snapchat account details on both", "y")],
          ["Contacts", ("Yes. Android: 4 of 10 Snapchat. iOS: 3 of 6", "y")], ["Messages", ("Yes. Matching conversations on both", "y")],
          ["Call information", ("Yes. Call logs on both", "y")], ["Media files", ("Yes. Images and videos counted", "y")],
          ["Application databases", ("Yes. arroyo.db on both", "y")], ["Location-related information", ("Examined. No result documented", "n")],
          ["Browser history", ("Examined. No result documented", "n")], ["Emails", ("Account email only", "p")], ["Device settings", ("Examined. No result documented", "n")], ["Cloud-related information", ("Examined. No result documented", "n")]])
      + panel("Application database architecture", "Illustration", '<div class="dscroll">' + svgs.snap_db() + '</div>', "Simplified structure built from the report's description. Explanatory reconstruction.", True)))
    S.append(("findings", "Findings", LEGEND + '<h3>Android and iOS compared</h3>' + table(["Item", "Android", "iOS"], [
        ["Model number", ("Not seen", "n"), ("Seen", "y")], ["OS version", ("Not seen", "n"), ("Seen", "y")], ["Serial number", ("Not seen", "n"), ("Seen", "y")], ["IMEI", ("Not seen", "n"), ("Seen", "y")],
        ["Jailbreak status", ("Not seen", "n"), ("Seen", "y")], ["Network interfaces", ("Not seen", "n"), ("Seen", "y")],
        ["Snapchat Memories database", ("Seen", "y"), ("Not seen", "n")], ["My Eyes Only database", ("Seen", "y"), ("Not seen", "n")], ["Journal database", ("Seen", "y"), ("Not seen", "n")]])
      + findings([("rec", "<strong>Contacts.</strong> Android showed 4 Snapchat contacts out of 10. iOS showed 3 out of 6."),
                  ("rec", "<strong>Media on Android.</strong> 6,212 images, of which 1,241 were Snapchat images. 24 videos, of which 11 were Snapchat."),
                  ("rec", "<strong>Media on iOS.</strong> 94 videos in the examined directory, of which 3 were Snapchat."),
                  ("rec", "<strong>Messages.</strong> 26 conversation rows in the database view, matching the message artefact. The report notes signs of deleted messages."),
                  ("conf", "<strong>Integrity.</strong> Hash values at the start and end matched on both devices."),
                  ("int", "<strong>Report interpretation.</strong> The report reads the iOS result as showing that iOS is harder to extract Snapchat data from. This is a reading of one comparison, not a general rule.")])))
    S.append(("gallery", "Visual evidence gallery", '<p>The original screenshots in this report contain account names, emails and device identifiers, so only a cropped example is shown.</p>' + gallery([("snap-cellebrite-database-view", "Exhibit SNP-01", "Database view.", "Cellebrite Physical Analyzer database view")], True)))
    S.append(("limits", "Limitations and challenges", findings([("lim", "<strong>Not all data could be extracted.</strong> The report states that not every item can be recovered with Cellebrite."),
        ("lim", "<strong>Platform differences.</strong> Snapchat-specific stores appeared on Android and not on iOS, so the two results are not like for like."),
        ("lim", "<strong>Extraction type.</strong> Both extractions were of the legacy type."),
        ("lim", "<strong>Unreported categories.</strong> Location, browser, settings and cloud areas were examined but no results are documented.")])))
    S.append(("skills", "Technical skills demonstrated", SK(["Android analysis", "iOS analysis", "SQLite application databases", "Write-ahead logs", "Hash verification", "Cross-platform comparison"])))
    S.append(("takeaway", "Final investigative takeaway", '<div class="takeaway"><p>The same app leaves different evidence on different platforms, so findings from one cannot be assumed for the other.</p><small>iOS gave richer device-level details. Android gave more Snapchat-specific stores. Matching hash values support that the examination did not alter the data.</small></div>'))
    return case_page("snapchat-mobile-forensics", "Snapchat mobile application forensics", "Snapchat Mobile Forensics",
        "Academic comparative investigation of Snapchat artefacts on Android and iOS using Cellebrite Physical Analyzer and Magnet AXIOM.",
        "SNP-03", "A comparative investigation of Snapchat artefacts across Android and iOS environments.", ACAD + '<span class="badge">Mobile</span>', hero, S, 2)

# =====================================================================
def ucb():
    hero = panel("Controlled environment", "Illustration", svgs.uc_card(), "Explanatory illustration of residual browser artefacts.", True)
    S = []
    S.append(("intro", "Project introduction", '<p>Private browsing aims to leave less behind. This investigation ran normal and incognito sessions in UC Browser inside a controlled virtual machine, then looked for what remained on disk.</p>'
      '<div class="note-box"><b>Academic case study</b>The activity was scripted by the examiner, so what was done is known. The report does not claim every private action was reconstructed.</div>'))
    S.append(("overview", "Investigation overview", kv([("Environment", "Windows 10 virtual machine in Oracle VM VirtualBox"), ("Configuration", "8 GB RAM, four processor cores, 30 GB virtual hard drive"), ("Browser", "UC Browser, normal and incognito modes"), ("Tools", "FTK Imager, X-Ways, DB Browser for SQLite, Magnet AXIOM")])
      + stats([("89,345", "items analysed in AXIOM", "te"), ("12", "matching cookie results", ""), ("323", "potential browser activity artefacts", "am"), ("12", "tables in the History database", "")])))
    S.append(("question", "Investigation objective", '<p class="q">What browser activity, private-browsing traces and residual artefacts can be recovered from a controlled Windows environment?</p>'))
    S.append(("background", "Background and context", '<p>Chromium-style browsers keep history, cookies and cache in per-user folders. Even when history is cleared, fragments can remain in unallocated space. UC Browser keeps its data under the user\'s AppData folder, and several of its files are encrypted.</p>'
      + details("Confirmed visit or potential activity?", "<p>A confirmed visit is one the examiner can match to activity actually performed, such as a history row for a site that was opened. A potential or system-generated artefact is a record that implies web activity without showing that this user opened the page, such as a cached URL, an autofill suggestion or a background request. AXIOM's 323 potential browser activity items are of this second kind: the report notes these URLs were not visited in the virtual machine.</p>")))
    S.append(("evidence", "Evidence sources", '<ul><li>The virtual machine\'s virtual disk, converted to a raw image.</li><li>The UC Browser History database and related folders under the user profile.</li><li>Microsoft Edge data, because Edge was used to download the UC Browser installer.</li></ul>'
      + panel("Virtual machine configuration", "Illustration", svgs.uc_vm(), "Configuration as stated in the report. Explanatory reconstruction.", True)
      + gallery([("uc-vm-hardware", "Exhibit UCB-01", "VirtualBox hardware step: memory and processors (source image, small).", "VirtualBox dialog for choosing memory and processor count")])))
    S.append(("tools", "Tools and technologies", SK(["Oracle VM VirtualBox", "FTK Imager", "X-Ways Forensics", "DB Browser for SQLite", "Magnet AXIOM"])
      + table(["Tool", "Strengths", "Limitations"], [["DB Browser for SQLite", "Direct access to raw databases", "Needs SQL knowledge, slow"], ["X-Ways Forensics", "Carving, raw disk access, deleted file recovery", "Little automation for browsers"], ["Magnet AXIOM", "Automated parsing, timelines", "Can hide low-level data"]])))
    S.append(("acquisition", "Acquisition methodology", '<p>The virtual disk was converted to a raw image with FTK Imager (File &gt; Create Disk Image). The image was saved as a multi-segment raw set, and the first segment was loaded into X-Ways after a refined volume snapshot.</p>'
      + flow([("Create VM", "VirtualBox, Windows 10."), ("Install", "Windows, then UC Browser."), ("Browse", "Seven sites in normal mode, one search in incognito."), ("Image", "FTK Imager to raw .dd."), ("Examine", "X-Ways, SQLite, AXIOM.")])
      + panel("Scripted browsing session", "Scenario design", '<div class="dscroll">' + svgs.uc_activity() + '</div>', "Sequence as described in the report. These are not recovered timestamps.", True)))
    S.append(("analysis", "Examination and analysis", '<h3>X-Ways search hits</h3><p>Keyword searches for the visited sites found URL fragments in unstructured and unallocated space. Their file system fields were blank, which suggests data outside normal file structures.</p>'
      + '<h3>SQLite History database</h3>' + panel("Database structure", "Illustration", svgs.uc_sqlite(), "Fields as described in the report. Explanatory reconstruction.", True)
      + '<p>Cookies, bookmarks and login data are encrypted, so they could not be examined in SQLite.</p>'
      + '<h3>Magnet AXIOM</h3><p>AXIOM parsed search history, cookies, LNK files, cached records, potential browser activity and locally accessed files.</p>'
      + gallery([("uc-axiom-search-results", "Exhibit UCB-02", "AXIOM search results (detail pane cropped).", "Magnet AXIOM matching results listing Google search entries"), ("uc-sqlite-cookies-table", "Exhibit UCB-03", "A cookies table opened in DB Browser for SQLite (title bar cropped).", "DB Browser for SQLite showing a table with creation, host and name columns")])))
    S.append(("findings", "Findings", LEGEND + findings([
      ("rec", "<strong>Recovered URL fragments.</strong> Google queries, video links and a download portal appeared in search hits, residual data from earlier activity."),
      ("conf", "<strong>Search history.</strong> AXIOM showed searches for the sites the examiner had visited, with URLs and timestamps."),
      ("rec", "<strong>Cookies.</strong> 12 matching results out of 89,345 items, with names, expiry dates and host names."),
      ("conf", "<strong>Execution.</strong> A UC Browser LNK file with creation and access times showed the browser was installed and run."),
      ("pot", "<strong>Potential browser activity.</strong> 323 items, mostly cached URLs, autofill and background requests. They were not visits made in the virtual machine."),
      ("rec", "<strong>Cache and local files.</strong> Cached records and frequent access to files in the browser's own folder support active use."),
      ("rec", "<strong>Storage location.</strong> Data was found under AppData\\Local\\UC Browser\\User Data_*, which gives a target for future extraction."),
      ("hyp", "<strong>An advert-style site.</strong> One entry, uc123.com, may be the site opened in incognito mode. The report does not confirm this.")])
      + table(["Artefact", "Confirmed visit?", "Reading"], [["History row for a visited site", ("Yes", "y"), "User-initiated, matches the script"], ["Search hit in unallocated space", ("Residual", "p"), "Shows earlier activity, source file unknown"], ["Cookie record", ("Residual", "p"), "Shows a site set a cookie"], ["Potential browser activity (323)", ("No", "n"), "Not shown to be a visit in this VM"]])))
    S.append(("gallery", "Visual evidence gallery", '<p>Source screenshots are small, so only legible ones are shown, at source size. Select to enlarge.</p>' + gallery([
      ("uc-vm-hardware", "Exhibit UCB-01", "VirtualBox hardware step.", "VirtualBox hardware dialog"), ("uc-axiom-search-results", "Exhibit UCB-02", "AXIOM search results.", "Magnet AXIOM search results"), ("uc-sqlite-cookies-table", "Exhibit UCB-03", "SQLite table view.", "DB Browser for SQLite table view")])))
    S.append(("limits", "Limitations and challenges", findings([
      ("lim", "<strong>No embedded video.</strong> UC Browser could not play embedded YouTube video here, so live video could not be tested."),
      ("lim", "<strong>Encrypted files.</strong> Cookies, bookmarks and login data were encrypted in the History database folder."),
      ("lim", "<strong>Password hashes.</strong> Some were found in AXIOM, and attempts to decrypt them failed."),
      ("lim", "<strong>Private browsing.</strong> The report shows traces remained after incognito use. It does not claim every private action was reconstructed.")])))
    S.append(("skills", "Technical skills demonstrated", SK(["Virtual lab design", "Disk imaging", "SQLite examination", "Carved URL analysis", "Cookie and cache analysis", "Artefact classification", "Tool comparison"])))
    S.append(("takeaway", "Final investigative takeaway", '<div class="takeaway"><p>Private browsing reduces traces but leaves residue, and good analysis separates a confirmed visit from a potential artefact.</p><small>Knowing where UC Browser stores its data lets an examiner target the right files. The 323 potential activity items show why a tool\'s label is not the same as evidence of a user action.</small></div>'))
    return case_page("uc-browser-forensics", "Browser forensics of UC Browser", "UC Browser Forensics",
        "Academic case study of UC Browser history, cookies, cache and private-browsing traces in a controlled Windows virtual machine.",
        "UCB-04", "Investigating browser activity, private browsing traces and residual digital artefacts in a controlled Windows environment.", ACAD + '<span class="badge">Browser</span>', hero, S, 3)


# =====================================================================
#  SOC ANALYST PROJECTS
# =====================================================================
TRN = '<span class="badge">Training exercise</span>'
def _hero_art(svg, cap_l, cap_r):
    return f'<figure class="hero-shot"><div class="dscroll" style="background:#0a1224;padding:6px">{svg}</div><figcaption><span>{cap_l}</span><span>{cap_r}</span></figcaption></figure>'

def darkside():
    hero = _hero_art(svgs.dark_card(), "Illustration", "Not a sample view")
    S = []
    S.append(("intro", "Project introduction",
      '<p>A threat profile of one ransomware sample, written as a cyber threat intelligence exercise for a simulated client, NorthByte Cybersecurity Ltd. The sample is a 32-bit Windows DLL that 54 of 62 antivirus engines on VirusTotal label as DarkSide.</p>'
      '<p>The profile answers three questions a SOC needs answered: what is this file, what does it do, and what should we do about it. It ends with indicators, ATT&amp;CK mappings, a detection rule and six prioritised actions.</p>'
      '<div class="note-box"><b>Training exercise, draft status</b>This is a draft (v1.0, for peer review) written on public-source intelligence. The original carries a TLP:AMBER marking, and this page is a summary. Several items in the original are still marked to complete, and they are listed under Limitations rather than hidden.</div>'))
    S.append(("overview", "Report overview",
      kv([("Subject", "DarkSide ransomware, 32-bit Windows DLL"), ("Analyst", "The portfolio owner"), ("Report date", "20 November 2026"), ("Status", "v1.0, draft for peer review"),
          ("Sample identity", "SHA-256 156335b9…0090673 (public hash); 55,810 bytes; imphash 6c8408bb…e68763"),
          ("Sources", "VirusTotal GUI and API v3 metadata, CISA/FBI advisory AA21-131A, and published reports from Trend Micro, Mandiant, Sophos, Qualys and others")])
      + stats([("54/62", "engines detect the file", "am"), ("5", "independent YARA rules match", "te"), ("15", "ATT&CK technique rows mapped", ""), ("6", "prioritised recommendations", "")])))
    S.append(("judgement", "Key judgements",
      LEGEND.replace('verified directly in the investigation output', 'directly supported by sample data') +
      findings([
        ("conf", "<strong>The sample is DarkSide ransomware (High confidence).</strong> 54 of 62 detections, vendor labels that agree on the family, five independent YARA rules, and sandbox runs that show ransom notes and renamed files."),
        ("int", "<strong>The brand is defunct but the model continues (Moderate confidence).</strong> The sample was compiled on 5 April 2021 and first seen on 1 May 2021. DarkSide closed in May 2021, and its operators are linked to BlackMatter and then ALPHV/BlackCat."),
        ("int", "<strong>Overall confidence is Moderate.</strong> Detection and sandbox data are strong. Static analysis is limited to VirusTotal metadata, and some checks are still outstanding.")])))
    S.append(("history", "History and lineage",
      table(["Date", "Event"], [["August 2020", "DarkSide first spotted"], ["November 2020", "Ransomware-as-a-service model launched"], ["March 2021", "DarkSide v2.0 released"], ["5 April 2021", "Compile timestamp of the assigned sample"],
        ["7 May 2021", "Colonial Pipeline attack; FBI later attributes it to DarkSide"], ["May 2021", "DarkSide announces it is shutting down"], ["31 July 2021", "BlackMatter appears, assessed as DarkSide returning"],
        ["November 2021", "BlackMatter shuts down"], ["April 2022", "FBI advisory links BlackCat to DarkSide and BlackMatter"]])
      + '<p style="margin-top:14px">DarkSide is sold as a service: operators build the ransomware and affiliates carry out the intrusions, so attribution depends on the affiliate. The operator group is tracked as GOLD WATERFALL by Sophos, and Mandiant tracks affiliate clusters UNC2465, UNC2628 and UNC2659. A claim that FIN7 operated DarkSide could not be corroborated, so it is not reported as attribution.</p>'))
    S.append(("lifecycle", "Attack lifecycle",
      panel("Attack lifecycle", "Illustration", '<div class="dscroll">' + svgs.dark_lifecycle() + '</div>', "Stages drawn from the report. Initial access varies by affiliate and is not visible in the sample itself.", True)
      + '<p>Reported initial access routes include spearphishing links, password spraying against VPN, and exploitation of exposed services. Operators have used PowerShell, Certutil and Bitsadmin to fetch the ransomware and PsExec and RDP to spread it. Stolen data went to Tor leak sites and file-sharing services.</p>'))
    S.append(("static", "Static analysis",
      '<p>The file is a small DLL with two non-standard sections and two sections whose entropy points to encrypted content. It statically imports a single function, so the rest of its behaviour is hidden until run time.</p>'
      + table(["Section", "Entropy", "Observation"], [[".text", "6.09", "Main code, below 7.0"], [".text1", "5.13", "Non-standard name; probably holds the entry point"], [".rdata", "3.22", "Very small read-only data"], [".data", ("7.71", "p"), "Likely packed or encrypted data"], [".ndata", ("7.94", "p"), "Non-standard name, highest entropy"]])
      + findings([("rec", "<strong>One static import.</strong> DisableThreadLibraryCalls only. Sandbox data shows the other APIs resolved at run time."),
                  ("int", "<strong>Packing is inferred, not named.</strong> VirusTotal did not name a packer. The evidence is indirect: entropy, section names, the single import and a ClamAV label of Packed."),
                  ("lim", "<strong>No signature data.</strong> VirusTotal returned none, so the file is treated as unsigned with Moderate confidence.")])))
    S.append(("behaviour", "Behaviour in sandbox runs",
      findings([("conf", "<strong>Execution via rundll32.exe</strong> with the DLL as the target."), ("rec", "<strong>Ransom note and renamed files.</strong> A README.[8-hex ID].TXT note and files renamed with an 8-hex suffix; the ID changes per run."),
                ("rec", "<strong>Environment checks.</strong> Disk, debugger, OS version and processor count were queried before encryption."), ("pot", "<strong>Long sleeps</strong> were tagged, which may be time-based evasion."),
                ("lim", "<strong>No persistence mechanism seen.</strong> Registry writes were ordinary WMI entries, not Run keys."),
                ("lim", "<strong>Mutex and registry names are not used for detection</strong>, because they matched Windows or sandbox noise.")])))
    S.append(("iocs", "Indicators of compromise",
      table(["Type", "Indicator (defanged)", "Confidence"], [["SHA-256", "156335b95ba216456f1ac0894b7b9d6ad95404ac7df447940f21646ca0090673", "High"], ["MD5", "f587adbd83ff3f4d2985453cd45c7ab1", "High"], ["Imphash", "6c8408bb5d7d5a5b75b9314f94e68763", ("Moderate", "p")],
        ["Domain", "baroquetees[.]com", ("Moderate", "p")], ["Domain", "rumahsia[.]com", ("Moderate", "p")], ["Domain", "survey-smiles[.]com", ("Low", "n")], ["File name", "README.[8-hex ID].TXT", "High"]])
      + '<p style="margin-top:14px">The two C2 domains come from Emerging Threats rules on TLS server names. The third was contacted in a sandbox run but is not corroborated. Fifteen sandbox IP addresses were not assessed, because many look like shared cloud infrastructure and need enrichment before any blocking.</p>'))
    S.append(("attack", "MITRE ATT&amp;CK mapping",
      table(["Tactic", "Technique", "Evidence"], [["Execution", "T1218.011 Rundll32", "Sandbox command lines; Sigma rule matched"], ["Execution", "T1047 WMI", "calls-wmi tag; wmiprvse.exe started (Moderate)"], ["Defense evasion", "T1027 / T1027.007", "Entropy and encoding signatures; dynamic API resolution"],
        ["Defense evasion", "T1497.001 / .003, T1622", "System checks, long sleeps, debugger detection"], ["Discovery", "T1082", "OS version, processors, machine GUID"], ["Impact", "T1486", "Renamed files, ransom note, 54 ransomware labels"],
        ["Impact", "T1490", "Reported, not seen in sandbox data"], ["Initial access, lateral movement, exfiltration", "T1566.002, T1078, T1110.003, T1190, T1021.001, T1567.002", "Reported for DarkSide affiliates, not observable in this sample"]])
      + '<p style="margin-top:14px">Rows from published reports are kept apart from rows evidenced by this sample, so the mapping does not claim more than the sample shows.</p>'))
    S.append(("detection", "Detection",
      '<p>No verified strings were available, because the sample was not downloaded and the metadata gives no readable strings from a packed file. Guessing strings from other DarkSide samples would risk false positives, so the rule matches structure instead.</p>'
      + details("YARA rule DarkSide_OU", '<pre class="code">import "hash"\nimport "pe"\nimport "math"\nrule DarkSide_OU {\n  meta:\n    description = "DarkSide ransomware x86 DLL: exact SHA-256, or structural fingerprint"\n    date = "2026-11-20"\n  condition:\n    hash.sha256(0, filesize) == "156335b95ba216456f1ac0894b7b9d6ad95404ac7df447940f21646ca0090673" or\n    ( uint16(0) == 0x5A4D and pe.is_dll() and pe.machine == pe.MACHINE_I386 and\n      pe.imphash() == "6c8408bb5d7d5a5b75b9314f94e68763" and\n      for any s in pe.sections : ( s.name == ".text1" ) and\n      for any s in pe.sections : ( s.name == ".ndata" and math.entropy(s.raw_data_offset, s.raw_data_size) &gt; 7.5 ) )\n}</pre>')
      + '<p>' + st("lim") + 'The rule has not yet been tested. The test run against a clean file and a positive control is still to be done.</p>'))
    S.append(("recs", "Recommendations",
      table(["#", "Action", "Category"], [["1", "Block baroquetees[.]com and rumahsia[.]com at DNS, proxy and firewall, and retro-hunt logs", "Prevent"], ["2", "Deploy the YARA rule plus the Elastic and McAfee ATR DarkSide rules to EDR", "Detect"],
        ["3", "Hunt for rundll32.exe loading DLLs from Temp or ProgramData, README.*.TXT files and mass renames to an 8-hex extension", "Detect"], ["4", "Isolate and reimage confirmed hits, restore from offline backups, and check for data theft before restoring", "Respond"],
        ["5", "MFA and password-spray detection on VPN, patching of internet-facing systems, restricted RDP", "Prevent"], ["6", "Train staff to spot phishing links", "Prevent"]])))
    S.append(("limits", "Limitations and open items",
      findings([("lim", "<strong>Draft status.</strong> Version 1.0, awaiting peer review. The reviewer is not yet named."), ("lim", "<strong>MISP search</strong> results are still to be added."), ("lim", "<strong>MalwareBazaar</strong> record and family tag are still to be checked."),
                ("lim", "<strong>YARA test results</strong> are not yet recorded."), ("lim", "<strong>Recent reporting.</strong> The newest source found is from April 2022, and a check for 2025 to 2026 reporting is still to be done."),
                ("lim", "<strong>Static analysis rests on VirusTotal metadata.</strong> The sample itself was not downloaded or detonated by the analyst.")])))
    S.append(("skills", "Skills demonstrated", SK(["Threat intelligence reporting", "Malware triage", "Static analysis from metadata", "MITRE ATT&CK mapping", "IOC handling and defanging", "YARA rule design", "Confidence language", "Prioritised recommendations"])))
    S.append(("takeaway", "Final takeaway", '<div class="takeaway"><p>A good threat profile says what is known, what is reported and what is still open.</p><small>The sample is clearly DarkSide. What the profile adds is a split between what this file shows and what the wider campaign is reported to do, with confidence stated at each step and the unfinished work listed.</small></div>'))
    return case_page("darkside-threat-profile", "DarkSide ransomware threat profile", "DarkSide Ransomware Threat Profile",
        "Training-exercise threat profile of a DarkSide ransomware DLL: classification, lifecycle, static analysis, indicators, ATT&CK mapping and detection.",
        "SOC-01", "A cyber threat intelligence profile of a 32-bit ransomware DLL, with indicators, ATT&CK mapping and detection guidance.", TRN + '<span class="badge">Threat intelligence</span><span class="badge">Draft v1.0</span>', hero, S, 0, "soc")

def nginx():
    hero = _hero_art(svgs.vuln_card(), "Illustration", "Lab environment")
    S = []
    S.append(("intro", "Project introduction",
      '<p>A vulnerability management exercise on a lab server. A baseline OpenVAS scan rated the highest finding on the target at 9.8 (Critical), and the nginx findings were version-based. The task was to upgrade nginx from 1.15.5 to 1.30.4 with an Ansible playbook, prove it worked, and make sure it could be undone.</p>'
      '<div class="note-box"><b>Lab exercise</b>Carried out as part of a team exercise (Team A) on a lab server that other team members also scanned. The server address, account names and key material are withheld on this page.</div>'))
    S.append(("overview", "Project overview",
      kv([("Role", "Consultant on the nginx finding, Team A"), ("Date", "11 November 2026 (baseline scan on 5 November 2026)"), ("Target", "nginx 1.15.5, source-built under /usr/local/nginx, on an Ubuntu server"),
          ("Tooling", "Ansible core 2.20.1, OpenVAS / Greenbone, nginx, curl, nano"), ("Goal", "Upgrade to nginx 1.30.4, verify, and keep a tested rollback")])
      + stats([("1.15.5 → 1.30.4", "nginx version", "te"), ("ok=19 · changed=5", "play recap", ""), ("failed=0", "play recap", "te"), ("9.8 → 0.0", "nginx severity in the re-scan", "am")])))
    S.append(("method", "Approach",
      panel("Remediation workflow", "Reconstruction", '<div class="dscroll">' + svgs.ansible_flow() + '</div>', "Workflow reconstructed from the report. Not an original screenshot.", True)
      + flow([("Prepare", "Confirmed Ansible core 2.20.1, wrote ansible.cfg and a local inventory, and proved the setup with an ansible ping that returned pong."),
              ("Write the playbook", "patch_nginx.yml reads the installed version with nginx -V, removes old bundled-library build options, compares the version with the target, prints a plan, upgrades, then confirms the version and that the site responds."),
              ("Test first", "A syntax check passed. A dry run with --check reported current 1.15.5, target 1.30.4 and upgrade needed."),
              ("Patch", "The real run ended with ok=19, changed=5, unreachable=0, failed=0 and the message SUCCESS: nginx upgraded to 1.30.4."),
              ("Verify and re-scan", "nginx -v and a curl header check confirmed the new version, then a fresh Greenbone scan checked the result.")])
      + '<p>The version check makes the playbook safe to run repeatedly, because it changes nothing when the target version is already installed.</p>'))
    S.append(("evidence", "Evidence",
      gallery([("vuln-patch-playbook", "Exhibit NGX-01", "The first part of patch_nginx.yml in the editor: variables and version-check tasks.", "Terminal editor showing the first part of an Ansible playbook for patching nginx"),
               ("vuln-patch-verification", "Exhibit NGX-02", "End of the real run: SUCCESS message and play recap with ok=19, changed=5, failed=0.", "Terminal output showing the Ansible success message and a play recap with no failures")], True)))
    S.append(("rollback", "Rollback playbook",
      '<p>Because the lab was shared, a second playbook, rollback_nginx.yml, restores the vulnerable 1.15.5 binary from the backup that the patch playbook creates. It stops if no backup exists. A dry run showed current 1.30.4, rollback to 1.15.5, rollback needed and backup found. The real run stopped nginx, restored the old binary, started nginx and ended with ROLLED BACK: nginx is 1.15.5 again.</p>'
      + gallery([("vuln-rollback-run", "Exhibit NGX-03", "Real rollback run: nginx stopped, old binary restored, started again and 1.15.5 confirmed.", "Terminal output showing nginx being stopped, the old binary restored and nginx started again")])
      + '<p>The lab was reset to 1.15.5 this way, a fresh baseline was captured, and the patch was applied again to collect the final evidence. That second run also ended with ok=19, changed=5, failed=0. A curl header check returned HTTP 200 with a Server header of nginx/1.30.4.</p>'))
    S.append(("verify", "Verification with OpenVAS",
      '<p>A new Greenbone scan after the patch finished with status Done, dated 11 November 2026, 22:00 UTC. The task still showed 9.8 (Critical), so the report was opened to find out why.</p>'
      + findings([("conf", "<strong>The 9.8 is not nginx.</strong> It is an Apache Tomcat AJP finding (Ghostcat) on port 8009, a different service outside Team A\'s scope of nginx on port 80."),
                  ("conf", "<strong>nginx 1.30.4 is detected with no vulnerability raised.</strong> Both nginx entries in the Applications tab are at severity 0.0 (Log)."),
                  ("int", "<strong>Why the task score stayed high.</strong> Greenbone reports the highest score for the whole host, and the scan used the All IANA assigned TCP port list.")])
      + gallery([("vuln-openvas-applications", "Exhibit NGX-04", "Applications tab of the post-patch report with nginx 1.30.4 at 0.0 (Log). Top bar and report details cropped.", "Greenbone report Applications tab listing detected applications with severity 0.0")], True)
      + '<p>The Tomcat finding was recorded as out of scope, for the service owner to handle.</p>'))
    S.append(("issues", "Issues and lessons learned",
      table(["Issue", "Cause", "Fix"], [["Playbook could not be found", "A mistyped command that also created a stray file named --check", "Listed the folder, then re-ran with the correct file name"], ["Risk of a failed upgrade", "Upgrading a source-built service replaces the running binary", "Dry run, a backup before changes and a tested rollback"], ["Scan still showed 9.8", "The finding belonged to Tomcat, not nginx", "Opened the report, filtered by nginx, and recorded the Tomcat finding as out of scope"]])
      + '<p style="margin-top:14px">Testing with a syntax check and --check before a real run catches mistakes safely, a built-in version check makes a playbook repeatable, and a rollback plan should be tested before it is needed.</p>'))
    S.append(("recs", "Recommendations",
      findings([("int", "<strong>Inventory and flag end-of-life software</strong>, such as nginx 1.15.5."), ("int", "<strong>Re-scan after every change</strong> to prove the fix."), ("int", "<strong>Keep remediation in Ansible</strong>, so the same fix can be applied across servers."), ("int", "<strong>Hide the version</strong> in banners with server_tokens off;.")])))
    S.append(("limits", "Limitations",
      findings([("lim", "<strong>Lab environment.</strong> A team exercise, not a production change with a change-approval process."), ("lim", "<strong>Single finding.</strong> The scope was nginx on port 80. Other findings, including the Tomcat one, were not remediated."),
                ("lim", "<strong>Scanner evidence only.</strong> Closure rests on the Greenbone re-scan and a version check, with no separate penetration test.")])))
    S.append(("skills", "Skills demonstrated", SK(["Vulnerability scanning (OpenVAS / Greenbone)", "Ansible playbooks", "Dry runs and syntax checks", "Backup and rollback planning", "Patch verification", "Scan result triage", "Remediation reporting"])))
    S.append(("takeaway", "Final takeaway", '<div class="takeaway"><p>A fix is not finished until a re-scan agrees, and a patch is not safe until it can be undone.</p><small>The nginx finding closed, the site stayed online, and the one remaining Critical result was correctly traced to a different service rather than being mistaken for a failed patch.</small></div>'))
    return case_page("nginx-ansible-remediation", "Remediating nginx with Ansible", "nginx Remediation with Ansible",
        "Lab vulnerability management: upgrading nginx 1.15.5 to 1.30.4 with Ansible, a tested rollback playbook, and verification with an OpenVAS re-scan.",
        "SOC-02", "Upgrading a vulnerable web server with a tested, reversible playbook, then proving the result with a re-scan.", TRN + '<span class="badge">Vulnerability management</span>', hero, S, 1, "soc")

def phish():
    hero = _hero_art(svgs.phish_card(), "Illustration", "Training sample")
    S = []
    S.append(("intro", "Project introduction",
      '<p>An email claiming to be from the supplier MedEquip Solutions reached the Accounts Payable mailbox of MediSure Health Network on Monday 9 September 2024 at 07:14 UTC. It said Invoice #MSH-2024-0912 was past due and demanded $18,740.00 within 24 hours, with a threat to halt medical supply delivery.</p>'
      '<p>The message was examined as a SOC case-study exercise and classified as malicious invoice fraud (business email compromise).</p>'
      '<div class="note-box"><b>Training sample</b>The domains, addresses and hash are fabricated indicators. Reputation lookups such as MXToolbox, VirusTotal and AbuseIPDB were deliberately not used, because they do not apply to made-up indicators.</div>'))
    S.append(("overview", "Case overview",
      kv([("Classification", "Malicious: invoice fraud / BEC phishing"), ("Target", "Accounts Payable mailbox, MediSure Health Network (fictional)"), ("Impersonated vendor", "MedEquip Solutions (fictional)"), ("Method", "Manual inspection of raw .eml headers and MIME structure, base64 decoding and SHA-256 hashing of the attachment")])
      + stats([("$18,740", "requested within 24 h", "am"), ("3", "sender identities", "te"), ("2", "credential-harvesting links", ""), ("3", "authentication checks failed or absent", "am")])))
    S.append(("headers", "Header and authentication analysis",
      '<p>The only Received header names mail.medequip-invoices.com at 192.168.0.50, a private (RFC 1918) address. A legitimate internet sender cannot present a private address to a public mail server, which points to an incomplete or falsified header chain. With a single hop there is no relay path to follow and no IP reputation to check.</p>'
      + table(["Check", "Result", "Meaning"], [["SPF", ("fail", "n"), "The sending IP is not authorised for medequip-invoices.com, and that domain differs from the visible From domain, so it would not align even on a pass."], ["DKIM", ("none", "n"), "The message is unsigned, so origin and integrity cannot be verified."], ["DMARC", ("fail, action=quarantine", "n"), "The visible From domain failed authentication and alignment, and the published policy calls for quarantine."]])
      + '<p style="margin-top:14px">Analogy: SPF is the guest list at the door, DKIM is the signature on a letter, and DMARC is the host\'s instruction for what to do when either check fails.</p>'
      + gallery([("phish-received-auth-headers", "Exhibit INV-01", "Received and authentication headers from the raw .eml, highlighted.", "Raw email headers with the received and authentication results highlighted")], True)
      + '<p>' + st("lim") + 'The headers record the DMARC disposition but do not show what the gateway actually did with the message, so the message trace should be checked to confirm it was held.</p>'))
    S.append(("identity", "Sender identity",
      panel("Sender identity", "Illustration", '<div class="dscroll">' + svgs.phish_flow() + '</div>', "Three different identities in one message.", True)
      + table(["Header", "Value"], [["From", "billing@medequip-solutions.com, the vendor identity shown to the reader"], ["Return-Path / Message-ID", "medequip-invoices.com, the lookalike domain that actually sent it"], ["Reply-To", "A free-mail address that diverts replies away from the vendor domain"]])
      + '<p style="margin-top:14px">The X-Mailer header shows PHPMailer 6.1.2, a general-purpose PHP mailing library often used by bulk and phishing mailers, rather than a billing system. The message is flagged X-Priority 1 to add urgency, and the Message-ID contains the string acctrecovery, echoing the Reply-To address.</p>'
      + gallery([("phish-sender-identity", "Exhibit INV-02", "Sender-related headers from the raw .eml.", "Raw email headers showing the From, Reply-To and mailer fields")], True)))
    S.append(("links", "Links, tracking pixel and attachment",
      findings([("conf", "<strong>Link mismatch.</strong> The HTML Review &amp; Pay Invoice button and the plain-text link point to two unrelated registrable domains. Both put the vendor name in a subdomain to look familiar."),
                ("conf", "<strong>Tracking pixel.</strong> A hidden 1x1 image loaded over plain HTTP reports when the email is opened, telling the sender the mailbox is active."),
                ("conf", "<strong>Disguised attachment.</strong> The body promises a PDF, but the file is Invoice_MSH-2024-0912.html containing only a script block. This matches the HTML-smuggling pattern. In this sample the script is a placeholder with no executable content.")])
      + gallery([("phish-links-pixel-attachment", "Exhibit INV-03", "Links, hidden pixel and attachment from the .eml (defanged).", "Email source showing two phishing links, a hidden tracking pixel and an HTML attachment")], True)))
    S.append(("time", "Timestamp analysis",
      '<p>The Date header (07:14:50) and the receipt time (07:14:52) are in the correct order, so the header timestamps show no anomaly. The content is less consistent: it says accounts more than 30 days past due face suspension, yet the invoice was due on 7 September 2024, only two days before the email arrived.</p>'))
    S.append(("verdict", "Justification",
      '<p>This is an attempt at fraudulent vendor invoice spoofing. The basis is a private originating IP, a lookalike sending domain, SPF, DKIM and DMARC failures, a free-mail Reply-To, two distinct credential-harvesting links, a tracking pixel, an HTML attachment shown as a PDF, scripted mailer tooling, an overdue claim that contradicts its own dates, urgency, and threats aimed at a healthcare supply chain.</p>'))
    S.append(("iocs", "Indicators of compromise",
      table(["Type", "Indicator (defanged)"], [["Domain", "medequip-invoices[.]com"], ["Domain", "thebandalisty[.]com"], ["Domain", "secure-invoicepay[.]com"], ["Email", "medequip.accounts.recovery@gmail[.]com"],
        ["URL", "hxxps://medequip-billing-review[.]secure-invoicepay[.]com/login?ref=MSH20240912"], ["URL", "hxxps://medequip-billing-review[.]thebandalisty[.]com/login?ref=MSH20240912"], ["URL", "hxxp://thebandalisty[.]com/o/MSH20240912.gif (tracking pixel)"],
        ["File", "Invoice_MSH-2024-0912.html"], ["SHA-256", "0bf21e8fa749d22699d9333ef244710492a689e15c5ea3f34537c64c319f575c"], ["Spoofed identity", "billing@medequip-solutions[.]com (confirm with MedEquip before blocking the vendor\'s real domain)"]])))
    S.append(("recs", "Recommendations",
      findings([("int", "<strong>Payment controls.</strong> Verify urgent invoices and bank-detail changes by phone using contact details already on file, and require dual approval."),
                ("int", "<strong>Email security.</strong> Apply SPF, DKIM and DMARC results consistently, enable impersonation protection for key vendor domains, tag external senders and flag Reply-To mismatches."),
                ("int", "<strong>Attachments and links.</strong> Block or sandbox external HTML attachments, enable time-of-click URL scanning and block remote images by default."),
                ("int", "<strong>Training.</strong> Invoice-fraud awareness and phishing simulations for finance and procurement staff."),
                ("int", "<strong>Response.</strong> Block the indicators, search mailboxes for related messages and remove them, review proxy and DNS logs, reset credentials for anyone who entered them, and notify MedEquip.")])))
    S.append(("limits", "Limitations",
      findings([("lim", "<strong>Training sample.</strong> Indicators are fabricated, so no reputation or threat-intelligence checks were possible."), ("lim", "<strong>Single hop.</strong> No relay path exists to trace."), ("lim", "<strong>Gateway action unconfirmed.</strong> The message trace is needed to confirm quarantine.")])))
    S.append(("skills", "Skills demonstrated", SK(["Email header analysis", "SPF, DKIM and DMARC interpretation", "Phishing triage", "MIME and attachment inspection", "IOC extraction and defanging", "Business email compromise recognition", "Response recommendations"])))
    S.append(("takeaway", "Final takeaway", '<div class="takeaway"><p>Authentication results should have stopped this message, but the headers alone do not prove they did.</p><small>Attackers register new lookalike domains cheaply, which is why payment verification, impersonation protection and finance-focused training are needed alongside SPF, DKIM and DMARC.</small></div>'))
    return case_page("invoice-fraud-phishing-analysis", "Invoice fraud phishing analysis", "Invoice Fraud Phishing Analysis",
        "SOC case-study exercise: analysing a business email compromise invoice message, with header and authentication analysis, indicators and response recommendations.",
        "SOC-03", "Triage of a suspected invoice-fraud email: headers, authentication, sender identity, links, attachment and response.", TRN + '<span class="badge">Email analysis</span>', hero, S, 2, "soc")

ALL = [alexa, raid, snap, ucb, darkside, nginx, phish]
