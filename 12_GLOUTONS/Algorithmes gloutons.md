# Algorithmes gloutons :

## 1. Définition et principe :

Les algorithmes gloutons sont des algorithmes d'optimisation qui résolvent des problèmes en faisant des choix **localement optimaux** à chaque étape, dans l'espoir que ces choix mèneront à une solution globalement optimale. 

Ces algorithmes sont simples et rapides, mais **ils ne garantissent pas toujours d'obtenir la meilleure solution possible**. Ils conviennent particulièrement lorsque la solution optimale peut être construite itérativement en **ajoutant** ou en **supprimant** des éléments de manière séquentielle.

Le principe fondamental des algorithmes gloutons est de faire des choix qui semblent optimaux à chaque étape sans se soucier des conséquences à long terme. Ils sont généralement caractérisés par une **boucle itérative** qui construit progressivement une solution en effectuant des **choix** localement optimaux. 

La clé du succès d'un algorithme glouton réside dans la définition d'une **fonction d'évaluation (ou critère) appropriée** pour guider les choix.

## 2. Le rendu de monnaie :

Le rendu de monnaie est un problème très ludique pour comprendre les algorithmes gloutons. Imaginons un distributeur de monnaie, celui dispose des pièces/billets suivants : 1,2,5,10,20,50,100,200. Ici pour le rendu de monnaie, le but est **de rendre le moins de pièces/billets possibles.**

<u>Question 1 :</u> Si cette machine doit me rendre 47 euros, donnez 3 solutions de rendus possibles.

Un algorithme glouton doit suivre une règle afin de faire des choix à chaque étape de la résolution.  Pour cela l’algorithme va suivre la règle suivante : On rend la monnaie la plus grande possible à chaque étape.

<u>Question 2 :</u> Pour rendre 47 euros et en suivant la règle ci-dessus, quel sera le rendu effectué ?

<u>Question 3 :</u> Ecrire une fonction `glouton` qui renvoie une ***liste*** contenant toutes les pièces rendues pour une somme donnée en suivant la règle ci-dessus. Un système de monnaie est aussi donné.  

​	a. Quels seront les paramètres de la fonction ? De quels types sont ils? 

​	b. Que renvoie la fonction ? Quel est le type de cette valeur renvoyée ? 

​	c. Ecrire une documentation de cette fonction

​	d. Ecrire la fonction, en pseudo code dans un premier temps. Puis en python une fois le raisonnement trouvé.

​	e. Ecrire des tests de la fonction (Pouvant être mis en commentaire)

<u>Question 4 :</u> Déterminer un système de monnaie où la règle “On rend la monnaie la plus grande possible à chaque étape.” ne permet pas un rendu de pièces optimal.

## 3. Le problème du sac à dos :

Le problème du sac à dos est le suivant : Nous possèdons un sac permettant de porter un certains poids maximal (Supposons en kg). Des objets sont mis à notre dispositions en quantité illimitée, chacun de ces objets à une valeur et un poids. 

Le but ? Récolter des objets afin d'avoir la valeur maximale dans notre sac.

Supposons ces objets :

| Poids de l'objet  | 7    | 4    | 3    | 3    |
| :---------------- | ---- | ---- | ---- | ---- |
| Valeur de l'objet | 13   | 12   | 10   | 8    |

Représenté en python sous la forme suivante 

```python
objets = ((7,13),(4,12),(3,3),(3,8))
```

Ici différentes règles sont possibles :

- 1. Prendre l'objet avec la plus grande valeur
- 2. Prendre l'objet ayant le plus petit poids

<u>Question 1 :</u> Tester chacune des règles avec un sac ayant un poids maximal à 15.

<u>Question 2 :</u> Ecrire la fonction `sac_a_dos` qui appliquera l'algorithme glouton à un set d'objet afin d'obtenir une valeur quasi-optimale en utilisant la règle 1.

<u>Question 3 :</u> Ecrire la fonction `sac_a_dos2` qui appliquera l'algorithme glouton à un set d'objet afin d'obtenir une valeur quasi-optimale en utilisant la règle 2.

<u>Pour chacune des fonctions :</u>

​	a. Quels seront les paramètres de la fonction ? De quels types sont ils? 

​	b. Que renvoie la fonction ? Quel est le type de cette valeur renvoyée ? 

​	c. Ecrire une documentation de cette fonction

​	d. Ecrire la fonction, en pseudo code dans un premier temps. Puis en python une fois le raisonnement trouvé.

​	e. Ecrire des tests de la fonction (Pouvant être mis en commentaire)
