import os
import json
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from boa_docs import *
from vis import *



# Import data
os.chdir('..')
with open('poc_arguements.json') as f:
	arg = json.load(f)

df_chkacct = read_boacsv(arg['boa_chk'][0])
df_cc = read_boacsv(arg['boa_cc'][0])

## Checking Expense
fig_chk = vis_networth(df_chkacct)

## Credit Expense
fig_cc = vis_expense(df_cc)

## All Expense
# Data
df_chkacct_temp = df_chkacct
df_chkacct_temp['Amount'] = df_chkacct_temp['Amount']*-1
df_all = pd.concat([df_chkacct_temp, df_cc], ignore_index=True)
df_all = df_all[df_all['Amount']>0]
fig_all = vis_expense(df_all)


# Dash Set up
app = dash.Dash()
app.layout = html.Div([
		dcc.Tabs(id='dashboard-tabs',value='net_worth',children=[
				dcc.Tab(label='Net Worth',value='net_worth',children=[
						html.Div(dcc.Graph(figure=fig_chk))
					]),
				dcc.Tab(label='Credit Card Expense',value='cc_expense',
					children=[
						html.Div(dcc.Graph(figure=fig_cc))
					]),
				dcc.Tab(label='All Expense',value='all_expense',children=[
						html.Div(dcc.Graph(figure=fig_all))
					])
			]
		)
	])

os.chdir('Version2')
if __name__ == '__main__':
    app.run_server(debug=True, port=8888)
