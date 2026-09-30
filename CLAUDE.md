# Portfolio website: working notes

Orlando (Lando) Adams's portfolio site. Final-year architecture student at Oxford Brookes. The portfolio is for architecture practice AND film/TV art departments, so copy should present both, not film only.

## Live site
- https://adamsorlando111-web.github.io/Portfolio/ (capital P matters; lowercase gives 404)
- GitHub Pages serves `main` branch root. A push to `main` goes live in about 2 minutes.

## Files
- `index.html`: the whole site in one file (HTML, CSS, JS inline). Hash routing: `#home`, `#architecture`, `#photography`, `#written`, `#contact`. Project anchors (`#set-one`, `#capoeira`, `#common-ground`, `#light`, `#offset`, `#graduation-station`, `#kochi`) open the right view/year automatically (see `sub` map in the script).
- `img/`: web-size JPGs, long edge about 1,600 to 1,800 px, quality about 78. Prefixes: `so-` Set One, `cg-` Common Ground, `cp-` Capoeira, `dc-` Digital Culture light studies, `ph-` photography, `me.jpg` portrait.
- `js/lenis.min.js`: vendored Lenis smooth scroll (MIT, licence in `js/lenis-LICENSE`). No CDN dependency.
- `.nojekyll`: keep it.

## Rules from Lando
- Images must come ONLY from his OneDrive folder `C:\Users\adams\OneDrive\Architecture\Portfolio` (never from the 5002 submission files).
- Never use em dashes in any copy.
- Keep copy short and plain. Don't invent facts (titles, locations, briefs); leave a visible placeholder and ask.
- Commit as `Claude <noreply@anthropic.com>` so commits show Verified.

## Design system
- Dark, single theme. Tokens in `:root`: ink #0F1113, panel #181B1E, line #2A2E33, text #E8E4DC, mute #8E949A, accent amber #E3A34A.
- Type: Inter Tight (Neue Haas Grotesk stand-in; real Neue Haas can't load from Google Fonts) + Courier Prime (typewriter) for captions, labels and story text.
- Subtle film-grain overlay (`body::after`).
- Renders shown as letterboxed "frames" with mono captions; drawings on white "plates".
- Image protection: right-click and drag blocked on images, copyright line in footer and Photography page.

## Motion and atmosphere (v2, Sept 2026)
- Refs Lando gave: locomotive.ca, awwwards.com/sleutelaar, archifol.io portfolios. He loves organic, atmospheric design, film grain and typewriter text: subtle but appreciable to a graphic designer.
- CSS layer is the `v2: motion, atmosphere, typewriter` block at the end of the `<style>`.
- Loader (once per session), page curtain between views, Lenis smooth scroll, fixed header that hides on scroll down, amber scroll progress line.
- Full-screen hero (so-aerial.jpg) with drifting mist, parallax and a faint projector flicker. Marquee reacts to scroll speed and direction.
- Reveals: `[data-reveal]` fade up, `[data-rimg]` image mask wipe, `[data-split]` word-by-line rise (all h2 auto-split). Eyebrows, `.num` and `[data-type]` type on like a typewriter with an amber caret. Courier text has a faint ink bleed (text-shadow).
- Animated grain, vignette and slow drifting light behind content. Custom cursor ("View" over images) and magnetic buttons on mouse devices only.
- Everything switches off under prefers-reduced-motion; a 6 s fallback shows all content if JS fails.
- Reveals use viewport checks, not IntersectionObserver (clip-path hid targets from IO in Chrome).

## Structure
- Home: portrait, intro, at-a-glance strip, 6 best-work tiles, Request CV (WhatsApp button + copyable phone/email).
- Architecture (public title "Selected work"): collapsible `<details>` per year: A levels (WIP only: EPQ floating home, Prek Toal; Terrarium House, outdoor classroom for Wymondham College; both placeholders), Year 1 (WIP only: Capoeira gym with images; Graduation Station placeholder), Year 2 (Offset Studios placeholder, Common Ground, Set One Studios, Light studies; open by default), Year 3 (in progress).
- Photography: chapter index, Chapter 01 Kochi, India (12 to 19 Dec 2025, grouped by capture day, story placeholder), Unsorted (2 photos, locations unknown). Oxford, Norfolk, Cambridge chapters to come.
- Written (WIP only): dissertation card (working title placeholder; topic: post-apocalyptic TV and architecture, Station Eleven and The Last of Us).

## Contact details shown on site
- WhatsApp 07484 750 932 (preferred), email adamsorlando111@gmail.com, based Oxford and Suffolk.

## Two versions: public and private WIP
- PUBLIC: GitHub Pages from `main` (URL above). Only finished work goes here.
- PRIVATE WIP: a Claude artifact, https://claude.ai/artifact/WYdkJ3zNnVrCpK8swg61DX ("Portfolio WIP"). Only Lando can open it unless he shares it. Shows an amber "Work in progress / private" tag (the tag hides itself on github.io).
- This repo is PUBLIC, so never push unfinished work to any branch here. Work in progress lives only in the artifact.
- ONE MASTER FILE builds both. The WIP artifact page is the master. In a new chat: `Artifact read` the WIP link, save it as `master.html` (scratchpad, not this repo), edit it, then run `python3 tools/build.py master.html` to get `index.html` (public) and `wip.html` (artifact page).
- Markers in the master: `<!--wip:start-->...<!--wip:end-->` and `/*wip:start*/.../*wip:end*/` are WIP only; `<!--pub:start ... pub:end-->` is public only; `<!--body-->` separates head from body.
- Publish WIP: Artifact publish `wip.html` with `url` = the WIP link and `files` = every `img/*` plus `js/lenis.min.js`.
- Go public (only when Lando says "publish" / "make it live"): commit the built `index.html` (+ any new images) to `main` and push. Never commit `master.html` or `wip.html`.
- WIP-only right now: A levels (EPQ floating home, Prek Toal; Terrarium House outdoor classroom for Wymondham College), Year 1 (Capoeira, Graduation Station) and the Capoeira home tile, and the Written page.
- Public since 30 Sept: rain on the hero (canvas, splashes on the letters of the name) and the name morph (big title closes onto one line and flies into the header on scroll).

## Workflow for updates
1. Lando drops images into his Portfolio folder (linked computer) or sends text in chat.
2. Make thumbnails on the device, stage the chosen ones, resize to web size, add to `img/`.
3. Edit `index.html`, check at 390 px width (no horizontal scroll), commit, push.
