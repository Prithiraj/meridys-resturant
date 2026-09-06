# Implementation notes

## Scope and design decisions

The requester approved implementation and publication to `Prithiraj/meridys-resturant`. The approved plan remains in `design-plan.md`. A brighter palette and more expressive editorial composition implement the follow-up request for vibrancy.

The site leads with a real steak photograph, generous serif type, an Exit 184 badge, and direct menu/directions actions. It moves through an image-led menu, warm story section, group/lounge cards, genuine review destinations, and a practical address/hours section. The route illustration is explicitly not to scale. No Three.js is used: genuine imagery carries the page; WebGL would add weight without helping a visit decision.

The release is a **public design preview**. This is an explicit departure from the original preference for an access-controlled preview: the requester asked for GitHub Pages publication, and a public Pages site is not a private review environment. Visible disclosures and `noindex` reduce confusion but do not provide access control. Business approval is still pending. Licensed stock imagery avoids publishing unlicensed business imagery and is never labeled as authentic Meridy’s photography.

## Architecture

The build is a Python script with a small escaped template renderer. All navigation, menu highlights, hours, disclosures, and calls to action render at build time. Pillow renders the original social share card. Google Fonts loads optional fonts with `display=swap`; system fonts remain usable when loading fails.

The browser receives static HTML, CSS, locally hosted images, and a small enhancement script. There are no runtime framework, package, map, analytics, or stock-image API dependencies. Native `details` works before JavaScript; JavaScript adds Escape/outside-click handling and active category indication.

`data/business.json` is the shared source for business facts, menu references, and source attribution. The menu is intentionally labeled **highlights**, not a complete current menu. No prices have been invented or copied as current. The disputed phone number is disclosed. No reservation, order, payment, capacity, dietary, or sourcing promise is invented.

## Images

Five original licensed photographs have 480, 900, and 1600 px WebP/JPEG variants. Each has a source page, photographer, license status, derivative checksum, dimensions, and byte count. Photographs are committed for deterministic offline builds. CSS makes visual crops; no generative food, service, room, or portion edits are made. Lazy loading is used below the fold, with the hero eager/high-priority.

## SEO and privacy

Every page has `noindex, follow`. `robots.txt` permits fetching those instructions; it does not falsely serve as access control. A sitemap is generated for a later reviewed migration, not submitted as an official restaurant property. Structured data describes a WebPage **about** a Restaurant instead of presenting the preview URL as an official restaurant domain. There are no aggregate ratings or opening-hours assertions in JSON-LD.

The website has no analytics, cookies, forms, accounts, local storage, or payment collection. GitHub Pages and Google Fonts receive ordinary resource requests; external business links lead to third-party sites when followed. This is disclosed publicly.

## Release process

A one-time archive import transfers locally authored source into the connected repository without needing local GitHub credentials. The import validates paths, preserves existing files outside its manifest, removes the bootstrap archive, and commits readable source. Subsequent builds use the normal `deploy.yml` workflow. Images were prepared by a separate, scoped repository workflow and committed with provenance. No secret values are stored in source or artifacts.

CI runs static integrity checks, Playwright browser checks at six widths, axe A/AA scans, no-JavaScript and reduced-motion cases, and three mobile Lighthouse runs. Deployment consumes the resulting `_site` artifact. Reports are retained as workflow artifacts; only measured results should be copied into release notes.
