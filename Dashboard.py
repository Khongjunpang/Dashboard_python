import dash
import pandas as pd
import plotly.express as px
from dash import dash_table, dcc, html

# Initialize the Dash app
app = dash.Dash(__name__)

# Load the data
df = pd.read_csv('LeadTime.csv')

# Create visualizations
bar_fig = px.bar(df, x="Assemble lot", y="Quantity", color="Product", barmode="group", title="Quantity by Assemble Lot")
line_fig = px.line(df, x="Day At Current Operation", y="Cycle Time (Days)", color="Product", title="Cycle Time Over Days")

# Calculate metrics for the dashboard
total_quantity = df['Quantity'].sum()
average_cycle_time = df['Cycle Time (Days)'].mean()
average_days_at_operation = df['Day At Current Operation'].mean()
product_count = df['Product'].nunique()

# Define the layout of the app
app.layout = html.Div(style={
    'display': 'flex',
    'flex-direction': 'row',
    'height': '100vh',
    'background': 'linear-gradient(to bottom, #2c3e50, #34495e, #5d6d7e)',  # Darker gradient background
    'maxWidth': '1920px',  # Maintain 16:9 aspect ratio (1920px / 1080px)
    'maxHeight': '1080px',
    'margin': '0 auto'  # Center the dashboard on the screen
}, children=[
    # Sidebar (if needed)
    html.Iframe(
        src='/assets/sidebar.html',
        style={'width': '250px', 'height': '100vh', 'border': 'none', 'transition': 'width 0.3s'}
    ),

    # Main Content
    html.Div(style={'flex': '1', 'padding': '20px', 'overflowY': 'auto', 'maxWidth': '1720px', 'maxHeight': '1080px'}, children=[
        # Assemble Lot Filter Dropdown
        html.Div([
            html.Label('Select Assemble Lot',
                    style={'color': 'white'}),
            dcc.Dropdown(
                id='assemble-lot-dropdown',
                options=[
                    {'label': 'Select All', 'value': 'Select All'}
                ] + [{'label': lot, 'value': lot} for lot in df['Assemble lot'].unique()],
                value='Select All',  # Default value (display all)
                style={'width': '40%'}
            )
        ], style={'margin-bottom': '20px'}),

        # Card Dashboard
        html.Div(style={'display': 'flex', 'flex-wrap': 'wrap', 'gap': '20px', 'margin-bottom': '20px'}, children=[
            # Total Quantity Card
            html.Div(id='total-quantity-card', style={
                'background': 'linear-gradient(to right, #00bcd4, #00e5ff)',
                'border': '1px solid #ccc',
                'border-radius': '8px',
                'padding': '20px',
                'flex': '1 1 200px',
                'transition': 'transform 0.3s, box-shadow 0.3s',
                'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                'cursor': 'pointer',
                'textTransform': 'uppercase'
            }),

            # Average Cycle Time Card
            html.Div(id='average-cycle-time-card', style={
                'background': 'linear-gradient(to right, #00bcd4, #00e5ff)',
                'border': '1px solid #ccc',
                'border-radius': '8px',
                'padding': '20px',
                'flex': '1 1 200px',
                'transition': 'transform 0.3s, box-shadow 0.3s',
                'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                'cursor': 'pointer',
                'textTransform': 'uppercase'
            }),

            # Average Days at Current Operation Card
            html.Div(id='average-days-at-operation-card', style={
                'background': 'linear-gradient(to right, #00bcd4, #00e5ff)',
                'border': '1px solid #ccc',
                'border-radius': '8px',
                'padding': '20px',
                'flex': '1 1 200px',
                'transition': 'transform 0.3s, box-shadow 0.3s',
                'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                'cursor': 'pointer',
                'textTransform': 'uppercase'
            }),

            # Unique Products Card
            html.Div(id='unique-products-card', style={
                'background': 'linear-gradient(to right, #00bcd4, #00e5ff)',
                'border': '1px solid #ccc',
                'border-radius': '8px',
                'padding': '20px',
                'flex': '1 1 200px',
                'transition': 'transform 0.3s, box-shadow 0.3s',
                'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
                'cursor': 'pointer',
                'textTransform': 'uppercase'
            })
        ]),

        # Graphs and Data Table in One Row
html.Div(style={
    'display': 'flex',
    'flex-direction': 'row',
    'gap': '20px',
    'overflowX': 'auto',
    'margin-bottom': '20px'
}, children=[
    # Bar plot container
    html.Div(id='bar-plot-container', style={
        'flex': '1 1 45%',  # Adjust size as needed
        'min-width': '300px'
    }),

    # Line plot container
    html.Div(id='line-plot-container', style={
        'flex': '1 1 45%',  # Adjust size as needed
        'min-width': '300px'
    }),

    
    
]),
    # Data Table
        html.Div(id='data-table-container', style={'margin-top': '20px'})
        
    ]),
])

