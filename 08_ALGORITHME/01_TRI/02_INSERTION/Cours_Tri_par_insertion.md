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
            while ind2>0 and comp(tab[ind2-1],val_a_placer) > 1 :
                    tab[ind2] = tab[ind2-1]
                    ind2 = ind2 - 1 
            tab[ind2] = val_a_placer
    return tab
```

## 2. Coût de l'algorithme :

Ce que l'on appelle coût ici est le nombre de comparaison faites entre deux éléments du tableau. Un tri est dit plus efficace qu'un autre si le coût est plus faible.

Prenons deux tableaux : [1,2,3,4,5] et [5,4,3,2,1] et calculons le coût du tri.

<u>Pour le premier tableau</u> nous avons : **4 comparaisons**

- La comparaison de 2 et 1
- La comparaison de 3 et 2
- La comparaison de 4 et 3
- La comparaison de 5 et 4

Le tableau étant déjà trié il n'y a ici qu'une seule comparaison par élément.

<u>Pour le second tableau</u> nous avons : **10 comparaisons**

- 1 comparaison pour placer le chiffre 4
- 2 comparaison pour placer le chiffre 3
- 3 comparaison pour placer le chiffre 2
- 4 comparaison pour placer le chiffre 1

**On remarque ici qu'en fonction du tableau, nous aurons un coût différent, il existe donc un pire et un meilleurs cas**

### 2. 1. Coût du pire des cas :

Le pire des cas se produit lorsque le tableau est trié en sens inverse. Le coût associé est **n(n-1)/2** (n étant la longueur du tableau). Il s'agit d'un coup **quadratique** d'ordre de grandeur **O(n²)**

### 2. 2. Coût du meilleur des cas :

Le meilleur des cas lui se produit lorsque le tableau est déjà trié, dans ce cas aucun décalage n'est à faire. On compare seulement les éléments 1 fois, de ce fait on obtient un coût égal à **n** (n étant la longueur du tableau). Il s'agit ici d'un coup dit **linéaire** d'ordre de grandeur **O(n)**
