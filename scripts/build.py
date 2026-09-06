#!/usr/bin/env python3
"""Build a dependency-light, progressively enhanced GitHub Pages site.

Python standard library renders all page content. Pillow creates only the social card.
Image derivatives are committed separately with provenance, never hotlinked at runtime.
"""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'
ICONS = {
    'arrow': '<path d="M4 12h15M13 6l6 6-6 6"/>',
    'northeast': '<path d="M6 18 18 6M6 6h12v12"/>',
    'pin': '<path d="M20 10c0 6-8 11-8 11S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    'phone': '<path d="m7 3 3 5-2 2c1.5 3 3 4.5 6 6l2-2 5 3-1 4C10 22 2 14 3 4Z"/>',
    'menu': '<path d="M4 3v6c0 2 4 2 4 0V3M6 3v18M16 3v8h4M20 3v18"/>',
    'plus': '<path d="M12 5v14M5 12h14"/>'
}
ALTS = {
    'steak': 'Sliced cooked steak on a wooden board; licensed illustrative photograph, not a Meridy’s dish.',
    'breakfast': 'Pancakes with syrup; licensed illustrative photograph, not a Meridy’s dish.',
    'burger': 'Burger and fries on a metal plate; licensed illustrative photograph, not a Meridy’s dish.',
    'coffee': 'Coffee being poured into a white mug; licensed inspiration photograph, not Meridy’s service.',
    'lounge': 'A drink being poured at a bar; licensed inspiration photograph, not the Meridy’s lounge.'
}

def escape(value: object) -> str:
    return html.escape(str(value), quote=True)

def icon(name: str) -> str:
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'

