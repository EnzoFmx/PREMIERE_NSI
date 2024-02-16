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
	ind = 0
    while ind < len(tab) - 1 :
        position_min = position_minimum(tab,ind)
        tmp = tab[ind]
        tab[ind] = tab[position_min]
        tab[position_min] = tmp        
        ind+=1
    return tab
```

## 2. Coût de l'algorithme :

Ce que l'on appelle coût ici est le nombre de comparaison faites entre deux éléments du tableau. Un tri est dit plus efficace qu'un autre si le coût est plus faible.

On admettra que pour un tableau de longueur n, le nombre de comparaisons est de l'ordre de : **(n*(n-1)) / 2**

<u>Prenons l'exemple d'un tableau de longueur 4 : [4,1,3,2]</u>

- Etape 1 : On cherche le minimum depuis la position 0 => on compare 4 à 1,3,2 => **3 comparaisons** => [1,4,3,2]
- Etape 2 : On cherche le minimum depuis la position 1 => on compare 4 à 3,2 => **2 comparaisons** => [1,2,3,4]
- Etape 2 : On cherche le minimum depuis la position 2 => on compare 3 à 4 => **1 comparaisons** => [1,2,3,4]
- La dernière étape n'est pas prise en compte pour le tri par insertion. 

Il y a ici bien 3+2+1 => 6 comparaisons soit : (4*(4-1)/2) => 6

Le coût  **(n*(n-1)) / 2** est considéré comme **quadratique** et est en O(n²)
