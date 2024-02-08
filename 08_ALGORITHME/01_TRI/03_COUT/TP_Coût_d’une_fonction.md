# TP : Coût d’une fonction

# 1. Introduction :

L’objectif du TP est d’appliquer les notions vues en cours. Nous avons de manière théorique introduit la notion de coût d’un algorithme.

Le but ici est de tester les algorithmes et de vérifier les coûts trouvés en cours.

# 2. Introduction à Pylab :

Pylab est un module de python permettant d’afficher des courbes. Ce module nous servira pour afficher le coût des algorithmes vus en cours en fonction du nombre d’éléments de chaque tableau (et de leur contenu). 
Le tout sera affiché par des courbes.

Tester ce code :

```python
import pylab

x = [1, 3, 4, 6]
y = [2, 3, 5, 1]
pylab.plot(x, y)

pylab.show()
```

Ce code affiche pour chaque valeur de x la valeur correspondante y dans une courbe. 

- plot() permet d’ajouter la courbe en mémoire
- show() affichera le(les) courbe(s) dans une nouvelle fenêtre. 

*Il est possible de donner un titre à ce fichier grâce à la fonction title(*)

Il est possible aussi de rajouter un nom à la courbe avec la méthode *legend( )*. 

Pour cela : (Testez le code)

```python
import pylab

x = [1, 3, 4, 6]
y = [2, 3, 5, 1]
# On rajoute un paramètre label = 'nom de la courbe'
# Ceci se fait dans la fonction plot
pylab.plot(x, y,label='courbe test')

#On décide d'afficher les legendes dans le rendu final
pylab.legend()

pylab.show()
```

# 3. Utilisation de Pylab pour le coût de fonction :

Afin de créer nos courbes nous allons devoir : 

- Créer les tableaux pour les tests
    - Il faudra des tableaux de différentes tailles
    - Des tableaux permettant de gérer les pires et meilleurs des cas (pour insertion)
- Simuler les algorithmes sur ces tableaux et relever le coût pour chaque algorithme
    - Ces coûts calculés seront stockés dans un autre tableau
- Une fois le coût calculé pour diverses tailles on crée la courbe associée

Par exemple : *(les résultats sont volontairement faux)*

- Tab_taille = [2,4,6,10,20,100,1000,10000,100000]
- Cout_selection = [0.1,0.3,0.7,1,3,10,100,5769]
- Cout_insertion_pire_cas = [0.2,0.03,0.7,1,39,20,100,5769]
- etc ....

Puis d’appliquer les méthodes de Pylab comme :

```python
Tab_taille = [2,4,6,10,20,100,1000,10000,100000]

Cout_selection = [c1,c2,c3....,cn] #C étant le cout
pylab.plot(Tab_taille, Cout_selection,label='courbe tri selection')

Cout_insertion_pire_des_cas = [c1,c2,c3....,cn] #C étant le cout
pylab.plot(Tab_taille, Cout_insertion_pire_des_cas,label='courbe tri insertion')

# etc...

pylab.legend()
pylab.show()
```

# 4. Construction des tableaux :

## 4. 1. Tableau contenant les tailles :

Le tableau de taille est à fixer nous même. En effet on choisit les tailles à tester 
(Ici nous testerons toutes les valeurs allant de 0 à 150)

Pensez donc à créer avant tout ce tableau [0,1....,149,150]

## 4. 2. Tableau contenant les valeurs en temps  :

### Calculer le coût d'un algorithme

Nous avons vu en cours que le coût d'un algorithme de tri dépend du nombre de comparaison. Afin de compter ce cout nous allons créer une variable cout dans notre code. Le fonctionnement sera le suivant :

- Avant de tester un tri => *cout*= 0
- Lorsqu'on compare avec la méthode comp( ) => *cout* +=1
- Une fois le tri fini, on ajoute *cout* dans le tableau des coûts.

Afin d'avoir une valeur globale du cout même en dehors de la fonction nous allons préciser dans le code python que la variable coût est globale au code **(Hors programme, il suffit d'appliquer ici)**

