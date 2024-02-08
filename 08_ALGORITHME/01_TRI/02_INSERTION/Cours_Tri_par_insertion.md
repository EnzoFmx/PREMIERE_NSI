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
