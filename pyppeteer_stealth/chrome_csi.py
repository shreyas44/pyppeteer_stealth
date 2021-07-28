from pathlib import Path

from pyppeteer.page import Page


async def chrome_csi(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/chrome.csi.js").read_text()
    )
