"""
Page Object Model (POM) — SauceDemo.
Sépare la logique de test (le "quoi") de la mécanique de page (le "comment").
C'est le standard d'une suite QA automation maintenable.
"""
from playwright.sync_api import Page, expect

BASE = "https://www.saucedemo.com"


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto(BASE, wait_until="domcontentloaded")
        return self

    def login(self, username: str, password: str):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")
        return InventoryPage(self.page)


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def assert_loaded(self):
        expect(self.page).to_have_url(f"{BASE}/inventory.html")
        return self

    def add_backpack(self):
        self.page.click("button[data-test='add-to-cart-sauce-labs-backpack']")
        return self

    def cart_badge(self) -> str:
        return self.page.locator(".shopping_cart_badge").inner_text()

    def open_cart(self):
        self.page.click(".shopping_cart_link")
        return CartPage(self.page)


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def checkout(self):
        self.page.click("#checkout")
        return CheckoutPage(self.page)


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_info(self, first: str, last: str, zip_code: str):
        self.page.fill("#first-name", first)
        self.page.fill("#last-name", last)
        self.page.fill("#postal-code", zip_code)
        self.page.click("#continue")
        return self

    def finish(self):
        self.page.click("#finish")
        return self

    def confirmation_text(self) -> str:
        return self.page.locator(".complete-header").inner_text()
