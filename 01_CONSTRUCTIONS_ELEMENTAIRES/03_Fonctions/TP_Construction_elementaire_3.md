# Construction élémentaire : Fonctions

------

## Exercice 1 : Fonction impair( )

1. Ecrire une fonction qui permet de savoir si `nombre` est impair

## Exercice 2 :

```python
var = 5
nbr = 1
def incr(nombre) :
    var = 7 
    return nombre+1
```

1. Que vaut `var` après l'exécution du code ? Pourquoi ?
2. Que fait la fonction `incr` ? Que renvoie `incr(nbr)` ?

Changez la ligne `return nombre+1` par `return var` puis réexécutez le code.

3. Que vaut `var` après l'exécution du code ? Pourquoi ?
4.  Que fait la fonction `incr` ? Que renvoie `incr(nbr)` ? 

> **Remarque :** Les variables écrites dans les fonctions sont dites **locales**. Elles apparaissent pendant l'appel de la fonction. Puis disparaissent quand la fonction est terminée. 
>
> Elles s'opposent à des variables **globales** qui sont écrites hors des fonctions et ne changent pas de valeurs sauf si on le fait soi-même.
>

## Exercice 3 : 

```python
var = 5
def incr(nombre) :
    test = 1
    print(var)
    print(test)
    return nombre+1
print(test)
```
<u>Exécuter ce code :</u>

1. Que se passe t'il lorsqu'on appelle la fonction `incr()` ? Expliquez 
2. Que vaut `test` lorsqu'on a exécuté le code? Lorsqu'on appelle `incr()` ? Après avoir appelé `incr()`


## Exercice 4 : 

```python 
def plus_grand_que(a,b) :
    if a > b : 
        print(a)
    elif a == b : 
        print(a)
    else :
        print(b)
```

1. Que fait cette fonction ? Que renvoie t'elle ? 
2. Ajoutez une valeur de retour à la fonction (Vous devez modifier la fonction)
3. Quel type `a` et `b` doivent avoir pour que la fonction fonctionne correctement ?

Pour qu'une fonction soit compréhensible pour l'utilisateur il faut écrire une **documentation**. Celle-ci est systématique et permet avant même d'écrire la fonction d'avoir une vue d'ensemble sur ce que l'on veut faire.

```python
def fonction(parametre1, parametre2) : 
    '''
    Phrase qui explique à quoi sert la fonction
    parametre1 : (type) a quoi sert parametre1
    parametre2 : (type) a quoi sert parametre2
    return : (type) Ce que la fonction renvoie
    '''
    #Blocs d'instruction de la fonction
```

4. Ecrire une documentation pour la fonction `plus_grand_que(a,b)`
