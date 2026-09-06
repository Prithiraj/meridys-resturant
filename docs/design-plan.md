# Meridy’s Restaurant & Lounge — Website Design Plan

**Version 1.0 baseline, with approved implementation addendum · Research checked September 7, 2026**

> **Implementation addendum — September 7, 2026.** The requester approved implementation and GitHub Pages publication, requested a more vibrant visual treatment, and retained photography-first interaction. All 17 baseline sections remain below for traceability. The implemented palette is cream `#fff8eb`, deep red `#8c302b`, mustard `#edbd53`, forest green `#234e43`, and dark ink `#30291f`. The base architecture and actions are retained. No Three.js is loaded: photography and restrained CSS provide the visual interest.
>
> **Public-preview scope:** Because no owner-approved current menu or business-photo permissions were supplied, the published Pages version is clearly identified as an independent design preview with noindex metadata, source-backed menu highlights, disclosed provisional hours/phone, and five licensed illustrative real photographs. These are not Meridy’s dishes or spaces; actual business photography remains an official-launch requirement. The user’s publication request replaces the baseline private-preview assumption, not the content/rights approval requirements. See [implementation notes](implementation.md), [image rights](image-rights.md), and [official launch checklist](launch-checklist.md).

---



**Recommended direction: a warm, editorial Kansas restaurant website.** Make the actual food, dining rooms, and roadside identity memorable, while making the menu, directions, and phone number effortless to find. This is a design and content plan, not an implemented website.

**Proposed PRIMARY_ACTIONS:** View Menu · Get Directions · Call Meridy’s.

## 1. Evidence baseline

Publicly documented facts are distinguished from operator-confirmed information. No direct owner interview, telephone verification, or image-license approval has occurred. The supplied Google Maps page could not be loaded directly; its listing should be verified before launch.

| Subject | Evidence found | Website decision |
|---|---|---|
| Identity and address | Meridy’s Restaurant & Lounge, 1220 S Fossil Street, Russell, KS 67665, appears in Kansas Tourism and the local Chamber directory. [1][2] | Use this business identity and address; confirm final spelling with the operator. |
| Phone | Kansas Tourism and the indexed Facebook listing show **785-483-4300**. The Chamber’s 2025 directory shows **785-483-2635**. [1][2][3] | Use 4300 as the proposed number, but require operator confirmation and a call-link test before launch. Never substitute the listing agent’s number. |
| Published hours | Tripadvisor lists **Monday–Saturday, 6 a.m.–10 p.m.; Sunday, 7 a.m.–10 p.m.** [4] | Provisional, not owner-confirmed. Confirm restaurant, buffet, lounge, and holiday schedules separately. No live “Open now” badge in version one. |
| Food | Kansas Tourism specifically mentions fresh-cut ribeyes, T-bones, and Kansas City strip steaks. The broker describes breakfast, lunch, and dinner. [1][5] | Lead with steaks and broad meal occasions. Do not infer all-day breakfast, sourcing, preparation methods, or current availability of every cut. |
| Buffet | Dated 2026 customer reviews describe buffet dining. [4] | A supported menu category, not evidence of its current schedule, daily contents, or price. |
| Spaces and services | Kansas Tourism lists private dining for meetings and banquets, a lounge, and Barney’s Bar in the evenings. [1] | Include group-dining and lounge content after operational confirmation. No invented capacity, packages, or entertainment calendar. |
| Parking | The broker advertises a large lot accommodating trucks, boats, and oversized vehicles. [5] | Potential traveler benefit. Confirm access and restrictions before making size-specific promises. |
| Road access | iExit places the restaurant near **I-70 Exit 184**, north of the interstate. [6] | Make exit and address information prominent; avoid estimated travel-time claims. |
| Community connection | Russell Sunrise Kiwanis publishes recurring breakfast meetings at Meridy’s. [7] | Supports a community-gathering narrative, not an endorsement or permission to display the club’s logo. |
| Social proof | Tripadvisor displayed **4.1/5 from 220 reviews** during research. [4] | Default to a source-linked review invitation. A numeric badge requires a fresh check, date, and maintenance owner. |
| Ownership/history | A broker advertises the restaurant for sale and describes a 30-plus-year history. [5] | Reconfirm current ownership and approved history. Exclude sale details and financial claims from the diner-facing website. |

