# Dockerfile pour le service scraper
FROM python:3.9

# Mettre à jour la liste des paquets et installer netcat-openbsd pour fournir la commande "nc"
RUN apt-get update && apt-get install -y netcat-openbsd

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
COPY scraping.py ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour attendre que MongoDB soit disponible et lancer le script de scraping
CMD ["sh", "-c", "while ! nc -z mongodb 27017; do echo 'Waiting for MongoDB...'; sleep 5; done && python scraping.py"]
