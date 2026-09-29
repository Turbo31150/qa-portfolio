# Rapport d'exécution des tests — Preuve d'exécution locale

**Date d'exécution :** 2026-09-29
**Machine :** Linux x86_64 (`Linux 7.0.0-34-generic`)
**Mode :** exécution locale réelle (venv Python), sorties collées telles quelles.

> Ce rapport contient les sorties **réelles** de `pytest`. Aucun résultat n'est inventé ni retouché.

---

## 1. Environnement

| Élément | Valeur |
|---|---|
| Python | 3.12.3 |
| pytest | 9.1.1 |
| requests | 2.34.2 |
| playwright (paquet Python) | 1.63.0 |
| Navigateur E2E | Chrome système (`channel="chrome"`, headless) |

Préparation de l'environnement :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest requests playwright
```

> Note : le paquet Python `playwright` est requis même pour les seuls tests API, car
> `conftest.py` importe `playwright.sync_api` au chargement de la session pytest.

---

## 2. Tests API — `qa_api_sample.py`

**Commande :** `pytest -v qa_api_sample.py`
**Cible :** `https://jsonplaceholder.typicode.com` (API publique de test)

Sortie réelle :

```
========================================================= test session starts ==========================================================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/turbo/qa-portfolio/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/turbo/qa-portfolio
collecting ... collected 4 items

qa_api_sample.py::test_get_user_ok PASSED                                                                                        [ 25%]
qa_api_sample.py::test_list_posts_count PASSED                                                                                   [ 50%]
qa_api_sample.py::test_create_post PASSED                                                                                        [ 75%]
qa_api_sample.py::test_not_found PASSED                                                                                          [100%]

========================================================== 4 passed in 2.59s ===========================================================
```

**Résultat : 4 passed** (code de sortie `0`).

---

## 3. Tests E2E (Page Object Model) — `test_checkout_pom.py`

**Commande :** `pytest -v test_checkout_pom.py`
**Cible :** `https://www.saucedemo.com` (banc d'essai QA public)
**Navigateur :** Chrome système (headless), sélectionné automatiquement par `conftest.py`.

Sortie réelle :

```
========================================================= test session starts ==========================================================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/turbo/qa-portfolio/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/turbo/qa-portfolio
collecting ... collected 3 items

test_checkout_pom.py::test_checkout_nominal PASSED                                                                               [ 33%]
test_checkout_pom.py::test_login_invalide PASSED                                                                                 [ 66%]
test_checkout_pom.py::test_utilisateur_bloque[locked_out_user] PASSED                                                            [100%]

========================================================== 3 passed in 15.92s ==========================================================
```

**Résultat : 3 passed** (code de sortie `0`).

> Reproductibilité : ces tests E2E nécessitent un navigateur. Ici, Chrome système
> était présent, donc ils ont tourné en local. Sur une machine sans navigateur,
> installer le chromium de Playwright (`playwright install chromium`) ou s'appuyer
> sur la CI GitHub Actions (voir section 4).

---

## 4. Intégration continue (GitHub Actions)

Le workflow [`.github/workflows/qa.yml`](.github/workflows/qa.yml) exécute, à chaque `push`
sur `main` et à chaque `pull_request`, la même suite avec un chromium installé
(`playwright install --with-deps chromium`) :

- `pytest -v qa_api_sample.py` (tests API)
- `pytest -v test_checkout_pom.py` (tests E2E POM)

L'état du badge CI dans le [README](README.md) reflète le dernier résultat public.

---

## 5. Synthèse

| Suite | Fichier | Résultat local | Code sortie |
|---|---|---|---|
| API REST | `qa_api_sample.py` | 4 passed | 0 |
| E2E POM | `test_checkout_pom.py` | 3 passed | 0 |
| **Total** | | **7 passed** | **0** |

Aucun échec constaté lors de cette exécution du 2026-09-29.
