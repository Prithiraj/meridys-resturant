import lighthouse from 'lighthouse';
import { launch } from 'chrome-launcher';
import fs from 'node:fs/promises';
import { startServer } from './server.mjs';
const {server,url}=await startServer();
const runs=[];
try {
  for(let i=1;i<=3;i++) {
    const chrome=await launch({chromeFlags:['--headless','--no-sandbox','--disable-dev-shm-usage']});
    try {
      const report=await lighthouse(url,{port:chrome.port,output:'json',logLevel:'error',onlyCategories:['performance','accessibility','best-practices','seo']});
      await fs.writeFile(`reports/lighthouse-mobile-${i}.json`,report.report);
      runs.push({run:i,performance:Math.round(report.lhr.categories.performance.score*100),accessibility:Math.round(report.lhr.categories.accessibility.score*100),bestPractices:Math.round(report.lhr.categories['best-practices'].score*100),seo:Math.round(report.lhr.categories.seo.score*100),lcp:report.lhr.audits['largest-contentful-paint'].numericValue,cls:report.lhr.audits['cumulative-layout-shift'].numericValue,totalByteWeight:report.lhr.audits['total-byte-weight'].numericValue});
    } finally {await chrome.kill();}
  }
  const median=[...runs].sort((a,b)=>a.performance-b.performance)[1].performance;
  const summary={tool:'Lighthouse 12.8.2',mode:'Default mobile simulated throttling, local gzip-enabled static server, GitHub-hosted Ubuntu runner',runs,medianPerformance:median,target:90,note:'SEO score intentionally reflects noindex on a design preview. Lab metrics are not field Core Web Vitals; no INP claim.'};
  await fs.writeFile('reports/lighthouse-summary.json',JSON.stringify(summary,null,2));
  console.log(JSON.stringify(summary,null,2));
  if(median<90)process.exitCode=1;
} finally {await new Promise(resolve=>server.close(resolve));}
