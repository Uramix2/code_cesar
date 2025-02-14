# Description: Ce programme permet de crypter et décrypter un mot ou un date en utilisant le chiffrement de César.
# Date de création: 04/02/2025 
# Date de modification: 09/02/2025
# Apprend la cyber avec CyberXploit : plateforme de cybersécrité en ligne avec des cours, des challenges et des tutoriels 100% gratuit adapté pour les débutants.
# Auteur: Uramix

# --- Importations --- #
from datetime import datetime

# --- Fonctions --- #

def code_cesar(mot, espace):
    """
     Chiffre un mot en utilisant le chiffrement de César avec un décalage spécifié.

    Paramètres :
    mot (str) : Le mot à crypter.
    espace (int) : Le nombre de positions à décaler chaque lettre.

    Retourne :
    str : Le mot crypté.
    """
    print("\033[1;33m")
    print("╔══════════════════════════╗")
    print("║     🔒 Code César 🔒     ║")
    print("║    ==== DONNÉES ====     ║")
    print("╚══════════════════════════╝")
    print("\033[0m")


    try:
        espace = int(espace)
        if espace < 0:
            raise ValueError
    except ValueError:
        print("\033[1;31m Utilisation incorrecte : 'espace' doit être un nombre entier positif.\033[0m")
        return "Utilisation incorrecte"

    mot_cryp = ""  # Initialisation du mot crypté

    for let in mot: 
        if "a" <= let <= "z":  
            ascii_let = ord(let) + espace
            if ascii_let > ord('z'):  # Gérer le retour à 'a' après 'z'
                ascii_let -= 26
            mot_cryp += chr(ascii_let)

        elif "A" <= let <= "Z":
            ascii_let = ord(let) + espace
            if ascii_let > ord('Z'):  # Gérer le retour à 'A' après 'Z'
                ascii_let -= 26
            mot_cryp += chr(ascii_let)
        
        elif "0" <= let <= "9":  # Pour les chiffres
            ascii_let = ord(let) + espace
            if ascii_let > ord('9'):  # Gérer le retour à '0' après '9'
                ascii_let -= 10
            mot_cryp += chr(ascii_let)

        else:
            mot_cryp += let  # Si c'est un autre caractère (comme un espace), on l'ajoute tel quel

    print(f"\033[1;36m🔑 Décalage {espace:2d} ⮞ {mot_cryp}\033[0m")  # Affiche le résultat du cryptage
    print("\033[1;32m")
    print("══════════════════════════════════════════════════════")
    print(f" ✅ cryptage avec le mot {mot} et la clé {espace} terminé ! 🎉")
    print("══════════════════════════════════════════════════════")
    print("\033[0m")

# --- Test --- # 

#print(code_cesar(input("Entrez le mot à crypter : "), input("Entrez une cle de chiffrement : ")))

# --- Test --- #

def decrypt_avec_cle(mot, espace):
    """
    Déchiffre un mot en utilisant le chiffrement de César avec un décalage spécifié.

    Paramètres :
    mot (str) : Le mot à décrypter.
    espace (int) : Le nombre de positions à décaler chaque lettre.

    Retourne :
    str : Le mot décrypté.
    """
    
    try:
        espace = int(espace)
        if espace < 0:
            raise ValueError
    except ValueError:
        print("\033[1;31m Utilisation incorrecte : 'espace' doit être un nombre entier positif.\033[0m")
        return "Utilisation incorrecte"


    print("\033[1;33m")
    print("╔══════════════════════════╗")
    print("║     🔒 Code César 🔒     ║")
    print("║    ==== DONNÉES ====     ║")
    print("╚══════════════════════════╝")
    print("\033[0m")


    mot_decryp = ""  # Initialisation du mot décrypté
    espace = int(espace)

    for let in mot:
        if "a" <= let <= "z":  
            ascii_let = ord(let) - espace
            if ascii_let < ord('a'):  # Gérer le retour à 'z' avant 'a'
                ascii_let += 26
            mot_decryp += chr(ascii_let)

        elif "A" <= let <= "Z":  
            ascii_let = ord(let) - espace
            if ascii_let < ord('A'):  # Gérer le retour à 'Z' avant 'A'
                ascii_let += 26
            mot_decryp += chr(ascii_let)

        elif "0" <= let <= "9":
            ascii_let = ord(let) - espace
            if ascii_let < ord('0'):  # Gérer le retour à '9' avant '0'
                ascii_let += 10
            mot_decryp += chr(ascii_let)   

        else:
            mot_decryp += let  # Si c'est un autre caractère (comme un espace), on l'ajoute tel quel

    print(f"\033[1;36m🔑 Décalage {espace:2d} ⮞ {mot_decryp}\033[0m")  # Affiche le résultat du décryptage
    
    print("\033[1;32m")
    print("══════════════════════════════════════════")
    print(f" ✅ Décryptage avec clé de {espace} terminé ! 🎉")
    print("══════════════════════════════════════════")
    print("\033[0m")


# --- Test --- # 

#print(decrypt_avec_cle(input("Entrez le mot à décrypter : "), input("Entrez une cle de chiffrement : ")))

# --- test --- #

