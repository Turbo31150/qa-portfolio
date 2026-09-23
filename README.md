# QA Portfolio — Manual Testing & QA Automation

[![QA](https://github.com/Turbo31150/qa-portfolio/actions/workflows/qa.yml/badge.svg)](https://github.com/Turbo31150/qa-portfolio/actions/workflows/qa.yml)

Portfolio de test logiciel : **rapports de bugs professionnels** + **tests automatisés exécutables** (Playwright & API). Chaque livrable est **reproductible et vérifié** — aucune donnée inventée.

> Manual QA + QA Automation portfolio: professional bug reports and runnable automated tests. Every artifact is reproducible and verified — no fabricated data.

---

## 📁 Contenu

| Fichier | Ce que ça démontre |
|---|---|
| [`qa_playwright_sample.py`](qa_playwright_sample.py) | Test **end-to-end navigateur** (login → panier → commande), assertions, capture-preuve sur échec |
| [`proof_checkout_pass.png`](proof_checkout_pass.png) | Capture du parcours **réussi** (preuve d'exécution) |
| [`qa_api_sample.py`](qa_api_sample.py) | Tests **API REST** (GET/POST, codes HTTP, schéma, cas 404) — 4 tests |
| [`BUG_REPORT_TEMPLATE.md`](BUG_REPORT_TEMPLATE.md) | Modèle de **rapport de bug** professionnel |
| [`BUG_REPORT_EXEMPLE.md`](BUG_REPORT_EXEMPLE.md) | Exemple **rempli et réaliste** (repro 5/5, logs, preuves) |
| [`PITCH_QA.md`](PITCH_QA.md) | Présentation / offre de service |
| [`test_checkout_pom.py`](test_checkout_pom.py) + [`pages.py`](pages.py) | Suite E2E en **Page Object Model** (parcours nominal + login invalide + user verrouillé) |
| [`.github/workflows/qa.yml`](.github/workflows/qa.yml) | **CI GitHub Actions** — les tests tournent à chaque push |

**Résultats locaux :** `test_checkout_pom.py` → **3 passed** · `qa_api_sample.py` → **4 passed** (7/7 verts).

## ▶️ Reproduire les tests

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install playwright pytest requests
playwright install chromium          # ou utilise Chrome système (channel="chrome")

# Test navigateur E2E
python qa_playwright_sample.py        # -> PASS + proof_checkout_pass.png

# Tests API
pytest -v qa_api_sample.py            # -> 4 passed
```

**Résultats obtenus** (environnement de dev) :
- `qa_playwright_sample.py` → `PASS parcours checkout complet` (exit 0)
- `qa_api_sample.py` → `4 passed`

## 🎯 Compétences

Test fonctionnel manuel · rédaction de bugs (repro, sévérité, preuve) · **Playwright** (E2E) · **pytest + requests** (API) · intégration CI · rigueur, traçabilité, respect des CGU et de la confidentialité (tests **on-premise** possibles).

## 🔒 Éthique

Bugs **réellement reproduits** et vérifiés manuellement. Sur les plateformes de test : je reproduis et documente moi-même ; l'outillage aide à la rédaction/automatisation, **jamais** à simuler une participation. Recherche de sécurité / bug bounty : **uniquement sur périmètre autorisé**.

## 📄 Réutilisation / Licence

Publié sous licence **[MIT](LICENSE)** — code et modèles librement réutilisables (attribution appréciée). Les exemples sont des artefacts de démonstration, adaptables à ton contexte.

---
*Cibles de démo : [saucedemo.com](https://www.saucedemo.com) et [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) — bancs d'essai publics conçus pour la pratique QA.*
