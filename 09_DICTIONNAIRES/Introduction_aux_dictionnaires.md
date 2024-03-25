# Introduction aux dictionnaires

------

## 1. Introduction :

Afin de stocker des informations dans une seule et même variable nous utilisons communément le **n-uplet (tuple)** **ou le tableau**. 

Par exemple :

- t = (’Dupond’, ‘Alice’, 171, 16)

Ce n-uplet semble stocker des informations sur une personne. Le problème vient du type d’information contenue dans cette structure qui n’est pas indiqué. On peut facilement deviner qu’il s’agit d’un nom, d’un prénom, d’une taille et d’un âge. Mais sans la confirmation du développeur du code cela n’est que supposition.

De plus, l’accès aux éléments se fait par numéro de colonne et non par type d’information.

A la différence d’un n-uplet, le **dictionnaire** permet d’associer à chaque valeur une clé (unique). Cette clé fonctionne comme un indice, en effet lorsque l’on voudra accéder à une valeur du dictionnaire il faudra l’appeler par sa clé. (Et non par sa position)

De plus la clé est forcément une chaine de caractère (ou un entier). (*Str (ou int)*)

Même exemple :

Voici ce que cela peut donner lorsque l’on reprend l’exemple du dessus avec un dictionnaire.

- d = {'nom': 'Dupond', 'prenom': 'Alice', 'age': 16, 'taille': 171}

Ici chaque valeur correspond à une clé. Et donc, la structure correspond mieux au stockage de ce type de donnée.

Question 1 :  Listez les clés et les valeurs de ce dictionnaire. 

Question 2 :  Comment obtenir la taille de *t* et *d* ? Quelle est cette valeur ? 

## 2. Découverte du dictionnaire :

### 2. 1. Création :

La création d’un dictionnaire peut se faire de 3 manières différentes.

```python
# Création d'un dictionnaire vide : 
d = dict()
d2 = {}
# Création d'un dictionnaire avec données :
d3 = {'nom': 'Dupond', 'prenom': 'Alice', 'age': 16, 'taille': 171}
```

### 2. 2. Accès aux données et modification :

L’accès aux données se fait par la clé qui lui est associée. La modification quant à elle se fait par l’accès de la donnée suivit de la nouvelle valeur.

Par exemple :

```python
# Accès à la donnée :
>>> d3["nom"]
'Dupond'
# Modification :
>>> d3["nom"]  = 'Timoleon'
```

### 2. 3. Ajout d’élément :

Pour ajouter un élément il suffit d’appeler le dictionnaire suivit de la clé associée (nouvelle), puis d’y affecter la nouvelle valeur.

```python
>>> d3["classe"] = 'première'
>>> d3
{'nom': 'Timoleon', 'prenom': 'Alice', 'age': 16, 'taille': 171, 'classe': 'première'}
```

Question 3 :  Modéliser les instructions suivantes en python.

- Nous souhaitons créer un dictionnaire contenant les fruits disponibles chez un fruitier.
- Ce fruitier dispose de 5 fraises, 3 raisins et 2 bananes.
- Après achat d’un client, il reste 5 fraises, 3 raisins et 0 banane.
- Des pèches sont arrivées au magasin, elles sont au nombre de 4

## 3. Parcours d’un dictionnaire :

Il est possible à l’aide d’une boucle *for* de parcourir les **clés** d’un dictionnaire. 

Question 4 : Completer le code suivant.

```python
d3 = {'nom': 'Timoleon', 'prenom': 'Alice', 'age': 16, 'taille': 171, 'classe': 'première'}
for ........ in ............ : 
		print("La cle", ......... , 'est associée à la valeur', ........ )
```

## 4. Méthodes associées :

Il existe des fonctions agissant sur les dictionnaires afin de récupérer les clés, valeurs et items (couple clé/valeur). Les voici : 

```python
# Récupération des clés : 
d3.keys()
# Récupération des valeurs :
d3.values()
# Récupération des items :
d3.items()
```

Ces fonctions renvoient un élément de type <class 'dict_keys'>, <class 'dict_values'>, <class 'dict_items'> difficilement manipulable. Il est donc conseillé de changer ce type par le type *list* (tableau python)

- list(d3.keys( )) / list(d3.values( )) / list(d3.items( ))

Question 5 :  Ecrire la suite d’instructions permettant d’afficher les *items* de d3  

Bonus :  Ecrire une fonction creer_dict(tupl_valeur,tupl_cle) qui prend en paramètre un tuple de clé et un tuple de valeur et qui **renvoie** un dictionnaire contenant les couples clé/valeur mis en paramètre.

<u>Par exemple :</u>

```python
>>> creer_dict(("Harry Potter","Livre") , ("Nom","Format")) 
{'Nom' : 'Harry Potter', 'Format' : 'Livre'}
```