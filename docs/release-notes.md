# Release notes — published design preview

## Publication

- **Live website:** https://prithiraj.github.io/meridys-resturant/
- **Menu highlights:** https://prithiraj.github.io/meridys-resturant/menu.html
- **Deployed source commit:** `c74c94330a5d48632b6f5e04e7abc54fc646c0df`
- **Successful workflow:** https://github.com/Prithiraj/meridys-resturant/actions/runs/34058037599
- **Verified UTC time:** 2026-09-06 20:29:53 UTC.
- **Release status:** Public independent design preview, not an operator-approved official restaurant website.

The deployment job reported success. Its subsequent HTTP checks retrieved the published homepage, menu page, and `build.json`, verified the expected page content, and confirmed that the served build SHA exactly matched the deployed source commit. The in-chat web-fetch environment did not permit opening the newly generated Pages URL; publication verification was performed by the GitHub-hosted deployment job, not by claiming a successful in-chat browser visit.

Documentation-only commits after this source SHA use `[skip ci]` and do not change the published website. Future normal pushes to `main` run the build, tests, and Pages deployment automatically.

## Delivered

A vibrant, responsive editorial homepage, an accessible menu-highlights page, a sources/photo-credits/privacy page, and a custom 404 page. The design uses cream, warm red, mustard, forest green, large food photography, readable type, an Exit 184 motif, and prominent Menu / Call / Directions actions. The shared business data lives in `data/business.json`.

Photography is real, licensed, and locally hosted in responsive JPEG/WebP variants. It is **illustrative stock photography, not photography of Meridy’s food, employees, or rooms**. Visible notices and the source register preserve that distinction. No invented prices, testimonials, ratings, ordering, booking, or payment workflow were added. No Three.js is required; photography remains the principal visual content.

The full approved plan and implementation addendum are preserved in [design-plan.md](design-plan.md). See [implementation.md](implementation.md), [image-rights.md](image-rights.md), [qa.md](qa.md), and [launch-checklist.md](launch-checklist.md).

## Measured quality results

Source: the `quality-report` artifact from the successful workflow linked above; artifact ID `9996603832`. Full reports and screenshots have a 14-day Actions retention period. These summary results remain in the repository.

| Check | Result |
|---|---|
| Static integrity checks | **349 / 349 passed** |
| Browser/integration checks | **187 / 187 passed** |
| Responsive test widths | **320, 375, 390, 768, 1024, 1440 px** |
| Axe scans | **0 violations in all 8 scans** across four pages at 390/1440 px |
| Keyboard behavior | Skip link, main focus, mobile navigation, Escape, restored focus passed |
| Resilience | No-JavaScript menu/FAQ, reduced motion, web-font failure, and reduced-viewport reflow passed |
| Compressed first-party CSS | **8,504 bytes** |
| Compressed first-party JavaScript | **804 bytes** |
| GitHub Pages deployment | **Successful; served build SHA verified** |

### Lighthouse mobile laboratory results

Lighthouse **12.8.2**, default mobile simulated throttling, gzip-enabled local static server, GitHub-hosted Ubuntu runner. All three runs are reported, including the slower first run.

| Run | Performance | Accessibility | Best practices | SEO | LCP | CLS | Transferred bytes |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 76 | 100 | 100 | 66 | 2.859 s | 0 | 352,091 |
| 2 | 94 | 100 | 100 | 66 | 3.024 s | 0 | 352,091 |
| 3 | 94 | 100 | 100 | 66 | 2.870 s | 0 | 352,091 |

**Median performance: 94 / 100**, exceeding the configured 90-point median release gate. The earlier font-swap layout shift was eliminated in these runs through early font fetching and optional display. Slow connections may retain the tested system-font fallback rather than swapping late.

The measured LCP values **did not meet the plan’s aspirational 2.5-second target**. Performance varied across runs; no field-performance or INP claim is made. All pages intentionally carry `noindex, follow` because this is a preview, which contributes to the lower SEO score. Automated accessibility scores do not establish complete WCAG conformance or replace assistive-technology testing.

## Outstanding before an official business launch

Obtain operator approval, authentic rights-cleared business photography, a complete current menu, verified phone/service hours, final brand/domain approval, and a responsible content owner. Replace the menu-highlights scope only with approved complete content. Review the preview disclosures and indexing settings as a separate controlled migration; a build guard prevents casually relabeling the preview as official.

No live telephone call, owner interview, VoiceOver/NVDA user session, real-device field performance study, or transaction was performed. The site has no analytics, forms, accounts, checkout, or online reservations.

### QA-tool dependency maintenance

The initial pinned npm QA dependency installation reported **21 audit findings (16 moderate, 5 high)**. Those development-tool findings have not been fully triaged or remediated in this release and need a reviewed dependency update. The deployed site contains static HTML/CSS, its own small JavaScript, and media; the npm QA packages and `node_modules` are **not deployed**. This scope distinction is not a claim that the findings are harmless or that the build environment has been security-certified. Install scripts are disabled in CI, and the normal build has read-only repository permissions; the deployment job receives only the permissions needed for Pages.
