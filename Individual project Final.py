# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:22:49 2022

@author: Peng
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

fig = px.scatter(df, x = "year", y = "price", color="model")
fig.update_xaxes(range = [2014.5, 2023.5])


app.layout = html.Div([
    html.H1('TrueCar Used Sport Car Dashboard',          
            style = {'textAlign' : 'center', 'font-size' : 45}),
    
    html.Br(),
    
    html.H6('MA 705 Individual Project: Jianpeng Huang ',          
            style = {'textAlign' : 'left', 'font-size': 18}),
    
    html.Div([
        
        html.Div([
            dcc.Markdown('''
                     **What is this dashboard about?**
                     ''', 
                     style = {'font-size': 15})]),
        html.Div([
            dcc.Markdown('''
                       The dashboard summarizeds the information of over three hundred used cars obtained from www.truecar.com.
                       It allows users to find an used car price and compare prices of a car over years.
                       
                       Also, the dashboard allows users to see the depreciation of a car over years.
                       ''')]),
        html.Div([
            dcc.Markdown('''
                         - **Make**: a list of all available car brands. **Model**: a list of all available car models.
                         ''')]),
        html.Div([
            dcc.Markdown('''
                         - **Body style**: a list of all available body style. **Year**: a list of all available year from 2015 to 2023.
                         ''')]),
      
       
           ], style = {'font-size': 13}
                         ),
                         
        html.Div([
            
            html.Div([
                dcc.Markdown('''
                         **How to use the dashboard?**
                         ''')],
                         style = {'font-size': 15}),
            html.Div([
                dcc.Markdown('''
                        Please check off the Make section first, a list of available models would pop up. 
                        Please select any models within the brands a user like. 
                        Then a list of body styles of a model would show up. 
                        
                        Finally, a list of years of a body style would show up.
                        The dashboard can do multiple checks off options for comparison.
                        
                        Please don’t forget to uncheck the options that a user doesn’t want 
                        data to show to go back last selecting options.  
                         ''')],
                         style = {'font-size': 13}), 
          

                ]),                  
        
    html.Div([
        html.Div([
            html.Div([
                
                html.H5('Make:'),
                dcc.Checklist(options = [{'label':i, 'value': i} for i in df['make'].unique()], 
                             value = [],
                             id = 'checklist_d1')],               
                style = {'width' : '20%'}),
            html.Div([    
                html.H5('Model'),
                dcc.Checklist(options = [{'label':i, 'value': i} for i in df['model'].unique()], 
                             value = [],
                             id = 'checklist_d2')],
                             
                style={'width': '20%'}),
            
            
            html.Div([
                html.H5('Body style'),
                dcc.Checklist(options = [{'label':i, 'value': i} for i in df['body style'].unique()],                
                             id = 'checklist_d3',
                             value = []
                             )
                    ], style={'width': '20%'}),
            html.Div([
                html.H5('Year'),
                dcc.Checklist(options = [{'label':i, 'value': i} for i in df['year'].unique()],                   
                             id = 'checklist_d4',
                             value = []
                             )
                    ], style={'width': '20%'}),
         
           ],style={'width': '40%','float': 'left'}),
        
        html.Div([
            html.Div([
                dcc.Graph(figure = fig, 
                      id = 'plot', 
                      style={'width' : '100%'
                             }),
            html.Div(generate_table(df),
                         id="final_table",
                         style={'width': '150%', 'font-size': 17}),
            ]),
          
            
            ], style = {'width': '60%', 'float': 'right'})
        
        
            ]),    
    
        html.Div([
          dcc.Markdown('''
           **References:**
               
              here is a list of data sources and references used in this course project
              '''),
          html.A('TrueCar Website: http://www.truecar.com',
                 href ='http://truecar.com',
                 target = '_blank'),
          
          html.Div([
          html.A('Dash Plotly Callbacks: https://dash.plotly.com/datatable/callbacks',
                 href ='https://dash.plotly.com/datatable/callbacks',
                 target = '_blank')
                  ]),
          html.Div([
          html.A('Dash Checklish Website: https://dash.plotly.com/dash-core-components/checklist',
                 href ='https://dash.plotly.com/dash-core-components/checklist',
                 target = '_blank'),
                  ]),
          html.Div([
          html.A('Dash Scatter Website: https://plotly.com/python/line-and-scatter/',
                 href ='https://plotly.com/python/line-and-scatter/',
                 target = '_blank')
                  ]),
              ])    
    
    ])




@app.callback(
    Output(component_id = 'checklist_d2', component_property = "options"),
    [
    Input(component_id = 'checklist_d1', component_property = "value"),
    ])

def update_checklist_d2(d1):
    print(d1)
    if(d1 != None):
        df_filtered = df[df.make.isin(d1)]
        return[{'label':i, 'value':i} for i in df_filtered['model'].unique()]
    else:
        return[]
    
@app.callback(
    Output(component_id = 'checklist_d3', component_property = "options"),
    [
    Input(component_id = 'checklist_d2', component_property = "value"),
    ])
def update_checklist_d3(d2):
    print(d2)
    if(d2 != None):
        df_filtered = df[df.model.isin(d2)]
        return[{'label':i, 'value':i} for i in df_filtered['body style'].unique()]
    else:
        return[]
    
@app.callback(
    Output(component_id = 'checklist_d4', component_property = "options"),
    [
    Input(component_id = 'checklist_d3', component_property = "value"),
    ])
   
def update_checklist_d4(d3):
     #print(d3)
     if(d3 != None):
         df_filtered = df[df['body style'].isin(d3)]
         return[{'label':i, 'value':i} for i in df_filtered['year'].unique()]
     else:
         return[]   


@app.callback(Output('final_table', 'children'), 
              [
                  Input('checklist_d1', 'value'),
                  Input('checklist_d2', 'value'),
                  Input('checklist_d3', 'value'),
                  Input('checklist_d4', 'value'),
              ])

def update_table(d1,d2,d3,d4):   
    if(d1 != None and d2 != None and d3 != None):
        df_filtered = df[(df.make.isin(d1)) & (df.model.isin(d2))
                         & (df['body style'].isin(d3)) & (df.year.isin(d4))]
        return generate_table(df_filtered)
              
@app.callback(Output('plot', 'figure'), 
              [
                  Input('checklist_d1', 'value'),
                  Input('checklist_d2', 'value'),
                  Input('checklist_d3', 'value'),
                  Input('checklist_d4', 'value'),
              ])

def update_plot(d1,d2,d3,d4):   
    if(d1 != None and d2 != None and d3 != None):
        df2 = df[(df.make.isin(d1)) & (df.model.isin(d2))
                 &(df['body style'].isin(d3)) & (df.year.isin(d4))]
        fig = px.scatter(df2, x="year", y="price", color = 'model', size = "price", 
                         title = "Used Sport Cars Price Over Years")
        return fig

    

if __name__ == '__main__':
   app.run_server(debug=False)