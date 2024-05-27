# Cours : Traitement de données en table

------

## 1. Introduction :

### 1. 1. Définition:

<u>**Table :**</u> tout type de fichier stockant de manière organisée des données. 

*Exemple :* 

| Nom | Prénom | Spe 1 | Spe 2 |
| --- | --- | --- | --- |
| Beta | Alice | NSI | Maths |
| Dupond | Bob | NSI | Anglais |

Plusieurs mots-clés découlent de ce tableau : 

- <u>Descripteur :</u> C’est une caractéristique de la table (ex :  Nom,Prénom...)
- <u>Objet :</u> C’est une ligne de la table (ex : Dupond,Bob,NSI,Anglais)

###  1. 2. Fichiers / Logiciels :

Il existe une multitude de logiciels pour traiter des données en table. Les plus connus sont les fichiers xls, ods. Ils sont manipulés par des logiciels tels que **Libreoffice calc ou Excel**. Afin de manipuler d’énormes bases de données, des fichiers **SQL** sont aussi utilisés. Ces fichiers sont manipulable via des logiciels de manipulation de bases de données. Ces logiciels permettent via le langage SQL de traiter efficacement un grand nombre de données. *(Programme terminale)*

Cette année en 1ère nous utiliserons des fichiers **csv**. 

Ce fichier a les particularités suivantes :

- Il est facilement compréhensible
- Manipulable par les logiciels de tableur (Excel...)
- Peut être écrit grâce à un éditeur de texte
- (Peut être manipulé par python)

<u>Fichier csv :</u>

Voici l’exemple ci-dessus écrit en .csv :

```
Nom;Prenom;Spe 1;Spe 2
Beta;Alice;NSI;Maths
Dupond;Bob;NSI;Anglais
```

Dans un fichier csv la première ligne correspond aux descripteurs (colonnes) de la table, les lignes suivantes correspondent aux objets.

Nous remarquons ici que chaque objet (donnée) est sur une seule ligne, les éléments de ces objets eux sont séparés par un **délimitateur** ici il s'agit de ;

### 1. 3. Ouverture d’un fichier en Python :

Pour ouvrir un fichier en python il existe une fonction native appelée *open()* pour ouvrrir et une fonction <u>close()</u> pour fermer le fichier.

```
file = open("monfichier.ext", 'r')
#
# Manipulation du fichier
#
file.close()

```

Ici la fonction *open()* prend deux paramètres : 

- Le nom du fichier (avec son extension)
- Le mode d’ouverture
    - **‘r’** pour **lecture** (read)
    - **‘w’** pour **écrire** dans le fichier (write)

Après cette ligne, le fichier est ouvert sous la variable *file.* Après avoir manipulé le fichier il faut le fermer, la méthode *close()* permet de faire cela.

### 1. 4. Manipulation de fichier csv en Python :

Afin de manipuler aisément les fichiers csv, il existe un **module csv**. Le module possède notamment une méthode *DictReader* permettant de récupérer les données sous forme de dictionnaire.

```python
import csv
t = []
file = open('table_pokedex.csv', 'r')
d = csv.DictReader(file,delimiter=',')
for i in d :
    t.append(dict(i))
file.close()
```

Que se passe t’il dans ce code ? 

- Le fichier est ouvert grâce à *open*
- Les données du fichier (file) sont récupéré dans la variable d
    - d est de type *csv.DictReader* **type semblable aux dictionnaire classiques**
- La boucle permet de transformer chaque ligne (objet) de *d* pour le transformer en un dictionnaire (grâce à *dict())*
- Chaque objet est ajouté à un tableau t

On manipulera les données grâce au tableau t désormais. 

<u>Exemple :</u> Voici un fichier csv

```
Nom;Prenom;Spe 1;Spe 2
Beta;Alice;NSI;Maths
Dupond;Bob;NSI;Anglais

Après exécution du code python le tableau t sera :

t => [["Nom","Prenom","Spe 1","Spe 2"],["Beta","Alice","NSI","Maths"],["Dupond","Bob","NSI","Anglais"]]
```

### 1. 5. Opérations possibles :

Il est possible de réaliser plusieurs opérations telles que : 

- Tri de la table selon un critère donné
- Sélections d’éléments avec ou sans critères
- Ajout d’une colonne
- Suppression de colonne
- Ajout d’élément
- Etc ...