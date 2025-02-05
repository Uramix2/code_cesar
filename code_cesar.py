 
def code_cesar(mot,espace):
    lettre = {1: 'a',2: 'b',3: 'c',4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
          11: 'k',12: 'l', 13: 'm', 14: 'n',15: 'o',
          16: 'p',17: 'q',18: 'r',19: 's',20: 't',
          21: 'u',22: 'v',23: 'w',24: 'x',25: 'y',26: 'z'}
    """
    Chiffre un mot en utilisant le chiffrement de César avec un décalage spécifié.

    Paramètres :
    mot (str) : Le mot à crypter.
    espace (int) : Le nombre de positions à décaler chaque lettre.

    Retourne :
    str : Le mot crypté.
    """
    
    mot_cryp = "" # variable pour inser le mot finale
    espace = int(espace) # Tranformer le paramètre espace en entier
    
    for let in mot: # Boucle qui parcour toute le parametre mot et retounre les le
       for key , val in lettre.items():
            if val == let:
                  numero = key
                  deca = (numero + espace ) % 26 # empêche le décalage des lettres si le rester de la division euclidienne est égale à 0
                  new_lettre = lettre[deca]
                  mot_cryp += new_lettre #ajoute les lettre décalé au mot crypté qui sera donné à l'utilisateur  
    return mot_cryp

#print(code_cesar(input("Entrez le mot à crypter : "), input("Entrez un nombre : ")))

def decrypt(mot):

    lettre = {1: 'a',2: 'b',3: 'c',4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
          11: 'k',12: 'l', 13: 'm', 14: 'n',15: 'o',
          16: 'p',17: 'q',18: 'r',19: 's',20: 't',
          21: 'u',22: 'v',23: 'w',24: 'x',25: 'y',26: 'z'}
    mot_decryp = ""
    for deca in range(1,27):
        for let in mot:
            if let in lettre.values():
                ascii_let = ord(let) - deca
                mot_decryp += chr(ascii_let)
                        
            else:
                mot_decryp += let
        print(f"Test n°{deca}: {mot_decryp}") 
                

print(decrypt("bonjour"))
            



        





