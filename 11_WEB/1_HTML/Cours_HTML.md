# Cours : Langage HTML

## 1. 1. Historique du langage :

Le langage HTML est crée en 1991 par Tim Berners-Lee. Ce langage n’est pas un langage de programmation. Ici il n’y a pas d’algorithmes et d’exécution de programme. Le langage structure la page avec des listes à puces, des titres, des passages en gras, etc ...

## 1. 2. Fonctionnement 

Afin de créer ces différents éléments nous allons utiliser des **balises**. Celles-ci doivent entourer le passage qui doit être structuré.

Par exemple :

```html
Ceci est une phrase 

#balise pour mettre un mot en gras :
Ceci est une <b>phrase</b>

#balise pour faire des paragraphes :
<p> Ceci est une phrase</p>

# Il est possible de mettre plusieurs balises dans la même phrase :
<p> Ceci est une <b> phrase </b></p>

# Il ne faut pas dans ces cas-là, mélanger les balises comme ceci :
<p> Ceci est une <b> phrase </p></b>
```

Ici la balise qui a été appliquée est la balise <b> cette balise permet de mettre en valeur un mot ou un passage pour le mettre en **gras.** La balise <p> permet de créer des paragraphes.

**Une page html commence toujours par une balise <html> et se finit toujours par une balise </html>**

## 2. 3. Composition d’une page HTML :

Une page HTML est composée de 2 parties distinctes.

### Head :

C’est la partie qui contiendra toutes les métadonnées de la page comme le titre, l’encodage des caractères, les pages CSS/Javascript associées, etc ... 

```html
<!DOCTYPE html>
<html lang='fr'>
<head>
    <title>Titre du document (apparaît dans l'onglet du navigateur)</title>
		<meta charset="utf-8"> # Il s'agit de l'encodage des caractères toujours mettre utf-8
		<link href="/endroit/ou/se/trouve/mon/fichier/CSS">
		<script src="javascript.js"></script>
</head>
</html>
```

Pour ce cours nous n’avons pas de fichier CSS et javascript donc inutile de mettre les balises link et script. Celles-ci seront ajoutées dans un prochain cours.

### Body :

La partie body contient elle le contenu de la page HTML. Tout ce qui doit apparaître dans la page figure dans cette balise.

```html
<!DOCTYPE html>
<html lang='fr'>
<head>
    <title>Titre du document (apparait dans l'onglet du navigateur)</title>
		<meta charset="utf-8"> # Il s'agit de l'encodage des caractères toujours mettre utf-8
</head>
<body>
<h1> Introduction : </h1>
		<p> Je suis une page html et je contient des <b>informations importantes</b></p>
<h2> Partie 1 de l'intro : </h2>
	<ul>
	  <li>Je suis un élement de la liste</li>
	  <li>Je suis un autre élement de la liste</li>
	  <li>Je suis un troisième élement de la liste</li>
	</ul>
</body>
</html>
```

## 3. Bien débuter en HTML :

Afin d’écrire du code HTML il faut le bon logiciel. Il est conseillé d’utiliser Notepad++ ou VScode. Dans le cas où aucun des deux logiciels n’est disponible utilisez le logiciel “notes” propre à Windows.

Les fichiers HTML ont une extension en **.html,** ils s’exécutent dans un moteur de recherche (pour avoir la mise en page).

- Afin de savoir si la page html est bien écrite (balises fermées et non mélangées) il existe un validateur html : [https://validator.w3.org](https://validator.w3.org/)
- Afin d’avoir plus d’information sur le code html voici une ressource **essentielle** pour tout développeur web : [https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/HTML_basics](https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/HTML_basics)
    - Vous y retrouverez une section HTML sur la gauche contenant plus de détails sur la notion.