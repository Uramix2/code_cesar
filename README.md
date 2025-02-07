# 🔐 Chiffrement de César

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Cryptography-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Incomplete-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)

> **Un programme en Python permettant de chiffrer et déchiffrer un texte avec le chiffrement de César.**

## 📜 **Description**
Ce programme propose trois fonctionnalités principales :

- 🔹 **`code_cesar(mot, espace)`** → Chiffre un mot avec une clé donnée.
- 🔹 **`decrypt_avec_cle(mot, espace)`** → Déchiffre un mot avec une clé donnée.
- 🔹 **`decrypt_sans_cle(mot)`** → Tente de déchiffrer un mot sans clé en testant les 26 possibilités.

Le tout avec un affichage **stylé et coloré** en terminal ! 🎨✨

---

## 🚀 **Installation & Exécution**

### 1️⃣ Prérequis
Assurez-vous d'avoir **Python 3.x** installé sur votre machine. Vous pouvez vérifier votre version avec :
```sh
python --version
```

### 2️⃣ Cloner le dépôt :
```sh
git clone https://github.com/ton-github/chiffrement-cesar.git
```

### 3️⃣ Se déplacer dans le dossier :
```sh
cd chiffrement-cesar
```

### 4️⃣ Exécuter le programme :
```sh
python3 césar.py
```

---

## 🎯 **Utilisation**

### 🔒 **Chiffrement d'un mot**
```sh
Entrez le mot à crypter : BONJOUR
Entrez un nombre : 3
```
**Sortie :**
```sh
🔑 Décalage  3 ⮞ ERQMRXU
✅ Cryptage terminé ! 🎉
```

### 🔓 **Déchiffrement avec clé**
```sh
Entrez le mot à décrypter : ERQMRXU
Entrez une clé de chiffrement : 3
```
**Sortie :**
```sh
🔑 Décalage  3 ⮞ BONJOUR
✅ Décryptage terminé ! 🎉
```

### 🔍 **Déchiffrement sans clé (brute-force)**
```sh
Entrez le mot à décrypter : ERQMRXU
```
**Sortie :**
```sh
🔑 Décalage  1 ⮞ DQPLQWT
🔑 Décalage  2 ⮞ CPOKOPV
🔑 Décalage  3 ⮞ BONJOUR  ✅
🔑 Décalage  4 ⮞ AMNJMTQ
...
```

---

## 📌 **Exemple d'affichage ASCII**

```
╔══════════════════════════╗
║     🔒 Code César 🔒    ║
║    ==== DONNÉES ====     ║
╚══════════════════════════╝
```

---

## 🛠 **Explication du Chiffrement de César**
Le **chiffrement de César** est une méthode de chiffrement par substitution où chaque lettre du texte est décalée d'un certain nombre de places dans l'alphabet. Exemple avec un décalage de 3 :

- A → D
- B → E
- C → F

Ainsi, "BONJOUR" devient "ERQMRXU" avec un décalage de 3.


---

## 🤝 **Contributions**
Les contributions sont les bienvenues ! Si vous avez des idées d'améliorations, n'hésitez pas à **forker** ce projet et à proposer une **pull request**.

### 📌 Étapes pour contribuer :
1. **Fork** ce dépôt 🍴
2. **Créez** une nouvelle branche : `git checkout -b feature-nouvelle-fonctionnalité`
3. **Commitez** vos modifications : `git commit -m 'Ajout d'une nouvelle fonctionnalité'`
4. **Poussez** vers votre dépôt : `git push origin feature-nouvelle-fonctionnalité`
5. **Créez** une pull request 🔄

---

## 📜 **Licence**
Ce projet est sous licence **MIT** - vous pouvez l'utiliser librement ! ✅

🚀 *Projet créé par [Uramix](https://github.com/Uramix2/).*

