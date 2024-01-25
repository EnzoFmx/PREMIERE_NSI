# Le tri par insertion :

Le tri par insertion est l’un des deux tris vus en première. Et celui-ci se défini comme suit :

```python
t => tableau à trier
taille => longueur(t)
pour ind allant de 1 à taille-1 (inclus) : 
#4		val_a_placer = t[ind]
#5		ind2 = ind
#6		tant que t[ind2-1] > val_a_placer et que ind2 > 0 :
#7			t[ind2] = t[ind2 - 1]
#8			ind2 = ind2 - 1
#9		t[ind2] = val_a_placer
renvoyer t
```

### I) Tableau de variable :

Compléter les tableau suivant en appliquant l’algorithme ci-dessus pour :

- [4,2,5,3,1,6]
- [4,3,2,1]
- [1,2,3,4,5,6]

Remplir le tableau ci-dessous, chaque ligne correspond à un tour de boucle **pour** (ligne 3)

| ind | #4 val_a_placer | Nombre de tour de boucle 'tant que' | Valeur de t après la boucle 'tant que' |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### II) Code en python :

1) Réécrire ce code en python :

   Bonus. Réécrire ce code en utilisant une fonction intermédiaire

2. En déduire une explication du code

### III) Exercice complémentaire :

1. Compter le nombre d’étape pour trier ce tableau par insertion, puis pour chaque étape compter le nombre d’étape de décalage.
    - Pour [1,3,2,5,4]
    - Pour [5,4,3,2,1]
    - Pour  [1,2,3,4,5]