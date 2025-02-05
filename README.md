# Chiffrement de César en Python

## Description
Ce programme implémente le chiffrement de César, un chiffrement par substitution où chaque lettre d'un message est remplacée par une autre située un certain nombre de positions plus loin dans l'alphabet. Il propose trois fonctionnalités :

1. **Chiffrement d'un mot avec un décalage donné.**
2. **Déchiffrement d'un mot avec une clé de décalage connue.**
3. **Déchiffrement sans clé par force brute** (affichage des 26 possibilités).

## Fonctionnalités

### 1. Chiffrement d'un mot avec le chiffrement de César
**Fonction : `code_cesar(mot, espace)`**

- **Paramètres** :
  - `mot` (str) : Le mot à crypter.
  - `espace` (int) : Le nombre de positions à décaler chaque lettre.
- **Retourne** :
  - Une chaîne de caractères représentant le mot chiffré.

#### **Exemple d'utilisation** :
```python
print(code_cesar("bonjour", 3))  # Sortie attendue : "erqmrxu"
```

---

### 2. Déchiffrement d'un mot avec une clé connue
**Fonction : `decrypt_avec_cle(mot, espace)`**

- **Paramètres** :
  - `mot` (str) : Le mot à décrypter.
  - `espace` (int) : Le nombre de positions à décaler en arrière.
- **Retourne** :
  - Une chaîne de caractères représentant le mot déchiffré.

#### **Exemple d'utilisation** :
```python
print(decrypt_avec_cle("erqmrxu", 3))  # Sortie attendue : "bonjour"
```

---

### 3. Déchiffrement sans clé (Brute Force)
**Fonction : `decrypt_sans_cle(mot)`**

- **Paramètres** :
  - `mot` (str) : Le mot à décrypter.
- **Affichage** :
  - Affiche les 26 possibilités de déchiffrement du mot.

#### **Exemple d'utilisation** :
```python
decrypt_sans_cle("erqmrxu")
```
**Sortie attendue :**
```
[Décalage  1] → dqplqwt
[Décalage  2] → cpokpvs
...
[Décalage 25] → fsrnsyw
[Décalage 26] → bonjour
```

---

## Instructions d'utilisation

1. **Exécute le script dans un interpréteur Python.**
2. **Utilise les fonctions en fournissant un mot et un décalage (sauf pour `decrypt_sans_cle`).**
3. **Si la clé est inconnue, utilise la fonction `decrypt_sans_cle()` pour tester toutes les possibilités.**

---

Bon chiffrement ! 🔐

