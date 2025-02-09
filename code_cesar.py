# Description: Ce programme permet de crypter et décrypter un mot en utilisant le chiffrement de César.
# Date de création: 04/02/2025 
# Date de modification: 08/02/2025
# Auteur: Uramix 

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
    
    espace = int(espace)  
    mot_cryp = "" 

    for let in mot: 
        if "a" <= let <= "z":  
            ascii_let = ord(let) + espace 
            if ascii_let > ord('z'):  
                ascii_let -= 26
            mot_cryp += chr(ascii_let)


        elif "A" <= let <= "Z":
            ascii_let = ord(let) + espace
            if ascii_let > ord('Z'):  
                ascii_let -= 26
            mot_cryp += chr(ascii_let)
        
        elif "0" <= let <= "9":
            ascii_let = ord(let) + espace
            if ascii_let > ord('9'):  
                ascii_let -= 10
            mot_cryp += chr(ascii_let)

        else:
            mot_cryp += let  
    
    print(f"\033[1;36m🔑 Décalage {espace:2d} ⮞ {mot_cryp}\033[0m")
    print("\033[1;32m")
    print("══════════════════════════════════════════════════════")
    print(f" ✅ cryptage avec le mot {mot} et la clé {espace} terminé ! 🎉")
    print("══════════════════════════════════════════════════════")
    print("\033[0m")

    


# --- Test --- # 

print(code_cesar(input("Entrez le mot à crypter : "), input("Entrez un nombre : ")))

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
    
    print("\033[1;33m")
    print("╔══════════════════════════╗")
    print("║     🔒 Code César 🔒     ║")
    print("║    ==== DONNÉES ====     ║")
    print("╚══════════════════════════╝")
    print("\033[0m")
    
    mot_decryp = "" 
    espace = int(espace)  
    for let in mot: 
        if "a" <= let <= "z":  
            ascii_let = ord(let) - espace
            if ascii_let < ord('a'):  
                ascii_let += 26
            mot_decryp += chr(ascii_let)

        elif "A" <= let <= "Z":
            ascii_let = ord(let) - espace
            if ascii_let < ord('A'):
                ascii_let += 26
            mot_decryp += chr(ascii_let)

        elif "0" <= let <= "9":
            ascii_let = ord(let) - espace
            if ascii_let < ord('0'):
                ascii_let += 10
            mot_decryp += chr(ascii_let)   

        else:
            mot_decryp += let  
    
    print(f"\033[1;36m🔑 Décalage {espace:2d} ⮞ {mot_decryp}\033[0m")
    
    print("\033[1;32m")
    print("══════════════════════════════════════════")
    print(f" ✅ Décryptage avec clé de {espace} terminé ! 🎉")
    print("══════════════════════════════════════════")
    print("\033[0m")


# --- Test --- #

print(decrypt_avec_cle(input("Entrez le mot à décrypter : "), input("Entrez une cle de chiffrement : ")))

# --- Test --- #



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

    for deca in range(1, 27):
        mot_decryp = ""

        for let in mot:
            if "a" <= let <= "z":  
                ascii_let = ord(let) - deca
                if ascii_let < ord('a'):
                    ascii_let += 26  
                mot_decryp += chr(ascii_let)

            elif "A" <= let <= "Z":  
                ascii_let = ord(let) - deca
                if ascii_let < ord('A'):
                    ascii_let += 26  
                mot_decryp += chr(ascii_let)


            elif "0" <= let <= "9":
                ascii_let = ord(let) - deca
                if ascii_let < ord('0'):
                    ascii_let += 10
                mot_decryp += chr(ascii_let)

            else:
                mot_decryp += let 

        print(f"\033[1;36m🔑 Décalage {deca:2d} ⮞ {mot_decryp}\033[0m")

    print("\033[1;32m")
    print("════════════════════════════")
    print(" ✅ Décryptage terminé ! 🎉")
    print("════════════════════════════")
    print("\033[0m")

# --- Test --- #

print(decrypt_sans_cle(input("Entrez le mot à décrypter : ")))

# --- Test --- #
