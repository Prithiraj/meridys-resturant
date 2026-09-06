#!/usr/bin/env python3
"""Dependency-free integrity and release-gate checks; run after scripts/build.py."""
from __future__ import annotations
from copy import deepcopy
import gzip
import importlib.util
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'_site'
DATA=json.loads((ROOT/'data/business.json').read_text())
BASE=urlparse(DATA['base_url']).path.rstrip('/')
errors=[]
checks=0

def check(condition, message):
    global checks
    checks+=1
    if not condition: errors.append(message)

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path=path; self.ids=[]; self.links=[]; self.imgs=[]; self.headings=0; self.metas={}; self.jsons=[]; self.json_buffer=None
        self.feed(path.read_text())
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'): self.ids.append(a['id'])
        if tag=='h1': self.headings+=1
        if tag in ('a','link') and a.get('href'): self.links.append(a['href'])
        if tag=='img': self.imgs.append(a)
        if a.get('src'): self.links.append(a['src'])
        if a.get('srcset'): self.links.extend(x.strip().split()[0] for x in a['srcset'].split(','))
        if tag=='meta': self.metas[a.get('name',a.get('property',''))]=a.get('content','')
        if tag=='script' and a.get('type')=='application/ld+json': self.json_buffer=''
    def handle_data(self,data):
        if self.json_buffer is not None: self.json_buffer+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.json_buffer is not None:
            self.jsons.append(json.loads(self.json_buffer)); self.json_buffer=None

pages={p.name:Page(p) for p in SITE.glob('*.html')}
check(set(pages)=={'index.html','menu.html','about-this-site.html','404.html'},'Expected four HTML pages')
for name,p in pages.items():
    check(p.headings==1,f'{name}: exactly one h1')
    check(len(p.ids)==len(set(p.ids)),f'{name}: duplicate ids')
    check('main' in p.ids,f'{name}: skip destination missing')
    check('noindex' in p.metas.get('robots',''),f'{name}: preview is indexable')
    check(bool(p.metas.get('description')),f'{name}: missing description')
    check(bool(p.metas.get('og:image')),f'{name}: missing share image')
    check(len(p.jsons)==1,f'{name}: missing JSON-LD')
    check(p.jsons[0]['about']['@type']=='Restaurant',f'{name}: missing restaurant entity')
    check('aggregateRating' not in json.dumps(p.jsons),f'{name}: unapproved rating')
    check('{{' not in p.path.read_text(),f'{name}: unresolved template')
    for a in p.imgs:
        check(bool(a.get('alt')),f'{name}: meaningful alt required')
        check(a.get('width','').isdigit() and a.get('height','').isdigit(),f'{name}: image dimensions required')
        check(a.get('loading') in ('eager','lazy'),f'{name}: explicit loading strategy')
    for link in p.links:
        url=urlparse(link)
        if url.scheme or url.netloc: continue
        local=unquote(url.path)
        if local.startswith(BASE+'/'): local=local[len(BASE)+1:] or 'index.html'
        elif local.startswith('/'):
            check(False,f'{name}: wrong project path: {link}'); continue
        if not local: local=name
        if local.endswith('/'): local+='index.html'
        target=SITE/local
        if target==SITE: target=SITE/'index.html'
        check(target.is_file(),f'{name}: broken local resource: {link}')
        if url.fragment and target.suffix=='.html' and target.name in pages:
            check(unquote(url.fragment) in pages[target.name].ids,f'{name}: broken anchor {link}')
    check('tel:+17854834300' in p.links,f'{name}: phone action missing')
    check(any('/maps/dir/' in x for x in p.links),f'{name}: directions action missing')

budgets={}
for name,limit in [('site.css',30000),('site.js',15000)]:
    size=len(gzip.compress((SITE/'assets'/name).read_bytes(),mtime=0))
    budgets[name]={'gzip_bytes':size,'budget_bytes':limit}
    check(size<=limit,f'{name}: gzip budget exceeded ({size})')
for width,limit in [(480,250000),(900,250000),(1600,400000)]:
    p=SITE/f'assets/images/steak-{width}.webp'
    check(p.stat().st_size<=limit,f'Hero {width} exceeds budget')
ET.parse(SITE/'sitemap.xml')
check((SITE/'assets/social-card.png').exists(),'Open Graph card absent')
check((SITE/'.nojekyll').exists(),'Pages fallback marker absent')
check('Disallow: /' not in (SITE/'robots.txt').read_text(),'robots must allow crawling the noindex directive')
spec=importlib.util.spec_from_file_location('site_build', ROOT/'scripts/build.py')
module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
unsafe=deepcopy(DATA); unsafe['preview']=False
try:
    module.validate_release(unsafe,json.loads((SITE/'assets/images/manifest.json').read_text()))
    check(False,'Official release gate must fail without approvals')
except ValueError: check(True,'Official release gate blocked unsafe launch')
report={'checks':checks,'passed':checks-len(errors),'errors':errors,'budgets':budgets,
        'scope':'Static integrity, image references, JSON-LD, project paths, compressed resource budgets, and production guard.'}
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports/static-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
