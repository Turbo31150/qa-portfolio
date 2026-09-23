#!/usr/bin/env python3
"""
Échantillon QA API (portfolio) — tests d'API REST avec pytest + requests.
Démontre : GET/POST, codes HTTP, schéma de réponse, assertions, données de test.
Cible : https://jsonplaceholder.typicode.com  (API publique de test, ouverte).

Installation :  pip install requests pytest
Exécution :     pytest -v qa_api_sample.py     (ou : python3 qa_api_sample.py)
"""
import requests

BASE = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def test_get_user_ok():
    """GET /users/1 -> 200, structure attendue, email valide."""
    r = requests.get(f"{BASE}/users/1", timeout=TIMEOUT)
    assert r.status_code == 200, f"attendu 200, obtenu {r.status_code}"
    u = r.json()
    for champ in ("id", "name", "email", "address"):
        assert champ in u, f"champ manquant: {champ}"
    assert "@" in u["email"], "email invalide"


def test_list_posts_count():
    """GET /posts -> 200, exactement 100 éléments (donnée de référence de l'API)."""
    r = requests.get(f"{BASE}/posts", timeout=TIMEOUT)
    assert r.status_code == 200
    posts = r.json()
    assert isinstance(posts, list) and len(posts) == 100, f"attendu 100 posts, obtenu {len(posts)}"


def test_create_post():
    """POST /posts -> 201, l'API renvoie l'objet créé avec un id."""
    payload = {"title": "QA test", "body": "corps de test", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload, timeout=TIMEOUT)
    assert r.status_code == 201, f"attendu 201, obtenu {r.status_code}"
    created = r.json()
    assert created.get("title") == "QA test"
    assert "id" in created, "l'id de la ressource créée est absent"


def test_not_found():
    """GET d'une ressource inexistante -> 404 (gestion d'erreur)."""
    r = requests.get(f"{BASE}/users/99999", timeout=TIMEOUT)
    assert r.status_code == 404, f"attendu 404, obtenu {r.status_code}"


if __name__ == "__main__":
    passed = 0
    for fn in (test_get_user_ok, test_list_posts_count, test_create_post, test_not_found):
        try:
            fn(); passed += 1; print(f"PASS  {fn.__name__}")
        except AssertionError as e:
            print(f"FAIL  {fn.__name__}: {e}")
        except Exception as e:
            print(f"ERR   {fn.__name__}: {e}")
    print(f"---- {passed}/4 tests OK ----")
    raise SystemExit(0 if passed == 4 else 1)
