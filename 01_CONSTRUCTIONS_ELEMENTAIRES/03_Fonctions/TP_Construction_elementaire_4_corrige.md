# TP construction élémentaire 4 : Corrigé

<h2><u> Exercice 1 : </h2></u>

```python
def reste(entier_1,diviseur) :
    """
    Fonction qui calcule le reste d'une division euclidienne sans utiliser l'opérateur %
    param entier_1 : (int) entier à diviser
    param diviseur : (int) diviseur
    return : (int) reste de la division euclidienne
    """
    quotient = entier_1//diviseur
    reste = entier_1 - (diviseur*quotient)
    return reste
```

<h2><u> Exercice 2 : </h2></u>

```python
def pythagore(cote1,cote2,hypothenuse) :
    """
    Fonction qui determine sur un triangle de coté : cote1,cote2,hypothenuse est rectangle
    param cote1 : (int) cote 1 du triangle
    param cote2 : (int) cote 2 du triangle
    param hypothenuse : (int) cote le plus grand des 3
    return : (bool) renvoie True si le triangle est rectangle, False sinon
    """
    res = False
    if cote1**2 + cote2**2 == hypothenuse**2 :
        res = True
    return res
```

<h2><u> Exercice 3 : </h2></u>

```python
def absolue(a):
    """
    Fonction qui renvoie la valeur absolue de a
    param a : (int) nombre à mettre à la valeur absolue
    return : (int) nombre a la valeur absolue
    """
    if a < 0 :
        a = -a
    return a
```

<h2><u> Exercice 4 : </h2></u>

```python
def max(a,b):
    """
    Fonction permettant de savoir quel est le plus grand entier entre a et b
    param a : (int) nombre à comparer
    param b : (int) nombre à comparer
    return : (int) a si a>b, b sinon
    """
    if a > b :
        return a 
    elif a == b : 
        return b 
    else :
        return b 

    """
    Le code de la fonction pourrait ressembler à cela
    res = b 
    if a > b :
        res = a 
    return b
    """

def max2(a,b,c) :
    """
    Permet de savoir quel est l'entier le plus grand entre a,b et c 
    param a : (int) nombre à comparer
    param b : (int) nombre à comparer
    param c : (int) nombre à comparer
    return : (int) a si a>b et a>c, b si b>a et b>c, c sinon
    """
    if c > max(a,b) :
        return c
    else :
        return max(a,b)    
```

<h2><u> Exercice 5 : </h2></u>

```python

def bissextile(annee) :
    """
    Permet de savoir si une année est bissextile ou non
    param annee : (int) Annee à traiter
    return : (bool) True si elle est bissextile, False sinon
    """
    if annne%4 == 0 :
        if annee%100 != 0:
            res = True 
        else :
            res = False
    elif annee%400 == 0:
        res = True
    else :
        res = False
    return res

def nombre_jour_annee(annee):
    """
    Renvoie le nombre de jour d'une année
    param annee : (int) Annee a traiter
    return : (int) 365 si annee n'est pas bissextile, 366 sinon
    """
    if bissextile(annee) == True :
        return 366
    else : 
        return 365
    
    """
    Version plus "propre" :
    res = 365 
    if bissextile(annee) :
        res = 366
    return res
    """

def nombre_jour_mois(annee,mois):
    """
    Permet de savoir combien de jour dans le mois d'une année
    param annee : (int) Annee en question
    param mois : (int) mois en question
    return : Le nombre de jour du mois 'mois' de l'annee 'annee'
    """
    if mois == 2 :
        if bissextile(annee) == True : 
            jour = 29
        else :
            jpur = 28
    elif mois <= 7 :
        jour = 30 + mois%2
    else :
        jour = 31- mois%2
    return jour
```