**Review interpretation:** Accessible feedback includes praise for hospitality, buffet meals, and rolls, alongside criticism of steak doneness and some selections. Use this as qualitative research—not a promise of flawless service, a fabricated testimonial, or evidence that every dish is homemade. [4]

**Competitive benchmark:** Waudby’s official site emphasizes downtown history, family dining, sports viewing, and ordering ahead. Meridy’s should not rely on generic “local and welcoming” positioning alone. The proposed distinction is the combination of steak-led dining, breakfast-to-dinner usefulness, and clear highway-stop information—not an unsupported claim of superiority. [8]

**Search-result caution:** Some restaurant-branded pages explicitly identify themselves as unofficial. Do not treat their menus, delivery claims, photos, or policies as owner-approved material. [9]

**Unresolved launch inputs:** Current operator, preferred phone, approved menu and prices, service schedules, current group-dining/catering scope, verified social accounts, production domain, logo files, and photography rights. Design can proceed after approval; unresolved claims cannot silently become production facts.

## 2. Audience

These are working audience hypotheses inferred from the documented location, meal offerings, and spaces—not demographic findings.

| Audience | Immediate question | Design response |
|---|---|---|
| I-70 travelers and nearby overnight guests | “Is this worth stopping for, and how do I get there?” | Real food and exterior photography, visible menu, exit reference, directions, and telephone. |
| Russell-area diners | “What can we eat, and when can we visit?” | Readable menu, reliable hours, familiar rather than formal visual tone. |
| Group organizers | “Can we meet or eat together here?” | Actual room photographs and a direct group-dining inquiry action, without invented availability. |
| Lounge visitors | “What is the setting, and when is the lounge operating?” | A restrained lounge introduction with separately verified information. |

Prioritize travelers and local diners in the first screen. Give groups a clear secondary path without making the homepage feel like a banquet-sales brochure.

## 3. Conversion goals

| Priority | Action | Placement and behavior |
|---|---|---|
| Primary discovery | **View Menu** | Dominant hero action; visible navigation link; opens the HTML menu page. |
| Primary visit intent | **Get Directions** | Companion hero action; mobile action bar; location section; opens the verified destination in Maps. |
| Direct contact | **Call Meridy’s** | Header, mobile action bar, location section, and closing CTA; native telephone link. |
| Secondary inquiry | **Call About Group Dining** | Group section only, after the service and contact route are confirmed. |

Do not introduce “Book a Table,” “Order Online,” gift cards, delivery, or a checkout without an approved, functioning business workflow. A telephone link must not imply an instantly confirmed reservation.

Optional measurement after approval: record aggregate menu visits, direction clicks, telephone clicks, and group-inquiry clicks. Treat them as **intent signals**, not completed visits, answered calls, or revenue. Establish a baseline before setting improvement targets; do not claim an invented conversion uplift. Choose analytics and any required disclosures before adding tracking.

## 4. Creative direction

### Concept: “Pull up a chair in Russell.”

**Mood:** classic, warm, grounded, and editorial—polished without pretending the business is a luxury tasting-menu restaurant.

Actual reference photography shows wood-paneled dining areas, practical table settings, and a distinctive pale stone roadside sign. Use those details as the visual starting point rather than generic steakhouse stock photography. Photo dates and current accuracy still require confirmation. [5]

Translate the evidence into a limestone-colored canvas, dark wood-toned typography, generous food photography, and menu layouts with the orderliness of a printed placemat. Introduce a restrained oxblood accent as a **proposed design choice**, not an asserted existing brand color.

The memorable moments should be a strong real-food hero, a generously typeset menu, and an exterior/sign photograph that helps guests recognize the restaurant on arrival. An original, subtle uneven divider can echo the stone sign without tracing its lettering or reproducing its superlative claims.

