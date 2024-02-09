# Projet Gestion Suivi Médical

## Contexte : 
L’idée est de pouvoir établir un suivi médical des constantes vitales d’une personne au cours du temps. L’utilisateur rentrerait ses données médicales via une interface web connecté à un serveur local en Python et le programme renverrait un rapport de son état de santé global comprenant un suivi de son pouls, de sa tension ainsi que de son IMC. Le but est d’automatiser la prise d’informations médicales de base afin de rendre un rapport détaillé avec des conseils en plus pour l’utilisateur.

## Wiki Utilisateur Pulse Report :

### Comment lancer l’application Web :
---

Afin de lancer l’application Web Pulse Report, vous devez premièrement exécuter la base de données en entrant la commande : « python create_db.py » puis vous pourrez exécuter l’application en entrant la commande : « python app.py ». Lorsque que l’application sera lancée en local, vous pourrez y accéder en cliquant sur le lien disponible dans le terminal (http://localhost:8080).

### Que faire lors de votre première connexion :
---

Pour commencer, vous arriverez sur une page de connexion où il vous sera demandé de rentrer vos données afin de créer votre compte. Une fois votre compte crée et votre identification effectuée, vous aurez accès à l’application dans son intégralité. Une première page vous demandera de rentrer vos informations médicales afin de réaliser le début de vos rapports. Dès que vous aurez rentré ces informations, vous aurez serez redirigé vers une nouvelle page où vous pourrez voir vos rapports médicaux (Suivi du BPM, de la saturation en oxygène, de l’IMC et de la pression artérielle). Vous ne pouvez rentrer vos informations qu’une seule fois par jour dans le but d’obtenir un réel suivi médical à travers le temps. Pour obtenir des rapports exploitables, il est recommandé d’utiliser l’application pendant au minimum une semaine dans le cadre d’un besoin médical.

### À quoi sert cette application et à qui est-elle adressée ?
---

Comme vu précédemment, l’objectif de cette application est de générer différents rapports médicaux afin de suivre les éléments basiques de votre santé en prenant en compte vos constantes vitales. Pour utiliser cette application de la meilleure manière possible, il est fortement recommandé voire nécessaire de posséder du matériel afin de mesurer ces constantes, à savoir un oxymètre et un tensiomètre au maximum. L’application est adressée aux personnes voulant suivre l’évolution des paramètres généraux de leur santé en fonction du temps, cela pourrait convenir aux personnes nécessitant un suivi médical que ce soit pour un besoin personnel ou auprès d’un professionnel dans ce domaine.

### Fonctionnalités à venir :
---

- Sécurité des données personnelles (hashing mot de passe)
- Modification des données journalières sur les rapports en cas d'erreur
- Amélioration du visuel de l'application web
- Possibilité de télécharger les rapports
- Notification pour rappeler d'entrer les données du jour
- Possibilité de modification des informations personnelles ou bien suppression du compte et des donnée relier a celui-ci
