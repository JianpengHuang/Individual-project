"""
Dashboard created in lecture Week 10
"""


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

url = 'https://raw.githubusercontent.com/JianpengHuang/Individual-project/main/Revised%20data.csv'

df = pd.read_csv(url)


stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

### pandas dataframe to html table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = dash.Dash(__name__, external_stylesheets = stylesheet)
server = app.server

fig = px.scatter(df, x = "year", y = "price", color = "model")
fig.update_xaxes(range = [2014.5, 2023.5])
#fig.update_yaxes(range = [0, 220000])

app.layout = html.Div([
    html.H1('Used sport car Dashboard!', 
            style = {'textAlign' : 'center'}),
    
    dcc.Graph(figure = fig, 
              id = 'plot', 
              style={'width' : '40%', 
                     'float' : 'right'}),
    
    html.Div([html.H4('Make:'),
              dcc.Checklist(
                  options = [{'label': 'BMW', 'value': 'BMW'}, 
                             {'label' : 'Audi', 'value': 'Audi'}, 
                             {'label': 'Mercedes-Benz', 'value': 'Mercedes-Benz'}, 
                             {'label': 'Nissan', 'value': 'Nissan'}, 
                             {'label': 'Porsche', 'value': 'Porsche'},
                             {'label': 'Tesla', 'value': 'Tesla'}],
                  value = ['BMW', 'Audi', 'Mercedes-Benz', 'Nissan', 'Porsche', 'Tesla'],
                  id = 'Makelist')],
             style = {'width' : '20%', 'float':'left'}),
    
    html.Div([html.H4('Year'),
        dcc.Checklist(df['year'].unique(),
                     'Year', 
                     id = 'xaxis-column'
                     )
            ], style={'width': '20%', 'float': 'left'}),
    
    html.Div(id = 'table'),
    html.Br(),
    html.Div(generate_table(df),
             id="table_div",
             style={'width': '25%', 'float': 'right'}),
    ])

@app.callback(
    Output(component_id = 'table_div', component_property = "children"),
    Input(component_id = 'Makelist', component_property = "value"),
    )

def update_table(brand_list):
    df2 = df[df.make.isin(brand_list)].sort_values('year')
    return generate_table(df2)
    
@app.callback(
    Output(component_id = 'plot', component_property = "figure"),
    Input(component_id = 'Makelist', component_property = "value"),
    )

def update_table(brand_list):
    df2 = df[df.make.isin(brand_list)].sort_values('year')
    fig = px.scatter(df2, x = "year", y = "price", color = "model")
    return fig



    

    
if __name__ == '__main__':
   app.run_server(debug=True)
