# Exercice : Représentation des caractères

## Exercice 1 : Application de cours

A l'aide de la table ASCII : 

1. Encoder votre prénom en hexadécimal.
2. Encoder la phrase : “Je suis heureux.se en NSI” hexadécimal
3. Encoder la phrase : “élève de NSI” hexadécimal
4. Quelle sera la taille de la représentation de la phrase ‘Je suis un élève de NSI’ en codage ASCII et avec la norme ISO8859 ?  Et pour une chaîne de longueur n ?

## Exercice 2 :

La méthode *upper( )* en python permet de mettre en majuscule une chaîne de caractère. 

```python
s = 'YooOOoUUuuHHhHHoUUU'
>>> print(s.upper())
'YOOOOOUUUUHHHHHOUUU'
```

Sauf que Bob est très têtu et ne veut pas s'aider de code déjà tout fait, il veut faire de lui même la fonction pour mettre une chaîne de caractère en majuscule.

1. Ecrire le code de la fonction *Up_Pour_Bob( )* permettant de mettre en majuscule les caractère d'un texte. (En vous aidant des fonction chr et ord )

```python
# Exemple :

>>> Up_Pour_Bob('YooOOoUUuuHHhHHoUUU')
'YOOOOOUUUUHHHHHOUUU'

>>> Up_Pour_Bob('YooOOoUUuuHHhHHoUUU   && & &  &')
'YOOOOOUUUUHHHHHOUUU   && & &  &'

>>> Up_Pour_Bob("J'ai 10 de moyenne en NSI")
"J'AI 10 DE MOYENNE EN NSI"
```

## Exercice 3 : Chiffrement de César

Le chiffrement de César permet de rendre un message chiffré, c'est à dire qu'il ne sera à première vue pas compréhensible.

Par exemple le texte 'OTJ' est le message codé de 'NSI', une manipulation à été faite pour passer d'une chaîne à l'autre.

1. Comment est on passé  du message 'NSI' vers 'OTJ' ?

Une fois le mécanisme compris il faut l'écrire en python. Pour simplifier le programme nous allons ici prendre en compte seulement les caractères en majuscule (ABCDEFGHIJKLMNOPQRSTUVWXYZ).

1. Une fois la méthode comprise écrire un algorithme *Chiffrement_cesar( t,v )* prenant en paramètre un texte **t** et une valeur **v** permettant d'encoder.
   - Aide : Il est possible de faire cette fonction sans utiliser les méthodes `chr`et `ord` 
2. Bonus : Prendre en compte les lettre en minuscule dans le code.
