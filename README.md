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

## Fill the placeholders
Search `src/` for: `[YOUR FULL PROFESSIONAL NAME]`, `[PROFESSIONAL EMAIL]`, `[LINKEDIN URL]`, `[GITHUB URL]`, `[LOCATION]`, `[INSTITUTION · DATES]`, `[JOB TITLE]`, and `YOUR-DOMAIN.example` (in `src/lib.py`). Rebuild afterwards.
Social links currently show a notice instead of navigating. Replace the `href="#" data-soon="..."` links with real URLs.

## Publish
Any static host works (Netlify, Vercel, Cloudflare Pages, GitHub Pages). Drag `dist/` onto Netlify Drop, or push it to a repo and point the host at the `dist` folder.
Custom domain: add the domain in the host's settings, then create the DNS records it shows (usually an A/ALIAS record for the root and a CNAME for `www`). Set `DOMAIN` in `src/lib.py` and rebuild so canonical, Open Graph and sitemap URLs are correct.

## Contact form
The form validates input and shows a confirmation, but it does not send anything. Connect it to a service (Formspree, Netlify Forms, your own endpoint) in `src/home.py` and `src/site.js`, then change the confirmation text.

## Add a new investigation
Add a function in `src/cases.py` that returns `case_page(...)` with a list of `(id, title, html)` sections, add it to `ALL`, add its entry to `PROJECTS` in `src/lib.py` and a card in `projects()` in `src/home.py`. Put cropped WebP images in `dist/assets/img/`.

## Privacy checklist before publishing
Screenshots from the source reports contained a student ID, university branding, names, emails, serial numbers and MAC/IP addresses. Only cropped images are included. Check any new image at full size before adding it, and strip metadata when exporting.


## Role views (added)
The home page has a switcher (Electrical Engineering / Digital Forensics / SOC Analyst). Anything marked `data-for="role1 role2"` shows only for those roles; the choice is remembered in the visitor's browser. Case pages set the role automatically.

- **Profile photos:** one per view. Save portraits (4:5, about 800x1000) as `assets/img/profile-electrical.webp`, `profile-forensics.webp` and `profile-soc.webp`. A missing one falls back to `profile.webp`, then to the placeholder.
- **CVs:** `src/cv.py` writes `CV-electrical-engineering.pdf`, `CV-digital-forensics.pdf` and `CV-soc-analyst.pdf`. Each role shows its own Download CV button. Fill the `[JOB TITLE]` and name placeholders there, then run `python3 src/cv.py && python3 src/build.py`.
- **SOC case studies:** `darkside()`, `nginx()` and `phish()` in `src/cases.py`. Server address, usernames and key details are deliberately withheld.
