"""Fixtures pytest partagées : une page Playwright neuve par test."""
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as p:
        # Chrome système si présent (dev local), sinon chromium de Playwright (CI).
        try:
            browser = p.chromium.launch(channel="chrome", headless=True)
        except Exception:
            browser = p.chromium.launch(headless=True)
        pg = browser.new_page()
        try:
            yield pg
        finally:
            browser.close()
