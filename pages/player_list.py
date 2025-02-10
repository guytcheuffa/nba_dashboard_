from dash import html, dcc, Input, Output, callback
import dash
import pandas as pd
import plotly.express as px
from data.fetch_data import fetch_nba_data

dash.register_page(__name__, path="/players")

data = fetch_nba_data()

layout = html.Div([
    html.H2("Liste des Joueurs NBA"),
    dcc.Dropdown(
        id='player-dropdown',
        options=[{'label': player, 'value': player} for player in data['Player'].unique()],
        placeholder="Sélectionner un joueur"
    ),
    html.Div(id='player-details')
])

@callback(
    Output('player-details', 'children'),
    Input('player-dropdown', 'value')
)
def display_player_details(player_name):
    if not player_name:
        return ""
    
    player_info = data[data['Player'] == player_name].iloc[0]
    return html.Div([
        html.Img(src=f"/assets/{player_name}.png", style={'width': '150px', 'borderRadius': '10px'}),
        html.H3(f"{player_name} - {player_info['Year']}"),
        html.P(f"Université : {player_info['College']}"),
        html.P(f"Points : {player_info['PTS']}"),
        html.P(f"Rebonds : {player_info['TRB']}"),
        html.P(f"Passes : {player_info['AST']}")
    ])
