#----------------------------# Load Your Dependencies#--------------------------#
import dash  # Dash
from dash import  dcc    # Dash core Components
from dash import html   # HTML for Layout and Fonts
import plotly.express as px           # Plotly Graphs uses graph objects internally
import plotly.graph_objects as go     # Plotly Graph  more customized 
import pandas as pd                   # Pandas For Data Wrangling
from dash import Input, Output  # Input, Output for  Call back functions

#--------------------------#Instanitiate Your App#--------------------------#

app = dash.Dash(__name__) 
server = app.server

#--------------------------# Pandas Section #------------------------------#

df =pd.read_csv('Churn_Modelling.csv') 
df['Age_']=pd.cut(df['Age'],3 , labels= ["Young","Mid_Aged","Old"])
df['Balance_']=pd.cut(df['Balance'],3 , labels= ["Low","Mid_Balance","High"])
df['Exited_'] = df['Exited'].map({0:'Non-Exited', 1:'Exited'})
df['Tenure_6']= (df['Tenure']>6).astype("int")

app.layout = html.Div([html.Div([html.A([html.H2('Bank Analysis Dashboard'),html.Img(src='/assets/logo.png')],  # A for hyper links
                                        href='http://projectnitrous.com/')],className="banner"),
                       html.Div([
                        html.H4('Balance for Exited and Non-Exited different clients'),
                    ],className="five columns", style={'padding':10}),
                       html.Div([
                        html.H4('Correlations between different fields affecting clients'),
                    ],className="five columns", style={'padding':10}),
                       html.Div([
                        dcc.RadioItems(
                            id='hist_radio',
                            options=[
                                {'label': 'Gender', 'value': 'Gender'},
                                {'label': 'No of Products', 'value': 'NumOfProducts'},
                                {'label': 'Has Credit Card', 'value': 'HasCrCard'},
                                {'label': 'IsActiveMember', 'value': 'IsActiveMember'}
                            ],
                            value='Gender',
                            labelStyle={'display': 'inline-block'}
                        ),
                        html.Div(['   '], style={'padding':5}),
                        html.Div([
                            dcc.Graph(id='hist_graph'),
                        ]),
                    ],className="five columns", style={'backgroundColor': '#e0dae2', 'border-radius': 25, 'padding':10}),
                       #, "border":"2px #a292b3 solid"
                       html.Div([
                        dcc.Dropdown(
                            id='heatmap_dropdown', 
                            options=[{'label':df.columns[i], 'value':df.columns[i]} for i in range(len(df.columns)) if (df[df.columns[i]].dtype== 'int64') or (df[df.columns[i]].dtype== 'float64')],
                            value=['Tenure', 'Balance'],
                            multi = True,
                            searchable=True,
                            clearable=False
                        ),
                        html.Div([
                            dcc.Graph(id='heatmap_graph'),
                        ]),
                    ],className="five columns", style={'backgroundColor': '#e0dae2', 'border-radius': 25, 'padding':10}),
                        
                       html.Div([html.Br(),],className="eleven columns"),
                       html.Div([
                        html.H4('Clients count'),
                    ],className="three columns", style={'padding':10}),
                       html.Div([
                        html.H4('No of products per gender'),
                    ],className="three columns", style={'padding':10}),
                       html.Div([
                        html.H4('No of products per multi factors'),
                        ],className="three columns", style={'padding':10}),
                       html.Div([
                        dcc.Dropdown(
                            id='geo_dropdown',
                            options=[
                                {'label': 'Geography', 'value': 'Geography'},
                                {'label': 'Gender', 'value': 'Gender'},
                                {'label': 'Tenure higher than 6', 'value': 'Tenure_6'},
                            ],

                            value=['Geography', 'Gender'],
                            multi=True,
                            searchable=True,
                            clearable=False
                        ),
                        html.Div([
                            dcc.Graph(id='geo_graph'),
                        ]),
                    ],className="three columns", style={'backgroundColor': '#e0dae2', 'border-radius': 25, 'padding':10}),
                       html.Div([
                        dcc.Dropdown(
                            id='gen_dropdown',
                            options=[
                                {'label': 'Gender', 'value': 'Gender'},
                                {'label': 'Is Active Member', 'value': 'IsActiveMember'},
                            ],

                            value=['Gender', 'IsActiveMember'],
                            multi=True,
                            searchable=True,
                            clearable=False
                        ),
                        html.Div([
                            dcc.Graph(id='gen_graph'),
                        ]),
                    ],className="three columns", style={'backgroundColor': '#e0dae2', 'border-radius': 25, 'padding':10}),
                       html.Div([
                        dcc.Dropdown(
                            id='sunburst_dropdown',
                            options=[
                                {'label': 'Exited', 'value': 'Exited_'},
                                {'label': 'Age', 'value': 'Age_'},
                                {'label': 'Balance', 'value': 'Balance_'},
                                {'label': 'IsActiveMember', 'value': 'IsActiveMember'}
                            ],

                            value=['Exited_', 'Age_','Balance_'],
                            multi=True,
                            searchable=True,
                            clearable=False
                        ),
                        html.Div([
                            dcc.Graph(id='sunburst_graph'),
                        ]),
                        ],className="three columns", style={'backgroundColor': '#e0dae2', 'border-radius': 25, 'padding':10}),
                        
                       html.Div([html.Br(),],className="eleven columns"),
                       html.Div([
                        html.H4('Count of clients per multiple factors'),
                    ],className="eleven columns", style={'padding':10}),
                       html.Div([
                        #html.H4('Count of clients per multiple factors', style={'color':'#3f2b56'}),
                           html.Div([
                                dcc.Dropdown(
                                    id='exit_ch',
                                    options=[{'label':i, 'value':i} for i in df.Exited_.unique()],
                                    value='Exited',
                                    clearable=False
                                ),
                           ], className="two columns"),
                           html.Div([
                                dcc.Dropdown(
                                    id='gender_ch',
                                    options=[{'label':i, 'value':i} for i in df.Gender.unique()],
                                    value='Male',
                                    clearable=False
                                ),
                           ], className="two columns"),
                           html.Div([
                                dcc.Dropdown(
                                    id='geog_ch',
                                    options=[{'label':i, 'value':i} for i in df.Geography.unique()],
                                    value='France',
                                    clearable=False
                                ),
                           ], className="two columns"),
                           
                           html.Div([
                                html.H3(html.Div(id='count_exit')),
                           ], className="eleven columns"),
                    ],className="eleven columns", style={'backgroundColor': '#e0dae2', 'border-radius': 25, 'padding':10}),
                       
                ])

