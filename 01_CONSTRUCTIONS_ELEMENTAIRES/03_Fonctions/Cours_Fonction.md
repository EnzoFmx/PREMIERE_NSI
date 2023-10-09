# Construction élémentaire : Fonction

------

## 1. Pourquoi utiliser une fonction 

Une fonction permet de stocker un bout de programmer et de le réutiliser quand on le veut. Supposons une fonction qui permet de savoir si un nombre est pair. 

<u>En langage naturel cela se traduit par :</u>

```
Si le nombre est un multiple de 2 alors il est pair.
```

<u>Sous python :</u>

```python
# Il faut définir le nombre, supposons 5
>>> nombre = 5
>>> if (nombre % 2) == 0 : 
        est_pair = True
    else :
        est_pair = False
>>> est_pair 
False
```

Cette opération est à répéter pour chaque nombre à tester. Et si l'on fait ces mêmes opérations pour plusieurs nombres, nous perdons du temps à tout réécrire. Puis cela prend de la place dans la console ou le fichier python.

Pour pallier ce problème nous allons définir une fonction. 

Appelons la `pair(nombre)` : 

- La fonction s'appelle `pair`
- La fonction prend un nombre en paramètre
  
## 2. Définition de la fonction sous python :

Afin d'écrire une nouvelle fonction il faut la définir, le mot-clé `def` permet cela.
Afin de savoir si un nombre est pair nous avons besoin d'un `nombre`, donc nous aurons 1 paramètre ici. 

PS : Ne pas oublier les ":" à la fin de `def`

```python
def pair(nombre) : 
```

Nous savons déjà comment savoir si un nombre est pair (voir au-dessus) alors nous pouvons compléter la fonction

```python
def pair(nombre) : 
    if (nombre % 2) == 0 : 
        est_pair = True
    else :
        est_pair = False
```

Si nous laissons la fonction telle quel il y aura un problème.

Supposons que j'utilise ma fonction :

```python
>>> pair(5)
```

Ici rien ne se passe, aucun moyen de savoir si 5 est pair ou non.

Il faut ajouter un mot-clé `return` qui permettra de renvoyer une valeur lorsqu'on appellera la fonction.
Ici on veut savoir si nombre est pair, la variable permettant qui détermine si un nombre est pair est la variable `est_pair` qui dans un cas vaut `True` et l'autre cas `False`

```python
def pair(nombre) : 
    if (nombre % 2) == 0 : 
        est_pair = True
    else :
        est_pair = False
    return est_pair
```

## 3. Appel de fonction :

Ici pour réutiliser la fonction il faut l'appeler. Il s'agit ni plus ni moins que d'écrire la fonction (ici pair) suivit du/des paramètre(s) associé(s).

La valeur à la quelle correspond la fonction est associé au return. Lorsque j'appelle pair( ) je veux la valeur associée à `est_pair`

```python
>>> pair(5)
False
>>> pair(4)
True
```