Avoid black-and-gold luxury clichés, fake heritage badges, distressed cowboy fonts, decorative flames, neon nightlife styling, and “best in Kansas” copy. Preserve an owner-supplied wordmark; any new typeset treatment requires approval.

## 5. Color system

| Role | Proposed color | Intended use |
|---|---|---|
| Limestone | `#F6F0E6` | Main background and light text on dark panels. |
| Warm paper | `#FFFCF6` | Menu and information surfaces. |
| Charcoal | `#24211D` | Main text, navigation, footer. |
| Oxblood | `#722F37` | Primary buttons and selective emphasis. |
| Walnut | `#685142` | Supporting text and secondary headings. |
| Brass | `#B28A52` | Decorative rules and small nonessential accents. |

Calculated flat-color contrast: charcoal on limestone approximately **14.14:1**; limestone on oxblood **8.51:1**; walnut on limestone **6.51:1**. Brass on limestone is approximately **2.79:1**, so it is not approved for essential text or standalone control boundaries.

Validate every actual component, including hover, focus, disabled, and image-overlay states. Keep text on solid panels where possible. Use a dual-tone visible focus indicator instead of relying on the brass accent. The accessibility target is WCAG 2.2 AA. [14]

## 6. Typography

**Headlines:** Fraunces, using restrained optical settings and medium-to-semibold weights. Its soft-serif character suits the proposed warm editorial direction. **Body, menu, hours, and controls:** Source Sans 3. Both projects publish open-font licensing; retain applicable notices and verify the selected release before deployment. [10][11]

Proposed scale: 42–52 px mobile hero headings, 64–88 px desktop hero headings, 30–44 px section headings, and 18 px body copy with approximately 1.55 line-height. Controls should be at least 16 px; secondary labels should remain comfortably readable, normally 14 px or larger.

Limit prose to approximately 60–70 characters per line. Keep menu names and prices visually distinct without relying on dotted leaders that become cramped on small screens. Use tabular numerals where useful for aligned prices and hours.

Load only necessary font subsets and weights. Provide Georgia and system-sans fallbacks so typography remains usable if custom fonts fail. No font files are included in this planning deliverable.

## 7. Image strategy

**Production priority:** operator-supplied photographs with confirmed rights, followed by commissioned business photography. Owner-controlled social posts are leads for obtaining originals—not automatic reuse permission.

| Placement | Desired photograph | Current status |
|---|---|---|
| Hero | An actual plated steak or representative meal photographed at Meridy’s, with recognizable table or room context. | Obtain current, approved original. |
| Menu introduction | Two or three confirmed dishes, including a breakfast option if still offered. | Photograph after menu verification. |
| Space/story | Main dining room and a closer table-setting detail. | Broker images are research references; commercial clearance is unconfirmed. |
| Groups/lounge | Actual private dining space and lounge, accurately captioned. | Verify present layout and obtain permission. |
| Visit | Entrance and stone roadside sign, showing what arriving guests should look for. | Fresh owner-approved images preferred. |
| Optional people | Current team member or genuine service moment. | Only with business approval and appropriate participant permission. |

Target six to eight strong photographs rather than a large, repetitive gallery. Request both landscape and portrait crops with space for responsive art direction. Preserve actual portions, plating, room dimensions, and signage; do not use generative edits to make the business appear different.

Maintain an asset register recording original source, photographer/rightsholder, capture date when available, permission evidence, permitted uses, expiry, required credit, alt text, and production status.

**No image discovered during this research is presumed commercially cleared.** For private design review, uncleared references must be labeled **“DEMO / REFERENCE ONLY — NOT CLEARED FOR COMMERCIAL USE.”** The label is a warning, not a license. Use placeholders instead when reproduction permission is uncertain. [12]

## 8. Information architecture

**Initial scope:** a focused homepage and a separate, accessible **Menu** page. Avoid an unnecessarily large multi-page site.

Homepage flow:

**Hero → quick reasons to visit → menu introduction → space/story → group dining and lounge → gallery/review link → location, hours, contact → closing CTA/footer.**

