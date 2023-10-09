# TP 2 Corrigé :

<h2><u> Exercice 1 :</h2></u>

**Question 1 :**
Il ne se passe rien, les variables sont juste créées on ne les manipule pas ici.

**Question 2 :**
Lorsqu'on appelle la variable chaine, "NSI" est renvoyé. Car chaine vaut "NSI"

**Question 3 :**
Lorsqu'on re-exécute le programme chaine vaut toujours "NSI" car ce qui est écrit dans la console est effacé une fois le code recompilé.

<h2><u> Exercice 2 :</h2></u>

**Question 1 :**
chaine2 < chaine3 == True car la comparaison se fait par ordre léxicographique (comme dans un dictionnaire) et dans cet ordre la chaine de caractère '2' est inférieur à '3'. (le premier caractère étant le même on passe au deuxième)

**Question 2 :**
chaine4 < chaine5 car 'z' est après 'b' (même explication que pour la question 1)

**Question 3 :**
La fonction len() calcule la longueur d'une chaine. 
Ici chaine4 a une longueur inférieure à chaine5.


<h2><u> Exercice 3 :</h2></u>

**Question 1 :**
Print permet juste d'afficher. Lorsqu'on essaie d'affecter à une variable un affichage cela ne fait rien. Un affichage ne peut être affecté et donc la variable ne vaut rien.

**Question 2 :**
Le type de var est de type "NoneType" cela signifie que var ne vaut rien (type(var))

<h2><u> Exercice 4 :</h2></u>

**Question 1 :**

Il y a plusieurs remarque à faire ici :
- print peut afficher :
  - le contenu d'une variable
  - une chaine de caractère
  - le resultat d'un calcul
- val = 6 est une affectation et donc n'affiche rien

<h2><u> Exercice 5 :</h2></u>

**Question 1 :**
Input renvoie un resultat de type "str" et permet a l'utilisateur d'écrire une chaine. 

<h2><u> Exercice 6 :</h2></u>

```python
res = input("ecrire une phrase")
res = res + " (Cette phrase à été écrite par l'utilisateur)"
print(res)
```

<h2><u> Exercice 7 :</h2></u>

```python
res = input("ecrire un nombre")
res = int(res)
res = res**2
if res%2 == 0 :
    print("Le nombre écrit au carré est divisible par 2")
else : 
    print("Le nombre écrit élevé au carré n'est pas divisble par 2")
```

<h2><u> Exercice 8 :</h2></u>

```python

res = input("ecrire une phrase")
if len(res) < 30 :
    res = res + input("ecrire une autre phrase")
    if len(res) < 30 :
        print("Malgré deux tentatives la phrase est toujours trop courte")
    else :
        print("Après deux tentatives l'utilisateur a écrit une phrase d'au moins 30 caractères")
else :
    print("En une seule tentative l'utilisateur à écrit une phrase d'au moins 30 caractères")
```



