# TD : Tableaux

------

## 1. Application de cours :

1. Quelles sont les caractéristiques permettant de différencier les structures de données ? 

2.  Expliquez les différences entre une chaine de caractère et un tableau
3. Expliquez les différences entre un tuple et un tableau
4. Ecrire en python les requêtes suivantes :
   1. Créer un tableau contenant les entiers de 0 à 10 nommé tab
   2. Créer une chaîne de caractères contenant les 15 premières lettres de l'alphabet en minuscule nommé chaine
   3. Créer un tuple contenant les valeurs : "Prénom", "Nom", 15, False,True,"Spe1","Spe2","Spe3"
   4. Accéder au troisième élément des deux structures
   5. Modifier l'élément de 6ème position par une valeur quelconque. Si cela n'est pas possible, afficher le message d'erreur.
   6. Déterminer la longueur des trois structures

## 2. Fonctions clées des tableaux :

### 2. 1. Append :

Afin d'ajouter un élément à un tableau il existe une fonction *append()*

```python
>>> t = [1,2]
>>> t.append(3)
>>> t
[1,2,3]
```

1. Ecrire une fonction *tableau*_*premier_nombre()* prenant en paramètre un entier *nb* et qui renvoie un tableau contenant les nombres de 0 à *nb*. 

```python
... tableau_premier_nombre(...) : 
	"""
	Documentation à écrire
	"""
	...
	...
	while ... : 
		...append(...)
		............
	........
```

2. Quel sera l'appel de fonction pour obtenir le résultat suivant : [0,
2. 1,2,3,4,5] ?

### 2. 2. Count :

t.*count(n)* permet de compter le nombre d'éléments n dans un tableau t

```python
>>> t = [1,2,2]
>>> t.count(2)
2
```

1. Ecrire une fonction compte_element(tab,el) qui prend en paramètre un tableau et un élément et renvoie le nombre de fois ou l'élément *el* apparaît dans tab. *(Sans utiliser la fonction count( ))*

```python
>>> compte_element(["e","a","e","e"],"a")
	1
>>> compte_element(["e","a","e","e"],"e")
	3
```

2. Ecrire un appel de fonction pour une liste contenant toutes les voyelles et compte le nombre d'éléments "p"

## 3. Connaître la présence d'un élément dans une structure :

Un mot-clé très utile est le mot-clé ***in*** celui-ci permet de connaître la présence ou non d'un élément dans une structure.

**1)** Ecrire des exemples d'utilisation du mot-clé *in*, quel est la valeur de retour après utilisation de ce dernier (Faites des recherches sur internet)

**2)** Ecrire une fonction element_in_structure(struct,el) qui renvoie un booléen, True si *el* est dans la structure *struct,* False sinon. (Deux manières possibles) *(Sans utiliser le mot clé in)*

## 4. Tableau par compréhension :

Il existe une autre méthode de construction de tableau, il s'agit des listes par compréhension. Celles-ci permettent de créer des tableaux en une seule ligne.

```python
>>> tab = []
>>> for i in range(5):
			tab.append(i)
>>> tab
[0,1,2,3,4]

>>> tab2 = [i for in in range(5)]
>>> tab2
[0,1,2,3,4]
```

1. Quel est le contenu du tableau tab après exécutions du code ci-dessous :

```python
l = [1, 7, 9, 15, 5, 20, 10, 8]
tab = [p for p in l if p > 10]
```

2. Transformer ce tableau par compréhension en un code construisant le même tableau mais sans compréhension

## 5. Matrice : Tableau de tableau :

Un tableau peut contenir toute sorte de type d'éléments, et parmi eux il y a : les tableaux

En effet un tableau peut contenir d'autres tableaux et cela se présente comme ceci : 

```python
>>> tab = [[0,1,2],[3,4,5],[6,7,8]]
# On accède au premier élément
>>> tab[0]
[1,2,3]
# tab[0] est un tableau donc on peut accéder aux éléments du tableau
# On accède donc au premier tableau,puis au premier élément de ce tableau
>>> tab[0][0]
1
# Autre exemple :
>>> tab[2][1]
7
```

1. Voici une matrice m = [[1,4,5,7],[3,7,0],[9,2,6,8]]
   1. Comment accéder au deuxième 7
   2. Que renvoie m\[0]\[0]
   3. Comment accéder à 9

2. Ecrire une fonction qui prend en paramètre un tableau de tableau (matrice) *m* qui parcours la matrice m et affiche chacun des éléments qu'elle possède.