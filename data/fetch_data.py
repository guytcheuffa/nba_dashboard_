import pymongo
import pandas as pd
import time

def fetch_nba_data():
    client = pymongo.MongoClient("mongodb://mongodb:27017/")
    db = client["nba_db"]
    collection = db["players_stats"]

    # Charger les données depuis MongoDB
    data = pd.DataFrame(list(collection.find({}, {"_id": 0})))  # Exclure l'ID MongoDB
    return data

def wait_for_mongodb():
    retries = 5
    for i in range(retries):
        try:
            client = pymongo.MongoClient("mongodb://mongodb:27017/", serverSelectionTimeoutMS=3000)
            client.server_info()  # Teste la connexion
            print("✔ MongoDB est prêt !")
            return client
        except pymongo.errors.ServerSelectionTimeoutError:
            print(f" MongoDB non disponible, tentative {i+1}/{retries}...")
            time.sleep(5)  # Attendre avant de réessayer

    raise Exception(" Impossible de se connecter à MongoDB après plusieurs tentatives.")

# Utilisation :
client = wait_for_mongodb()
db = client["nba_db"]
