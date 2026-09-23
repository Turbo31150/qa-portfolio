#!/usr/bin/env python3
"""
Échantillon QA AUTOMATION (portfolio) — test end-to-end Playwright.
Démontre : navigation, auth, panier, assertions, capture-preuve sur échec.
Cible : https://www.saucedemo.com  (banc d'essai QA public, autorisé pour la démo).

Installation :
    pip install playwright pytest
    playwright install chromium
Exécution :
    pytest -v qa_playwright_sample.py
    # ou en direct :
    python3 qa_playwright_sample.py
"""
from playwright.sync_api import sync_playwright, expect

BASE = "https://www.saucedemo.com"
USER, PWD = "standard_user", "secret_sauce"   # identifiants de démo PUBLICS du banc d'essai


def run_checkout_flow(headless=True):
    """Parcours nominal : login → ajout au panier → checkout → confirmation."""
    with sync_playwright() as p:
        # Utilise le Chrome système s'il est présent (pas de download), sinon le chromium de Playwright.
        try:
            browser = p.chromium.launch(channel="chrome", headless=headless)
        except Exception:
            browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        try:
            # 1) Authentification
            page.goto(BASE, wait_until="domcontentloaded")
            page.fill("#user-name", USER)
            page.fill("#password", PWD)
            page.click("#login-button")
            expect(page).to_have_url(f"{BASE}/inventory.html")

            # 2) Ajout d'un article au panier
            page.click("button[data-test='add-to-cart-sauce-labs-backpack']")
            badge = page.locator(".shopping_cart_badge")
            expect(badge).to_have_text("1")

            # 3) Passage en caisse
            page.click(".shopping_cart_link")
            page.click("#checkout")
            page.fill("#first-name", "QA")
            page.fill("#last-name", "Tester")
            page.fill("#postal-code", "31000")
            page.click("#continue")
            page.click("#finish")

            # 4) Assertion finale = confirmation de commande
            expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
            # Capture-preuve du succès (artefact portfolio)
            page.screenshot(path="proof_checkout_pass.png", full_page=True)
            print("PASS  parcours checkout complet (login → panier → commande) — preuve: proof_checkout_pass.png")
            return True
        except Exception as e:
            # Preuve automatique sur échec (indispensable en QA)
            shot = "/tmp/qa_failure.png"
            page.screenshot(path=shot, full_page=True)
            print(f"FAIL  {e}\n      preuve -> {shot}")
            return False
        finally:
            browser.close()


# --- Intégration pytest (pour un vrai pipeline CI) ---
def test_checkout_flow():
    assert run_checkout_flow(headless=True) is True


if __name__ == "__main__":
    ok = run_checkout_flow(headless=True)
    raise SystemExit(0 if ok else 1)
