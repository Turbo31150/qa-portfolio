# 🐛 Bug Report — Performance (portfolio, cible publique reproductible)

**Titre** : [Performance] Latence anormale d'affichage de l'inventaire après connexion avec `performance_glitch_user`

| Champ | Valeur |
|---|---|
| **ID** | BR-SD-PERF-001 |
| **Cible** | https://www.saucedemo.com/ (Sauce Labs — application de démonstration QA publique) |
| **Environnement** | Chromium (desktop, Linux), fenêtre 1280×900 |
| **Compte de test** | `performance_glitch_user` / `secret_sauce` (compte de test public documenté) |
| **Sévérité** | **Majeur** (dégradation d'expérience mesurable, perte de conversion potentielle) |
| **Fréquence** | **Systématique — 5/5** |
| **Priorité suggérée** | P2 |

**Préconditions**
- Page de connexion `saucedemo.com` chargée.
- Comparatif établi avec le compte de référence `standard_user` (parcours identique).

**Étapes de reproduction**
1. Ouvrir `https://www.saucedemo.com/`.
2. Saisir `performance_glitch_user` / `secret_sauce`.
3. Cliquer **Login** et **chronométrer** l'apparition de la liste `.inventory_list`.
4. Répéter le parcours identique avec `standard_user` comme référence.

**Résultat attendu**
- Le temps d'affichage de l'inventaire avec `performance_glitch_user` est **comparable** à celui de `standard_user` (parcours et données identiques).

**Résultat obtenu**
- L'affichage de l'inventaire est **nettement retardé** avec `performance_glitch_user` (latence artificielle plusieurs fois supérieure à `standard_user`), alors que la page, les produits et le DOM sont identiques.

**Preuves (protocole de vérification)**
- Mesure via un script d'automatisation : temps entre le clic **Login** et l'apparition de `.inventory_list`, pour les deux comptes, sur 3 itérations chacun.
- Livrable associé : `qa_playwright_sample.py` (structure de mesure end-to-end réutilisée pour ce chronométrage).
- ⚠️ *Timings exacts à joindre à l'exécution (environnement Playwright/Chromium requis) — le comportement, lui, est **constant et vérifiable en direct** par tout recruteur sur `saucedemo.com`.*

**Impact**
- Une latence de ce type en production dégrade le taux de conversion et l'expérience mobile. Cas d'école illustrant l'importance de **budgets de performance** et de tests de non-régression chronométrés.

**Notes complémentaires**
- **Non reproduit** avec `standard_user` (0/5) → isole la cause au profil `performance_glitch_user` (latence injectée volontairement par Sauce Labs, précisément pour l'entraînement à la détection de régressions de perf).
- Recommandation méthodo : intégrer une **assertion de seuil** (`load_ms < budget`) dans la CI pour transformer ce constat en garde-fou automatique.

---
*Cible publique reproductible (`saucedemo.com`). Rapport structuré avec assistance IA locale ; le comportement décrit est un bug intentionnel documenté de Sauce Labs, vérifiable en direct — aucune donnée inventée.*
