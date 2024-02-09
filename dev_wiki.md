Wiki Développeur Pulse Report :

Contexte du projet :

Ce projet est une application Web développée en Python à partir du Framework Flask comprenant une base de données et un affichage du front en localhost sur le port 8080.
Le but est de pouvoir générer des rapports médicaux à l’aide des informations que l’utilisateur aura rentré dans les différents inputs, ces données seront ensuite récupérées par le back puis envoyées dans la base de données et seront retraitées dans le back afin de renvoyer un graphique avec une phrase de contextualisation de ces valeurs.

Explication globale de la structure du projet :

Pour la base, le fichier « app.py » contient la base même de l’application via le Framework Python Flask, le fichier « pulse_report.db » est là où se trouve base de données en SQLite et le fichier « create_db.py » permet la création globale de la base de données. Le fichier « view.py » comprend la gestion des pages et du système de routage Web. Le dossier « static » contient l’ensemble des fichiers CSS avec un dossier « images » où sont stockés les graphiques et le dossier « templates » comprend les pages HTML.
La structure du projet est ensuite divisée en plusieurs catégories de fonctions. La première catégorie est celle des fonctions gérant la base de données comprenant l’envoi des informations et la gestion des différents paramètres à ce propos, ces fonctions sont contenues dans le fichier « database_functions.py ». Puis il y a la seconde catégorie comprenant les fonctions gérant la récupération des informations dans la base de données contenues dans le fichier « getvalues_functions.py ». Pour terminer sur les deux dernières catégories avec les fonctions permettant la réalisation des graphiques avec la bibliothèque Python « matplotlib » dans le fichier « graph_functions » ainsi que les fonctions permettant de traiter et de renvoyer le stade des informations médicales au sein du fichier « checkvalues_functions ».

Point de vue technique :

-	Utilisation du Framework Python Flask
-	Back en Python 
-	Base de données en SQLite
-	Front en HTML 5 et CSS
