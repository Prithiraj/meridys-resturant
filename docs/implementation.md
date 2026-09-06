# Implementation notes

## Scope and design decisions

The requester approved implementation and publication to `Prithiraj/meridys-resturant`. The approved plan remains in `design-plan.md`. A brighter palette and more expressive editorial composition implement the follow-up request for vibrancy.

The site leads with a real steak photograph, generous serif type, an Exit 184 badge, and direct menu/directions actions. It moves through an image-led menu, warm story section, group/lounge cards, genuine review destinations, and a practical address/hours section. The route illustration is explicitly not to scale. No Three.js is used: genuine imagery carries the page; WebGL would add weight without helping a visit decision.

The release is a **public design preview**. This is an explicit departure from the original preference for an access-controlled preview: the requester asked for GitHub Pages publication, and a public Pages site is not a private review environment. Visible disclosures and `noindex` reduce confusion but do not provide access control. Business approval is still pending. Licensed stock imagery avoids publishing unlicensed business imagery and is never labeled as authentic Meridy’s photography.

## Architecture

The build is a Python script with a small escaped template renderer. All navigation, menu highlights, hours, disclosures, and calls to action render at build time. Pillow renders the original social share card. Google Fonts supplies optional fonts; system fonts remain usable when loading fails.

The browser receives static HTML, CSS, locally hosted images, and a small enhancement script. There are no runtime framework, package, map, analytics, or stock-image API dependencies. Native `details` works before JavaScript; JavaScript adds Escape/outside-click handling and active category indication.

`data/business.json` is the shared source for business facts, menu references, and source attribution. The menu is intentionally labeled **highlights**, not a complete current menu. No prices have been invented or copied as current. The disputed phone number is disclosed. No reservation, order, payment, capacity, dietary, or sourcing promise is invented.

## Images

Five original licensed photographs have 480, 900, and 1600 px WebP/JPEG variants. Each has a source page, photographer, license status, derivative checksum, dimensions, and byte count. Photographs are committed for deterministic offline builds. CSS makes visual crops; no generative food, service, room, or portion edits are made. Lazy loading is used below the fold, with the hero eager/high-priority.

## Typography and layout stability

The first Lighthouse pass exposed late web-font swaps moving the hero image. The implementation now preloads the three Google-hosted font resources actually requested by the test browser and requests `display=optional` instead of `swap`. This gives the intended typography an early fetch while allowing the fallback to remain stable when the web font arrives late. No font files are copied into this repository. If the Google Fonts API changes its resource URLs, review the preloads against its network requests; obsolete preloads should be updated or removed.

This choice deliberately favors readable, stable content on slow connections over forcing a late brand-font swap. The system-font layout is tested separately. References: [web.dev font best practices](https://web.dev/articles/font-best-practices) and [preloading optional fonts](https://web.dev/articles/preload-optional-fonts).

## SEO and privacy

Every page has `noindex, follow`. `robots.txt` permits fetching those instructions; it does not falsely serve as access control. A sitemap is generated for a later reviewed migration, not submitted as an official restaurant property. Structured data describes a WebPage **about** a Restaurant instead of presenting the preview URL as an official restaurant domain. There are no aggregate ratings or opening-hours assertions in JSON-LD.

The website has no analytics, cookies, forms, accounts, local storage, or payment collection. GitHub Pages and Google Fonts receive ordinary resource requests; external business links lead to third-party sites when followed. This is disclosed publicly.

## Release process

A one-time archive import transferred locally authored source into the connected repository without needing local GitHub credentials. The import validated paths, preserved existing files outside its manifest, removed the bootstrap archive, and committed readable source. The one-time import workflow was then removed. Subsequent builds use the normal `deploy.yml` workflow. Images were prepared by a separate, scoped repository workflow and committed with provenance. No secret values are stored in source or artifacts.

CI runs static integrity checks, Playwright browser checks at six widths, axe A/AA scans, no-JavaScript and reduced-motion cases, and three mobile Lighthouse runs. Deployment consumes the resulting `_site` artifact and verifies the served `build.json` commit against the workflow SHA. Reports are retained as workflow artifacts; only measured results should be copied into release notes.

Node packages are QA-only and are not deployed. Keep their lockfile maintained and review dependency-audit findings separately from visitor-facing runtime exposure. Automated accessibility or Lighthouse scores are not a security certification.
