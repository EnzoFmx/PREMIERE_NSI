Révision :

## Tableau / Construction élémentaire :

### Exercice 1 :

Ecrire une fonction **premiers_elements(n : int)** qui renvoi la liste des premiers éléments de 0 à n (inclus)

```python
>>> premiers_elements(7)
[0,1,2,3,4,5,6,7]
```

### Exercice 2 :

Ecrire une fonction **premieres_lettre(n : int)** qui renvoi la liste des premiers éléments de la lettre 'a' à nième lettre de l'alphabet (inclus)

```python
>>> premieres_lettre(7)
['a','b','c','d','e','f','g']
>> premieres_lettre(27)
['a','b','c','d','e','f',...,'x','y','z']
```

### Exercice 3 :

a) Ecrire une fonction **suite_mystere(a : int ,b : int ,c : int)** qui renvoie le nombre d'étape nécessaire à la suite suite écrite si dessous pour que le résultat de la suite soit supérieur à 10000 :

- U(n) = (U(n-1)+a+b)*c
- U(0) = a+b 

```python
>>> suite_mystere(2,3,4)
5
```

b) Ecrire une fonction **suite_mystere(a : int ,b : int ,c : int)** qui renvoie le nombre d'étape nécessaire à la suite suite écrite si dessous pour que le résultat de la suite soit supérieur à 10000 :

- U(n) = (U(n-1)+a+b)*c si U(n-1) est pair, U(n) =(U(n-1)+a+c)\*b sinon
- U(0) = a+b 

```python
>>> suite_mystere(2,3,4)
6
```

### Exercice 4 :

Ecrire une fonction **add(tab1,tab2)** qui prend en paramètre deux tableaux et les additionne

```python
>>> add([1,2],[3,4])
[1,2,3,4]
```

### Exercice 5 :

Ecrire une fonction **inverse(tab)** qui prend en paramètre un tableau est qui renvoie le tableau mais à l'envers.

### Exercice 6 :

Ecrire une fonction **fusion(tab1,tab2)** qui prend en paramètre deux tableaux est qui fusionne et tri deux tableaux.

```python
>>> fusion([1,3,5],[2,4,6])
[1,2,3,4,5,6]
```

 ### Exercice 7 :

Ecrire une fonction **grille(nb_col,nb_ligne)** qui prend en paramètre deux entiers et qui créer une grille composées de *nb_col* colonnes et *nb_ligne* lignes, le résultat sera un tableau de tableau composé de 0.

```python
>>> grille(3,2)
[[0,0,0],[0,0,0]]
```

### Exercice 8 :

Ecrire une fonction **representation(grille)** qui prend en paramètre un tableau de tableau (grille) et affiche la représentation en str de cette grille