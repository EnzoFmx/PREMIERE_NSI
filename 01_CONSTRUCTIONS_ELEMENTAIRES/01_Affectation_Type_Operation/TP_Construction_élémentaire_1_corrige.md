# TP 1 Corrigé :

<h2><u> Exercice 1 :</h2></u> 

```python
>>> a = 5
>>> a
5

>>> val = 5 + 7
>>> val
12

>>> 4-6
-2

>>> val = 7
>>> val2 = 9
>>> val * val2
63

>>> val = 5
>>> val / 2
2.5

>>> 2**3
8

>>> val = 5
>>> val // 2
2

>>> val = 5
>>> val % 2
1

>>> 5.0 + 2
7.0

>>> 3.2 + 3.4
6.6

>>> 5.0 + 3,2
8.0,2
```

<h2><u> Exercice 2 :</h2></u>

1) A quoi correspond l'opérateur "/" ? 
    **L'opérateur "/" permet de faire une division "simple" qui laissera apparaître une partie décimale (Résultat en float)**

2) A quoi correspond l'opérateur "//" ?
    **L'opérateur "//" permet de faire une division euclidienne et renverra le quotion de celle-ci**

3) A quoi correspond l'opérateur "%" ? 
    **L'opérateur "%" permet de faire une division euclidienne et renverra le reste de celle-ci**

4) A quoi correspond l'opérateur "** ?
    **L'opérateur "\*\*" d'élever à la puissance un nombre (a\*\*b élève a à la puissance b)**


<h2><u> Exercice 3 :</h2></u>

```python

>>> 7 + 3 
10

>>> 20 % 8
4 

>>> 15 % 7
1

>>> 15 / 4
3.75

>>> 16 // 4
4

>>> b = 4
>>> 5 + b
9

>>> val = 2
>>> 5*val
10
```

<h2><u> Exercice 4 :</h2></u>

Retranscrire sous python les phrases suivante : 

- J'affecte à une variable 'test' la valeur 10 + 2
\>>> test = 10+2

- J'appelle 'test'
\>>> test

- J'affecte à une variable 'test2' la valeur test ** 2
\>>> test2 = test**2

- J'appelle 'test2'
\>>> test2

- Obtenir le quotient de la division euclidienne de 15 par 6
\>>> 15//6

- Obtenir le reste de la division euclidienne de 17 par 7
\>>> 17%7


<h2><u> Exercice 5 :</h2></u>

Une chaine de caractère est délimité par des ' ' ou des " " 
Exemple :
-  'Je suis une chaine de caractère'
-  "Je suis une autre chaine de caractère"

```python
# Affecter à la variable chaine la valeur 'Je suis une chaine de caractère'
>>> chaine = 'Je suis une chaine de caractère'

>>> 'Je suis un bout ' + 'de chaine'
'Je suis un bout de chaine'

>>> "Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? " * 10
"Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? Repete et copain sont sur un bateau, copain tombe du bateau, qui reste t il a bord ? "
``` 

<h2><u> Exercice 6 :</h2></u>

Retranscrire sous python les phrases suivante :

- J'affecte à la variable test la chaine de caractère "Je suis un test"
\>>> test = "Je suis un test"

- Completer la phrase test avec la chaine " simple"
\>>> test = test + " simple"

- Appeler la variable test
\>>> test
