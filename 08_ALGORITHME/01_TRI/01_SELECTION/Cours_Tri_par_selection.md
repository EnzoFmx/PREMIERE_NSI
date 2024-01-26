# Cours tri par sélection :

## 1. Première implémentation :

Voici un code permettant de trier un tableau par ordre croissant : 

```python
def comp(elem1,elem2) :
    """Fonction qui compare deux élément, 
    renvoie -1 si elem1 < elem2
    renvoie 0 si elem1 == elem2
    renvoie 1 si elem1 > elem2
    """
    if elem1<elem2 :
        return -1
    elif elem1==elem2:
        return 0
    else:
        return 1
   

def position_minimum(tab,ind):
    """
    Fonction qui renvoie la position de l'élément minimum d'un tableau tab 	   	   à partir de l'indice in
    ind (int) : valeur de départ pour la recherche du minimum
    tab (list) : Tableau de valeur
    return (int) : position du plus petit element
    """
    mini = tab[ind]
    pos_mini = ind
    while ind < len(tab) :
        if comp(tab[ind], mini) == -1  :
            mini = tab[ind]
            pos_mini = ind
        ind = ind +1
    return pos_mini
    
def tri_selection(tab) : 
	'''
	Fonction qui trie un tableau tab grâce au tri par sélection
	param tab: (list) tableau à trier
	return :  (list) tableau trié
	'''
	mini = tab[ind]
    pos_mini = ind
    while ind < len(tab) :
        if comp(tab[ind], mini) == -1  :
            mini = tab[ind]
            pos_mini = ind
        ind = ind +1
    return pos_mini
```