Desktop navigation: **Menu · Inside Meridy’s · Group Dining · Visit**. Keep the phone visible and use View Menu as the principal navigation CTA. Remove Group Dining from navigation when that service is not approved for publication.

The menu page will contain the complete operator-approved menu as HTML, category jump links, prices where approved, and an optional matching downloadable menu supplied by the business. Do not make a PDF or photograph the only menu.

Keep privacy information proportionate to the actual hosting, analytics, and integrations. No empty blog, placeholder booking page, unmaintained events feed, or fabricated policy page. All navigation must work through ordinary links without JavaScript.

## 9. Section-by-section layout

### 9.1 Header

A compact warm-paper header: business wordmark on the left, restrained navigation, visible phone, and View Menu. On mobile, preserve a direct menu link instead of burying every useful action inside navigation. Do not display an unverified opening-status message.

### 9.2 Hero

Desktop: approximately 44% text and 56% authentic photography. Mobile: business identity, headline, short explanation, actions, then a purpose-cropped image. Avoid a forced full-screen hero that pushes useful details below the fold.

**Proposed copy, subject to final fact approval:**

> **Meridy’s Restaurant & Lounge · Russell, Kansas**  
> # Pull up a chair in Russell.  
> Steaks, breakfast, and classic American dining near I-70 Exit 184.

**Actions:** View Menu · Get Directions. Place the telephone nearby as a quieter link. The factual ingredients come from the baseline; the headline is new creative copy. [1][4][5][6]

### 9.3 Quick reasons to visit

A simple typographic strip, not a wall of icon cards. Proposed subjects: **Steaks · Breakfast, lunch & dinner · Restaurant & lounge**. Publish only after confirming current operations. A compact location reference can sit at the end of the strip.

### 9.4 Menu introduction

Use an editorial layout: one generous food image beside readable category summaries and a strong View Menu action. Proposed categories are **Steaks**, **Breakfast**, and **Classic Dinners**, with final labels taken from the approved menu rather than forced into a template.

Give buffet information a separate note or panel only after its current service is confirmed. Do not imply that buffet service, breakfast, and the lounge share the restaurant’s entire opening schedule. No scraped prices, invented specials, or unsupported “house favorite” labels.

In a private prototype, an incomplete selection must say **Menu Preview**. A live page promising the full menu requires an approved complete menu; otherwise the reduced content scope needs separate approval.

### 9.5 Inside Meridy’s / story

Pair an actual wide room photograph with a smaller detail and approximately 60–90 words of approved copy. Emphasize the real setting and different reasons to gather. A current team portrait is optional, not a reason to invent a chef profile.

Do not publish a founding year, current ownership claim, family biography, “made from scratch” story, or sourcing narrative without direct support. The Kiwanis information can guide the community theme; it does not authorize an endorsement claim. [7]

### 9.6 Group dining and lounge

Use a calm two-part composition: a light group-dining panel and a darker walnut/charcoal lounge panel. Show the actual rooms. Keep descriptions practical rather than promising bespoke events or premium cocktails.

**Group action:** Call About Group Dining. **Lounge action:** view confirmed visiting information or call. Catering receives a separate mention only if the operator confirms the current offering; no packages, minimum spends, capacity, or instant availability are assumed.

### 9.7 Gallery and social proof

Display four to six complementary photographs in a fixed grid, with ordinary captions where useful. No autoplay carousel. Avoid repeating the hero crop simply to fill space.

Default social proof is a compact **Read Guest Reviews** link to the verified business listing. Add a rating or short attributed excerpt only after source, date, reproduction conditions, and upkeep are approved. No invented customer names, synthetic portraits, blended ratings, or selective paraphrases presented as quotations.

### 9.8 Visit, closing CTA, and footer

Make **1220 S Fossil Street, Russell, KS 67665**, the confirmed telephone, and approved weekly hours prominent. Include an entrance/sign photograph and directions link. Publish special-service hours separately where relevant. Provide approved practical parking information rather than making blanket access guarantees.

Use the verified destination address or place identifier for directions—not the viewport coordinates in the supplied Maps URL. Standard Maps URLs support cross-platform directions links without requiring a Maps API key. [13]

