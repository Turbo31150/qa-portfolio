# 🐛 Bug Report — Exemple rempli (portfolio)

**Titre** : [Progression] La progression du niveau 3 n'est pas sauvegardée après une fermeture forcée de l'application

| Champ | Valeur |
|---|---|
| **ID** | BR-20260923-001 |
| **Environnement** | Xiaomi Redmi Note 12, Android 13 (MIUI 14), app *DemoRunner* v1.4.0 build 210 |
| **Réseau** | Wi-Fi (stable, 80 Mb/s) |
| **Compte de test** | tester_07 (compte de test fourni par le studio) |
| **Sévérité** | **Majeur** (perte de progression joueur) |
| **Fréquence** | **Systématique — 5/5** |
| **Priorité suggérée** | P1 |

**Préconditions**
- Compte `tester_07` connecté.
- Niveaux 1 et 2 terminés ; niveau 3 en cours (checkpoint 2/4 atteint).

**Étapes de reproduction**
1. Lancer *DemoRunner*, charger la sauvegarde `tester_07`.
2. Jouer le niveau 3 jusqu'au **checkpoint 2/4** (l'UI affiche « Progression sauvegardée ✓ »).
3. Fermer l'application via le **multitâche Android** (swipe up), sans passer par le menu Quitter.
4. Relancer l'application et charger la sauvegarde `tester_07`.

**Résultat attendu**
- Le niveau 3 reprend au **checkpoint 2/4** (dernier point sauvegardé confirmé par l'UI à l'étape 2).

**Résultat obtenu**
- Le niveau 3 **redémarre au checkpoint 0/4** (début du niveau). La progression depuis le checkpoint 1 est perdue, malgré le message « Progression sauvegardée ✓ ».

**Preuves**
- 🎥 `repro_BR-20260923-001.mp4` (0:42, montre les 4 étapes + la perte au relancement).
- 📄 `logcat_BR-20260923-001.txt` — ligne 1187 : `SaveManager: flush() skipped (app killed before onPause commit)`.
- 📷 `before.png` (checkpoint 2/4 « sauvegardé ») et `after.png` (checkpoint 0/4 au relancement).

**Impact**
- Perte de progression réelle du joueur → frustration, risque de désinstallation et d'avis négatifs. Touche potentiellement tous les joueurs fermant l'app via le multitâche (comportement courant sur Android).

**Notes complémentaires**
- **Non reproduit** en quittant via le menu *Quitter* (0/5) → la sauvegarde n'est commitée qu'à `onPause`, pas à `onStop`/kill.
- **Reproduit** aussi sur Samsung Galaxy A54 / Android 14 (3/3). Suggère une sauvegarde à `onStop` ou un flush périodique.
- Première build observée : v1.4.0 (non testé sur v1.3.x).

---
*Reproduit et vérifié manuellement (5/5). Rapport structuré avec assistance IA locale ; toutes les valeurs proviennent d'observations réelles et des preuves jointes.*
