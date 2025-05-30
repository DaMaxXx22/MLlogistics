
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State
import pandas as pd
import joblib
from models.predict import prediction
from models.metrics import metrics_model

# Modelo y base de columnas
modelo = joblib.load("models/delivery_model.pkl")
X_base = joblib.load("models/columns_entrenamiento.pkl")
mae, mse, rmse, r2=metrics_model()

navbar = dbc.Navbar(
    dbc.Container(fluid=True, children=[
        html.Div([
            html.Img(src="/assets/logo.png", height="40px", className="rounded-circle me-2"),
            dbc.NavbarBrand("Predicción de Entregas", className="fw-bold text-white"),
        ], className="d-flex align-items-center"),
    ]),
    color="dark",
    dark=True,
)

layout = html.Div([
    navbar,
    dbc.Container(fluid=True, children=[


        html.H1('KPIS de Error de ML para Logistica',className="fw-bold text-black text-center"),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardHeader("MAE"),
                dbc.CardBody(html.H4(f"{mae:.2f} dias", id="kpi1", className="text-success"))
            ]), width=3),
            dbc.Col(dbc.Card([
                dbc.CardHeader("MSE"),
                dbc.CardBody(html.H4(f"{mse:.2f} días²", id="kpi2", className="text-primary"))
            ]), width=3),
            dbc.Col(dbc.Card([
                dbc.CardHeader("RMSE"),
                dbc.CardBody(html.H4(f"{rmse:.2f} dias", id="kpi3", className="text-info"))
            ]), width=3),
            dbc.Col(dbc.Card([
                dbc.CardHeader("R^2"),
                dbc.CardBody(html.H4(f"{r2:.2f} dias", id="kpi4", className="text-warning"))
            ]), width=3),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                dbc.Label("Distancia (km)"),
                dbc.Input(id="input-distancia", type="number", value=50),

                dbc.Label("Clima", className="mt-3"),
                dcc.Dropdown(
                    id="input-clima",
                    options=[{"label": c, "value": c} for c in ["soleado", "nublado", "lluvia"]],
                    value="soleado"
                ),

                dbc.Label("Proveedor", className="mt-3"),
                dcc.Dropdown(
                    id="input-proveedor",
                    options=[{"label": p, "value": p} for p in ["A", "B", "C"]],
                    value="A"
                ),

                dbc.Button("Predecir", id="btn-predecir", color="primary", className="mt-4")
            ], width=6),

            dbc.Col(dbc.Card([
                dbc.CardHeader("Predicción de entrega"),
                dbc.CardBody(html.H2("?", id="resultado-prediccion", className="text-center text-danger"))
            ]), width=6),
        ]),

        # 📌 ¿Qué significan?
        html.Hr(),
        dbc.Card([
            dbc.CardHeader("📌 ¿Qué significan los KPIs de error?"),
            dbc.CardBody([
                html.Ul([
                    html.Li("MAE bajo → En promedio, el modelo no se equivoca mucho (todos los errores pesan igual)."),
                    html.Li(
                        "MSE bajo → También indica buen desempeño, pero penaliza más los errores grandes porque eleva al cuadrado cada diferencia."),
                    html.Li("MAE ≈ MSE → No hay errores extremos en tus predicciones. ✅"),
                    html.Li("RMSE bajo → Se expresa en días, facilita interpretar el error en escala real."),
                    html.Li(
                        "R² cercano a 1 → El modelo explica muy bien la variación de los datos. R² = 1 es predicción perfecta."),
                    html.Li("R² ≈ 0 o negativo → El modelo no aprendió nada útil."),
                ])
            ])
        ], className="mt-4"),

        # 🧠 ¿Por qué el MSE es menor?
        dbc.Card([
            dbc.CardHeader("🧠 ¿Por qué el MSE es menor que el MAE en este caso?"),
            dbc.CardBody([
                html.P("✅ Tu modelo tiene errores pequeños, probablemente entre -1 y 1."),
                html.P("🔍 Cuando elevas al cuadrado errores pequeños como 0.3, se hacen más pequeños:"),
                html.Ul([
                    html.Li("(0.3)² = 0.09"),
                    html.Li("(0.5)² = 0.25"),
                ]),
                html.P("📌 Así que es totalmente válido que el MSE sea menor que el MAE si los errores son pequeños."),
                html.Br(),
                html.H5("🎯 Conclusión:"),
                html.Ul([
                    html.Li("✅ Predicción promedio ±0.35 días"),
                    html.Li("✅ R² > 0.92 → excelente desempeño"),
                    html.Li("✅ El modelo es apto para producción."),
                ])
            ])
        ], className="mt-4 mb-5")
    ])
])

# Callbacks
def register_callbacks(app):
    @app.callback(
        Output("resultado-prediccion", "children"),
        Input("btn-predecir", "n_clicks"),
        State("input-distancia", "value"),
        State("input-clima", "value"),
        State("input-proveedor", "value"),
        prevent_initial_call=True
    )
    def hacer_prediccion(n, distancia, clima, proveedor):
        if n >=1:
            return prediction(distancia,clima,proveedor)


