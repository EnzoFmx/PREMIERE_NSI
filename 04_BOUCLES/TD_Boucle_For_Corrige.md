# Corrigé TD Boucle for :

## Exercice 1 :
Question 1 : la boucle for permet de répeter un nombre déterminé de fois un bloc d'instruction
Question 2 : La fonction range va itérer des entier de 0 à n-1
Question 3 : '_' permet de ne pas stocker de variable
Question 4 : i et ind valent respéctivement les valeurs de 0 à 3 (i) et 0 à 44 (ind)
Question 5 : range(n,m) permettra d'obtenir les valeur comprise entre n et m-1
Question 6 : range(n,m,o) permettra d'obtenir les valeur comprise entre n et m-1 avec un pas o
Question 7 : i vaudra 2,3 ind => 10 15 20 25 30 35 40

## Exercice 2 :

```python
def puissance(nombre,n):
    """
    Fonction qui renvoie nombre à la puissance n
    param nombre : (int) nombre à élever à la puissance n
    param n : (int) puissance
    return : (int) nombre**n
    """
    total = 1
    for _ in range(n):
    	total = total*nombre
    return total
```

```python
def factorielle(n):
    """
    Fonction qui renvoie la factorielle de n
    param nombre : (int) n nombre
    return : (int) n factorielle
    """
    total = 1
    for fact in range(1,n+1):
    	total = total*fact
    return total
```

```python
def livret_epargne(somme,nb_annee):
    """
    Fonction qui renvoie la somme accumulée au bout de nb_annee.
    La fonction affiche aussi chaque année le bénéfice crée
    Le taux est de 1,5% par an
    param somme : (int) Somme de départ
    param nb_annee : (int) Nombre d'année à accumulé
    return : (float) montant accumulé en nb_annee
    """
    total = nb_annee
    for i in range(nb_annee):
    	interet = total*1.5/100
    	print("Il y a eu ",interet," euro d'interet cette année")
    	total = total+interet
    return total
```

## Etats de variables :

|                | n    | total | ind  |
| -------------- | ---- | ----- | ---- |
| Initialisation | 6    | 1     | ...  |
| Tour 1         | 6    | 1     | 1    |
| Tour 2         | 6    | 2     | 2    |
| Tour 3         | 6    | 6     | 3    |
| Tour 4         | 6    | 24    | 4    |
| Tour 5         | 6    | 120   | 5    |
| Tour 6         | 6    | 720   | 6    |

|                | a    | b    | c    |
| -------------- | ---- | ---- | ---- |
| Initialisation | 5    | 10   | 3    |
| Tour 1         | 10   | 6    | 15   |
| Tour 2         | 6    | 17   | 11   |
| Tour 3         | 17   | 16   | 22   |
| Tour 4         | 16   | 27   | 21   |
| Tour 5         | 27   | 30   | 32   |
| Tour 6         | 30   | 42   | 35   |
| Tour 7         | 42   | 49   | 47   |
| Tour 8         | 49   | 63   | 54   |

# Boucle for avec les chaines de caractères :

```python
def voyelle(chaine):
    """
    Fonction qui renvoie la chaine sans consonnes
    param chaine : (str) chaine de caractère
    return : (str) chaine sans consonnes
    """
    chaine_finale = ''
    for i in chaine :
        if i =='a' :
        	chaine_finale = chaine_finale + i
        elif i =='e' :
        	chaine_finale = chaine_finale + i
        elif i =='i' :
        	chaine_finale = chaine_finale + i
        elif i =='o' :
        	chaine_finale = chaine_finale + i
        elif i =='u' :
        	chaine_finale = chaine_finale + i
        elif i =='y' :
        	chaine_finale = chaine_finale + i
    return chaine_finale
```

# Ecriture d'un entier en base :

```python
>>> int('10000', 2)
16
>>> int('2e' , 16)
46
>>> hex(17)
'0xf1'
>>> hex(175)
'0xaf'
>>> bin(37)
'0b100101'
>>> bin(78)
'0b1001110'
```

# Fonction polygone :

```python
import turtle
def polygone(nb_cotes):
	"""Fonction dessinant un polygone en fonction du nombre de côtés demandés"""
    for i in range(nb_cotes):
        turtle.forward(50)
        turtle.left(360/nb_cotes)
```

