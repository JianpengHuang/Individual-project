"""
Dashboard created in lecture Week 10
"""


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


df = pd.read_csv('C:/Users/lrnru/Desktop/Bentely/Bentley 2022 Fall/MA 705/individual project/Revised data.csv')


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
    
    
    
    html.Div([
        html.H2('Make:'),
        dcc.RadioItems(options = [{'label':i, 'value': i} for i in df['make'].unique()], 
                     value = None,
                     id = 'dropdown_d1')],
        style = {'width' : '20%', 'float':'left'}),
    
    html.Div([html.H4('Year'),
        dcc.RadioItems(options = [{'label':i, 'value': i} for i in df['year'].unique()], 
                     
                     id = 'dropdown_d3',
                     value = None
                     )
            ], style={'width': '20%', 'float': 'left'}),
    
    html.Div(id = 'table'),
    html.Br(),
    dcc.Graph(figure = fig, 
              id = 'plot', 
              style={'width' : '40%', 
                     'float' : 'right'}),
    html.Div(generate_table(df),
             id="final_table",
             style={'width': '25%', 'float': 'right'}),
    
    html.Div([html.H4('Model'),
        dcc.RadioItems(options = [{'label':i, 'value': i} for i in df['model'].unique()], 
                     
                     id = 'dropdown_d2',
                     value = None
                     )
            ], style={'width': '20%', 'float': 'left'}),
    html.Div([html.H4('Body style'),
        dcc.RadioItems(options = [{'label':i, 'value': i} for i in df['body style'].unique()], 
                     
                     id = 'dropdown_d4',
                     value = None
                     )
            ], style={'width': '20%', 'float': 'left'})
    ])




@app.callback(
    Output(component_id = 'dropdown_d2', component_property = "options"),
    [
    Input(component_id = 'dropdown_d1', component_property = "value"),
    ])

def update_dropdown_2(d1):
    print(d1)
    if(d1 != None):
        df_filtered = df[(df["make"] == d1)]
        return[{'label':i, 'value':i} for i in df_filtered['model'].unique()]
    else:
        return[]

@app.callback(Output('final_table', 'children'), 
              [
                  Input('dropdown_d1', 'value'),
                  Input('dropdown_d2', 'value'),
                 
              ])
def update_table(d1,d2):   
    if(d1 != None and d2 != None):
        df_filtered = df[(df['make']==d1) & (df['model'] ==d2)]
        return generate_table(df_filtered)




if __name__ == '__main__':
   app.run_server(debug=True)