def decrypt_sans_cle(mot):
    """
    Déchiffre un mot en utilisant le chiffrement de César en brute force.

    Paramètres :
    mot (str) : Le mot à décrypter.

    Affiche :
    Les 26 possibilités du mot décrypté.
    """

    print("\033[1;33m")
    print("╔══════════════════════════╗")
    print("║     🔒 Code César 🔒     ║")
    print("║    ==== DONNÉES ====     ║")
    print("╚══════════════════════════╝")
    print("\033[0m")


    for deca in range(1, 27):  # Essayer tous les décalages de 1 à 26
        mot_decryp = ""

        for let in mot:
            if "a" <= let <= "z":  
                ascii_let = ord(let) - deca
                if ascii_let < ord('a'):
                    ascii_let += 26  # Gérer le retour à 'z' avant 'a'
                mot_decryp += chr(ascii_let)

            elif "A" <= let <= "Z":  
                ascii_let = ord(let) - deca
                if ascii_let < ord('A'):
                    ascii_let += 26  # Gérer le retour à 'Z' avant 'A'
                mot_decryp += chr(ascii_let)

            elif "0" <= let <= "9":
                ascii_let = ord(let) - deca
                if ascii_let < ord('0'):
                    ascii_let += 10  # Gérer le retour à '9' avant '0'
                mot_decryp += chr(ascii_let)

            else:
                mot_decryp += let  # Si c'est un autre caractère (comme un espace), on l'ajoute tel quel

        print(f"\033[1;36m🔑 Décalage {deca:2d} ⮞ {mot_decryp}\033[0m")  # Affiche chaque possibilité

    print("\033[1;32m")
    print("════════════════════════════")
    print(" ✅ Décryptage terminé ! 🎉")
    print("════════════════════════════")
    print("\033[0m")


# --- Test --- # 

#print(decrypt_sans_cle(input("Entrez le mot à décrypter : ")))

# --- test --- #

def is_valid_date(text):
    """
    Vérifie si une date est valide.

    """
    try:
        datetime.strptime(text, "%d/%m/%Y")
        return True  
    except ValueError:  
        return False 

def decrypt_date(date):
    """
    Déchiffre une date en utilisant le chiffrement de César en brute force.
    """
     
    status_date = False # Initialisation de la variable pour vérifier si une date valide a été trouvée

    for i in range(0, 10):  # Essayer tous les décalages de 0 à 9
        decrypted_date = ""

        for e in date:
            if "0" <= e <= "9":
                new_digit = (int(e) - i) % 10  # Décalage vers l'arrière
                decrypted_date += str(new_digit) 
            else:
                decrypted_date += e  # Garder les autres caractères inchangés nottament le '/' entre les chiffres

        if is_valid_date(decrypted_date):  # Affiche la date si elle est valide
            status_date = True
            print(f"\033[1;36m🔑 Décalage {i:2d} ⮞ {decrypted_date}\033[0m")
       

    if status_date == True:  # Si aucune date valide n'a été trouvée
        print("\033[1;32m")
        print("════════════════════════════")
        print(" ✅ Décryptage terminé ! 🎉")
        print("════════════════════════════")
        print("\033[0m")
    else:    # Vérifie si la date est valide
        print("\033[1;31m Date invalide !\033[0m")
        print("\033[1;32m")
        print("════════════════════════════")
        print(" ❌ Décryptage impossible ! ")
        print("════════════════════════════")
        print("\033[0m")
    

    

# --- Test --- # 

#print(decrypt_date(input("Entrez la date : ")))

# --- Test --- #

# --- Fonction principale --- #
def main():
    """
    Fonction principale du programme.
    """
    print("\033[1;33m") # Couleur jaune
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║ 🔒 Menu de Chiffrement et Déchiffrement de code césar 🔒  ║")
    print("║                  Sélectionnez une option :                ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print("\033[0m") 

    print("\033[1;36m") # Couleur cyan
    print("1 : Crypter un mot/date")
    print("2 : Décrypter un mot avec une clé")
    print("3 : Décrypter un mot en brute force")
    print("4 : Décrypter une date en brute force")
    print("\033[0m") 

    choix = input("	\033[1;35m Entrez votre choix : \033[0m")  # Demande à l'utilisateur de choisir une option

    if choix == "1":
        mot = input("\033[1;32m Entrez le mot à crypter : \033[0m ")
        nombre = input("\033[1;32mEntrez un nombre : \033[0m") 
        code_cesar(mot, nombre)

    elif choix == "2":
        mot = input("\033[1;32m Entrez le mot à décrypter : \033[0m")
        cle = input("\033[1;32m  Entrez une clé de chiffrement : \033[0m")
        decrypt_avec_cle(mot, cle)

    elif choix == "3":
        mot = input("\033[1;32m  Entrez le mot à décrypter : \033[0m")
        decrypt_sans_cle(mot)

    elif choix == "4":
        date = input("\033[1;32m Entrez la date : \033[0m")
        decrypt_date(date)

    else:
        print("\033[1;31m Choix invalide !\033[0m") # Si l'utilisateur entre un choix invalide

# --- Exécution --- #
main()

# --- Fin  --- #
