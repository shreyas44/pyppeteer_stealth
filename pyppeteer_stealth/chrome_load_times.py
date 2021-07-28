from pathlib import Path

from pyppeteer.page import Page


async def chrome_load_times(page: Page, **kwargs) -> None:
    await page.evaluateOnNewDocument(
        Path(__file__).parent.joinpath("js/chrome.loadTimes.js").read_text()
    )
