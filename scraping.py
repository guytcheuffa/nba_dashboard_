import pandas as pd
import requests
import time
import pymongo

#  Attendre MongoDB avant de commencer
def wait_for_mongo():
    for _ in range(10):  
        try:
            client = pymongo.MongoClient("mongodb://mongodb:27017/")
            client.admin.command("ping")
            print(" MongoDB est prêt !")
            return client
        except Exception:
            print(" MongoDB n'est pas encore prêt... Attente de 5 sec.")
            time.sleep(5)
    print(" MongoDB ne répond pas.")
    exit(1)

# Connexion MongoDB
client = wait_for_mongo()
db = client["nba_db"]
collection = db["players_stats"]

#  Fonction pour récupérer les statistiques des joueurs
def fetch_top_players_and_stats(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_totals.html"
    try:
        tables = pd.read_html(url)
        nba_totals = tables[0].head(200)  
        nba_totals["Year"] = year  

        players_data = nba_totals[["Player", "PTS", "TRB", "2P", "3P", "Year"]]
        store_in_mongo(players_data)

        print(f" Données des joueurs {year} insérées dans MongoDB.")
        return players_data
    except Exception as e:
        print(f" Erreur pour {year}: {e}")
        return pd.DataFrame()

#  Insérer les données dans MongoDB
def store_in_mongo(players_stats):
    if not players_stats.empty:
        collection.insert_many(players_stats.to_dict("records"))
        print(" Données insérées dans MongoDB avec succès.")
    else:
        print(" Aucune donnée à insérer.")

#  Exécution du script
if __name__ == "__main__":
    for year in [2021, 2022, 2023, 2024]:
        fetch_top_players_and_stats(year)