End with **“Your next stop: Meridy’s.”** and Get Directions / Call Meridy’s. The footer repeats the essential contact details and includes the verified Facebook profile. Do not add Instagram, TikTok, or an email address merely to fill the layout.

## 10. Three.js / animation plan

**No Three.js or WebGL in the recommended implementation.** A 3D steak, rotating room, or interactive highway scene does not serve the principal dining decisions.

Use restrained CSS transitions: approximately 120–180 ms for button and navigation state changes. No autoplay video, parallax, scroll hijacking, cursor effects, compulsory gallery animation, or elaborate loading sequence. Essential content is visible immediately; it must never wait for a reveal script.

Honor `prefers-reduced-motion: reduce` by removing nonessential motion and smooth scrolling, while preserving obvious state changes. The media feature exists to respect a user’s preference for reduced motion. [15]

With JavaScript unavailable, the menu, photos, navigation, contact details, hours, and action links remain present and usable.

## 11. Responsive behavior

| Layout range | Intended behavior |
|---|---|
| 320–639 px | Single-column flow, full-width main actions, compact header, no overlapping image/text treatments. |
| 640–1023 px | Selective two-column sections where content remains readable; gallery scales naturally. |
| 1024 px and above | Split hero, editorial image/text pairings, maximum content width around 1,280 px. |

These are starting ranges, not rigid device assumptions. Use approximately 20 px mobile gutters and progressively larger spacing on wide screens. Keep menu descriptions readable before adding decorative columns.

A mobile bottom action bar offers **Menu · Call · Directions** with text labels, comfortable hit areas, safe-area spacing, and sufficient page padding. It must not obscure content or focused controls; disable fixed positioning in constrained layouts when necessary.

Test at 320, 375, 390, 768, 1024, and 1440 px, in both orientations where useful. Verify text enlargement and zoom reflow, not just screenshots at normal size. [14]

## 12. Accessibility

Target **WCAG 2.2 AA**, supported by manual testing—not a claim of certification from an automated score. Use semantic landmarks, a skip link, one main heading per page, logical section headings, and an address element for contact information. Use links for navigation and native controls for state changes. [14]

Every action must work by keyboard with an obvious focus indicator. Sticky elements must not hide focus. Avoid unnecessary modal navigation and image lightboxes; an expanded navigation control needs accurate state and predictable focus behavior. Never rely on hover or color alone. [14]

Provide image-specific alt text. Describe the visible dish or room without guessing ingredients, dietary suitability, or identities. Decorative elements use empty alt text. Keep the menu and hours available as real text. [19]

Aim for 44–48 px controls; WCAG 2.2’s AA minimum target-size criterion is 24 CSS pixels subject to its exceptions, so the proposed design target is deliberately more generous. [16]

Test contrast, keyboard order, 200% text sizing, zoom/reflow, VoiceOver or NVDA, and reduced motion. Record and resolve critical issues rather than relying exclusively on automated checks. [14]

## 13. Performance

Proposed engineering budgets, not measured results:

| Resource | Target |
|---|---|
| Initial mobile page transfer | At most approximately 800 KB, before below-fold lazy-loaded media. |
| Hero image | Approximately 250 KB mobile; 400 KB desktop maximum where feasible. |
| Compressed CSS / first-party JavaScript | Approximately 30 KB / 15 KB respectively. |
| Font transfer | Approximately 120 KB total, through carefully selected subsets and weights. |

Serve appropriately sized AVIF/WebP images with conventional fallbacks, responsive sources, and explicit dimensions. Do not lazy-load the hero; prioritize the actual largest-content image. Lazy-load below-fold images and reserve their layout space. [19]

Avoid embedded social feeds, an automatically loaded map, background video, large icon libraries, and a JavaScript framework for this static scope. Use external social and Maps links instead. Preserve text with system-font fallbacks during font loading.

Target good Core Web Vitals: **LCP ≤2.5 seconds, INP ≤200 ms, CLS ≤0.1**, assessed at the 75th percentile when sufficient real-user data exists. Prelaunch lab tests provide useful checks but are not equivalent to field performance. [17]

