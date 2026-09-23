"""
Tests E2E via Page Object Model (pytest + Playwright).
Lisibilité : chaque test lit comme un scénario métier, la mécanique est dans pages.py.
"""
import pytest
from pages import LoginPage

USER, PWD = "standard_user", "secret_sauce"   # identifiants de démo PUBLICS de SauceDemo


def test_checkout_nominal(page):
    """Parcours d'achat complet : login → panier → commande confirmée."""
    inventory = LoginPage(page).goto().login(USER, PWD)
    inventory.assert_loaded().add_backpack()
    assert inventory.cart_badge() == "1"
    checkout = inventory.open_cart().checkout()
    checkout.fill_info("QA", "Tester", "31000").finish()
    assert checkout.confirmation_text() == "Thank you for your order!"


def test_login_invalide(page):
    """Cas d'erreur : identifiants invalides → message d'erreur affiché."""
    LoginPage(page).goto().login("bad_user", "bad_pass")
    err = page.locator("[data-test='error']")
    assert err.is_visible()
    assert "Username and password do not match" in err.inner_text()


@pytest.mark.parametrize("user", ["locked_out_user"])
def test_utilisateur_bloque(page, user):
    """Cas limite : un utilisateur verrouillé ne doit pas accéder à l'inventaire."""
    LoginPage(page).goto().login(user, PWD)
    err = page.locator("[data-test='error']")
    assert err.is_visible()
    assert "locked out" in err.inner_text().lower()
