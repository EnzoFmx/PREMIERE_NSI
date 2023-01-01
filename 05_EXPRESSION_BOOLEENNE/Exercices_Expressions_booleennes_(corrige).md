# Exercices : Expressions booléennes (corrige)

------

# Application de cours :

## Exercice 1 :

1) True 

2) True 

3) False 

4) False

5) 1 

6) 0 

7) True

8) 0

## Exercice 2 :

**s1 = !a | b**

| a    | b    | !a   | !a\|b |
| ---- | ---- | ---- | ----- |
| 1    | 1    | 0    | 1     |
| 1    | 0    | 0    | 0     |
| 0    | 1    | 1    | 1     |
| 0    | 0    | 1    | 1     |

**s2 = (a & b) | c** 

| a    | b    | c    | a&b  | a&b\|c |
| ---- | ---- | ---- | ---- | ------ |
| 1    | 1    | 1    | 1    | 1      |
| 1    | 1    | 0    | 1    | 1      |
| 1    | 0    | 1    | 0    | 1      |
| 1    | 0    | 0    | 0    | 0      |
| 0    | 1    | 1    | 0    | 1      |
| 0    | 1    | 0    | 0    | 0      |
| 0    | 0    | 1    | 0    | 1      |
| 0    | 0    | 0    | 0    | 0      |

**s3 = (a | b) & !c**

| a    | b    | c    | a\|b | !c   | a\|b & !c |
| ---- | ---- | ---- | ---- | ---- | --------- |
| 1    | 1    | 1    | 1    | 0    | 0         |
| 1    | 1    | 0    | 1    | 1    | 1         |
| 1    | 0    | 1    | 1    | 0    | 0         |
| 1    | 0    | 0    | 1    | 1    | 1         |
| 0    | 1    | 1    | 1    | 0    | 0         |
| 0    | 1    | 0    | 1    | 1    | 1         |
| 0    | 0    | 1    | 0    | 0    | 0         |
| 0    | 0    | 0    | 0    | 1    | 0         |

# Opérateurs booléens :

## Exercice 1 :

```python
#1 : not False
#2 : True and True
#3 : True and False
#4 : False and not True
#5 : False and True
#6 : (True and False) or (not(True or True))
#7 : not((not(True | False) & True))
#8 : ((True or True) and (True or True) & False)
```

## Exercice 2 :

```python
def xor(bool1,bool2) :
	"""
	Prédicat renvoyant le résultat de bool1 xor bool2
	param bool1 (bool) : Booléen à comparer
	param bool2 (bool) : Booléen à comparer
	return (bool) : résultat de bool1 xor bool2
	"""
	return (bool1 and not bool2) or (not bool1 and bool2))
```

## Exercice 3 :

```python
def est_triangle(long1,long2,long3) : 
	"""
	Fonction renvoyant le type de triangle en fonction des 3 longueurs
	param long1 (int) : Longueur d'un côté
	param long2 (int) : Longueur d'un côté
	param long3 (int) : Longueur d'un côté
	return (str) : Le type du triangle / Erreur sinon
	"""
    if long1 +long2 >= long3 and long1+long3 >= long2 and long3 + long2 >= long1 :
        if long1 == long2 and long2 == long3 :
            return 'Triangle équilatéral'
        elif long1 == long2 or long2 == long3 or long3==long1 :
            return 'Triangle isocèle'
        else :
            return 'Triangle scalène'
	else :
        return 'Les côtés ne permettent pas de former un triangle '
```

## Exercice 4 :

```python
def bibliotheque(client, livre) :
    '''Fonction renvoyant l'étage correspondant au type de livre recherché, selon le type de client (chaque client à certaines 		catégories accessible)
    param client (str) : Type de client enfant/ado/adulte
    param livre (str) : Type de livre jeunesse/fantaisie/sf/politique/economie
    return (str) : Un message correspondant à l'étage autorisé si permis, refus sinon'''
    if livre == 'sf' or livre == 'politique' :
        if client =='adulte' : 
            return 'etage 3'
    elif livre =='fantaisie' or livre =='sf' :
        if client == 'ado' or client == 'adulte' :
            return 'etage 2'
    elif livre =='jeunesse' :
        return 'etage 1'
    else :
        return 'Type de livre non dispo'
```

