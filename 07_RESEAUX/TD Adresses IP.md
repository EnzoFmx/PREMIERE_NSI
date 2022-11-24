# TD : Adresses IP

## 1. Adresse IP :

Chaque adresse IP possède une partie consacrée au réseau et une autre consacrée à la partie machine. Pour différencier ces deux parties, il faut regarder la fin de l'adresse IP, celle après le '/'.

<u>Par exemple :</u>

165.73.2.8/24 est une adresse IP ayant ses 24 bits de gauche consacré à la partie réseaux

- Le masque réseau est donc 255.255.255.0

- 165.73.2.0 sera l'adresse réseau
- Adresse de diffusion sera 165.73.2.255

### Exercice 1 :

Voici des adresses IP :

- 145.245.45.225/16
- 202.2.48.149/24
- 97.124.36.142/8
- 192.45.76.8/24
- 89.78.78.78/8

<u>1. Pour chaque adresse :</u>

- Déterminez le masque réseau
- Déterminez l'adresse réseau
- Déterminez l'adresse de broadcast

<u>2. Prenons l'adresse IP : 145.205.35.125/16</u>

- l'adresse 145.205.2.0/16 appartient au même réseau? (Justifiez)
- l'adresse 144.205.0.0/8 appartient au même réseau? (Justifiez)
- l'adresse 147.245.1.1/16 appartient au même réseau? (Justifiez)

## 2. Création de sous réseaux

Les sous réseaux sont utilisés pour structurer notre réseau, mais avant de les introduire parlons des classes d'adresse IP.

<u>Classes d'adresse IP :</u>
Il existe plusieurs types d'adresses IP :

- De type A allant de 0.0.0.0 à 127.255.255.255
- De type B allant de 128.0.0.0 à 191.255.255.255
- De type C allant de 192.0.0.0 à 223.255.255.255

Chaque classes d'adresses possède son masque réseau :

- Type A : Le masque réseau est 255.0.0.0
- Type B : Le masque réseau est 255.255.0.0
- Type C : Le masque réseau est 255.255.255.0

<u>Par exemple :</u>

Prenons l'adresse réseaux : 192.155.255.0
Son masque réseau est 255.255.255.0 (/24) (Classe C)

Le masque de sous réseau lui commencera forcément par **255.255.255.xx** et sera compris entre /25 et /32

#### 2. 1. Comment savoir à quel sous réseaux l'adresse IP appartient elle :

- Il suffit de faire une opération bit à bit entre le masque de sous réseaux et l'adresse IP

<u>Exemple :</u> Supposons un masque de sous-réseau 255.255.255.224 (soit /27) et une adresse **192.155.255.33**/27

      192.155.255.33 
    & 255.255.255.224
    = 192.155.255.32


 L'adresse IP 192.155.255.33 appartient au sous réseau 192.155.255.32

#### 2. 2. Comment créer des sous réseaux à partir d'une adresse réseaux :

Prenons l'adresse IP : 

- Il faut attribuer un nombre de bit sois même pour le sous réseau.

Dans notre exemple j'ai 24 bits attribués à mon masque de réseaux (Car l'adresse est de classe C), il m'en reste donc 8 pour créer un masque sous réseaux.

Sur mes 8 bits je décide d'attribuer 3 bits pour l'adressage de sous réseaux, il m'en reste donc 5. (pour les hôtes)

Mon masque de sous réseaux devient 11111111.11111111.11111111.11100000 soit 255.255.255.224 ou encore /27

En ayant attribué 3 bits pour les sous réseaux j'ai donc en théorie 8 sous réseaux (2 ** 3 = 8)

Soit :
- 255.255.255. **000** 00000 => 255.255.255.0
- 255.255.255. **001** 00000 => 255.255.255.32
- 255.255.255. **010** 00000 => 255.255.255.64
- 255.255.255. **011** 00000 => 255.255.255.96
- 255.255.255. **100** 00000 => 255.255.255.128
- 255.255.255. **101** 00000 => 255.255.255.160
- 255.255.255. **110** 00000 => 255.255.255.192
- 255.255.255. **111** 00000 => 255.255.255.224

Il reste maintenant 5 bits pour les hôtes de ces sous-réseaux. Ce qui fait en théorie 2 ** 5 = 32 hôtes.

Sauf qu'il existe une adresse de broadcast (diffusion) et une adresse réseau pour chaque sous réseau

Soit ici 32 - 2 = 30 hôtes.

Prenons l'adresse de sous réseau 192.155.255.224/27

Cette adresse peut avoir donc comme hôte :

```python
- 192.155.255.224 /27 = > add sous réseau
- 192.155.255.225 /27 => Hôte 
- 192.155.255.226 /27 => Hôte
- …
- 192.155.255.253 /27 => Hôte
- 192.155.255.254 /27 => Hôte
- 192.155.255.255 /27 => Broadcast
```

### Exercice 2 :

Vous travaillez dans une boite informatique, une adresse réseau de type B vous à été donnée 191.254.0.0.

1. Quel est le masque réseau de cette adresse ? De combien de bit à 1 est il composé?

Nous attribuons 6 bits sur notre adresse pour créer des sous réseaux.

1. Donnez le nouveau masque de sous réseaux que l'on utilisera. Combien de sous réseaux avons nous crée ?
2. Combien de bit cela nous laisse ?
3. Combien d'hôtes pourrons nous avoir sur chaque sous réseaux?

#### Bonus :

Une adresse IP de type A vous est attribué.

1. Combien d'hôtes et de sous réseaux aurons nous avec un masque de sous réseaux en /15 ?