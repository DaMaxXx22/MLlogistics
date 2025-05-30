import dash
import dash_bootstrap_components as dbc

from app.layout import layout, register_callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Predicción de Entregas"
app.layout = layout

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)

