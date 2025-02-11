import dash
from dash import html, dcc
from components.navbar import create_navbar

#  Créer l'application en premier
app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

#  Ensuite, importer les pages après l'instanciation de l'app
import pages.points_page
import pages.player_list

# Définition du layout principal
app.layout = html.Div([
    create_navbar(),
    dcc.Location(id='url', refresh=False),
    dash.page_container
])

if __name__ == "__main__":
    app.run_server(debug=True)
