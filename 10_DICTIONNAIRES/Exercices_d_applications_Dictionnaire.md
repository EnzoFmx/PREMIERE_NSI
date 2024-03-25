# Exercices d’applications : Dictionnaire

------

## Exercice 1 : Nombre d'occurrence des lettres dans un texte

Ecrire une fonction nombre_occ(texte) qui prend un texte en paramètre et renvoie un dictionnaire contenant toutes les lettres du texte et leur occurrence.

```python
>>> nombre_occ('phraase ')
{'p':1,'h':1,'r':1,'a':2,'s':1,' ':1}
```

Bonus :  Ecrire une fonction nombre_occ_mot(texte) qui prend un texte en paramètre et renvoie un dictionnaire contenant tous les mots du texte et leur nombre d’apparition

## Exercice 2 : Calcul d'une moyenne

Ecrire une fonction moyenne(d) qui prend en paramètre un dictionnaire qui contient en clé la note et en valeur le nombre d’élève ayant cette note. Cette fonction renvoie la moyenne de ses notes.

```python
>>> moyenne({15:1,10:2,8.6:4})
9.857142857142858
```