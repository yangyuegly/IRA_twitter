import dash
import dash_core_components as dcc
import dash_html_components as html
# -*- coding: utf-8 -*-
import dash
import pandas as pd
import json
import flask
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from flask import render_template
#from bar_chart.py import datelist,counterNoFURLs, counterFURLs
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from url_count import fake_news_accounts, counters, datelist

print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
])



#------------------Get data code-------------------------


#get start and end dates
start, end = {},{}
with open('start_end.json','r') as json_file:
        news_dates= (json.load(json_file))
#print(news_dates[0])
for i in range(len(news_dates)):
    start[news_dates[i]['AccountName']] = news_dates[i]['Start']
    end[news_dates[i]['AccountName']] = news_dates[i]['End']
print(start,end)
    
    
#get real news sources associated with fake accounts
with open('real_news.json','r') as json_file:
        news_urls= (json.load(json_file))
#print(news_urls[0])

urls = {}
for account in fake_news_accounts:
    curr_url = []
    for i in range(len(news_urls)):
        if news_urls[i]["fake account name"] == account:
            curr_url.append((news_urls[i]["URL of real websites"],news_urls[i]["Frequency"]))
            #print(curr_url)
    urls[account] = curr_url
#print(urls['TodayPittsburgh'])



#--------------------Graph------------------------------
#traces for the stack bar

traces ={}
for news in fake_news_accounts:
    traces[news+str(1)] = go.Bar(
        x=datelist,
        y=counters[news][0],
        name='with URLs'
    )
    traces[news+str(2)] = go.Bar(
        x=datelist,
        y=counters[news][1],
        name='without URLs'
    )

#html and graph components

page_1_layout = html.Div([
    html.H1('IRA Fake Twitter Accounts'),

    html.Div(children='''
        Select a fake twitter account name to view information about its activity
    '''),
    html.Div(
    [       
            dcc.Dropdown(
                id="AccountNames",
                options=[{
                    'label': i,
                    'value': i
                } for i in fake_news_accounts],
                value='NewOrleansON'),
            html.Div(id='page-1-content'),
            html.Br(),
            html.Div('This account was active from: ',id = "Dates"),
            html.H6("Here are a list of urls that it mentioned most requently in its tweets: "),
            html.Div(id = "Urls"),
            html.H6("Here are a graph showing the monthly distribution of its tweets with urls and without urls: "),
    ],
    style={'width': '25%',
               'display': 'inline-block'}),
    
    dcc.Graph(id='bar_plot',
              figure=go.Figure(data=[traces['NewOrleansON1'], traces['NewOrleansON2']],
                               layout=go.Layout(barmode='stack'))
    
    )
#    html.Div(
#    [
#        dcc.Link('Go to Page 2', href='/page-2'),
#            html.Br(),
#            dcc.Link('Go back to home', href='/')
#    ], style={'width': '25%',
#               'display': 'inline-block'})
    
])


   
    
#---------------------------------------------end graph




#updating 
@app.callback(
    [dash.dependencies.Output('bar_plot', 'figure'),dash.dependencies.Output('Dates', 'children'), dash.dependencies.Output('Urls', 'children')],
    [dash.dependencies.Input('AccountNames', 'value')])
def update_output(value):
    print('This account was active from: '+start[value] + " to "+ end[value])
    return [{
            'data':[traces[value+str(1)], traces[value+str(2)]],
            'layout':
                go.Layout(barmode='stack'),        
    },
                html.P('This account was active from: '+start[value] + " to "+ end[value]),
                html.Div(
            [html.Ul([
            html.Li(url[0]+" for "+ str(url[1]) + " times") 
            ]) for url in urls[value]])
    ]
    
    


page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)