# 🐛 Bug Report — Visuel / Données (portfolio, cible publique reproductible)

**Titre** : [Visuel] Toutes les vignettes produits affichent la **même image** avec le compte `problem_user`

| Champ | Valeur |
|---|---|
| **ID** | BR-SD-VIS-001 |
| **Cible** | https://www.saucedemo.com/ (Sauce Labs — application de démonstration QA publique) |
| **Environnement** | Chromium (desktop, Linux), fenêtre 1280×900 |
| **Compte de test** | `problem_user` / `secret_sauce` (compte de test public documenté) |
| **Sévérité** | **Majeur** (impossible de distinguer les produits → parcours d'achat faussé) |
| **Fréquence** | **Systématique — 5/5** |
| **Priorité suggérée** | P2 |

**Préconditions**
- Page de connexion `saucedemo.com` chargée.
- Référence : le compte `standard_user` affiche une image **distincte et correcte** par produit.

**Étapes de reproduction**
1. Ouvrir `https://www.saucedemo.com/`.
2. Se connecter avec `problem_user` / `secret_sauce`.
3. Observer la grille de produits (`.inventory_item` → `img.inventory_item_img`).
4. Comparer avec le rendu obtenu via `standard_user`.

**Résultat attendu**
- Chaque produit affiche **sa propre** image (comme avec `standard_user`).

**Résultat obtenu**
- **Toutes** les vignettes affichent la **même** image (le même visuel répété pour tous les articles) → les produits ne sont plus distinguables visuellement.

**Preuves (protocole de vérification)**
- Capture de la grille produits `problem_user` vs `standard_user` (côte à côte).
- Vérification programmatique : extraire l'attribut `src` de chaque `img.inventory_item_img` et vérifier l'**unicité** (`len(set(srcs)) == nb_produits`). Sous `problem_user`, l'ensemble se réduit à **1 seule** URL d'image.
- ⚠️ *Captures à joindre à l'exécution ; le comportement est **constant et vérifiable en direct** par tout recruteur sur `saucedemo.com`.*

**Impact**
- En production, un tel défaut rend le catalogue inutilisable (le client ne peut pas identifier ce qu'il achète) → abandon de panier, retours, litiges. Illustre l'intérêt d'un **contrôle d'intégrité des assets** (unicité/validité des images) dans la suite de tests.

**Notes complémentaires**
- **Non reproduit** avec `standard_user` (0/5) → isole la cause au profil `problem_user` (défaut injecté volontairement par Sauce Labs pour l'entraînement à la détection de bugs visuels/données).
- Recommandation méthodo : ajouter une **assertion d'unicité des `src`** dans la suite E2E (`test_checkout_pom.py`) pour capter automatiquement ce type de régression d'assets.

---
*Cible publique reproductible (`saucedemo.com`). Rapport structuré avec assistance IA locale ; bug intentionnel documenté de Sauce Labs, vérifiable en direct — aucune donnée inventée.*
