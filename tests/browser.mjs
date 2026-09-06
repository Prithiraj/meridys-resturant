import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import fs from 'node:fs/promises';
import { startServer } from './server.mjs';
const {server,url}=await startServer();
await fs.mkdir('reports/screenshots',{recursive:true});
const results=[],failures=[];
const check=(condition,message)=>{results.push({message,passed:Boolean(condition)});if(!condition)failures.push(message);};
const browser=await chromium.launch({headless:true});
try {
  for (const width of [320,375,390,768,1024,1440]) {
    const context=await browser.newContext({viewport:{width,height:900},reducedMotion:'reduce'});
    const page=await context.newPage();
    const runtimeErrors=[]; page.on('pageerror',e=>runtimeErrors.push(e.message));
    for (const file of ['index.html','menu.html','about-this-site.html','404.html']) {
      const response=await page.goto(url+(file==='index.html'?'':file),{waitUntil:'networkidle'});
      await page.evaluate(()=>document.fonts.ready);
      // Trigger native lazy-loading before checking the complete gallery.
      await page.evaluate(()=>{document.querySelectorAll('img').forEach(i=>i.loading='eager');});
      await page.evaluate(()=>Promise.all([...document.images].map(i=>i.decode().catch(()=>{}))));
      check(response.status()===200,`${file}@${width}: HTTP 200`);
      check(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`${file}@${width}: no horizontal overflow`);
      check(await page.locator('h1').count()===1,`${file}@${width}: one main heading`);
      check(await page.evaluate(()=>[...document.images].every(i=>i.naturalWidth>0)),`${file}@${width}: every photograph loads`);
      check((await page.locator('a[href="tel:+17854834300"]').count())>0,`${file}@${width}: functional phone URL`);
      if (file==='index.html'||file==='menu.html') await page.screenshot({path:`reports/screenshots/${file.replace('.html','')}-${width}.png`,fullPage:true});
      if ([390,1440].includes(width)) {
        const scan=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).analyze();
        await fs.writeFile(`reports/axe-${file}-${width}.json`,JSON.stringify({violations:scan.violations,incomplete:scan.incomplete,passes:scan.passes.length},null,2));
        check(scan.violations.length===0,`${file}@${width}: axe WCAG A/AA (${scan.violations.length} violations)`);
      }
    }
    await page.goto(url,{waitUntil:'networkidle'});
    await page.keyboard.press('Tab');
    check(await page.locator('.skip-link').evaluate(e=>e===document.activeElement),`keyboard@${width}: skip link is first`);
    await page.keyboard.press('Enter');
    check(await page.locator('#main').evaluate(e=>e===document.activeElement),`keyboard@${width}: skip reaches main`);
    if (width<=1023) {
      await page.locator('.mobile-navigation summary').click();
      check(await page.locator('.mobile-navigation').evaluate(e=>e.open),`navigation@${width}: native menu opens`);
      await page.keyboard.press('Escape');
      check(await page.locator('.mobile-navigation').evaluate(e=>!e.open),`navigation@${width}: Escape closes menu`);
      check(await page.locator('.mobile-navigation summary').evaluate(e=>e===document.activeElement),`navigation@${width}: focus restored`);
    }
    check(await page.evaluate(()=>getComputedStyle(document.documentElement).scrollBehavior==='auto'),`motion@${width}: reduced motion respected`);
    check(runtimeErrors.length===0,`runtime@${width}: no JavaScript errors (${runtimeErrors.join(', ')})`);
    await context.close();
  }
  // Real navigation, JavaScript disabled, system-font fallback, and expanded-text reflow.
  const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
  const page=await nojs.newPage();
  await page.goto(url);
  await page.locator('.hero-buttons .button').click();
  check(page.url()===url+'menu.html','no-JS: menu navigation works');
  await page.locator('.questions summary').nth(1).click();
  check(await page.locator('.questions details').nth(1).getAttribute('open')!==null,'no-JS: native FAQ expands');
  check(await page.locator('.menu-items li').count()===9,'no-JS: menu text present');
  await nojs.close();
  const fallback=await browser.newContext({viewport:{width:1280,height:900}});
  const fallbackPage=await fallback.newPage();
  await fallbackPage.route('**/fonts.googleapis.com/**',route=>route.abort());
  await fallbackPage.route('**/fonts.gstatic.com/**',route=>route.abort());
  await fallbackPage.goto(url,{waitUntil:'networkidle'});
  await fallbackPage.evaluate(()=>document.documentElement.style.zoom='2');
  check(await fallbackPage.evaluate(()=>document.documentElement.scrollWidth<=document.documentElement.clientWidth+1),'200% CSS zoom: reflow without horizontal overflow');
  await fallbackPage.screenshot({path:'reports/screenshots/fallback-200-percent.png',fullPage:true});
  await fallback.close();
} catch(e) {failures.push(e.stack||String(e));}
finally {
  await fs.writeFile('reports/browser-checks.json',JSON.stringify({checks:results.length,passed:results.filter(x=>x.passed).length,failures,results},null,2));
  console.log(JSON.stringify({checks:results.length,passed:results.filter(x=>x.passed).length,failures},null,2));
  await browser.close();await new Promise(resolve=>server.close(resolve));
}
process.exitCode=failures.length?1:0;