```python
def comp(elem1,elem2) :
    """Fonction qui compare deux élément, 
    renvoie -1 si elem1 < elem2
    renvoie 0 si elem1 == elem2
    renvoie 1 si elem1 > elem2
    """
    global cout
    cout+=1
    if elem1<elem2 :
        return -1
    elif elem1==elem2:
        return 0
    else:
        return 1
```

### Construire les tableaux à tester :

Pour construire les tableaux à tester il faut faire une distinction entre deux cas :

- Lorsqu’on teste le tri par sélection il n’y a pas de meilleur/pire des cas donc on crée des tableaux avec des valeurs aléatoires
- Lorsqu’on à un pire et meilleur des cas nous testons avec des tableaux prédéfinis
    - Le pire des cas aura des tableaux dans un ordre inverse : [4,3,2,1]
    - Le meilleur des cas aura des tableaux dans le bon ordre : [1,2,3,4]

Pour créer ces tableaux nous pouvons utiliser des fonctions qui génèrent les tableaux

```python
import random

def construit_tab_alea(taille) :
		"""
		Fonction qui crée un tableau avec des valeur aléatoire de taille *taille*
		param taille : (int) Taille du tableau
		return : (list) Tableau à renvoyer
		"""
		tab = []
		for i in range(taille) : 
				val = random.randint(0,taille)
				tab.append(val)
		return tab

def construit_tab_bon_ordre(taille) :
		"""
		Fonction qui crée un tableau avec des valeur rangées par ordre croissant de taille *taille*
		param taille : (int) Taille du tableau
		return : (list) Tableau à renvoyer
		"""
		tab = []
		for i in range(taille):
			tab.append(i)
		return tab

def construit_tab_ordre_inverse(taille) :
		"""
		Fonction qui crée un tableau avec des valeur rangées par ordre décroissant de taille 
		*taille*
		param taille : (int) Taille du tableau
		return : (list) Tableau à renvoyer
		"""
		return construit_tab_bon_ordre(taille).reverse()

```

****

### Création du tableau avec le coût :

Une fois que l’on sait créer les tableaux, et comment mesurer le coût de chaque algorithme il faut l’appliquer. 

Le but maintenant est de récupérer le coût de chaque algorithme pour une taille donnée et de créer les courbes.

<u>A faire :</u>

1) Ecrire les tableaux de coût d’exécution des algorithmes suivants pour des tableaux de taille 1 à 150:

- Recherche d’un élément dans un tableau (On recherche la dernière valeur tout le temps)
- Tri par insertion : pire des cas
- Tri par insertion : meilleur des cas
- Tri par sélection

2) Une fois les tableaux obtenus, écrire grâce au module Pylab, le code pour créer les courbes de chaque algorithme.

## Bonus 1 : Et si on calculait le temps ?

Une autre mesure moins théorique peut être le calcul en temps

### Mesurer le temps d’exécution d’un algorithme

Afin de mesurer les temps il faut utiliser le module time

```python
import time 

#Comment mesurer le temps d'exécution d'une fonction :
t0 = time.process_time()
fonction(test)
t1 = time.process_time()
duree = (t1-t0)
```

La méthode process_time() permet de relever une heure à l'instant donné. (pour plus de précisions voir (https://docs.python.org/fr/3/library/time.html#time.process)). 
Naturellement à la fin d'une exécution on relève l'heure à nouveau afin d'avoir l'heure de fin. On soustrait la deuxième à la première afin d'avoir le temps d'exécution.

**Il faut donc mesurer le temps d’exécution de chaque fonction pour un tableau de taille donnée.**

1. Appliquer cette méthode afin de calculer le temps de chaque tri.

## Bonus 2 : Un peu plus de précision

Afin d’être plus précis sur le temps d’exécution des algorithmes il est idéal de tester pour une longueur donnée sur différents tableaux.

Pour cela il faudra récupérer la moyenne des temps d’exécution pour un tableau de taille n, puis un tableau de taille n+1, etc ... 

1) Faire en sorte que les test s’appliquent à des résultats de moyenne de temps au lieu d’un résultat d’un seul temps sur un seul tableau.
