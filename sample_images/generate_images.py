import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

BASE = Path(r"c:\Users\PC_user\Documents\リンクアップたかはし株式会社\sample_images")

slides = [
    ("slide1_hero.html", "01_hero.png"),
    ("slide2_feature.html", "02_feature.png"),
    ("slide3_advantage.html", "03_advantage.png"),
    ("slide4_benefit.html", "04_benefit.png"),
    ("slide5_howto.html", "05_howto.png"),
    ("slide5_trust.html", "06_trust.png"),
    ("slide6_safety.html", "07_safety.png"),
    ("slide8_cta.html", "08_cta.png"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for html_file, png_file in slides:
            page = await browser.new_page(
                viewport={"width": 700, "height": 700},
                device_scale_factor=2
            )
            url = (BASE / html_file).as_uri()
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_timeout(3000)
            await page.screenshot(path=str(BASE / png_file), type="png")
            await page.close()
            print(f"Created: {png_file}")
        await browser.close()

asyncio.run(main())
