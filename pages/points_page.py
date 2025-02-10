from dash import html, dcc, register_page
import plotly.express as px
from data.fetch_data import fetch_nba_data

register_page(__name__, path="/stats")

data = fetch_nba_data()

layout = html.Div([
    html.H2("Top Joueurs par Points Marqués"),
    dcc.Graph(
        id='points-chart',
        figure=px.bar(
            data.sort_values(by="PTS", ascending=False).head(20),
            x="Player",
            y="PTS",
            title="Meilleurs Scoreurs NBA",
            labels={"PTS": "Points", "Player": "Joueur"},
            color="PTS",
            color_continuous_scale=px.colors.sequential.Blues
        )
    )
])
