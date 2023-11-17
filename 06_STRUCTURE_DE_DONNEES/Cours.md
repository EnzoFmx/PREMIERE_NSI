# Cours : Structures de données

------

**Structure de données :** Collection d'information dans laquelle il est possible de stocker, traiter, organiser, extraire des données. Appelé aussi **type construit**. 

A la différence d'une donnée telle qu'un entier, un booléen qui contient qu'une seule valeur, la structure peut contenir un grand nombre de valeur. Toute structure possède des caractéristiques telle que l'indexation des éléments, la taille de la structure (fixe ou dynamique), la mutabilité. 

Afin de comprendre chacune des caractéristiques nous allons utiliser une structure de données déjà connue, qui est la **chaine de caractère**. En effet celle-ci permet de stocker de manière organiser des caractères.

## 1. Caractéristique des structures de données :

### 1. 1. **Indexation :**

Une structure de données indexée est une structure dans la quelle les éléments sont rangés par indice (Celui-ci commence à 0).

<u>**Cas des chaines de caractères :**</u>

- Par exemple la chaîne de caractères "Vive la nsi" contient 11 caractères.
    - Numéroté de 0 à 10, le premier élément est donc "V" puis "i", ainsi de suite.

En python il est possible d'accéder aux différents éléments d'une structure indexée grâce aux [ ] :

```python
>>> chaine = "Vive la nsi"
>>> chaine[0]
"V"
>>> chaine[1]
"i"
```

### 1. 2. Taille statique ou dynamique :

Une structure possède une taille, dans la grande majorité des cas cette taille est définie par le nombre d'éléments quelle possède. 

Une structure avec une taille dynamique peut donc changer de taille en fonction de l'ajout/suppression des éléments. 

<u>**Cas des chaines de caractères :**</u>

Le cas de la chaîne de caractères est assez particulier car si à première vu la chaîne peut avoir une taille dynamique la réalité est toute autre.

```python
>>> chaine = "Vive la nsi" 
>>> chaine = chaine + '!!'
>>> chaine
"Vive la nsi!!"
```

En réalité, lorsque l'on concatène (opérateur +) *chaine* avec une autre chaine de caractère nous créons en mémoire une nouvelle chaine de caractère. 

Cette taille est donc **fixe** pour les chaînes.

### 1. 3. Mutabilité :

La mutabilité est un terme résumant **la possibilité ou non de modifier l'interieur d'une structure de données**. 

Une structure de données mutable peut donc modifier son contenu.

<u>**Cas des chaines de caractères :**</u>

Pour savoir si une structure est mutable il suffit de :

- Vérifier s'il éxiste des fonction manipulant la structure
- Le faire manuellement

```python
#Utilisation de fonction propre à la structure
>>> chaine = 'JE SUIS UN TEST'
>>> chaine.lower()
'je suis un test'

# Changement de manière "manuelle"
>>> chaine[2]
' '
>>> chaine[5]
'I'
>>> chaine[5] = 'U'
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Ici il faut noter deux choses :

- La fonction lower( ) recréer une chaîne de caractères *(même problématique que pour la taille de la chaine)*
- Il n'est pas possible de changer les élèments même "manuellement"

La chaîne de caractère est donc **non mutable.**

## 2. Le tableau :

La chaine de caractère permet donc de stocker des caractères, mais qu'en est-il des entiers ? des booléens ?

C'est la que le tableau intervient, celui-ci permet de stocker des éléments de tout type. Et se décrit comme suit : 

| Structure | Indexé | Taille | Mutable | Type d'élément |
| --- | --- | --- | --- | --- |
| Chaine de caractère | Oui | Statique | Non | str |
| Tableau (théorique) | Oui | Statique | Oui | Eléments de même type |
| Tableau (list python) | Oui | Dynamique | Oui | Eléments de tous types |

Le tableau peut donc stocker tout type éléments, qu'ils soient de type entier, flottant, chaine de caractère, booléens, même tableau.

**Cas des tableau python :**

En théorie, un tableau possède une taille statique. Cependant python ne suit pas cette propriété.

Quelques différences sont notables avec les *list* python :

- La taille des structures est dynamique
- On peut y mettre plusieurs types d'éléments (Un tableau contenant des entiers et des chaînes par exemple)

```python
# Comment créer un tableau vide sous python :
tab = []
tab2 = list()

# Créer un tableau contenant des éléments
tab3 = [1,2,3]
tab4 = list([1,2,3])
```

## 3. Le n-uplet :

Le n-uplet (ou tuple) se différencie du tableau en deux points :

- Il n'est pas mutable
- Les éléments peuvent être de types différents

```python
# Comment créer un tuple :
tu = tuple()
tu2 = ()

# Créer un tuple contenant des éléments
tu3 = (1,"Nom",True)
tu4 = tuple((1,False,"prenom"))
```

| Structure             | Indexé | Taille    | Mutable | Type d'élément         |
| --------------------- | ------ | --------- | ------- | ---------------------- |
| Chaine de caractère   | Oui    | Statique  | Non     | str                    |
| Tableau (théorique)   | Oui    | Statique  | Oui     | Eléments de même type  |
| Tableau (list python) | Oui    | Dynamique | Oui     | Eléments de tous types |
| Tuple                 | Oui    | Statique  | Non     | Eléments de tous types |