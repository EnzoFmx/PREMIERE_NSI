# 1 Application de cours :

"""
1. Voir cours
2. Voir cours
3. Voir cours

4.

>>> tab = [0,1,2,3,4,5,6,7,8,9,10]
>>> s = 'abcdefghijklmno'
>>> t = ("Prof",'NSI',15,False,True,'N','S','I')
>>> tab[2]
>>> s[2]
>>> t[2]

>>> tab[6] = 718
# Impossible pour tuple et chaine de caractère
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'str' object does not support item assignment

Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


# Longueur
>>>len(tab)
>>>len(t)
>>>len(s)
"""
## 2.1 Append
def tableau_premier_nombre(nb : int) -> list:
    """
    Fonction construisant un tableau de nombre
    allant de 0 à nb (inclus)
    param nb : (int) valeur maximal du tableau
    return : (list) tableau contenant les valeurs 0 jusqu'à nb
    """
    depart = 0
    tab = []
    while depart <= nb :
        tab.append(depart)
        depart += 1
        # depart = depart + 1
    return tab

#2. >>> tableau_premier_nombre(5)

## 3. Connaitre la présence d'un élement dans une structure :

'''In permet de connaitre la présence d'un element dans une structure :

Par exemple :
>>> 5 in [1,2,5]
True
>>> s = 'oui'
>>> 'a' in s
False
'''
def element_in_structure(struct,element) -> bool :
    """
    Fonction renvoyant True ou False si element est dans la structure struct
    param struct : (list/str/tupl) Structure
    param element : () Element à trouver dans struct
    return : (bool) True si dans la structure, False sinon
    Attention d'autres versions du code sont possible
    """
    trouver = False
    for i in struct :
        if i == element :
            trouver = True
    return trouver
        
    

## 4. Count

def compte_element(tab : list, element : str) -> int :
    """
    Fonction qui compte le nombre d'élément element dans un tableau tab
    param tab : (list) tableau d'element
    param element : (str) valeur a chercher
    return : (ind) nombre de fois ou element apparait dans tab
    """
    compte = 0
    for caractere in tab :
        if caractere == element :
            compte += 1
    return compte

# >>> compte_element(['a','e','i','o','u','y'],'p')
# 0

## 5. Tableau par compréhension 

'''
le tableau tab contient toutes les valeur de l qui sont supérieure à 10
'''
l = [1, 7, 9, 15, 5, 20, 10, 8]
tab = []
for i in l :
    if p >10 :
        tab.append(p)
        
## 5. Matrice :

'''
1.
    1. m[1][1]
    2. 1
    3. m[2][0]
'''

def affiche_matrice(mat: list) -> None :
    """
    fonction affichant les éléments de mat
    """
    for i in mat :
        for j in mat :
            # ,end = '' permet juste d'afficher les element à la ligne
            print(j, end='')
