# Synthèse : Dictionnaire

Le dictionnaire est donc un type construit fonctionnant avec un système de clé/valeur ayant les caractéristiques suivantes :

### Accès aux éléments :

L’accès aux éléments d’un dictionnaire se fait par clé

```python
>>> d = {"fraises" : 3, 'raisins' : 2}
# Accès :
>>> d["fraise"]
3
```

### Mutabilité :

Le dictionnaire est mutable

```python
>>> d = {"fraises" : 3, 'raisins' : 2}
# Mutabilité 
d['raisins'] = 15
```

### Taille de la structure :

La taille d’un dictionnaire est dynamique

```python
>>> d = {"fraises" : 3, 'raisins' : 2}
#Ajout de valeur :
d['peche'] = 5
```

### Types des éléments de la structure :

- Les clés sont de type str (ou entier)
- Les valeurs peuvent être de tout type.

### Tableau récapitulatif :

| Nom de la structure | Accès aux éléments | Taille | Mutabilité | Type d’éléments |
| --- | --- | --- | --- | --- |
| Chaines de caractère | Indexé | Fixe | Non | str |
| Tableau (théorique) | Indexé | Fixe | Oui | Différents |
| Tableau (python) | Indexé | Dynamique | Oui | Identique |
| Tuple | Indexé | Fixe | Non | Différents |
| **Dictionnaire** | **Par clé** | **Dynamique** | **Oui** | **Différents** |