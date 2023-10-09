# Construction élémentaire : Utilisation de la console / Conditions 

## Exercice 1 : Utilisation de la partie "éditeur de programme"

Dans la partie d'édition de programme écrire le programme suivant : 

```
chaine = 'NSI'
var = 6 
var2 = 16
```
Puis l'exécuter

1. Que se passe-t-il ? Pourquoi ? 

2. Que se passe-t-il lorsqu'on appelle la variable `chaine` ? Pourquoi ce résultat ?

<u>Ecrire la ligne ci-dessous dans la console python :</u>

```python
>>> chaine = '7'
```

3. Re-exécuter le programme. Que se passe-t-il lorsqu'on appelle la variable `chaine` ? Pourquoi ?

## Exercice 2 : 

```
chaine2 = '123'
chaine3 = '14'
chaine4 = 'az'
chaine5 = 'abbbbbbbbbbbb'
```

1. Tester chaine2 < chaine3. Que se passe t-il ? Pourquoi ? 

2. Tester chaine4 < chaine5. Que se passe t-il ? Pourquoi ? 

3. Tester len(chaine4) < len(chaine5). Que se passe t-il ? Pourquoi ? 


## Exercice 3 : Communiquer avec l'utilisateur

Il y a deux manières (parmi tant d'autres) pour communiquer avec l'utilisateur (celui qui exécute le programme). L'une d'elle est la fonction `print()`.

`print()` permet **d'afficher** une valeur.

<u>Ecrire ce bout de code dans la console python :</u>

```
>>> var = print(5)
>>> var 
```

1. Que s'est-il passé ? Que vaut var ? 

2. Quel est le type de la variable var ? (Utilisez `type(var)`)

## Exercice 4 : 

Ecrire le programme suivant : 

```python
print(5) 
print(7+9) 
print('7+9') 
val = 6  
print(val) 
print('val')
```

1. Expliquer les différents appels de print( )

## Exercice 5 : 

Une autre manière de communiquer avec l'utilisateur est la fonction input()

La fonction input prend un paramètre une valeur écrite par l'utilisateur.

<u>Ecrire cette ligne :</u>

```python
val_utilisateur = input("Ecrire une phrase") 
```

<u>Exécuter le code, puis dans la console écrire :</u>

```python
>>> val_utilisateur 
>>> type(val_utilisateur)  
```

1. Que peut on en déduire ?

## Exercice 6 : 

1. Ecrire ce programme en python

```
Demander à l'utilisateur d'écrire une phrase qui sera affectée à une variable
Ajouter à cette phrase la chaine de caractère, `"(Cette phrase à été écrite par l'utilisateur)"`
Pour finir, afficher cette phrase
```

## Exercice 7 : 

1. Ecrire ce programme sous python (Essayer d'utiliser la fonction `int()`)

```
Demander à l'utilisateur d'écrire un nombre qui sera affectée à une variable
Puis élever ce nombre au carré
Si le nombre est divisible par 2 
    Alors afficher `"Le nombre écrit élevé au carré est divisble par 2"`
Sinon
    afficher `"Le nombre écrit élevé au carré n'est pas divisble par 2"`
```

## Exercice 8 : 

1. Ecrire ce programme sous python

```
Demander à l'utilisateur d'écrire une phrase
qui sera affectée à une variable
Si la longueur de la phrase est inférieur ou égale à 30
    Alors demander à l'utilisateur d'écrire une autre phrase et ajoutez la à la première phrase 
    Si la longueur de la phrase est inférieure à 30
        Alors afficher `"Malgré deux tentatives la phrase est trop courte"
    Sinon 
        Afficher "Apres deux tentatives l'utilisateur a écrit une phrase d'au moins 30 caractères"
Sinon 
    Afficher "l'utilisateur à écrit une phrase de 30 caractères en une seule tentative"
```
​    