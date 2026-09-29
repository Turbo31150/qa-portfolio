# Matrice des cas de test

**Dernière mise à jour :** 2026-09-29
**Portée :** cas de test **réellement présents dans le code** de ce dépôt.
**Source de vérité :** `qa_api_sample.py`, `test_checkout_pom.py`, `pages.py`.

> Chaque ligne correspond à une fonction de test existante. Les entrées et résultats
> attendus sont ceux codés dans les assertions. Le statut reflète l'exécution locale
> du 2026-09-29 (voir [`TEST_EXECUTION_REPORT.md`](TEST_EXECUTION_REPORT.md)).

---

## Suite 1 — API REST (`qa_api_sample.py`)

**Cible :** `https://jsonplaceholder.typicode.com` · **Outils :** pytest + requests · **Timeout :** 10 s par requête

| ID | Fonction | Description | Entrée | Résultat attendu (assertions) | Statut |
|---|---|---|---|---|---|
| API-01 | `test_get_user_ok` | Lecture d'un utilisateur existant | `GET /users/1` | HTTP 200 ; le JSON contient les champs `id`, `name`, `email`, `address` ; `email` contient `@` | PASS |
| API-02 | `test_list_posts_count` | Volumétrie de la collection des posts | `GET /posts` | HTTP 200 ; réponse de type liste ; longueur exactement `100` | PASS |
| API-03 | `test_create_post` | Création d'une ressource | `POST /posts` avec `{"title":"QA test","body":"corps de test","userId":1}` | HTTP 201 ; le JSON renvoyé a `title == "QA test"` et contient un champ `id` | PASS |
| API-04 | `test_not_found` | Gestion d'une ressource inexistante | `GET /users/99999` | HTTP 404 | PASS |

---

## Suite 2 — E2E Page Object Model (`test_checkout_pom.py` + `pages.py`)

**Cible :** `https://www.saucedemo.com` · **Outils :** pytest + Playwright (Chrome/chromium headless) · **Identifiants publics du banc d'essai**

| ID | Fonction | Description | Entrée | Résultat attendu (assertions) | Statut |
|---|---|---|---|---|---|
| E2E-01 | `test_checkout_nominal` | Parcours d'achat complet : login → panier → commande | Login `standard_user` / `secret_sauce`, ajout du "Sauce Labs Backpack", infos client `QA` / `Tester` / `31000` | URL de l'inventaire = `/inventory.html` ; badge panier == `"1"` ; texte de confirmation == `"Thank you for your order!"` | PASS |
| E2E-02 | `test_login_invalide` | Cas d'erreur : identifiants invalides | Login `bad_user` / `bad_pass` | Le message d'erreur `[data-test='error']` est visible et contient `"Username and password do not match"` | PASS |
| E2E-03 | `test_utilisateur_bloque[locked_out_user]` | Cas limite : utilisateur verrouillé | Login `locked_out_user` / `secret_sauce` (paramétré via `@pytest.mark.parametrize`) | Le message d'erreur `[data-test='error']` est visible et contient (insensible à la casse) `"locked out"` | PASS |

---

## Objets de page utilisés (`pages.py`)

La suite E2E s'appuie sur un Page Object Model qui isole la mécanique d'interface :

| Classe | Rôle | Actions clés |
|---|---|---|
| `LoginPage` | Page de connexion | `goto()`, `login(username, password)` |
| `InventoryPage` | Inventaire produits | `assert_loaded()`, `add_backpack()`, `cart_badge()`, `open_cart()` |
| `CartPage` | Panier | `checkout()` |
| `CheckoutPage` | Tunnel de commande | `fill_info(first, last, zip)`, `finish()`, `confirmation_text()` |

---

## Récapitulatif de couverture

| Suite | Nombre de cas | Type | Résultat local (2026-09-29) |
|---|---|---|---|
| API REST | 4 | GET, POST, code succès, code erreur (404) | 4 PASS |
| E2E POM | 3 | Nominal + erreur d'authentification + cas limite (compte bloqué) | 3 PASS |
| **Total** | **7** | | **7 PASS** |

> Le script `qa_playwright_sample.py` reprend le même parcours nominal E2E que `E2E-01`
> sous forme de script autonome producteur de preuve (`proof_checkout_pass.png`) ; il n'est
> pas recompté ici pour éviter les doublons de comptage.
