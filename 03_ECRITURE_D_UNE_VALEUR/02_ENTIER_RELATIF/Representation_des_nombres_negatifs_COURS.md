# Représentation des nombres négatifs :

------

## 1. Présentation :

Un nombre relatif est un nombre **entier** compris entre [-infini; + infini], celui-ci est donc positif ou négatif.

En base 10 ces nombres sont marqué d'un signe ' - ', mais qu'en est-il pour la base 2?

## 2. Représentation :

La représentation d'un nombre doit garantir :

- Que chaque nombre possède une seule et unique représentation
- L'addition de deux nombres opposés renvoie 0

Il existe une méthode permettant de trouver la représentation d'un nombre négatif, il s'agit **du complément à deux.**

*Dans ce cours nous manipulerons des octets (8bits)*

**<u>Fonctionnement :</u>**

- **Avoir un nombre négatif**
- **Prendre sa valeur absolue, la coder en binaire** 
- **Inverser tout les bits** 
- **Ajouter 1 au résultat.**

<u>Exemple avec la valeur -13 :</u>

- Valeur absolue : 13 => 00001101
- Inversion : 11110010
- On ajoute 1 => 11110011

**Le bit de poids fort (celui le plus à gauche) ici représente le signe. Tous les autres bits permettent donc de représenter le nombre.**

## 3. Plage des nombres possibles sur n bits :

Ce qu'il faut comprendre ici est qu'avec un nombre n de bits il est possible de représenter au maximum 2**n nombres.

- Par exemple, avec 3 bits je peux représenter 8 nombres différents. (000, 001, 010, 011,100,101,110,111) 

Sauf qu'ici nous devons utiliser ces bits pour représenter à la fois les nombres positif et les négatifs. 
Pour un problème d'équité nous utiliserons une moitié pour les positifs et une moitié pour les négatifs.

- Avec notre exemple sur 3 bits j'aurais 4 nombres positifs et 4 nombres négatifs.

Alors on pourrait imaginer que c'est si simple, nous pourrions aller de 4 à -4, sauf qu'au total cela permet de coder 9 nombres.
Et oui, il faut aussi coder le nombre 0.

En binaire, le nombre 0 est représenté seulement par des 0, donc le bit de signe est considéré comme positif. Dans ce cas, par logique il y aura 1 nombres positifs représenté en moins. 

- Avec notre exemple sur 3 bits j'aurai donc, 3 nombres positifs, 0 , 4 nombres négatifs.
- Ce qui me permet de représenter les valeurs allant de 3 à -4.

De manière générale avec un nombre n de bits, on représentera les valeurs allant de **(2\*\*n/2)-1 à (2\*\*n/2)**

- Pour la représentation des nombres sur 3 bits 

  | Codage binaire | Représentation des entiers naturels | Représentation des entiers relatifs |
  | -------------- | ----------------------------------- | ----------------------------------- |
  | 111            | 7                                   | -1                                  |
  | 110            | 6                                   | -2                                  |
  | 101            | 5                                   | -3                                  |
  | 100            | 4                                   | -4                                  |
  | 011            | 3                                   | 3                                   |
  | 010            | 2                                   | 2                                   |
  | 001            | 1                                   | 1                                   |
  | 000            | 0                                   | 0                                   |

  *(ces représentations peuvent être obtenue avec le complément à deux)*