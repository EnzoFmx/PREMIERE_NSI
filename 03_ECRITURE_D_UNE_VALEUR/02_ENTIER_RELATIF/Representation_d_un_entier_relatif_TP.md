# Représentation d'un entier relatif : TP

------

## 1. Première partie :

La première partie du TP à pour but de créer une/plusieurs fonction(s) qui renvoie(nt) la représentation d'un entier relatif.

<u>Rappel (complément à deux) :</u>

- Avoir un nombre négatif
- Prendre sa valeur absolue, la coder en binaire 
- Inverser tout les bits 
- Ajouter 1 au résultat.

*Si le nombre est positif on n'applique évidemment pas le complément à deux.*

```python
# Exemple de résultat souhaité :
# Avec nombre de bits :
>>> representation(-2,3)
"110"
>>> representation(2,3)
"010"

#Sans nombre de bits => de base 8 :
>>> representation(-2)
"11111110"
>>> representation(2)
"00000010"
```

**Attention : Avant de commencer il faut penser à quelle structure de données on peut utiliser, combien de fonctions seront nécessaire (et que feront elles)**

## Partie 2 . Addition de deux nombres :

Le but est d'écrire une fonction addition prenant deux nombres relatifs sous forme binaire et renvoyant l’addition de ces deux nombres.

*A savoir : lorsque l’on additionne deux nombres représentés sur N bits et que le résultat de l’addition est sous N+1 bits alors le bit de poids fort (Celui tout à gauche est supprimé)*

- *Exemple :*

  ​    *110*

  *\+  010*

  *=1000*

*Le résultat de ce calcul est bien 000, nous avons représenté nos nombres sous 3 bits, le résultats reste donc sous 3 bits.*

**Il ne faut pas oublier que sur n bits nous pouvons représenter que des nombres allant de (2\*\*
(n-1))- 1 à -(2\*\*(n-1)). Si l’addition de deux nombres ne rentre pas dans cette tranche nous le
traitons pas ici. **

Exemple sur 4 bits => tranche allant de 7 à -8, 7+7 est impossible. 

On considère que l'utilisateur à connaissance de cette contrainte (pas à coder, juste dans la doc)

```python
# Exemple d'une possible fonction :
>>> addition("110","010")
"000"
>>> addition("1001","0110")
"1111"
```