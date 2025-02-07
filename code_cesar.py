# Description: Ce programme permet de crypter et décrypter un mot en utilisant le chiffrement de César.
# Date de création: 04/02/2025 
# Date de modification: 06/02/2025
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
    
    espace = int(espace)  
    mot_cryp = "" 

    for let in mot: 
        if "a" <= let <= "z":  
            ascii_let = ord(let) + espace 
            if ascii_let > ord('z'):  
                ascii_let -= 26  
            
            mot_cryp += chr(ascii_let)
        else:
            mot_cryp += let  
    
    return mot_cryp


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
    mot_decryp = "" 
    espace = int(espace)  
    
    for let in mot: 
        if "a" <= let <= "z":  
            ascii_let = ord(let) - espace
            if ascii_let < ord('a'):  
                ascii_let += 26  
            
            mot_decryp += chr(ascii_let)
        else:
            mot_decryp += let  
    
    return mot_decryp

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
    for deca in range(1, 27):
        mot_decryp = ""

        for let in mot:
            if "a" <= let <= "z":  
                ascii_let = ord(let) - deca
                if ascii_let < ord('a'):
                    ascii_let += 26  
                mot_decryp += chr(ascii_let)
            else:
                mot_decryp += let  
        print(f"Décalage {deca} → {mot_decryp}")
    return "THE END"

# --- Test --- #

print(decrypt_sans_cle(input("Entrez le mot à décrypter : ")))

# --- Test --- #

         








