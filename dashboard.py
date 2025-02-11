import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import pymongo
import time

def connect_to_mongo(retries=10, delay=10):
    for i in range(retries):
        try:
            client = pymongo.MongoClient("mongodb://mongodb:27017/")
            db = client["nba_db"]
            collection = db["players_stats"]
            print(" Connexion à MongoDB réussie !")
            return collection
        except pymongo.errors.ServerSelectionTimeoutError:
            print(f" Tentative {i+1}/{retries} : MongoDB n'est pas prêt... Attente {delay} sec.")
            time.sleep(delay)
    print(" Impossible de se connecter à MongoDB.")
    return None

# Connexion à MongoDB
collection = connect_to_mongo()

# Récupération des données depuis MongoDB
def load_data():
    data = list(collection.find({}, {"_id": 0}))
    return pd.DataFrame(data)

df = load_data()

# Initialisation de l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Analytics NBA - Parcours Universitaire des Joueurs"),
    
    dcc.Tabs([
        dcc.Tab(label="Carte des Universités", children=[
            html.H2("Répartition Géographique des Universités d'où proviennent les joueurs"),
            dcc.Graph(id="map-graph")
        ]),
        
        dcc.Tab(label="Statistiques par Université", children=[
            html.H2("Analyse par Université"),
            dcc.Dropdown(
                id="year-dropdown",
                options=[{"label": year, "value": year} for year in df["Year"].unique()],
                value=df["Year"].max(),
                clearable=False
            ),
            dcc.Graph(id="university-bar-chart")
        ]),
        
        dcc.Tab(label="Statistiques des Joueurs", children=[
            html.H2("Statistiques des Joueurs"),
            dcc.Dropdown(
                id="player-dropdown",
                options=[{"label": player, "value": player} for player in df["Player"].unique()],
                placeholder="Sélectionner un joueur"
            ),
            dcc.Dropdown(
                id="season-dropdown",
                options=[{"label": year, "value": year} for year in df["Year"].unique()],
                placeholder="Sélectionner une saison"
            ),
            dcc.Graph(id="player-stats-radar")
        ]),
        
        dcc.Tab(label="Distribution des Points", children=[
            html.H2("Distribution des Points"),
            dcc.Dropdown(
                id="year-dropdown-hist",
                options=[{"label": year, "value": year} for year in df["Year"].unique()],
                value=df["Year"].max(),
                clearable=False
            ),
            dcc.Dropdown(
                id="player-dropdown-hist",
                options=[{"label": player, "value": player} for player in df["Player"].unique()],
                placeholder="Sélectionner un joueur (optionnel)"
            ),
            dcc.Graph(id="histogram")
        ])
    ])
])

# Callbacks pour mettre à jour les graphiques
@app.callback(
    Output("map-graph", "figure"),
    Input("year-dropdown", "value")
)
def update_map(selected_year):
    filtered_df = df[df["Year"] == selected_year]
    fig = px.scatter_mapbox(filtered_df, lat="Latitude", lon="Longitude", hover_name="College",
                             size="Points", color="Points",
                             mapbox_style="carto-positron")
    return fig

@app.callback(
    Output("university-bar-chart", "figure"),
    Input("year-dropdown", "value")
)
def update_university_chart(selected_year):
    filtered_df = df[df["Year"] == selected_year]
    univ_counts = filtered_df.groupby("College").size().reset_index(name="Nombre de joueurs")
    fig = px.bar(univ_counts.sort_values("Nombre de joueurs", ascending=False).head(15),
                 x="College", y="Nombre de joueurs",
                 title=f"Top 15 des Universités par Nombre de Joueurs ({selected_year})")
    return fig

@app.callback(
    Output("player-stats-radar", "figure"),
    [Input("player-dropdown", "value"), Input("season-dropdown", "value")]
)
def update_radar_chart(selected_player, selected_season):
    if not selected_player or not selected_season:
        return px.line_polar()
    
    player_data = df[(df["Player"] == selected_player) & (df["Year"] == selected_season)]
    if player_data.empty:
        return px.line_polar()
    
    stats = player_data.iloc[0][["PTS", "TRB", "2P", "3P"]]
    radar_data = pd.DataFrame({"Stat": stats.index, "Valeur": stats.values})
    
    fig = px.line_polar(radar_data, r="Valeur", theta="Stat", line_close=True)
    fig.update_layout(title=f"Profil statistique de {selected_player} ({selected_season})")
    return fig

@app.callback(
    Output("histogram", "figure"),
    [Input("year-dropdown-hist", "value"), Input("player-dropdown-hist", "value")]
)
def update_histogram(selected_year, selected_player):
    filtered_df = df[df["Year"] == selected_year]
    fig = px.histogram(filtered_df, x="Points", nbins=20, title=f"Distribution des Points Marqués en {selected_year}")
    if selected_player:
        player_points = filtered_df[filtered_df["Player"] == selected_player]["Points"]
        fig.add_trace(px.histogram(player_points, x="Points", nbins=20, color_discrete_sequence=["red"]).data[0])
    return fig

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)

