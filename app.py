import dash
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, dcc, html

app = dash.Dash()

# Layout of the app
app.layout = html.Div([
    # Location component to track the URL
    dcc.Location(id='url', refresh=False),
    html.Div(
        className="topbar",
        children=[
            html.H1("Intel Corporation", style={"margin": "0", "padding": "10px"})
        ]
    ),
    # Sidebar
    html.Div(
        id="sidebar",
        className="sidebar",
        children=[
            # Logo and Menu Button
            html.Div(
                className="logo-details",
                children=[
                    html.Div("Intel", className="logo_name"),
                    html.I(className="bx bx-menu", id="btn", n_clicks=0)
                ]
            ),
            # Navigation List
            html.Ul(
                className="nav-list",
                children=[
                    html.Li([  # Leadtime link
                        html.A(
                            href="/leadtime",
                            children=[
                                html.I(className="bx bx-timer"),
                                html.Span("Leadtime", className="links_name")
                            ]
                        ),
                        html.Span("Leadtime", className="tooltip")
                    ]),
                    html.Li([  # Lot link
                        html.A(
                            href="/lot",
                            children=[
                                html.I(className="bx bx-cube"),
                                html.Span("Lot", className="links_name")
                            ]
                        ),
                        html.Span("Lot", className="tooltip")
                    ]),
                    html.Li([  # Editing Instruction link
                        html.A(
                            href="/editing-instruction",
                            children=[
                                html.I(className="bx bx-edit-alt"),
                                html.Span("Editing Instruction", className="links_name")
                            ]
                        ),
                        html.Span("Editing Instruction", className="tooltip")
                    ]),
                    html.Li([  # Table link
                        html.A(
                            href="/table",
                            children=[
                                html.I(className="bx bx-table"),
                                html.Span("Table", className="links_name")
                            ]
                        ),
                        html.Span("Table", className="tooltip")
                    ]),
                    html.Li([  # Alarm link
                        html.A(
                            href="/alarm",
                            children=[
                                html.I(className="bx bx-bell"),
                                html.Span("Alarm", className="links_name")
                            ]
                        ),
                        html.Span("Alarm", className="tooltip")
                    ]),
                    html.Li([  # Plan link
                        html.A(
                            href="/plan",
                            children=[
                                html.I(className="bx bx-calendar"),
                                html.Span("Plan", className="links_name")
                            ]
                        ),
                        html.Span("Plan", className="tooltip")
                    ]),
                ]
            )
        ]
    ),
    
    # Hidden store to keep track of sidebar state
    dcc.Store(id='sidebar-state', data={'open': False})
])

# Callback to toggle sidebar state
@app.callback(
    [Output('sidebar', 'className'),
     Output('sidebar-state', 'data')],
    [Input('btn', 'n_clicks')],
    [State('sidebar-state', 'data')]
)
def toggle_sidebar(n_clicks, state):
    if n_clicks % 2 == 0:
        # If n_clicks is even, set the sidebar to closed
        return 'sidebar', {'open': False}
    else:
        # If n_clicks is odd, set the sidebar to open
        return 'sidebar open', {'open': True}

if __name__ == "__main__":
    app.run_server(debug=True)
