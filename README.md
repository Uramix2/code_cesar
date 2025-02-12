# 🔐 Chiffrement de César

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Cryptography-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-complete-vert?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Faucheur/Baptium-white?style=for-the-badge)

Ce programme permet de **crypter** et **décrypter** un mot ou une date en utilisant le **chiffrement de César**.  
📅 **Date de création:** 04/02/2025  
🔄 **Dernière modification:** 09/02/2025  
👨‍💻 **Auteur:** Uramix  

> Apprend la cyber avec **CyberXploit** : plateforme de cybersécurité en ligne avec des cours, des challenges et des tutoriels 100% gratuits adaptés pour les débutants.

---
## 📜 **Description**
Ce programme propose plusieurs fonctionnalités :

- 🔹 **`code_cesar(mot, espace)`** → Chiffre un mot avec une clé donnée.
- 🔹 **`decrypt_avec_cle(mot, espace)`** → Déchiffre un mot avec une clé donnée.
- 🔹 **`decrypt_sans_cle(mot)`** → Tente de déchiffrer un mot sans clé en testant les 26 possibilités.
- 🔹 **`decrypt_date(date)`** → Déchiffre une date en brute force en testant les décalages de 0 à 9 tout en s'assurant qu'elle soit valide..

Le tout avec un affichage **coloré et interactif** dans le terminal ! 🎨✨

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


## ⚙️ **Utilisation**

Pour exécuter le programme, assurez-vous d'avoir **Python** installé sur votre machine.

```bash
python3 main.py
```

Au démarrage, un **menu interactif** s'affichera :

```
1 : Crypter un mot/date
2 : Décrypter un mot avec une clé
3 : Décrypter un mot en brute force
4 : Décrypter une date en brute force
```

Choisissez l'option souhaitée en entrant le **numéro correspondant**.

---
## 📚 **Explications des Fonctions**

### 1. `code_cesar(mot, espace)`
Chiffre un mot en utilisant le **chiffrement de César** avec un décalage donné.

### 2. `decrypt_avec_cle(mot, espace)`
Déchiffre un mot en connaissant le **décalage utilisé** pour le chiffrement.

### 3. `decrypt_sans_cle(mot)`
Déchiffre un mot par **force brute** en essayant tous les décalages de 1 à 26.

### 4. `decrypt_date(date)`
🔑 **Déchiffre une date** en utilisant tous les décalages de 0 à 9.

### 5. `is_valid_date(text)`
Vérifie si une chaîne de caractères correspond à une **date valide** au format `jj/mm/aaaa`.

---


## 🧪 **Exemple d'Utilisation**

### Chiffrement
```
Entrez le mot à crypter : bonjour
Entrez un nombre : 3
🔑 Décalage  3 ⮞ erqmrxu
```

### Déchiffrement avec clé
```
Entrez le mot à décrypter : erqmrxu
Entrez une clé de chiffrement : 3
🔑 Décalage  3 ⮞ bonjour
```


###  Déchiffrement sans clé (brute-force)
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
### Déchiffrement date souus format `jj/mm/aaaa`
```sh
Entrez la date à décrypter : 45/35/5358
```
**Sortie :**
```sh
🔑 Décalage  3 ⮞ 12/02/2025  ✅
...
```


---

## 📌 **Affichage ASCII début**

```
╔═══════════════════════════════════════════════════════════╗
║ 🔒 Menu de Chiffrement et Déchiffrement de code césar 🔒 ║
║                  Sélectionnez une option :                ║
╚═══════════════════════════════════════════════════════════╝


1 : Crypter un mot/date
2 : Décrypter un mot avec une clé
3 : Décrypter un mot en brute force
4 : Décrypter une date en brute force
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

