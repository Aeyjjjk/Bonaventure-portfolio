# Digital Forensics & Cyber Investigations portfolio

Static site: plain HTML, CSS and JavaScript. No build step is needed to host it.

## Contents
- `dist/` the finished site. Upload this folder as it is.
  - `index.html` one-page portfolio (home, investigations, skills, method, about, contact)
  - four case-study pages (`alexa-iot-forensics.html`, `raid-windows-forensics.html`, `snapchat-mobile-forensics.html`, `uc-browser-forensics.html`)
  - `assets/downloads/CV.pdf` the CV behind every "Download CV" button
  - `assets/img/` WebP images (cropped to remove identifiers), `og.png` for link previews
  - `sitemap.xml`, `robots.txt`
- `src/` the generator. `python3 src/build.py` rebuilds `dist/`; `python3 src/cv.py` rebuilds the CV and OG image (needs Playwright).



## Add a new investigation
Add a function in `src/cases.py` that returns `case_page(...)` with a list of `(id, title, html)` sections, add it to `ALL`, add its entry to `PROJECTS` in `src/lib.py` and a card in `projects()` in `src/home.py`. Put cropped WebP images in `dist/assets/img/`.

## Privacy checklist before publishing
Screenshots from the source reports contained a student ID, university branding, names, emails, serial numbers and MAC/IP addresses. Only cropped images are included. Check any new image at full size before adding it, and strip metadata when exporting.

## Then other add-ons
