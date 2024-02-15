import math

def binaire(nombre,nb_bit):
    """
    Fonction permettant de passer de la base 10 à 2, permet aussi d'écrire le nombre binaire
    sur un nombre de bit défini par nb_bit
    param nombre : (int) nombre en base 10
    param nb_bit : (int) nombre de bit de nombre en binaire
    return : (list) tableau contenant la représentation de nombre en binaire sous nb_bit bits
    return : (str) Chaîne indiquant que la transformation est impossible si le nombre de bit est insufisant
    (int,int => list)
    """
    # On verifie si le nombre binaire peut être écrit
    
    # On construit le tableau qui contiendra les bits
    
    # Ajout des bits restants
    


def complement(tab):
    """Fonction effectuant la méthode du complément à deux sur un nombre binaire
    param tab (list) : Tableau modélisant le nombre binaire
    return (list) : Nombre opposé."""
    # Inversion des bits
    

    # Ajout de la valeur 1 :
    



def relatif(nb,nb_bit):
    """Donne l'écriture relative d'un nombre
    param nb : (int) nombre en base 10
    param nb_bit : (int) nombre de bit de nombre en binair
    return (str) : Representation relative d'un nombre en chaine de caractère
    """
    
    # Transformation tableau => chaine
    

def str_to_tab(nb_str):
    """
    Fonction qui transforme un nombre en chaîne de caractères en tableau
    exemple :
    >>> str_to_tab("1110101")
    [1, 1, 1, 0, 1, 0, 1]
    """
    
        
# Version vue en cours
def addition2(nb1_en_str,nb2_en_str) :
    """Effectue l'addition entre deux nombre relatif représenté par des chaînes de caractères"""
    # La chaine de caractères étant non mutable on transforme le nombre en tableau pour pouvoir manipuler chaque bits :
    nb1 = str_to_tab(nb1_en_str)
    nb2 = str_to_tab(nb2_en_str)
    # On verifie ici que les nombres sont représenté sur un même nombre de bits
    
    #Si le resultat possède plus de bits que t1 ou t2
    


        
