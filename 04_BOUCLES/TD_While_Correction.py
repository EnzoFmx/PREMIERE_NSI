# Exercice 1 :
"""
for i in range(4): 
    print("Je suis la phrase numéro ",i)
    
i = 0
while i < 4 : 
    print("Je suis la phrase numéro ",i)
    i = i+1
 
for ind in range(45): 
    print(ind)

ind = 0
while ind < 45 :
    print(ind)
    ind += 1
"""

# Exercice 2 :
"""
for _ in range(2,5): 
    print("Je suis un bloc d'instruction de la boucle for")

t = 2
while t < 5 :
    print("Je suis un bloc d'instruction de la boucle for")
    t+=1
 
for ind in range(10,45,5): 
    print(ind)
    
ind = 10
while ind < 45 :
    print(ind)
    ind += 5
"""
def puissance(nombre,n):
    """
    Fonction qui renvoie nombre à la puissance n
    param nombre : (int) nombre à élever à la puissance n
    param n : (int) puissance
    return : (int) nombre**n
    """
    total = 1
    tour_de_boucle = 0
    while tour_de_boucle < n : 
        total = total*nombre
        tour_de_boucle = tour_de_boucle + 1
    return total




def voyelle(chaine):
    """
    Fonction qui renvoie la chaine sans consonnes
    param chaine : (str) chaine de caractère
    return : (str) chaine sans consonnes
    """
    chaine_finale = ''
    l = 0 
    while l< len(chaine):
        if chaine[l]=='a' :
            chaine_finale = chaine_finale + chaine[l]
        elif chaine[l] =='e' :
            chaine_finale = chaine_finale + chaine[l]
        elif chaine[l]=='i' :
            chaine_finale = chaine_finale + chaine[l]
        elif chaine[l] =='o' :
            chaine_finale = chaine_finale + chaine[l]
        elif chaine[l] =='u' :
            chaine_finale = chaine_finale + chaine[l]
        elif chaine[l] =='y' :
            chaine_finale = chaine_finale + chaine[l]
        l = l+1
    return chaine_finale


# COMPTE A REBOURS :

import time

def compte_a_rebours(temps):
    while temps>0 :
        print(temps)
        temps = temps-1
        # Permet de faire une pause d'une seconde
        time.sleep(1)
    return 'Fin'




# PIERRE FEUILLE CISEAUX :


"""
Raisonnement approximatif :

tant qu'un des deux joueur n'a pas 3 points

    joueur 1 choisi entre pierre feuille ou ciseaux
    joueur 2 choisi entre pierre feuille ou ciseaux

    comparaison des deux réponses :
        selon les choix =>
            soit j1 gagne 1 point
            
            soit j2 gagne 1 point
            
            soit personne ne gagne de point

"""



def pfc():
    resultat_J1 = 0
    resultat_J2 = 0

    while resultat_J1  != 3 and resultat_J2 != 3 :
        choix_J1 = input("Joueur 1 choisis entre pierre feuille et ciseaux")
        choix_J2 = input("Joueur 2 choisis entre pierre feuille et ciseaux")
        
        if choix_J1 == "pierre" and choix_J2 == "ciseaux" :
            print("J1 gagne cette manche")
            resultat_J1 += 1 #resultat_J1 = resultat_J1 + 1
        elif choix_J1 == "feuille" and choix_J2 == "pierre" :
            print("J1 gagne cette manche")
            resultat_J1 += 1 #resultat_J1 = resultat_J1 + 1
        elif choix_J1 == "ciseaux" and choix_J2 == "feuille" :
            print("J1 gagne cette manche")
            resultat_J1 += 1 #resultat_J1 = resultat_J1 + 1
        elif choix_J1 == "feuille" and choix_J2 == "ciseaux" :
            print("J2 gagne cette manche")
            resultat_J2 += 1 #resultat_J1 = resultat_J1 + 1
        elif choix_J1 == "ciseaux" and choix_J2 == "pierre" :
            print("J2 gagne cette manche")
            resultat_J2 += 1 #resultat_J1 = resultat_J1 + 1
        elif choix_J1 == "pierre" and choix_J2 == "feuille" :
            print("J2 gagne cette manche")
            resultat_J2 += 1 #resultat_J1 = resultat_J1 + 1
        else :
            print('Egalité')

    if resultat_J1 == 3 :
        print('GG J1')
    else :
        print('GG J2')




