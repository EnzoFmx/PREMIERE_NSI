# Chiffrement de Vigenère :

Le chiffrement de Vigenère est un chiffrement fonctionnant sur le même principe qu'un chiffrement de césar, sauf qu'ici la clé est un texte et non plus 1 seul caractère.

Par exemple :

'JE SUIS UN ELEVE DE NSI' codé par la clé 'ABD' donnera => 'JF VUJV UO HLFYE EH NTL'

Comment cela fonctionne :

- La première lettre est avancée de 0 cases (Clé A)
- La deuxième lettre est avancée de 1 case (Clé B)
- La troisième lettre est avancée de 3 case (Clé D)
- La quatrième lettre est avancée de 0 case (Clé A)
- ... 
- ...
- Etc.

1. Ecrire la fonction *vigenere( )* qui prend en paramètre un texte et une clé et renvoie le message codé grâce au chiffrement de Vigenère :

```python
# Divers exemples d'application :

>>> vigenere('JE SUIS UN ELEVE DE NSI','ABD')
"JF VUJV UO HLFYE EH NTL"
>>> vigenere('JE SUIS UN ELEVE DE NSI','AZ')
"JD STIR UM EKEUE CE MSH"
>>> vigenere('JE SUIS UN ELEVE DE NSI','JESUISCONTENT')
"SI KOQK WB REIIX MI FMQ"
>>> vigenere('JE SUIS UN ELEVE DE NSI & JE suis content','JESUISCONTENT')
"SI KOQK WB REIIX MI FMQ & BG suis content"
```