@app.callback(
    Output('hist_graph', 'figure'),
    Input('hist_radio', 'value'),
    )

def hist_value(value):
    fig = px.histogram(df, x=value, y="Balance", color=value, pattern_shape="Exited_")
    fig.update_layout({'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    #'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    return fig

@app.callback(
    Output('heatmap_graph', 'figure'),
    Input('heatmap_dropdown', 'value'),
    )

def heatmap_value(value):
    corr_matrix = df[value].corr()
    fig = px.imshow(corr_matrix, text_auto='.1f', aspect="auto", color_continuous_scale='RdBu_r')
    fig.update_layout({'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig

@app.callback(
    Output('geo_graph', 'figure'),
    Input('geo_dropdown', 'value'),
    )

def sunburst1_value(value):
    fig = px.sunburst(data_frame=df, path=value)
    fig.update_traces(textinfo='label+percent root')
    fig.update_layout({'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig

@app.callback(
    Output('gen_graph', 'figure'),
    Input('gen_dropdown', 'value'),
    )

def sunburst2_value(value):
    fig = px.sunburst(data_frame=df, path=value, values='NumOfProducts')
    fig.update_traces(textinfo='label+value')
    fig.update_layout({'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig

@app.callback(
    Output('sunburst_graph', 'figure'),
    Input('sunburst_dropdown', 'value'),
    )

def sunburst3_value(value):
    fig = px.sunburst(df, path=value, values='NumOfProducts')
    fig.update_traces(textinfo="label")
    fig.update_layout({'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig

@app.callback(
    Output('count_exit', 'children'),
    Input('exit_ch', 'value'),
    Input('gender_ch', 'value'),
    Input('geog_ch', 'value'),
    )

def sum_value(value1, value2, value3):
    res = df[(df['Exited_']==value1) & (df['Gender']==value2) & (df['Geography']==value3)]['Exited'].count()
    
    return 'The total no of {}, {} clients in {} are {}'.format(value1, value2, value3, res)

if __name__ == '__main__':
    app.run_server()
