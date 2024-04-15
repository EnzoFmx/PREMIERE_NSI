# Fichier élève :

import pylab
import time
import random

def comp(elem1,elem2) :
    '''Fonction qui compare deux élément, 
    renvoie -1 si elem1 < elem2
    renvoie 0 si elem1 == elem2
    renvoie 1 si elem1 > elem2
    '''
    global cout
    cout+=1
    if elem1<elem2 :
        return -1
    elif elem1==elem2:
        return 0
    else:
        return 1

def cherche_elem(tab,elem) :
    """
    Fonction permettant de vérifier si un élément elem est présent dans un tableau tab
    param tab : (list) Tableau contenant les éléments à vérifier
    param elem : (   ) Elément à trouver dans tab
    return : (bool) True si elem est dans tab, False sinon
    """
    trouve = False
    for i in tab :
        if comp(i,elem) == 0 :
            trouve = True
    return trouve
    
def tri_insertion(tab) : 
    '''
    Fonction qui trie un tableau grâce au tri par insertion
    param tab: (list) tableau à trier
    return : (list) tableau trié
    '''
    taille = len(tab)
    for ind in range(1,taille) : 
            val_a_placer = tab[ind]
            ind2 = ind
            while ind2>0 and comp(tab[ind2-1],val_a_placer) == 1 :
                    tab[ind2] = tab[ind2-1]
                    ind2 = ind2 - 1 
            tab[ind2] = val_a_placer
    return tab

def tri_selection(tab) : 
    '''
    Fonction qui trie un tableau tab grâce au tri par sélection
    param tab: (list) tableau à trier
    return :  (list) tableau trié
    '''
    taille = len(tab)
    for i in range(taille-1) : 
            indice_valeur_minimale = i
            for j in range(indice_valeur_minimale,taille) :
                    # On compare les deux valeurs :
                    if comp(tab[j],tab[indice_valeur_minimale]) <= 0 :
                            indice_valeur_minimale = j
            #Echange des valeurs : 
            tab[indice_valeur_minimale],tab[i] = tab[i],tab[indice_valeur_minimale]
    return tab


def construit_tab_alea(taille) :
		"""
		Fonction qui crée un tableau avec des valeur aléatoire de taille taille
		param taille : (int) Taille du tableau
		return : (list) Tableau à renvoyer
		"""
		tab = []
		for i in range(taille) :
				val = random.randint(0,taille)
				tab.append(val)
		return tab


def construit_tab_bon_ordre(taille) :
		"""
		Fonction qui crée un tableau avec des valeur rangées par ordre croissant de taille taille
		param taille : (int) Taille du tableau
		return : (list) Tableau à renvoyer
		"""
		tab = []
		for i in range(taille):
			tab.append(i)
		return tab

def construit_tab_ordre_inverse(taille) :
    """
    Fonction qui crée un tableau avec des valeur rangées par ordre décroissant de taille
    taille
    param taille : (int) Taille du tableau
    return : (list) Tableau à renvoyer
    """
    tab = construit_tab_bon_ordre(taille)
    tab.reverse()
    return tab

t_taille = [i for i in range(500)]



########################################################################### Cout en nombre de comparaison ###########################################################################


# Construction du tableau des abscisses : 
t_taille = [i for i in range(151)] # Tableau par compréhension

### Calcul du coût pour tri_selection pour chaque taille (1 à 150 ici):
cout_selection = []
for taille in t_taille :
    cout = 0
    tri_selection(construit_tab_alea(taille))
    cout_selection.append(cout)

### Calcul du coût pour tri_insetion pour chaque taille (1 à 150 ici) :

## Meilleur des cas :
cout_tri_insertion_meilleur_cas = []
for taille in t_taille :
    cout = 0
    tri_insertion(construit_tab_bon_ordre(taille))
    cout_tri_insertion_meilleur_cas.append(cout)

## Pire des cas :
cout_tri_insertion_pire_cas = []
for taille in t_taille :
    cout = 0
    tri_insertion(construit_tab_ordre_inverse(taille))
    cout_tri_insertion_pire_cas.append(cout)

### Calcul du coût pour la recherche d'élément pour chaque taille (1 à 150 ici):
cout_recherche_element = []
for taille in t_taille :
    cout = 0
    cherche_elem(construit_tab_alea(taille),0)
    cout_recherche_element.append(cout)




# Création des courbes moyenne avec pylab :
pylab.plot(t_taille,cout_recherche_element,label = 'recherche d element')
pylab.plot(t_taille,cout_tri_insertion_pire_cas,label = 'tri insertion pire cas')
pylab.plot(t_taille,cout_tri_insertion_meilleur_cas,label = 'tri insertion meileur cas')
pylab.plot(t_taille,cout_selection,label = 'tri selection')


pylab.legend()
pylab.show()





