from dash import html, dcc

def create_navbar():
    return html.Nav([
        html.Div([
            html.Img(src='/assets/nba_logo.png', style={'height': '40px', 'marginRight': '10px'}),
            html.H1("NBA Player Stats Dashboard", style={'display': 'inline', 'fontSize': '24px', 'color': 'white'})
        ], style={'display': 'flex', 'alignItems': 'center'}),
        
        html.Div([
            dcc.Link(" Joueurs", href="/players", style={'marginRight': '20px', 'color': 'white', 'textDecoration': 'none'}),
            dcc.Link(" Statistiques", href="/stats", style={'color': 'white', 'textDecoration': 'none'}),
        ], style={'display': 'flex'})
    ], style={
        'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center',
        'padding': '1em', 'backgroundColor': '#0074D9', 'color': 'white'
    })
