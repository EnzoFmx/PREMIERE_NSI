# Construction élémentaire : Conditions et comparaisons

------

## 1. Opérateurs de comparaisons :

Il existe d'autres **opérateurs** sous python. Ce sont des opérateurs de comparaison, et ont besoin de deux valeurs d'entrée.

Voici la liste des opérateurs vus dans ce cours : 
- ***<***  Inférieur à
- **<=** Inférieur ou égal à
- **\>** Supérieur à
- **\>=**  Supérieur ou égal à
- ***==*** Egal à
- **!=** Différent de

<u>Exemple :</u>

```python
# 5 est bien inférieur à 6
>>> 5 < 6
True
# 5 n'est pas supérieur à 6
>>> 5 > 6 
False
# 7 est bien inférieur ou égal à 7
>>> 7<=7
True
# 5 est égal à 5
>>> 5 == 5
True
# 5 n'est pas égal à '5'
>>> 5 == '5'
False
# 5 est différent de "chaine de caractère"
>>> 5 != "chaine de caractère"
True
```

## 2. Type booléen et condition :

### 2. 1. Booléen

Les valeurs de retour vues dans l'exemple si dessus sont de type **bool**

Celui ci peut avoir deux valeurs possible :
-  True (Vrai)
-  False (Faux)

Ce type offre de nombreuses possibilités de programmation, l'une d'elles est la **condition**. 

### 2. 2. Condition

La condition permet en fonction du résultat de celle-ci d'effectuer une portion de code python. 

Elle se caractérise par le mot-clé **if** sous python

<u>Exemple en langage naturel :</u> 

```
Valeur = 15
Si valeur vaut 16
    Alors chaine vaut "La variable valeur vaut 16"
```

<u>Ecriture en python :</u>

```python
valeur = 15
if valeur == 16 :
    chaine = "La variable valeur vaut 16"
```

Complexifions ce bout de code, si `valeur` ne vaut pas 16 nous voudrions avoir une `chaine` l'indiquant.

Afin de faire cela nous utiliserons le mot-clé **else**. 

<u>Exemple en langage naturel :</u>

```
Valeur = 15
Si valeur vaut 16
    Alors chaine vaut "La variable valeur vaut 16"
Sinon
    chaine vaut "La variable ne vaut pas 16"
```
<u>Ecriture en python :</u>

```python
valeur = 15
if valeur == 16 :
    chaine = "La variable valeur vaut 16"
else :
    chaine = "La variable ne vaut pas 16"
```

Le mot-clé **elif** permet de complexifier d'autant plus le code, il se traduit par **sinon si**.
Il est placé toujours après un `if` et avant un autre `elif` ou `else` 

<u>Exemple en langage naturel :</u>

```
Valeur = 15
Si valeur vaut 16
    Alors chaine vaut "La variable valeur vaut 16"
Sinon si valeur est inférieur à 16
    Alors chaine vaut "La variable est inférieur à 16"
Sinon
    chaine vaut "La variable est supérieure à 16"
```
<u>Ecriture en python :</u>

```python
valeur = 15
if valeur == 16 :
    chaine = "La variable valeur vaut 16"
elif valeur < 16:
    chaine = "La variable est inférieur à 16"
else :
    chaine = "La variable est supérieure 16"
```
