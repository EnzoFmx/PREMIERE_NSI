# Explication détaillée du phénomène d'encapsulation des données :

1. **Couche Application :**
   - Lorsqu'une application (par exemple, un navigateur Web) souhaite envoyer des données, elle les transmet à la couche Application.
   - À cette couche, les données sont encapsulées dans un format spécifique au protocole de la couche Application, comme **HTTP** pour le web, **SMTP** pour le courrier électronique, etc.
   - Les données encapsulées, maintenant appelées **message** ou **segment de couche Application**, sont passées à la couche Transport.

2. **Couche Transport :**
   - À la couche Transport, les données de la couche Application sont encapsulées dans des **segments**.
   - Le protocole de la couche Transport (**TCP** ou **UDP**) ajoute des informations de contrôle, telles que **les numéros de port source et de destination**, **ainsi que des informations de vérification d'erreur pour garantir la fiabilité des données**.
   - Les segments sont ensuite transmis à la couche Internet.

3. **Couche Internet :**
   - La couche Internet encapsule les segments de la couche Transport dans des **paquets**.
   - Elle ajoute des informations cruciales telles que les **adresses IP source et destination**.
   - Les paquets sont ensuite transférés à la couche Accès réseau.

4. **Couche Accès réseau :**
   - À la couche Accès réseau, les paquets de la couche Internet sont encapsulés dans des **trames**.
   - Cette couche ajoute des informations spécifiques au réseau physique, comme **les adresses MAC source et destination**.
   - Les trames sont ensuite transmises à travers le réseau physique, que ce soit via **des câbles, des fibres optiques ou des ondes**.

Lorsque les données atteignent la destination, le processus de **désencapsulation se produit dans l'ordre inverse**. Chaque couche retire les informations qu'elle a ajoutées, et les données finales sont remises à l'application destinataire.

Ce processus d'encapsulation et de désencapsulation permet aux données de traverser le réseau de manière **ordonnée**, chaque couche jouant un rôle spécifique dans le transfert efficace et fiable des informations.