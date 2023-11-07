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