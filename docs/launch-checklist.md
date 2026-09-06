# Official restaurant launch checklist

The GitHub Pages build is an independent, public design preview. Publishing the preview is not a claim that the restaurant has approved an official commercial website.

## Required business approvals

- [ ] Current operator authorizes the official site, proposed branding, and domain.
- [ ] Preferred telephone confirmed: Tourism lists 785-483-4300; Chamber 2025 lists 785-483-2635.
- [ ] Restaurant, buffet, lounge, and holiday schedules confirmed separately.
- [ ] Current complete menu, descriptions, prices, and availability approved for publication.
- [ ] Private dining and any other services confirmed; no unsupported packages or capacity statements.
- [ ] Official social profile and review destinations verified.
- [ ] Current authentic business photographs supplied with appropriate copyright and participant permissions.
- [ ] Content owner and update process designated.

## Required code/content migration

Replace illustrative stock photos with approved business imagery; record rights and derivative checksums. Replace menu highlights with the operator-approved complete HTML menu. Review and remove preview copy only where approval supports it. Update source notes, page titles, descriptions, social card, and privacy disclosures. Set canonical URLs to the approved official destination. Add only verified Restaurant properties; do not copy third-party aggregate ratings into markup.

Update `approvals` in `data/business.json` with documented evidence, but do not simply flip `preview` to false. `validate_release()` deliberately requires a reviewed migration even after approval flags change. Change that guard only as part of the reviewed official-release commit, with tests ensuring complete approved content and correct indexing. Re-run all checks and obtain final operator sign-off before submitting the official sitemap or changing Business Profile links.

## Further accessibility and operations checks

Run a real VoiceOver or NVDA walkthrough with keyboard, actual browser zoom/text enlargement, and representative mobile hardware. Automated axe checks and screenshot review are not a WCAG certification. Test the preferred phone with an actual call; no telephone call was placed during this implementation. Confirm route links on mobile Maps applications. Test any subsequently added forms, ordering, or reservations as real workflows rather than decorative controls.
