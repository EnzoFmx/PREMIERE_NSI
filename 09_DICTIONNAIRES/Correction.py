# Introduction aux dictionnaires :

# Q1 :
    # Clés : "nom","prenom","age",'taille'
    # Valeurs : "Dupond",'Alice',16,171

# Q2 :
"""
taille_t = len(t)
taille_d = len(d)
"""
#Q3 :
fruits = { 'fraise' : 5, 'raisins' : 3, 'bananes' : 2}
# Achat client
fruits['bananes'] = 0
# Ajout pèches :
fruits['peches'] = 4

# Q4 :
d3 = {'nom': 'Timoleon', 'prenom': 'Alice', 'age': 16, 'taille': 171, 'classe': 'première'}
for cle in d3 : 
    print("La cle", cle , 'est associée à la valeur', d3[cle] )

def nb_occ(texte):
    d = {}
    # Pour chaque lettre du texte
    for lettre in texte :
        # Si la lettre est dans le dictionnaire => on l'a déjà comptée une fois
        if lettre in d :
            d[lettre] +=1
        # Sinon
        else: 
            d[lettre] = 1
    return d

def moyenne(d) :
    num = 0
    den = 0
    # Pour chaque note de mon dictionnaire
    for u in d :
        num =num + (u * d[u])
        den = den + d[u]
    return num/den

# Fonction écrite en cours :
def moyenne(dico):
    res = 0
    somme_coef = 0
    for j in dico :
        cle = j
        valeur = dico[j]
        res += cle * valeur
        somme_coef += valeur
    return res/somme_coef