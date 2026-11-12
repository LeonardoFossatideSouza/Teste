const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto('file:///home/user/Teste/fonte-falstad/relatorio.html', { waitUntil: 'load' });
  await page.waitForTimeout(1500);
  await page.pdf({
    path: '/home/user/Teste/Relatorio_Fonte_Chaveada_Leonardo_Fossati.pdf',
    format: 'A4', printBackground: true,
    margin: { top: '0mm', bottom: '0mm', left: '0mm', right: '0mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="width:100%;font-size:7.5pt;color:#6a7883;font-family:Arial;padding:0 15mm;display:flex;justify-content:space-between;"><span>Leonardo Fossati de Souza Nunes &middot; Eletrônica de Potência &middot; Fonte Chaveada Flyback</span><span class="pageNumber"></span>/<span class="totalPages"></span></div>',
  });
  await browser.close();
  console.log('PDF gerado');
})();
