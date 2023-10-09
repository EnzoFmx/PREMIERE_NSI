# Cours : Boucle (for/while)

------

Un programme nécessite souvent un grand nombre d'instructions, celles-ci sont diverses. Pour réaliser un programme, il est parfois nécessaire de réutiliser certaines instructions un certain nombre de fois.

**Par exemple**, lorsque l'on veut dessiner un carré sur turtle nous allons dessiner chaque côté 4 fois. Ces instructions sont les mêmes, une boucle permet de ne pas réécrire 4 fois cette même instruction.

**Un autre exemple**, lorsque l'on joue à un morpion (tic tac toe), il n'y a pas qu'un seul tour du jeu, il y en a 9 au maximum (taille de la grille de base). Tant qu'un joueur n'a pas gagné ou que la grille n'est pas remplie alors il y a un tour du jeu. Ce tour sera écrit dans une boucle.

- **En python il existe deux types de boucles (ce n'est pas forcément le cas dans d'autre langages)**

## 1. Boucle for :

La boucle **for** est une boucle bornée. Il y a un nombre précis de boucles. Celle-ci utilise une **variable de boucle** et une **structure** à parcourir.

En python celle-ci s'écrit comme :

```python
for variable_de_boucle in structure : 
    #Instruction
```

### 1. 1. Grâce à **range() :**

La fonction range propre à python permet de créer une suite de nombres. La variable de boucle prendra comme valeur chaque nombre de cette suite. Le paramètre prit par la fonction est exclu de la suite : 

- Si l'on écrit range(5), il s'agit des entiers allant de 0 à 4.

Pour plus d'informations sur la fonction range() :

- Voir le TP boucle
- Voir la doc officielle de python (https://docs.python.org/fr/3/library/stdtypes.html#range)

Exemple : 

```python
for variable_de_boucle in range(4): 
    print("Je suis la phrase numéro ",variable_de_boucle) 
 
# Le résultat affiché sera :
"Je suis la phrase numéro 0"
"Je suis la phrase numéro 1"
"Je suis la phrase numéro 2"
"Je suis la phrase numéro 3"
```

### 1. 2. Grâce à une structure :

Une boucle for peut aussi s'effectuer avec une structure de données, un exemple de structure de données est la **chaîne de caractères (str).** Lorsque l'on boucle sur une structure la **variable de boucle prendra comme valeur chaque élement de la structure**.

- Une structure de taille **n** permettra de faire **n tours de boucles**.

```python
for variable_de_boucle in 'Je_suis_une_structure': 
    print(variable de boucle) 
 
# Le résultat affiché sera :
'J'
'e'
'_'
's'
# Ainsi de suite jusqu'à :
'r'
'e'
```

## 2. Boucle while :

La boucle **while** est une boucle non bornée. Il n'y a pas de nombre précis de boucles.

La boucle while est un "mélange" entre une **boucle for et une condition (if)**.

En effet cette boucle va s'exécuter **tant que** l'expression booléenne la complétant est vraie.

<u>Par exemple :</u>  

```python
# Tant que expression_bool est vraie alors on rentre 
# dans la boucle
while expression_bool : 
	# Condition
```

<u>**Parallèle à la boucle for :**</u>

Tout ce qui est possible de faire avec la boucle for est possible avec la boucle while. Cependant l'inverse n'est pas vrai.

### 2. 1. Comment faire une boucler n fois avec la boucle while ?

 Pour boucler n fois avec la boucle for il faut utiliser la fonction *range()* 

```python
# Supposons que je veuille boucler 5 fois

# Avec la boucle for
for i in range(5):
	print(i)

# L'équivalent en boucle while :
i = 0
while i < 5 :
	print(i)
	i = i + 1
```

Avec la boucle while, il n'y a pas de **variable de boucle.** Le seul moyen d'arrêter la boucle est d'avoir une **expression booléenne fausse**.

|  | i < 5  | print(i) | i |
| --- | --- | --- | --- |
| Initialisation | x | x | 0 |
| Tour 1 | True | Affiche 0 | 1 |
| Tour 2 | True | Affiche 1 | 2 |
| Tour 3 | True | Affiche 2  | 3 |
| Tour 4 | True | Affiche 3 | 4 |
| Tour 5 | True | Affiche 4 | 5 |
| Tour 6 | False | X | X |

Lors du 6ème tour de boucle, i vaut 5 et donc l'expression booléenne i<5 devient fausse. De ce fait on ne rentre pas dans la boucle et notre programme s'arrête.

#### 2. 1. 1. Attention aux boucles infinies :

Un problème récurrent avec les boucles while est que l'expression booléenne n'est jamais fausse. De ce fait, le programme va boucler à l'infini.

```python
# Ces programmes boucleront à l'infini
i = 0
while i < 5 :
	print(i)

while True :
	print("Je boucle")
```

Dans le premier cas il manque l'incrémentation de i : 

|  | i < 5  | print(i) | i |
| :-- | :-- | :-- | :-- |
| Initialisation | X | x | 0 |
| Tour 1 | True | Affiche 0 | 1 |
| Tour 2 | True | Affiche 1 | 2 |
| Tour 3 | True | Affiche 2 | 3 |
| Tour 4 | True | Affiche 3 | 4 |
| Tour 5 | True | Affiche 4 | 5 |
| Tour 6 | False | X | X |

Comme la valeur de i ne change pas alors alors la condition i < 5 sera toujours vraie.

<u>Dans le second cas **l'expression booléenne** vaut toujours True, celle-ci ne change pas donc cela bouclera à l'infini.</u>

### 2. 2. Parcours de structure :

Afin de parcourir une structure il faut utiliser les indices. 

**Une structure de données** telle qu'une chaîne de caractères possède des **élément positionné à un indice i.**

```python
#Comment utiliser la notion d'indice : 
>>> chaine = 'NSI'
>>> chaine[0] 
'N'
>>> chaine[3]
	Traceback (most recent call last):
	File "<pyshell>", line 1, in <module>
	IndexError: string index out of range
```

Les indices vont de 0 à la **longueur de la structure - 1.** 

Notre chaîne 'NSI' compte 3 caractères alors les indices sont : 0,1,2

Pour parcourir cette chaîne il faut donc :

```python
>>> chaine = 'NSI'
>>> indice = 0
# Tant que l'indice est inférieur à la longueur de chaine
# Soit 3
>>> while indice < len(chaine) : 
			print(chaine[indice])
			#On oublie pas d'incrémenter l'indice
			indice = indice + 1
```