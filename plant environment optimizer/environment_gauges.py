import arduino_functions as af
import database_functions as df
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import dash_daq as daq


def create_gauges(plant_name):
    port = "COM3"
    baud_rate = 9600

    low_moisture, high_moisture = df.get_moisture_data(plant_name)
    low_temp, high_temp = df.get_temp_data(plant_name)
    low_humidity, high_humidity = df.get_humidity_data(plant_name)

    app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

    app.layout = dbc.Container(
        [
            dcc.Interval(id='update-value', interval=2000, n_intervals=0),
            dcc.Store(id="arduino-data"),
            html.Div(
                style={'text-align': 'center'},
                children=[
                    html.H1(f"Plant Name: {plant_name.title()}"),  # Display plant_name parameter
                    daq.Gauge(
                        color={"gradient": True,
                               "ranges": {"#FF0000": [0, low_moisture], "green": [low_moisture, high_moisture],
                                          "#FF0100": [high_moisture, 100]}},
                        id='moisture-gauge',
                        label="Moisture",
                        value=0,
                        max=100,
                        min=0,
                        style={'display': 'inline-block'}
                    ),
                    daq.Gauge(
                        color={"gradient": True,
                               "ranges": {"#FF0000": [0, low_temp], "green": [low_temp, high_temp],
                                          "#FF0100": [high_temp, 100]}},
                        id='temperature-gauge',
                        label="Temperature",
                        value=0,
                        max=100,
                        min=0,
                        style={'display': 'inline-block'}
                    ),
                    daq.Gauge(
                        color={"gradient": True,
                               "ranges": {"#FF0000": [0, low_humidity], "green": [low_humidity, high_humidity],
                                          "#FF0100": [high_humidity, 100]}},
                        id='humidity-gauge',
                        label="Humidity",
                        value=0,
                        max=100,
                        min=0,
                        style={'display': 'inline-block'}
                    )
                ]
            ),
        ],
        fluid=True,
    )

    @app.callback(Output('arduino-data', 'data'), Input('update-value', 'n_intervals'))
    def update_gauge_value(n_intervals):
        data = af.read_data(port, baud_rate)
        return data

    @app.callback(Output('moisture-gauge', 'value'), Input('arduino-data', 'data'))
    def update_gauge(value):
        return value[2]

    @app.callback(Output('humidity-gauge', 'value'), Input('arduino-data', 'data'))
    def update_gauge(value):
        return value[1]

    @app.callback(Output('temperature-gauge', 'value'), Input('arduino-data', 'data'))
    def update_gauge(value):
        return value[0]

    return app