# Callback to update the cards, graphs, and table based on the selected assemble lot
@app.callback(
    [dash.dependencies.Output('total-quantity-card', 'children'),
     dash.dependencies.Output('average-cycle-time-card', 'children'),
     dash.dependencies.Output('average-days-at-operation-card', 'children'),
     dash.dependencies.Output('unique-products-card', 'children'),
     dash.dependencies.Output('bar-plot-container', 'children'),
     dash.dependencies.Output('line-plot-container', 'children'),
     dash.dependencies.Output('data-table-container', 'children')],
    [dash.dependencies.Input('assemble-lot-dropdown', 'value')]
)
def update_dashboard(selected_assemble_lot):
    if selected_assemble_lot == 'Select All':
        filtered_df = df
    else:
        filtered_df = df[df['Assemble lot'] == selected_assemble_lot]

    # Update the cards with the filtered data
    total_quantity = filtered_df['Quantity'].sum()
    average_cycle_time = filtered_df['Cycle Time (Days)'].mean()
    average_days_at_operation = filtered_df['Day At Current Operation'].mean()
    product_count = filtered_df['Product'].nunique()

    # Cards content
    total_quantity_card = html.Div([
        html.Div(style={'fontSize': '40px'}, children='💰'),
        html.H4("Total Quantity", style={'text': 'bold','color': 'darkblue'}),
        html.H2(f"{total_quantity}", style={'text': 'bold','color': 'darkblue'}),
    ])

    average_cycle_time_card = html.Div([
        html.Div(style={'fontSize': '40px'}, children='⏳'),
        html.H4("Average Cycle Time (Days)", style={'text': 'bold','color': 'darkblue'}),
        html.H2(f"{average_cycle_time:.2f}", style={'text': 'bold','color': 'darkblue'}),
    ])

    average_days_at_operation_card = html.Div([
        html.Div(style={'fontSize': '40px'}, children='📅'),
        html.H4("Average Days at Current Operation", style={'text': 'bold','color': 'darkblue'}),
        html.H2(f"{average_days_at_operation:.2f}", style={'text': 'bold','color': 'darkblue'}),
    ])

    unique_products_card = html.Div([
        html.Div(style={'fontSize': '40px'}, children='🔢'),
        html.H4("Unique Products", style={'text': 'bold','color': 'darkblue'}),
        html.H2(f"{product_count}", style={'text': 'bold','color': 'darkblue'}),
    ])

    # Update the bar chart
    bar_fig = px.bar(filtered_df, x="Assemble lot", y="Quantity", color="Product", barmode="group", title="Quantity by Assemble Lot")

    # Update the line chart
    line_fig = px.line(filtered_df, x="Day At Current Operation", y="Cycle Time (Days)", color="Product", title="Cycle Time Over Days")

    # Update the data table
    data_table = dash_table.DataTable(
        id='lead-time-table',
        columns=[{"name": i, "id": i} for i in filtered_df.columns],
        data=filtered_df.to_dict('records'),
        page_size=8,
        
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
    )
        

    return total_quantity_card, average_cycle_time_card, average_days_at_operation_card, unique_products_card, dcc.Graph(figure=bar_fig), dcc.Graph(figure=line_fig), data_table

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
