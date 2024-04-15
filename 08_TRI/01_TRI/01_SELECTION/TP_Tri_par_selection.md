# Découverte tri par sélection :

## 1. Démonstration :

Le tri par sélection peut être illustré comme ceci : 

![Selection-Sort-Animation](./tri.gif)

1. Déduire les grandes étapes du tri.

## 2. Application du tri (par ordre croissant) :

1) Décrire les états des tableaux suivant à chaque étape du tri par sélection :

ex : [1,3,2] => [1,3,2],[1,2,3],[1,2,3]

- t1 = [2,4,5,1]
- t2 = [1,2,3,4]
- t3 = [4,3,2,1]
- t4 = [8,7,54,3,2,5,5]

## 3. Création de l’algorithme :

1. Ecrire un algorithme en **pseudo code** avec les étapes de la première partie.

   - Voici quelques exemple d'étape du tri (dans le désordre) :
     - échange de valeur
     - recherche du minimum
     - renvoie du tableau trié
     - Boucle

2. Pour finir, l’écrire en **python** sous 3 fonctions :

   - Une fonction comp(elem1,elem2)
   - Une fonction position_minimum(tab,ind)
   - Une fonction tri_selection(tab) qui utilise **comp et position_minimum**

   ```python
   def comp(elem1,elem2) :
   	"""
   	Fonction qui compare deux élément, 
       renvoie -1 si elem1 < elem2
       renvoie 0 si elem1 == elem2
       renvoie 1 si elem1 > elem2
       """
      
   
       
       
   def tri_selection(tab):
   	"""
       Fonction qui trie un tableau tab grâce au tri par sélection
   	param tab: (list) tableau à trier
   	return :  (list) tableau trié
   	"""
   ```
   

## 4. Nombre de comparaisons :

1. Reprendre les tableaux t1, t2, t3, t4 et compter le nombre de fois où la fonction `comp(elem1,elem2)`est appelée pour chaque tableau.

2. Généraliser pour un tableau contenant n éléments. Quel sera le nombre de comparaisons faites.