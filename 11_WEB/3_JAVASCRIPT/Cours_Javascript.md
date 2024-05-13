# Cours : Le langage Javascript

------

## 1. Introduction 

Javascript est un langage très important pour le WEB, il permet de créer de l’interactivité dans une page WEB (Côté client). Ce qu'on appelle côté client est  la machine de l'utilisateur, c'est à dire que les interactions seront calculées/exécutées sur sa machine. C'est en opposition avec le **côté serveur**, qui lui nécessite un envoi de données au serveur afin de créer de interaction via les requêtes HTTP(S).(Voir le cours sur les formulaires et requêtes HTTPS). 

Le langage Javascript a été crée en 1995 par Brendan Eich 

Afin de créer du code en Javascript il faut une page HTML/CSS 

Le code Javascript peut être écrit directement dans la page HTML (très déconseillé) ou rattacher à la page grâce à la balise :

```html
<script src="chemin/vers/le/script.js"></script>
```

*Il est possible de soi placer cette balise dans le HEAD du fichier html OU juste avant </body>*

On le voit ici, le fichier possède une extension en .js
Afin d'écrire ce coder ce type de fichier, il faut utiliser une app dédiée tel que Notepad++ ou VS code.

## 2. Premiers pas en Javascript :

Le langage Javascript communique avec la page HTML et permet donc de créer des interactions. Pour cela, le code Javascript doit savoir quand s’exécuter.

### 2. 1. Appel de fonction

<u>Exemple :</u> 

```jsx
Alert("Voici une alerte javascript")
```

*La fonction Alert est une fonction qui affichera une petite fenêtre lors de son exécution, elle est native a Javascript*

Le code Javascript est exécuté dès que la page HTML s’ouvre (il s'agit d'un appel de fonction simple, la fonction est donc exécutée dès que le code Javascript est exécuté).

### 2. 1. Création d'une fonction

La construction de fonction peut être semblable à Python, cependant certains éléments de syntaxes diffèrent. 

<u>Voici un exemple de fonction :</u>

```jsx
function change_couleur(){
	document.getElementById('test').style.color='green';
}
```

Plusieurs choses sont à noter ici : 

- Une fonction est définie par ***function*** (***def*** en python)
- Une fonction est délimitée par **{ }**
- Les instructions se terminent par ***;***

<u>Ici la fonction va :</u>

- Sélectionner le document html
    - Dans ce document on sélectionne (grâce à getElementById*)* la balise d’ID ***test***
    - On va modifier le style de cette balise (css)
    - La couleur devient verte

Comme en Python, ici nous avons juste défini la fonction, si j’ouvre ma page HTML rien ne se passera. Maintenant il faut l’utiliser. Pour cela :

```jsx
change_couleur() //Comme en python, il suffit de l'appeler
```

## 3. Création d’événement

Alors faire des fonctions c’est bien, pouvoir les utiliser aussi. Mais ici nous sommes confrontés à un problème.

**Toutes les fonctions s’exécutent à l’ouverture de la page**

Pour régler ce problème, nous allons créer des événements pour cela il y a deux manières.

### 3. 1. Appeler les fonctions dans le fichier HTML 

Cette méthode moins recommandée que la seconde permet d’appeler directement dans le code HTML la fonction javascript.

<u>Par exemple :</u>

```html
<button id='but' onclick="change_couleur()"> Appuyer ici pour changer la couleur de #test </button>
```

Si l’on clique sur ce bouton dans le fichier HTML, alors la fonction ***change_couleur()*** se lancera, et donc changera la couleur de la balise ayant l’ID *test*

### 3. 2. Créer des évènements en Javascript 

Il est possible de rajouter directement dans le Javascript ceci : 

```javascript
document.getElementById('but').addEventListener('click',change_couleur);
```

Ce qu’il se passe ici : 

- Dans le document HTML
    - On sélectionne l’élément d’id *but*
    - On lui ajoute un événement
        - Lorsqu’on ***click*** dessus on exécute la fonction **change_couleur** (attention sans parenthèses)

Cas d’une fonction avec des paramètres :

```javascript
document.getElementById('but').addEventListener('click',function(){
    /* Ici il faut écrire le code à exécuter, s'il n'y a qu'une fonction alors appeler cette fonction */
    fonction_avec_param(p1,p2);
}                                
```

## 4. Condition

Les conditions en Javascript sont presque semblables à du python sauf que :

- La condition est mise entre ( )
- Après avoir écrit la condition le bloc d’instruction **dans** la condition est mis entre { }

Ce qui peut donner :

```jsx
function testNum(a) {
  let result;
  if (a > 0) {
    result = 'positive';
  } else {
    result = 'NOT positive';
  }
  return result;
}
```

## 5. Variable

Le langage Javascript est un langage nécessitant de préciser un mot clé avant l'affectation d'une variable.
Il existe deux manières d'initialiser une variable, soit avec le mot clé **let**, soit avec le mot clé **var**.

La différence entre les deux proviens de la portée de la définition de variable.

```javascript
/* La fonction console.log() permet d'afficher un message dans la console */
function varScoping() {
  var x = 1;
  if (true) {
    var x = 2;
    console.log(x); // will print 2
  }
  console.log(x); // will print 2
}

function letScoping() {
  let x = 1;
  if (true) {
    let x = 2;
    console.log(x); // will print 2
  }
  console.log(x); // will print 1
}
```

## 6. Sélection d'éléments 

Pour sélectionner des éléments en JS il y a énormément de possibilités :

- Utiliser *getElementById* permet de sélectionner un élément par son ID
- Utiliser *getElementsByClassName* permet de sélectionner tous les éléments ayant le même nom de classe :
    - getElementsByClassName(’test’) ira chercher toutes les balises ayant comme paramètre class=’test’
- Utiliser *querySelector* permet d’aller chercher dans la page HTML le premier élément correspondant au paramètre
    - Utiliser querySelector(’h3’) ira chercher la première balise h3 du fichier HTML

## Remarque :

**Il n’est pas demandé pour un élève de NSI de savoir coder en Javascript. Il faut comprendre la notion d’événement, savoir reconnaitre du code JS (par rapport à du Python par exemple).** 

*Un bon développeur ne sait pas coder dans tous les langages mais il sait s’adapter et sait où chercher les bonnes informations*