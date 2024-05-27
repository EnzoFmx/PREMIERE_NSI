# TP : Traitement de données en table

------

## 1. Objectif :

- Manipuler des données provenant d’un fichier csv.
- Créer une interface

## 2. Traitement de données en table :

Pour ce TP nous allons manipuler des données de pokemon. 
Pour cela nous auront besoin :

- D'un fichier python élève 
- D'un fichier CSV contenant nos données

Le fichier table_pokedex.csv contient donc les données à traiter. 
Le fichier TP_NOM contient lui un début de code permettant d’ouvrir le fichier CSV et de récupérer les données.

Une fois les fichier récuperés et le code exécuté. Répondre aux questions suivantes :

Question 1 : De quel type est la variable t ? Quelle commande faire pour le savoir ? 

Question 2 : De quel type sont les éléments de t ? Quelle commande faire pour le savoir ? 

Question 3 : Ecrire la commande permettant d’afficher tous les éléments de t 

### 2. 1. Sélection d’éléments :

Afin de selectionner les éléments de t nous allons devoir créer un nouveau tableau contenant les éléments sélectionnés. Par exemple :

| Nom | Prénom | Spé 1 | Spé 2 |
| --- | --- | --- | --- |
| Beta | Alice | NSI | Maths |
| Dupond | Bob | NSI | Anglais |

```
Si je veux récupérer les objets ayant comme prénom “Alice”, je vais :

- Parcourir le tableau ci-dessus (Dans notre fichier c’est t)
- Vérifier pour chaque éléments si le prenom == ‘Alice’
  - Si c’est le cas alors j’ajoute cet élément dans un nouveau tableau
- On renvoie le nouveau tableau
```

Question 4 : Ecrire les instructions permettant de sélectionner tous les pokémons légendaires.

Question 5: Ecrire les instructions permettant de sélectionner **les noms** de tous les pokemon de type feu.

Bonus : Que fait la commande suivante 

```python
>>> [o[’Name’] for o in t if o[’Generation’] == "3"]
```

### 2. 2. Ajout d’éléments :

Par malheur les deux dernières générations de pokemon ne sont pas dans cette table, nous voulons donc voir comment faire pour ajouter ces pokemons.

Question 6 : Ecrire les instructions permettant d’ajouter un pokémon. Ajouter un pokémon ‘imaginaire’ dans le tableau t

### 2. 3. Ajout d’une colonne dans la table :

Afin de donner du sens aux statistiques du tableau nous aimerions ajouter une colonne nommée ‘total_stat’ qui serait la somme des colonnes suivantes : ‘Attack’, ‘Defense’, ‘Sp Atk’, ‘Sp Def’ et ‘Speed’

Question 7 : Ecrire les instructions permettant d’ajouter la colonne ‘total_stat’ pour chaque objet

### 2. 4. Tri de la table :

Pour l’instant les pokémon sont triés par id (numéro pokédex), mais nous pourrions trier la table en fonction des HP par exemples. 

Pour cela nous allons utiliser une fonction de tri, ici pas de panique nous allons nous servir de *sort( )* une fonction native de python permettant de trier directement une structure.

```
def cle_tri(t):
	return t['HP']
t.sort(key = cle_tri, reverse=True)
```

La méthode *sort* permet de modifier directement le tableau t et donc n’a pas de valeur de retour (*return*). Il est donc possible de consulter le tableau t directement trié.

- Le premier paramètre *key* permet d’informer à la fonction le descripteur à prendre en compte pour le tri (ici les hp)
- Le deuxième paramètre *reverse* permet de trier si la valeur est True par ordre décroissant (False pour croissant)

Question 8 : Après avoir exécuté le code ci-dessus, écrire l’instruction permettant de trouver **le nom** du pokémon avec le plus de HP ? Idem pour celui ayant le moins de HP.

### 2. 5. Slices :

Il est possible de recupérer les n premiers ou n derniers éléments d’un tableau. Pour cela : 

```
>>> t = [0,1,2,3,4,5,6,7,8,9]
>>> t[:5]
[0,1,2,3,4]
>>> t[5:]
[5,6,7,8,9]
>>> t[2:5]
[2,3,4]
```

Les **slices** permettent de sélectionner une partie d’un tableau. 

Question 9 : Avec les exemples ci-dessus, écrire les instructions permettant de trouver les 3 premiers pokémon avec le plus de HP. Et les 3 derniers.

### Bonus :

Le but de cette partie est de réecrire les données dans un nouveau fichier csv. Pour cela lors de l’ouverture de ce nouveau fichier, il faudra mettre ‘w’ en paramètre au lieu de ‘r’. Pour écrire dans ce fichier, il suffit d’utiliser la méthode *write( )*

```
file2 = open('nouveau_fichier.csv','w')
file2.write('j adore la nsi')
file2.close()
```

Remarques : 

- N’oubliez pas la structure d’un fichier csv
    - 1ère ligne ⇒ Descripteurs
    - Les descripteurs de chaques objets sont séparé d’un délimitateur
        - , ou ;
    - La fin de ligne est symbolisée par le caractère *\n*

Si vous avez réussi cette partie, ajoutez votre fichier csv dans le rendu. 

Si le code n’est pas fini ou trop compliqué, essayez d’expliquer ce qui pourrait être envisageable à l’écrit (commentaires python)

## 3. Création d'une interface

Le but de la deuxième partie est de créer une interface qui utilisera les pokemons du fichier CSV, celle-ci est totalement libre mais doit respecter la règle suivante :

- Un utilisateur ne sachant pas coder doit pourvoir utiliser le programme.

Il peut être possible de :

- Créer son équipe
- Voir des pokémons de tel ou tel type
- Ajouter de nouveaux pokemons
- Etc.