Use repeatable mobile lab tests with stated settings; target a median Lighthouse performance score of at least 90 over three comparable runs. Record actual results and exceptions at QA.

## 14. SEO / local discovery

**Proposed homepage title:** Meridy’s Restaurant & Lounge | Russell, KS

**Proposed meta description:** Explore Meridy’s Restaurant & Lounge in Russell, Kansas. Find the menu, restaurant hours, and directions to 1220 S Fossil Street near I-70.

Use a distinct menu-page title and description. Keep business name, address, telephone, menu, and hours consistent across visible content and approved business listings. Confirm the production domain before choosing canonicals; do not invent a domain or claim control of existing restaurant-branded pages.

Use **Restaurant** JSON-LD with approved `name`, `url`, `image`, `telephone`, `address`, `servesCuisine`, and `hasMenu`. Add `sameAs`, geographic coordinates, and `openingHoursSpecification` only after verifying them. Do not invent `priceRange`, reservation acceptance, payment methods, or opening dates. Structured data must match the visible content. [18][20]

Do not copy Google/Tripadvisor aggregate ratings into the markup. Google treats self-serving LocalBusiness/Organization review markup as ineligible for review-star features; do not promise stars or rankings. [21]

Provide Open Graph title, description, canonical URL, site name, `website` type, and a rights-cleared image with descriptive alternative text. Create a dedicated approximately 1200 × 630 share crop rather than reusing an illegible screenshot. [22]

Generate a sitemap, appropriate indexing rules, and consistent canonical URLs. Keep preview builds access-controlled and non-indexable. After launch approval, verify the website/menu links in the owner’s Business Profile and arrange Search Console access through the operator.

## 15. Rights / licensing notes

A publicly visible business photograph is not automatically available for commercial reuse. The photographer is generally the initial copyright owner, subject to exceptions; operator or broker approval must cover the underlying rights rather than merely access to the image. [12]

Broker photographs, Google Maps contributions, Tripadvisor photos, and editorial images are **research references until cleared**. No hotlinking, watermark removal, or uncredited copying. Attribution alone does not supply permission. A demo label does not make unauthorized publication acceptable.

For production, record written permission covering the website and planned social/Open Graph uses, relevant edits/crops, duration, and any attribution requirements. Obtain appropriate permission for recognizable people used in promotional photography. Confirm logo rights and use accurate current imagery.

Use review excerpts only with accurate attribution, preserved meaning, and appropriate permission/platform compliance. Keep font-license notices for selected releases. No uncleared image, fabricated testimonial, fake award, or misleading heritage claim may pass the launch gate.

## 16. Implementation sequence

1. **Approve the plan.** Confirm creative direction, proposed primary actions, initial pages, and whether group dining is included. No site implementation begins before this approval.
2. **Lock content and rights.** Obtain the current menu, contact details, schedules, approved story/services, logo, cleared photography, domain/hosting decision, and responsible content owner. Record unresolved items explicitly.
3. **Approve visual layouts.** Prepare mobile-first wireframes and representative desktop compositions using the approved content. Review hero, menu, and visit sections before extending the full system.
4. **Build the accessible static site.** Use semantic HTML, CSS, and minimal progressive JavaScript. Render content and structured data from one verified business record. Integrate with an existing stack only when required; no unnecessary framework migration or speculative integrations.
5. **Complete QA.** Test content accuracy, telephone/Maps destinations, menu completeness, accessibility, responsive layouts, JavaScript failure, metadata, structured data, performance, and asset rights.
6. **Obtain launch approval and hand over.** Deploy only after operator sign-off. Document menu/hour updates and asset replacement, verify production links, and establish measurement without making unsupported conversion claims.

Name a person responsible for maintaining hours, menu prices, services, and contact details. Update the single content record whenever operations change. Recheck any published rating on a defined schedule, such as monthly, or remove the numeric badge.

## 17. Acceptance criteria

