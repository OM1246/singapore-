const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const results = [];
  for (const size of [{ name: 'desktop', width: 1440, height: 900 }, { name: 'mobile', width: 390, height: 844 }]) {
    const page = await browser.newPage({ viewport: { width: size.width, height: size.height } });
    const messages = [];
    page.on('console', msg => {
      if (['error', 'warning', 'warn'].includes(msg.type())) messages.push({ type: msg.type(), text: msg.text() });
    });
    await page.goto('http://127.0.0.1:5173/index.html', { waitUntil: 'load' });
    const measure = await page.evaluate(() => {
      const hero = document.querySelector('.hero-img-section');
      const heroText = document.querySelector('.hero-text');
      const nav = document.querySelector('.nav');
      const bg = document.querySelector('.hero-img-section-bg');
      const heroRect = hero.getBoundingClientRect();
      const textRect = heroText.getBoundingClientRect();
      return {
        title: document.title,
        viewport: { width: innerWidth, height: innerHeight },
        hero: { top: heroRect.top, height: heroRect.height, bottom: heroRect.bottom },
        heroTextTop: textRect.top,
        navHeight: nav.getBoundingClientRect().height,
        bgImagePresent: getComputedStyle(bg).backgroundImage !== 'none',
        bgSize: getComputedStyle(bg).backgroundSize,
        fills: Math.abs(heroRect.top) < 1 && heroRect.height >= innerHeight - 1 && textRect.top >= innerHeight - 1,
        noOverlay: !document.body.innerText.includes('Failed to compile') && !document.body.innerText.includes('Internal server error')
      };
    });
    await page.screenshot({ path: `C:/Users/Om/Documents/Demo_singpour/hero-${size.name}.tmp.png`, fullPage: false });
    await page.evaluate(() => window.scrollTo(0, window.innerHeight));
    const scrollMeasure = await page.evaluate(() => {
      const band = document.querySelector('.hero-band');
      const rect = band.getBoundingClientRect();
      return { scrollY, bandTop: rect.top, bandBottom: rect.bottom, firstBelowVisible: rect.top <= 1 && rect.bottom > 0 };
    });
    results.push({ name: size.name, measure, scrollMeasure, messages });
    await page.close();
  }
  await browser.close();
  console.log(JSON.stringify(results, null, 2));
})();