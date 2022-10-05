# TD : Boucle while

## 1. Comparaison avec la boucle For :

<u>Question de cours :</u> Expliquez les différences entre les boucles for et les boucles while

### Exercice 1 :

Transformer ces boucles for en boucles while 

```python
for i in range(4): 
    print("Je suis la phrase numéro ",i) 
 
for ind in range(45): 
    print(ind)
```

1. Que se passe t'il avec la variable **i** et **ind ?**

### Exercice 2 :

Transformer ces boucles for en boucles while

```python
for _ in range(2,5): 
    print("Je suis un bloc d'instruction de la boucle for") 
 
for ind in range(10,45,5): 
    print(ind)
```

### Exercice 3 :

1. Ecrire une fonction puissance(nombre,n) qui renvoie nombre à la puissance n *(Sans utiliser '**') (à l'aide cette fois-ci de la boucle while)*

### Exercice 4 :

1. Ecrire une fonction voyelle(chaine) qui va réécrire la chaine passée en paramètre sans consonnes. (On supposera que la chaine ne possède pas d'accent) *(à l'aide cette fois-ci de la boucle while)*

## 2. Application des notions des cours :

### Exercice 1 :

1. Ecrire une fonction *compte_a_rebour(temps)* prenant en paramètre un *temps (type int)* et faisant le compte à rebours de temps jusqu'à 0.

<u>Exemple d'appel de fonction :</u>

```python
>>> compte_a_rebour(7)
7
6
5
4
3
2
1
'Fin'
```

Normalement le code écrit ne permet pas d'attendre '*temps'* secondes, une amélioration du code pourrait permettre ce changement. Pour cela il faut importer le module *Time.*

Pour rappel l'importation d'un module se fait comme ceci :

```python
#Comme pour le module turtle (import turtle)
import time

```

Cette importation demande lorsqu'on appelle les fonctions du module time de précéder le nom du module et d'un point avant toute fonction de ce module. *(Comme pour le module turtle)*

La fonction que nous allons utiliser ici est la fonction sleep() celle-ci prend en paramètre un entier et permet de faire une pause dans le programme.

```python
>>> import time
>>> time.sleep(2)
# Le programme va "dormir" deux seconde
```

2. Rajouter la fonction time à votre fonction afin de créer un vrai compte à rebours 

3. Ecrire les appels de fonctions pour un compte à rebours de 2min30, 1h, 30 sec.