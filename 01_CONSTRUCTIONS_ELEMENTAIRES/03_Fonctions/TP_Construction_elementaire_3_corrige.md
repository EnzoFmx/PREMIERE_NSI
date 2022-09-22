# Construction élémentaire TP 3 : corrigé 

<h2><u> Exercice 1 : </h2></u>

```python
def impair(nombre):
    """
    Fonction qui détermine si un nombre est impair
    param nombre : (int) Nombre à traiter
    return (bool) True si nombre est impair, False sinon
    """
    res = False
    if nombre%2 == 1:
        res = True
    return res
```

<h2><u> Exercice 2 : </h2></u>

**Question 1 :** 
_var_ vaut 5 après l'éxécution du code. L'ambiguité porte sur la fonction incr qui pourrait changer
la valeur de var car il y a une deuxième affectation. Cependant cette fonction est juste définie mais
n'est pas appellée ici. De plus même dans le cas où elle serait appellée cela ne changerai rien, var redeviendrai 5 après l'éxécution de la fonction

**Question 2 :**
La fonction _incr(nombre)_ incrémente _nombre_ de 1 et le renvoie
_incr(nombre)_ renvoie donc _nombre+1_

**Question 3 :**
_var_ vaut toujours 5 après l'éxécution de la fonction

**Question 4 :** 
La fonction _incr(nbr)_ va renvoyer 7 peut importe le paramètre.


<h2><u> Exercice 3 : </h2></u>

**Question 1 :**
Plusieurs choses sont à noter ici :
- Il y a une erreur lorsqu'on compile le code ici. En effet la variable _test_ n'existe que dans la fonction _incr()_ et donc _test_ n'éxiste pas dans la mémoire globale du programme. 
- Lorsqu'on appelle _incr()_ :
  - _nombre+1_ nous est retourné
  - _test_ est affiché 
  - _var_ est aussi affiché, car _var_ est une **variable globale** celle-ci appartient au programme et donc existe aussi dans la mémoire lorsqu'on appel la fonction. 

**Question 2 :**
Lorsqu'on éxécute le code _test_ ne vaut rien car test n'existe pas dans le programme.
Lorsqu'on appelle _incr()_ test vaut 1. (Seulement pendant l'appel de la fonction)
Lorsqu'on a fini d'appeler la fonction _incr()_ test ne vaut à nouveau plus rien.

<h2><u> Exercice 4 : </h2></u>

**Question 1 :** 
Cette fonction permet de savoir quelle valeur entre _a_ et _b_ est la plus grande.
Mais cette fonction **ne renvoie** rien.

**Question 2 :**
```python 
def plus_grand_que(a,b) :
    if a > b : 
        return a
    elif a == b : 
        return a
    else :
        return b
```

**Question 3 :**

L'opérateur de comparaison permet de comparer entier, flottant ou chaine de caractère. Donc _a_ et _b_ doivent être de **même** type, mais soit _int_ soit _float_ soit _str_.

**Question 4 :**

```python
def plus_grand_que(a,b) :
    """
    Fonction permettant de savoir quelle valeur entre a et b est la plus grande
    param a : (int/float/str) element à comparer
    param b : (int/float/str) element à comparer
    CU : Les deux paramètres doivent être de même type
    return : (int/float/str) Element le plus grand
    """
    if a > b : 
        return a
    elif a == b : 
        return a
    else :
        return b
```





