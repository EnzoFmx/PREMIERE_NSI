# TD : Boucle for

***Pour chaque fonction il ne faut pas oublier d'écrire la documentation***

## 1. Découverte :

### Exercice 1 :

1. Après avoir réussi avec brio un certain nombre de niveaux sur **compute it** expliquer l'utilité d'une boucle **for** :

*En python nous coderons la boucle for avec le mot clé for et le mot clé in*

Tester ces bouts de code (Une boucle à la fois)

```python
for _ in range(5): 
    print("Je suis un bloc d'instruction de la boucle for") 
 
for i in range(4): 
    print("Je suis la phrase numéro ",i) 
 
for ind in range(45): 
    print(ind)
```

2. Expliquez ce que fait la fonction range(n)

3. Que permet selon-vous la variable '_' ?

4. Que valent i et ind ? Pourquoi ?

Tester ces bouts de code (Une boucle à la fois)

```python
for _ in range(2,5): 
    print("Je suis un bloc d'instruction de la boucle for") 
 
for i in range(2,4): 
    print("Je suis la phrase numéro ",i) 
 
for ind in range(10,45,5): 
    print(ind)
```

5. Expliquez ce que fait la fonction range(n,m)

6. Expliquez ce que fait la fonction range(n,m,o)

7. Que valent i et ind ? Pourquoi ?

## 2. Application de cours :

### Exercice 1 :

1. Ecrire une fonction puissance(nombre,n) qui renvoie nombre à la puissance n *(Sans utiliser '**')*

2. Ecrire une fonction factorielle(n) qui factorielle de n *(factorielle(0) vaut 1)*

​		a. Que vaut factorielle de 5 ? 15 ? 25 ?

### Exercice 2 :

1.  Ecrire une fonction livret_epargne(somme,nb_annee) qui prend en paramètre une somme donnée et un nombre d'années. Cette fonction doit :

   - Avoir un taux de 1.5%

   - Afficher les intérêts annuels

   - Renvoyer la somme totale gagnée à l'année *nb_annee*
     
       a. Quel sera l'intérêt d'un compte ayant pour mise de départ 1600e au bout de 3 ans ? 10 ans ?


## 3. Etat des variables :

- Compléter ce tableau en utilisant factorielle(6):

|  | n | total | ind |
| --- | --- | --- | --- |
| Initialisation |  |  |  |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

Voici du code :

```python
a = 5 
b = a*2 
c = b*a//15
for ind in range(8) :  
    a = b 
    b = c+a//3 
    c = 5+a
```

Compléter le tableau ci-dessous :

|  | a | b | c |
| --- | --- | --- | --- |
| Initialisation |  |  |  |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |
| 7 |  |  |  |
| 8 |  |  |  |

## 4. Boucle for avec les chaînes de caractères :

Tester ce code : 

```python
chaine = "J adore la NSI"
for ind in chaine : 
    print(ind)
```

**Question 1 :** Expliquer ce qu'il se passe ici

### Exercice 1 :

1. Ecrire une fonction voyelle(chaine) qui va réécrire la chaine passée en paramètre sans consonnes. (On supposera que la chaine ne possède pas d'accent)

## 5. Ecriture d'un entier en base :

 Afin de manipuler des entier en base il existe certaines fonctions :

```python
#La fonction bin() prend un entier en paramètre et renvoie une chaine de caractère 
avec le nombre en base deux
>>> bin(10) 
'0b1010'
#Le nombre en base 2 est précéder de la chaine '0b' indiquant que ce nombre est 
écrit en base 2 
 
#La fonction hex() prend un entier en paramètre et renvoie une chaine de caractère 
avec le nombre en base 16
>>> hex(10) 
'0xa'
#Le nombre en base 16 est précéder de la chaine '0x' indiquant que ce nombre est 
écrit en base 16 
 
#La fonction int() permet de passer d'une base quelconque à la base 10
4 / 5
>>> int('1010',2) 
10
#Le nombre codé en base ici n'est pas précéder de '0b' ou '0x', de plus un 
#deuxième paramètre permet de renseigner la base d'origine.
```

*ll faut faire attention au type ici, les nombres créés en base 2 et 16 (par bin() et hex()) sont des chaines de caractère. Contrairement à int() qui prend une chaine et renvoie un entier)*

### Exercice 1 :

Compléter les '...' : 

```python
>>> int('10000', ...) 
16
 
>>> int(... , 16) 
46 
 
>>> hex(17) 
... 
 
>>> hex(...) 
'0xAF' 
 
>>> bin(...) 
'0b100101' 
 
>>> bin(78) 
...
```

Afin de comprendre le mécanisme utilisé pour créer ses chaines nous allons coder sous python les méthodes utilisées en cours pour passer d'une base à une autre. (Sans utiliser bin/dec/hex)

### Exercice 2 :

1. Ecrire une fonction dec_to_hex(nombre) qui prend en paramètre un nombre entier et renvoie une chaine de caractère sous la forme '0x...' décrivant le nombre en hexadécimal

```python
>>> dec_to_hex(15) 
'0xF'
```

2. Ecrire une fonction hex_to_dec(nb_chaine) qui prend en paramètre une chaine de caractère représentant le nombre en base 16 et renvoie un nombre en base 10

```python
>>> hex_to_dec('0xF') 
15
```

### Exercice 3 :

1. Ecrire une fonction bin_to_hex(nb_chaine) qui va transformer une chaine d'un nombre en base 2 vers une chaine d'un nombre en base 16

```python
>>> bin_to_hex('0b1111') 
'0xF'
```

2. Ecrire une fonction hex_to_bin(nb_chaine) qui va transformer une chaine d'un nombre en base 16 vers une chaine d'un nombre en base 2

```python
>>> hex_to_bin('0xF') 
'0b1111'
```

### Exercice Bonus :

- Ecrire une fonction *base_to_dec(nb_chaine, b)* qui prend en chaine un nombre codé en base b et le transforme en entier.
- Ecrire une fonction *polygone(nb_cote)* qui dessine à l'aide de turtle un polygone de cote nb_cote