def render(template: str, values: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            raise ValueError(f'Unknown template variable: {key}')
        return values[key]
    return re.sub(r'\{\{([a-zA-Z_][a-zA-Z0-9_]*)\}\}', replace, template)

def picture(name: str, base: str, *, hero: bool = False, sizes: str = '(max-width: 700px) 100vw, 45vw') -> str:
    prefix = f'{base}/assets/images/{name}'
    widths = (480, 900, 1600)
    srcset = ', '.join(f'{prefix}-{width}.webp {width}w' for width in widths)
    fallbackset = ', '.join(f'{prefix}-{width}.jpg {width}w' for width in widths)
    image_manifest = json.loads((ROOT / 'public/assets/images/manifest.json').read_text())
    record = next(item for item in image_manifest if item['name'] == name)
    variant = next(v for v in record['variants'] if v['file'] == f'{name}-900.jpg')
    loading = 'fetchpriority="high" loading="eager"' if hero else 'loading="lazy"'
    return (f'<picture><source type="image/webp" srcset="{srcset}" sizes="{sizes}">'
            f'<img src="{prefix}-900.jpg" srcset="{fallbackset}" sizes="{sizes}" '
            f'width="{variant["width"]}" height="{variant["height"]}" '
            f'alt="{escape(ALTS[name])}" {loading} decoding="async"></picture>')

def validate_release(data: dict, images: list[dict]) -> None:
    if not data.get('preview', True):
        pending = [name for name, approved in data.get('approvals', {}).items() if approved is not True]
        required = {'operator', 'phone', 'hours', 'menu', 'photos', 'social'}
        pending += sorted(required - set(data.get('approvals', {})))
        illustrative = [img['name'] for img in images if img.get('status') != 'approved-business-photography']
        if pending or illustrative:
            raise ValueError('Official launch blocked. Missing approvals: '
                             + ', '.join(pending) + '; non-business imagery: ' + ', '.join(illustrative))
        raise ValueError('Official mode requires a reviewed content migration: replace preview-only copy, menu highlights, photo credits, and structured data. See docs/launch-checklist.md.')

def social_card() -> None:
    from PIL import Image, ImageDraw, ImageFont
    # System fonts are rendered into the image; no font files are distributed.
    card = Image.new('RGB', (1200, 630), '#fff8eb')
    draw = ImageDraw.Draw(card)
    serif_paths = ['/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', '/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf']
    sans_paths = ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf']
    def font(paths: list[str], size: int):
        for path in paths:
            if Path(path).exists():
                return ImageFont.truetype(path, size)
        return ImageFont.load_default(size=size)
    draw.rectangle((0, 0, 1200, 15), fill='#8c302b')
    draw.rectangle((0, 546, 1200, 630), fill='#8c302b')
    draw.text((65, 64), 'RESTAURANT & LOUNGE  /  RUSSELL, KANSAS', font=font(sans_paths, 22), fill='#234e43')
    draw.text((60, 142), 'Meridy’s', font=font(serif_paths, 129), fill='#8c302b')
    draw.text((67, 335), 'Pull up a chair in Russell.', font=font(serif_paths, 43), fill='#234e43')
    draw.text((68, 415), 'Steaks. Breakfast. Classic American dining.', font=font(sans_paths, 25), fill='#665b4b')
    draw.ellipse((934, 140, 1134, 340), fill='#edbd53', outline='#8c302b', width=2)
    draw.text((974, 177), 'EXIT', font=font(sans_paths, 28), fill='#8c302b')
    draw.text((968, 220), '184', font=font(serif_paths, 58), fill='#8c302b')
    draw.text((67, 574), 'INDEPENDENT WEBSITE DESIGN PREVIEW', font=font(sans_paths, 22), fill='#fff8eb')
    card.save(OUT / 'assets/social-card.png', optimize=True)

def build() -> None:
    data = json.loads((ROOT / 'data/business.json').read_text())
    image_dir = ROOT / 'public/assets/images'
    manifest_path = image_dir / 'manifest.json'
    if not manifest_path.exists():
        raise FileNotFoundError('Image bundle missing. Run Prepare licensed photography in GitHub Actions; see README.md.')
    images = json.loads(manifest_path.read_text())
    validate_release(data, images)
    for photo in images:
        for variant in photo['variants']:
            file = image_dir / variant['file']
            if not file.exists() or hashlib.sha256(file.read_bytes()).hexdigest() != variant['sha256']:
                raise ValueError(f'Missing or modified photograph: {file}. Update its provenance before building.')
    site_url = os.environ.get('SITE_URL', data['base_url']).rstrip('/')
    parsed_url = urlparse(site_url)
    if parsed_url.scheme not in ('http', 'https') or not parsed_url.netloc:
        raise ValueError('SITE_URL must be an absolute HTTP(S) URL.')
    base = parsed_url.path.rstrip('/')
    if OUT.exists(): shutil.rmtree(OUT)
    shutil.copytree(ROOT / 'public', OUT)
    (OUT / '.nojekyll').write_text('')
    values = {k: escape(v) for k, v in data.items() if isinstance(v, (str, int))}
    values.update(base=escape(base), site_url=escape(site_url), year='2026')
    values.update({f'icon_{key}': icon(key) for key in ICONS})
    values['preview_notice'] = (f'<aside class="preview-banner" aria-label="Website preview notice"><strong>DESIGN PREVIEW</strong>'
        f'<span class="preview-detail">Illustrative photography · business details awaiting approval.</span>'
        f'<a href="{base}/about-this-site.html">About this preview ↗</a></aside>')
    values['hours_table'] = '<table><caption class="visually-hidden">Published weekly opening hours</caption><tbody>' + ''.join(
        f'<tr><th scope="row">{escape(row["days"])}</th><td>{escape(row["display"])}</td></tr>' for row in data['hours']) + '</tbody></table>'
    values['photo_steak_hero'] = picture('steak', base, hero=True, sizes='(max-width: 700px) 100vw, 48vw')
    values['photo_coffee'] = picture('coffee', base)
    values['photo_lounge'] = picture('lounge', base)
    summaries = {'steaks': 'Ribeye, T-bone, and Kansas City strip. Call for today’s cuts.', 'breakfast': 'Start your day with a little comfort and something warm.', 'classics': 'Burgers, sandwiches, and familiar dinner plates.'}
    cards, menu_sections = [], []
    for i, category in enumerate(data['menu'], 1):
        category_id, image = category['id'], category['image']
        cards.append(f'<article class="food-card"><a href="{base}/menu.html#{category_id}"><div class="food-photo">'
          + picture(image, base, sizes='(max-width: 700px) 100vw, 30vw')
          + f'<span class="food-number" aria-hidden="true">0{i}</span></div><div class="food-copy"><p class="eyebrow">{escape(category["eyebrow"])}</p>'
          + f'<div class="food-heading"><h3>{escape(category["title"])}</h3><span class="card-arrow" aria-hidden="true">{icon("arrow")}</span></div>'
          + f'<p>{escape(summaries[category_id])}</p></div></a></article>')
        source = data['sources'][category['source']]
        menu_sections.append(f'<section class="menu-detail" id="{category_id}" aria-labelledby="heading-{category_id}"><div class="menu-detail-photo">'
          + picture(image, base) + '<span class="image-disclosure">Illustrative food photography</span></div>'
          + f'<div class="menu-detail-copy"><p class="eyebrow">0{i} / {escape(category["eyebrow"])}</p><h2 id="heading-{category_id}">{escape(category["title"])}</h2>'
          + f'<p>{escape(category["description"])}</p><ul class="menu-items">' + ''.join(f'<li>{escape(item)}</li>' for item in category['items'])
          + f'</ul><p class="menu-source">Published reference: <a href="{escape(source["url"])}">{escape(source["name"])}</a>. Current availability is not confirmed.</p></div></section>')
    values['food_cards'] = ''.join(cards)
    values['menu_sections'] = ''.join(menu_sections)
    values['photo_credits'] = ''.join(f'<article class="credit-card">{picture(photo["name"], base, sizes="(max-width: 700px) 45vw, 25vw")}'
        f'<h3>{escape(photo["photographer"])}</h3><p>{escape(photo["name"].title())} · illustrative, not Meridy’s</p><a href="{escape(photo["source"])}">Original photograph ↗</a></article>' for photo in images)
    values['source_list'] = '<ul class="source-list">' + ''.join(f'<li><a href="{escape(source["url"])}">{escape(source["name"])}</a><p>{escape(source["supports"])}</p></li>' for source in data['sources']) + '</ul>'
    pages = {
        'index': ('home', 'Meridy’s Restaurant & Lounge | Russell, KS — Design Preview', 'Explore a website design preview for Meridy’s in Russell, Kansas. Menu highlights, published hours, and directions near I-70 Exit 184.'),
        'menu': ('menu', 'Menu Highlights | Meridy’s Restaurant & Lounge — Preview', 'Explore published steak, breakfast, and American dining highlights for Meridy’s in Russell, Kansas. Call for today’s menu, availability, and prices.'),
        'about-this-site': ('about-this-site', 'Photo Credits & Sources | Meridy’s Design Preview', 'Photography credits, business-information sources, privacy details, and launch approvals for this independent Meridy’s website design preview.'),
        '404': ('404', 'Page Not Found | Meridy’s Design Preview', 'Find your way back to the Meridy’s website design preview, menu highlights, and directions to Russell, Kansas.')
    }
    layout = (ROOT / 'templates/layout.html').read_text()
    for filename, (template, title, description) in pages.items():
        canonical = site_url + ('/' if filename == 'index' else f'/{filename}.html')
        schema = {'@context': 'https://schema.org', '@type': 'WebPage', 'name': title, 'url': canonical, 'description': description,
            'about': {'@type': 'Restaurant', 'name': data['name'], 'servesCuisine': 'American',
                'address': {'@type': 'PostalAddress', 'streetAddress': data['street'], 'addressLocality': data['city'], 'addressRegion': data['region'], 'postalCode': data['postal_code'], 'addressCountry': data['country']}}}
        page_values = values | {'page': escape(template), 'title': escape(title), 'description': escape(description),
            'canonical': escape(canonical), 'robots': 'noindex, follow', 'schema': json.dumps(schema, ensure_ascii=False).replace('<', '\\u003c'),
            'menu_current': 'aria-current="page"' if filename == 'menu' else ''}
        page_values['content'] = render((ROOT / f'templates/{template}.html').read_text(), page_values)
        (OUT / f'{filename}.html').write_text(render(layout, page_values))
    # Allow crawlers to fetch the noindex directives. A robots Disallow would hide them.
    (OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n# Public design preview: each page has a noindex meta directive.\n')
    (OUT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'  <url><loc>{escape(site_url + ("/" if file == "index" else "/" + file + ".html"))}</loc></url>\n' for file in pages if file != '404') + '</urlset>\n')
    (OUT / "build.json").write_text(json.dumps({"commit": os.environ.get("GITHUB_SHA", "local"), "mode": "design-preview", "pages": list(pages)}) + "\n")
    social_card()
    print(f'Built {len(pages)} pages at {OUT}. Public design-preview mode, noindex. Base path: {base or "/"}')

if __name__ == '__main__':
    try: build()
    except (OSError, ValueError, KeyError, StopIteration, json.JSONDecodeError) as error:
        print(f'Build failed: {error}', file=sys.stderr)
        raise SystemExit(1)
