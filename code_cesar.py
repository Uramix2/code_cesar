lettre = {1: 'a',2: 'b',3: 'c',4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
          11: 'k',12: 'l', 13: 'm', 14: 'n',15: 'o',
          16: 'p',17: 'q',18: 'r',19: 's',20: 't',
          21: 'u',22: 'v',23: 'w',24: 'x',25: 'y',26: 'z'} 

def code_cesar(mot,espace):

    """
    Chiffre un mot en utilisant le chiffrement de César avec un décalage spécifié.

    Paramètres :
    mot (str) : Le mot à crypter.
    espace (int) : Le nombre de positions à décaler chaque lettre.

    Retourne :
    str : Le mot crypté.
    """
    
    mot_cryp = "" 
    espace = int(espace) 
    
    for let in mot: 
       for key , val in lettre.items():
            if val == let:
                  numero = key
                  deca = (numero + espace ) % 26 
                  new_lettre = lettre[deca]
                  mot_cryp += new_lettre 
    return mot_cryp


# --- Test --- # 
print(code_cesar(input("Entrez le mot à crypter : "), input("Entrez un nombre : ")))
# --- Test --- #


def decrypt_avec_cle(mot,espace):
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
       for key , val in lettre.items():
            if val == let:
                  numero = key
                  deca = (numero - espace ) % 26 
                  new_lettre = lettre[deca]
                  mot_decryp += new_lettre 
    return mot_decryp


# --- Test --- #

print(decrypt_avec_cle(input("Entrez le mot à décrypter : "), input("Entrez une clé de chiffrement : ")))

# --- Test --- #



def decrypt_sans_cle(mot):
    """
    Déchiffre un mot en utilisant le chiffrement de César en brute force.

    Paramètres :
    mot (str) : Le mot à décrypter.
    
    Retourne :
    str : Les 26 possibilités du mot décrypté.
    """

    lettre = {1: 'a',2: 'b',3: 'c',4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
          11: 'k',12: 'l', 13: 'm', 14: 'n',15: 'o',
          16: 'p',17: 'q',18: 'r',19: 's',20: 't',
          21: 'u',22: 'v',23: 'w',24: 'x',25: 'y',26: 'z'}
    for deca in range(1,27):
        mot_decryp = "" # Réinitialisation pour chaque test
        for let in mot:
            if let in lettre.values():
                ascii_let = ord(let) - deca
                mot_decryp += chr(ascii_let)
                        
            else:
                mot_decryp += let
        print(f"[Décalage {deca:2d}] → {mot_decryp}") 
                


# --- Test --- #

print(decrypt_sans_cle(input("Entrez le mot à décrypter : ")))

# --- Test --- #
