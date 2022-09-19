# Construction élémentaire : Fonction 2

------

## Exercice 1 :

1. Ecrire la fonction reste(entier_1,diviseur) qui calcule le reste de la division euclidienne de entier_1 par diviseur **sans utiliser l'opérateur "%"** :

## Exercice 2 : 

1. Ecrire une fonction Pythagore(cote1,cote2,hypotenuse) qui renvoie un booléen si les trois côtés forment un triangle rectangle

## Exercice 3 : 

1. Ecrire une fonction absolue(a) qui renvoie la valeur absolue de a

## Exercice 4 : 

1) Ecrire une fonction max(a,b) qui renvoie le plus grand des deux entiers a et b
2) Ecrire une fonction max2(a,b,c) qui renvoie le plus grand entiers entre a,b et c (aidez vous de la fonction max())

## Exercice 5 : 

1) Ecrire une fonction bissextile(annee) qui renvoie un booléen si année est bissextile
    Rappel : Une année est bissextile si 
    
    - Elle est divisible par 4 mais **non** divisible par 100
    - Elle est Divisible par 400 
2) Ecrire une fonction nombre_jour_annee(annee) qui renvoie le nombre de jour dans l'année (utilisez bissextile)
    - Rappel : 366 pour une année bissextile, 365 sinon
3) Ecrire une fonction nombre_jour_mois(annee, mois) qui renvoie le nombre de jour dans un mois (utilisez bissextile)
    - Utilisez cette formule :
      - Pour le mois de février :
        - 29 jours si bissextile
        - 28 sinon
      - Pour les mois avant juillet (juillet compris)
        - 30 + mois%2
      - Sinon
        - 31 - mois%2
