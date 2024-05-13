# Cours : Formulaire et transmission de paramètres d’une page WEB

------

## 1. Rappel URL et requête HTTP(S) :

### Définition :

**URL :** chemin vers un fichier sur un réseau

Lorsque l’on tape un URL dans notre navigateur WEB nous écrivons en réalité le chemin que l’on doit prendre dans un serveur pour accéder au fichier.

Par exemple :

Lorsque le client écrit l’URL *http://mon-super-site/menu/principal/index.html*

- Le nom de domaine du serveur ‘*mon-super-site*’ est isolé
    - Une requête DNS est effectué pour retrouver l’adresse IP du serveur.
- Une fois l’adresse IP et le chemin établi vers le serveur, alors via la requête http le navigateur demande la ressource *index.html* se trouvant dans le dossier *menu* puis *principal ...*
- Le serveur WEB renvoie la page *index.html* au client

**HTTP(S) :** Protocole utilisé pour une communication client-serveur sur le WEB. Le client envoie donc une **requête** et le serveur renvoie une **réponse.** 

La requête comporte plusieurs éléments 

Par exemple voici une requête http :

```markdown
GET /menu/principal/index.html HTTP/1.1
Host : www.mon-super-site
```

Plusieurs choses sont à noter, premièrement nous utilisons la méthode GET (nous verrons plus tard dans le cours le détail de cette méthode). Il y a aussi la version du protocole ici c’est la version 1.1
L’hôte est bien www.mon-super-site qui correspond via le protocole DNS à une certaine adresse IP

Voici un exemple de réponse http :

```markdown
HTTP/1.1 200 OK
Date: Thu, 06 May 2022 15:03:32 GMT
Server: Apache/2.0.54 (Debian GNU/Linux) DAV/2 SVN/1.1.4
Content-Type: text/html; charset=ISO-8859-1

<!DOCTYPE html... (suivi du reste de la page html)
```

Plusieurs choses sont à noter ici aussi. 

- Le numéro 200 indique qu’il n’y a pas eu d’erreur dans le requête du client (a la différence du code 404 par exemple).
- Le serveur est basé sous Linux (OS libre), il s’agit d’un serveur Apache tournant sur l’OS Debian. Apache est le logiciel permettant de recevoir et traiter les requêtes http. C’est le type de serveur majoritairement utilisé dans le monde.
- Le contenu renvoyé par le serveur est de l’html, encodé en ISO-8859 ici.
- La page HTML est envoyé directement dans la réponse

Remarque : Https est une version sécurisée du protocole http, en effet avant toute communication il y a une demande de connexion sécurisée. Une fois acceptée les données envoyées et reçues sont chiffrées. 

Lorsqu’on envoie des données importantes (mots de passe/ données personnelles) il faut toujours vérifier que le protocole utilisé est en https. Sinon quelqu’un peut intercepter vos données et les lire sans qu’elles soient chiffrées. 

## 2. Formulaire et méthode d’envoi (GET/POST) :

### Formulaire en HTML :

Un formulaire permet d'interagir entre le client et le serveur. En effet lors de la saisie du formulaire le client va envoyer des données qui seront traitées par le serveur.

La création du formulaire se fait dans la page HTML en voici un exemple :

```html
<form action="page_a_ouvrir_avec_les_resultats.html" method="post">
					<label>Nom</label> : <input type="text" name="nom" />
					<label>Prénom</label> : <input type="text" name="prenom" />
					<input type="submit" value="Envoyer" />
</form>
```

Une fois le formulaire écrit, complété par l’utilisateur alors il sera possible de l’envoyer grâce au bouton *(input)* envoyer.
Lorsqu’on **envoie** les donnée alors *page_a_ouvrir_avec_les_resultats* s’ouvre et traite les résultats envoyés.

### Méthodes d’envoi :

En première nous voyons deux méthodes liées aux requêtes html. La méthode choisie s’écrit dans la le paramètre *method* de la balise **<from>.**

**Méthode GET :**

Cette méthode va stocker les paramètres du formulaire dans l’URL. Il est donc possible de retrouver une page WEB avec les bons paramètres simplement avec une URL grâce à la méthode GET.

Exemple :

Un exemple d’URL résultant du formulaire ci-dessus peut être : 

- *http://mon-super-site/menu/principal/*page_a_ouvrir_avec_les_resultats.html?nom=Dupond&prenom=Bob

Cependant stocker les paramètres dans l’URL n’est pas une bonne idée lorsque l’on envoie des données sensibles (mots de passes, numéro carte bancaire, etc ...)

**Méthode POST :**

La méthode POST permet elle de stocker les paramètres du formulaire dans la requête HTML et donc n’apparaissent pas dans l’URL. Cependant pour accéder à une page contenant les paramètres d’une requête POST il faut ressaisir le formulaire.

### Traitement des données :

Le traitement des données s’effectue par le serveur. Pour avoir un serveur local (dans un premier temps) il y a plusieurs solutions, voici les deux solutions les plus courantes : 

- Avoir une machine sous Linux et faire tourner un serveur (Apache) et traiter les données en PHP
- Utiliser le module Flask de python (Peut importe l’OS)