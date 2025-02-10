NBA Player Stats Dashboard
Ce projet a pour objectif de scraper des données de statistiques NBA, les stocker dans une base de données MongoDB, et d'afficher ces données via un tableau de bord interactif créé avec Dash. 
L'application permet de visualiser des informations détaillées sur les joueurs NBA, leurs statistiques et des analyses liées à leurs performances.

Fonctionnalités
Scraping des données NBA : Le scraper collecte les statistiques des joueurs NBA depuis Basketball Reference pour les saisons 2021, 2022, 2023 et 2024.
Base de données MongoDB : Les données récupérées sont stockées dans une base MongoDB pour permettre des analyses et des visualisations rapides.
Dashboard interactif : L'application Dash offre plusieurs graphiques interactifs pour explorer les données des joueurs, y compris les points marqués, les statistiques par université et la distribution des points.
Graphiques interactifs : Affichage des données sous forme de cartes, graphiques en barres, graphiques en radar, et histogrammes.

Architecture
Le projet est divisé en plusieurs services Docker qui interagissent entre eux :

MongoDB : Contient les données des joueurs NBA.
Scraper : Scrape les données depuis le site de Basketball Reference et les stocke dans MongoDB.
Dashboard : Affiche les données via un tableau de bord interactif.


Prérequis:
Avant de démarrer le projet, assure-toi d'avoir les outils suivants installés :

Docker et Docker Compose:
Python 3.8+
Pip pour installer les dépendances Python.


Installation
1. Cloner le projet:
- git clone https://github.com/ton-utilisateur/nba-player-stats-dashboard.git
- cd nba-player-stats-dashboard

Installer les dépendances Python:
- pip install -r requirements.txt

Configurer Docker:
Le projet utilise Docker pour conteneuriser les services. Tu peux démarrer les services en utilisant Docker Compose.

1. Construire et démarrer les services Docker :
- docker-compose up --build
Cela va construire les images Docker et démarrer les services MongoDB, Scraper et Dashboard.

2. Vérifier que MongoDB est prêt :
Le service scraper dépend de MongoDB et attend qu'il soit prêt avant de commencer à scraper les données. MongoDB sera accessible sur localhost:27017.

3. Accéder au Dashboard :
Une fois les services lancés, le dashboard sera accessible à l'adresse suivante dans ton navigateur :

http://localhost:8050


Scraping des données:
Le scraper récupère les données des joueurs pour les années spécifiées (2021, 2022, 2023, 2024). Il les insère dans la base de données MongoDB.

Pour exécuter le scraping manuellement, tu peux lancer le script suivant :
- python scraping.py

Fonctionnement du Dashboard:

1. Page des Joueurs : Permet de visualiser les informations sur chaque joueur, y compris son année, son université, et ses statistiques.
2. Page des Statistiques : Affiche un graphique des meilleurs scoreurs NBA et permet de visualiser la distribution des points marqués par les joueurs.


Structure du projet:

nba-player-stats-dashboard/
├── app.py                    # Fichier principal de l'application Dash
├── dashboard.py              # Interface du tableau de bord avec Dash
├── docker-compose.yml        # Configuration des services Docker
├── Dockerfile                # Dockerfile pour le scraper
├── Dockerfile.dashboard      # Dockerfile pour l'application Dash
├── requirements.txt          # Liste des dépendances Python
├── scraping.py               # Script pour scraper les données
├── player_list.py            # Page de liste des joueurs
├── points_page.py            # Page des statistiques des joueurs
├── navbar.py                 # Navbar utilisée dans le tableau de bord
└── assets/                   # Images et autres ressources statiques


Utilisation

- Joueurs : Dans la page "Joueurs", tu peux sélectionner un joueur et voir ses informations détaillées.
- Statistiques : Dans la page "Statistiques", tu peux voir les meilleurs scoreurs de la saison et interagir avec des graphiques pour explorer les statistiques.

Développement:
Pour contribuer au projet, tu peux cloner le dépôt et créer une branche pour ajouter des fonctionnalités ou corriger des bugs. Après avoir fait tes modifications, soumets une pull request pour révision.

Technologies utilisées

Dash : Framework Python pour créer des applications web interactives.
MongoDB : Base de données NoSQL utilisée pour stocker les données des joueurs.
Plotly : Bibliothèque pour générer des graphiques interactifs.
Docker et Docker Compose : Outils pour conteneuriser l'application et ses services.
Pandas : Bibliothèque Python pour le traitement des données.
BeautifulSoup4 : Utilisé pour parser et extraire les données HTML lors du scraping.

Auteurs: Guy Tcheuffa, Elysee Mugabire
Nous declaron sur l'honneur que ce projet est le fruit de notre travail personnel et de chatgpt.