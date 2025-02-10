
#!/bin/bash

# README généré pour le projet NBA Player Stats Dashboard

echo "### 📝 NBA Player Stats Dashboard README"

# Titre du projet
echo "# NBA Player Stats Dashboard"

# Description du projet
echo "Ce projet a pour objectif de scraper des données de statistiques NBA, les stocker dans une base de données MongoDB, et les afficher via un tableau de bord interactif créé avec Dash. L'application permet de visualiser des informations détaillées sur les joueurs NBA, leurs statistiques et des analyses liées à leurs performances."

echo ""

# Fonctionnalités
echo "## 🚀 Fonctionnalités"
echo "- **Scraping des données NBA** : Le scraper collecte les statistiques des joueurs NBA depuis [Basketball Reference](https://www.basketball-reference.com/) pour les saisons 2021, 2022, 2023 et 2024."
echo "- **Base de données MongoDB** : Les données récupérées sont stockées dans une base MongoDB pour permettre des analyses et des visualisations rapides."
echo "- **Dashboard interactif** : L'application Dash offre plusieurs graphiques interactifs pour explorer les données des joueurs, y compris les points marqués, les statistiques par université et la distribution des points."
echo "- **Graphiques interactifs** : Affichage des données sous forme de cartes, graphiques en barres, graphiques en radar, et histogrammes."

echo ""

# Architecture
echo "## 🛠️ Architecture"
echo "Le projet est divisé en plusieurs services Docker qui interagissent entre eux :"
echo "1. **MongoDB** : Contient les données des joueurs NBA."
echo "2. **Scraper** : Scrape les données depuis le site de Basketball Reference et les stocke dans MongoDB."
echo "3. **Dashboard** : Affiche les données via un tableau de bord interactif."

echo ""

# Prérequis
echo "## 🧑‍💻 Prérequis"
echo "Avant de démarrer le projet, assure-toi d'avoir les outils suivants installés :"
echo "- **Docker** et **Docker Compose**"
echo "- **Python 3.8+**"
echo "- **Pip** pour installer les dépendances Python."

echo ""

# Installation
echo "## 🚧 Installation"
echo "### Cloner le projet"
echo "\`\`\`bash"
echo "git clone https://github.com/ton-utilisateur/nba-player-stats-dashboard.git"
echo "cd nba-player-stats-dashboard"
echo "\`\`\`"

echo "### Installer les dépendances Python"
echo "\`\`\`bash"
echo "pip install -r requirements.txt"
echo "\`\`\`"

echo "### Configurer Docker"
echo "Le projet utilise Docker pour conteneuriser les services. Tu peux démarrer les services en utilisant Docker Compose."

echo "1. **Construire et démarrer les services Docker** :"
echo "\`\`\`bash"
echo "docker-compose up --build"
echo "\`\`\`"
echo "Cela va construire les images Docker et démarrer les services MongoDB, Scraper et Dashboard."

echo "2. **Vérifier que MongoDB est prêt** :"
echo "Le service `scraper` dépend de MongoDB et attend qu'il soit prêt avant de commencer à scraper les données. MongoDB sera accessible sur `localhost:27017`."

echo "3. **Accéder au Dashboard** :"
echo "Une fois les services lancés, le dashboard sera accessible à l'adresse suivante dans ton navigateur :"
echo "\`\`\`"
echo "http://localhost:8050"
echo "\`\`\`"

echo "### Scraping des données"
echo "Le scraper récupère les données des joueurs pour les années spécifiées (2021, 2022, 2023, 2024). Il les insère dans la base de données MongoDB."

echo "Pour exécuter le scraping manuellement, tu peux lancer le script suivant :"
echo "\`\`\`bash"
echo "python scraping.py"
echo "\`\`\`"

echo ""

# Fonctionnement du Dashboard
echo "## 📊 Fonctionnement du Dashboard"
echo "1. **Page des Joueurs** : Permet de visualiser les informations sur chaque joueur, y compris son année, son université, et ses statistiques."
echo "2. **Page des Statistiques** : Affiche un graphique des meilleurs scoreurs NBA et permet de visualiser la distribution des points marqués par les joueurs."

echo ""

# Structure du projet
echo "## 📂 Structure du projet"
echo "\`\`\`"
echo "nba-player-stats-dashboard/"
echo "├── app.py                    # Fichier principal de l'application Dash"
echo "├── dashboard.py              # Interface du tableau de bord avec Dash"
echo "├── docker-compose.yml        # Configuration des services Docker"
echo "├── Dockerfile                # Dockerfile pour le scraper"
echo "├── Dockerfile.dashboard      # Dockerfile pour l'application Dash"
echo "├── requirements.txt          # Liste des dépendances Python"
echo "├── scraping.py               # Script pour scraper les données"
echo "├── player_list.py            # Page de liste des joueurs"
echo "├── points_page.py            # Page des statistiques des joueurs"
echo "├── navbar.py                 # Navbar utilisée dans le tableau de bord"
echo "└── assets/                   # Images et autres ressources statiques"
echo "\`\`\`"

echo ""

# Développement
echo "## 💻 Développement"
echo "Pour contribuer au projet, tu peux cloner le dépôt et créer une branche pour ajouter des fonctionnalités ou corriger des bugs. Après avoir fait tes modifications, soumets une pull request pour révision."

echo ""

# Technologies utilisées
echo "## 🖥️ Technologies utilisées"
echo "- **Dash** : Framework Python pour créer des applications web interactives."
echo "- **MongoDB** : Base de données NoSQL utilisée pour stocker les données des joueurs."
echo "- **Plotly** : Bibliothèque pour générer des graphiques interactifs."
echo "- **Docker** et **Docker Compose** : Outils pour conteneuriser l'application et ses services."
echo "- **Pandas** : Bibliothèque Python pour le traitement des données."
echo "- **BeautifulSoup4** : Utilisé pour parser et extraire les données HTML lors du scraping."

echo ""

# Auteurs
echo "## 👨‍💻 Auteurs"
echo "- **Guy Tcheuffa, Elysee Mugabire**"

echo ""

echo "Nous declarons sur l'honneur que ce projet a été réaliser par nous meme et l'aide de chatgpt."

echo ""