| Area | Required result |
|---|---|
| Business accuracy | Every factual claim has a source and required operator approval; no unresolved phone, schedule, ownership, or service claim is silently published. |
| Distinctiveness | The site uses Meridy’s real food, spaces, and roadside identity—not interchangeable restaurant stock imagery. |
| Conversions | View Menu, Call, and Directions are obvious and functional; every action leads to a real destination or approved workflow. |
| Menu | Approved current content is readable as HTML; no invented prices, incomplete menu labeled “full,” or image-only menu. |
| Photography and rights | Every production asset is cleared and accurately represents the business; all demo/reference-only assets are removed or replaced. |
| Mobile use | No unintended horizontal overflow at the target widths; sticky controls do not obscure content or keyboard focus. |
| Accessibility | Manual keyboard, screen-reader, contrast, zoom, and reduced-motion checks pass without unresolved critical issues. |
| Resilience | Essential content and navigation remain usable without JavaScript or custom-font loading. |
| Performance | Resource budgets and lab results are recorded; deviations are fixed or explicitly accepted. Field metrics are monitored when available. |
| Discovery | Metadata and Restaurant JSON-LD validate, match visible approved facts, and use the approved production domain. |
| Maintenance | The operator receives a clear process for changing hours, menus, contact details, and images. |
| Release control | No public launch without final content, rights, and operator approval. |

**Approval requested:** the warm editorial direction, homepage-plus-menu structure, and primary actions **View Menu · Get Directions · Call Meridy’s**.

---

## Research and standards references

Accessed or checked September 7, 2026. Search-indexed snippets and partially accessible pages are not the same as live operator confirmation. Reference URLs below are source locations, not production asset licenses.

[1] Kansas Tourism — Meridy’s listing: `https://www.travelks.com/listing/meridys-restaurant-%26-lounge/11861/`

[2] Russell Area Chamber of Commerce — 2025 members: `https://russellchamber.org/our-members-2025`

[3] Publicly identified Meridy’s Facebook page; phone supported by indexed listing: `https://www.facebook.com/p/Meridys-Restaurant-Lounge-100066921303576/`

[4] Tripadvisor — listing, published hours, rating, and dated reviews: `https://www.tripadvisor.in/Restaurant_Review-g39037-d821127-Reviews-Meridy_s_Restaurant_Lounge-Russell_Kansas.html`

[5] About You Realty — sale listing and actual-business photo references: `https://www.aboutyourealty.com/details.html?id=30660`

[6] iExit — I-70 Exit 184: `https://www.iexitapp.com/Kansas/I-70/Exit%20184/9265`

[7] Russell Sunrise Kiwanis — meeting information: `https://k11075.site.kiwanis.org/`

[8] Waudby’s Sports Bar & Grill — official competitor website: `https://waudbys.net/`

[9] Example explicitly unofficial directory: `https://meridys-restaurant-lounge.hey-restaurants.com/`

[10] Fraunces — original project and licensing: `https://github.com/undercasetype/Fraunces`

[11] Source Sans 3 — Adobe project and licensing: `https://github.com/adobe-fonts/source-sans`

[12] U.S. Copyright Office — photographs: `https://www.copyright.gov/engage/photographers/`

[13] Google Maps URLs documentation: `https://developers.google.com/maps/documentation/urls/get-started`

[14] W3C — WCAG 2.2 and quick reference: `https://www.w3.org/TR/WCAG22/` and `https://www.w3.org/WAI/WCAG22/quickref/`

[15] MDN — prefers-reduced-motion: `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion`

[16] W3C — Understanding Target Size (Minimum): `https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html`

[17] Google web.dev — Web Vitals: `https://web.dev/articles/vitals`

[18] Schema.org — Restaurant: `https://schema.org/Restaurant`

[19] MDN — HTML image element: `https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img`

[20] Google Search Central — LocalBusiness structured data: `https://developers.google.com/search/docs/appearance/structured-data/local-business`

[21] Google Search Central — Review snippet guidelines: `https://developers.google.com/search/docs/appearance/structured-data/review-snippet`

[22] Open Graph protocol: `https://ogp.me/`
