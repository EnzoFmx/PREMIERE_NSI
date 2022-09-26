# Cours : Ecriture d'un entier en base

------

## 1. Objectifs :
- Ecrire un entier positif dans une base >= 2 
- Passer de la représentation d’une base dans une autre (base 2 10 16).

## 2. Présentation

Un ordinateur peut afficher des dizaines de milliers de caractères différents à l'écran, cependant ils sont tous représentés de la même manière en langage machine par des 0 et des 1. (_Voir cours Architecture machine_)

C'est que l'on appelle des chiffres binaires ou bits. Ils sont manipulés par la machine (Mémoire RAM, ROM).
Un ordinateur de 32 bits peut manipuler 32 chiffres binaires à la fois (64 bits pour 64 chiffres binaires). 

Un regroupement de 8 bits est appelé un **octet**.  

Il est possible grâce aux bits 0 et 1 de représenter toute sortes de choses, comme les nombres entier, les nombres réels, du texte, un son, une image. Tout dépendra du codage utilisé pour représenter l'information.

## 3. Encodage des entiers naturels

Voici la formule mathématique pour l'encodage des entiers naturels selon une base b :

n = n<sub>k-1</sub> * b<sup>k-1</sup> + n<sub>k-2</sub> * b<sup>k-2</sup> + ............................... + n<sub>1</sub> * b<sup>1</sup> + n<sub>0</sub> * b<sup>0</sup> 

Avec : 
- **n** le nombre à encoder
- **k** le nombre de chiffre de **n** 
- **b** la base où **n** est encodé

### 3. 1. Base 10

La base 10 est la plus connue, c'est la plus utilisée. Celle-ci comporte des chiffres compris entre 0 et 9 .(**10-1**)
Concrétisons avec le nombre 92021 qui s'encode de la manière suivante : 

**92021** = **9** * 10<sup>4</sup> + **2** * 10<sup>3</sup> + **0** * 10<sup>2</sup> + **2** * 10<sup>1</sup> +  **1** * 10<sup>0</sup> 
ou encore 
**92021** = **9** * 10000 + **2** * 1000 + **0** * 100 + **2** * 10 + **1** * 1

On écrira (30092021)<sub>10</sub> pour dire que 30092021 est écrit en base 10

### 3. 2. Base 2


La base 2 comporte les chiffres 0 et 1. Chaque chiffre d'un nombre aura un poids de 2<sup>i</sup> (i la position du chiffre)

Voici un nombre en base 2 : **101**

#### 3. 2. 1. Passer de la base 2 à la base 10 :

(**101**)<sub>2</sub> = **1** * 2<sup>2</sup> + **0** * 2<sup>1</sup> + **1** * 2<sup>0</sup> 
        = 4 + 0 + 1
        = 5

(101)<sub>2</sub> vaut donc (5)<sub>10</sub>

#### 3. 2. 2. Passer de la base 10 à la base 2

Pour faire ceci il faut faire une suite de division euclidienne :

<u>Première méthode :</u>

Exemple avec (77)<sub>10</sub> :

77 = 38 * 2 + **1** 
38 = 19 * 2 + **0** 
19 = 9 * 2  + **1** 
9  = 4 * 2  + **1** 
4  = 2 * 2  + **0** 
2  = 1 * 2  + **0** 
1  = 0 * 2  + **1** 

Le nombre se lit de bas en haut

Donc : (77)<sub>10</sub> => (1001101)<sub>2</sub>

### 3. 3. Base 16


La base 16 ou **hexadécimale** est elle aussi très utilisée. Celle-ci comporte 16 symboles. 

Il s'agit de 

- Des chiffres 0 à 9 
- Puis des symboles :
  - A => 10
  - B => 11
  - C => 12
  - D => 13
  - E => 14
  - F => 15

#### 3. 3. 1. Passer de la base 16 à la base 10

Il suffit d'utiliser la formule d'encodage. 

Par exemple le nombre (01BA)<sub>16</sub> donne en base 10 :

(01BA)<sub>16</sub> = **0** * 16<sup>3</sup> + **1** * 16<sup>2</sup> + **B** * 16<sup>1</sup> + **A** * 16<sup>0</sup> <br>
= 0 + 1 * 256 + 11 * 16 + 10 * 1 
= 256 + 171 + 10
= 437

(01BA)<sub>16</sub> vaut donc (437)<sub>10</sub>

#### 3. 3. 2. Passer de la base 2 vers la base 16


Il faut regrouper votre nombre binaires par des groupes de 4 bits (en commençant à droite) puis les convertir en hexadécimal.

Exemple :

(0 1010 1010 0001 1011)<sub>2</sub> donnera (0 A A 1 B)<sub>16</sub> soit (AA1B)<sub>16</sub>

#### 3. 3. 3. Passer de la base 16 à base 2

En utilisant le tableau, transformer les symboles hexadécimal en binaire.

Exemple : (A02B)<sub>16</sub> vaut (1010 0000 0010 1011)<sub>2</sub>