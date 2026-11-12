const { chromium } = require('playwright');

(async () => {
  const [url, outfile, waitMs, scale] = process.argv.slice(2);
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const ctx = await browser.newContext({
    viewport: { width: 1180, height: 760 },
    deviceScaleFactor: parseInt(scale || '2', 10),
  });
  const page = await ctx.newPage();
  const logs = [];
  page.on('console', m => logs.push(`[${m.type()}] ${m.text()}`));
  page.on('pageerror', e => logs.push(`[pageerror] ${e.message}`));

  await page.goto(url, { waitUntil: 'load', timeout: 90000 });
  await page.waitForTimeout(parseInt(waitMs || '15000', 10));
  await page.screenshot({ path: outfile });

  console.log('--- CONSOLE (' + logs.length + ') ---');
  console.log(logs.slice(0, 40).join('\n'));
  await browser.close();
})();
