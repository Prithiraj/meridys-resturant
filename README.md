# Meridy’s Restaurant & Lounge

A vibrant, mobile-first restaurant website, built for **Russell, Kansas** with warm cream, deep red, mustard, large photographic layouts, and obvious menu, call, and directions actions.

**Website:** https://prithiraj.github.io/meridys-resturant/

**Publication status: independent design preview, not an owner-approved official restaurant website.** Actual licensed photographs are used, but they are illustrative—not Meridy’s food, staff, or rooms. Every page is marked `noindex`; image disclosures, source notes, and menu limitations are visible. No unlicensed business photograph is republished.

## What is included

- Homepage, HTML menu highlights, photo credits/source/privacy page, and custom 404.
- Source-backed location, published hours with a caveat, working native telephone links, and Google Maps directions.
- Responsive image variants served locally; no runtime stock-photo API or hotlinks.
- Semantic HTML, native keyboard-operable navigation/FAQs, visible focus, reduced-motion support, and no-JavaScript fallback.
- Open Graph share card, page metadata, sitemap, and conservative WebPage/Restaurant structured data. No unapproved rating, price, reservation, or operating-hours schema.
- GitHub Actions build, static checks, browser/axe audits, three mobile Lighthouse runs, and Pages deployment.

## Documentation

[Design plan](docs/design-plan.md) retains all 17 approved planning sections and records the implementation addendum. Read [implementation notes](docs/implementation.md), [image rights](docs/image-rights.md), [launch checklist](docs/launch-checklist.md), and [QA scope](docs/qa.md).

## Run locally

Python 3.12+ is needed for the build; Pillow generates only the share card. No Python or Node server runs in production.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build.py
python tests/check_site.py
```

The default build uses the GitHub project path `/meridys-resturant`. For a local root preview:

```sh
SITE_URL=http://localhost:8000 python scripts/build.py
python -m http.server 8000 --directory _site
```

Before project-path tests, rebuild using the default `SITE_URL`:

```sh
unset SITE_URL
python scripts/build.py
npm ci --ignore-scripts
npx playwright install chromium
npm run test:browser
npm run test:lighthouse
```

Node 22+ and the Node dependencies are **development/QA only**. Browser tests start their own server on port 4173. Reports and screenshots are saved in `reports/`, and CI uploads them as a `quality-report` artifact. The site itself ships only static files, CSS, and a small enhancement script.

## Maintain the content

`data/business.json` is the central business record. Update facts only from approved evidence; maintain the source and approval notes. `templates/` contains the semantic page layouts, `public/assets/site.css` the visual system, and `public/assets/site.js` the progressive interactions.

Photograph sources, licenses, sizes, dimensions, and checksums live in `public/assets/images/manifest.json`. The build rejects missing or modified photographs whose provenance is not updated. Images are already committed; routine builds do not download them again.

Do not turn `preview` off to make the website official. The release guard requires verified business details, an approved full menu, authentic business imagery, and a reviewed content/metadata migration. See the [launch checklist](docs/launch-checklist.md).

## Deployment

GitHub Pages was already enabled for this repository. The `Build, test, and deploy Pages` workflow publishes `_site` after checks pass. Select **GitHub Actions** as the Pages source if repository settings are changed. No private token, API key, or backend is required. Do not place secrets in the public source or the generated site.

## Licensing

The repository does not grant a blanket license over restaurant trademarks or third-party photographs. Selected photos are used under their individually documented Unsplash license. The proposed typeset wordmark is not claimed to be the restaurant’s official logo. Google Fonts serves Fraunces and Source Sans 3; font files are not redistributed in this repository.
