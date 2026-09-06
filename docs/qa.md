# Quality assurance

## Repeatable checks

`python tests/check_site.py` validates all HTML pages, single main headings, image dimensions/alt text, internal asset paths and anchors, phone/directions links, JSON-LD, noindex, sitemap parsing, image presence, resource budgets, and the official-release guard. The initial local run passed **349 checks**. Re-run after any change; the generated report is authoritative.

`npm run test:browser` opens all four pages at 320, 375, 390, 768, 1024, and 1440 px, loads the photographs, checks horizontal overflow, and records screenshots for the home and menu pages. It checks keyboard skip navigation, mobile menu dismissal/focus restoration, JavaScript errors, no-JavaScript menu/FAQ behavior, reduced motion, font failure, and a 200% CSS-zoom reflow case. Axe scans A/AA rules at 390 and 1440 px. No failing rule is disabled or excluded.

`npm run test:lighthouse` performs three mobile Lighthouse 12.8.2 runs on a gzip-enabled local server in GitHub-hosted CI and requires median performance of at least 90. Results include LCP, CLS, transferred bytes, and performance/accessibility/best-practices/SEO scores. The preview intentionally uses noindex, so the SEO score is not optimized to an inappropriate public-indexing target. Lab results do not establish real-user Core Web Vitals or INP.

## Local visual inspection

Before source import, locally rendered desktop/mobile home layouts were inspected using the authored HTML, CSS, and real image bytes. The local Chromium environment blocked URL navigation, so these initial visual renders inlined assets and used system-font fallback. This was a layout inspection, not a claim of successful network integration. Full URL navigation, actual font loading, and integration are tested separately in CI.

The visual pass caught missing whitespace across responsive hero line breaks. Static tests caught a renderer pattern that omitted digits in template keys and a test resolver issue for home-page anchors; both were corrected before publication.

## Known scope boundaries

No actual VoiceOver/NVDA user session, real telephone call, owner interview, real transaction, or on-device field performance study has been performed. Automated scans do not prove accessibility for every user. A production content/rights migration remains required. See `launch-checklist.md`.

Reports and screenshots are attached to the deployment workflow as **quality-report**. The live-deployment step checks the published homepage and menu response after publishing. Final deployment results belong in `release-notes.md` after verification, not before.
