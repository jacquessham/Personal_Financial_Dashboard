import os
import json
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *
from boa_docs import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
os.chdir('..')
with open('poc_arguements.json') as f:
	arg = json.load(f)

df_chkacct = read_boacsv(arg['boa_chk'][0])
df_cc = read_boacsv(arg['boa_cc'][0])

## Checking Account
# Data
data = []
data.append(go.Scatter(x=df_chkacct['Date'], y=df_chkacct['Running_Bal'],
					mode='lines'))
# Layout
layout = {
	'title':{'text':'Personal Net Worth', 'x':0.5},
	'plot_bgcolor':'rgba(0,0,0,0)'
}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='chk_balance_viz.html')

## Credit Expense
# Data
data = []
data.append(go.Pie(labels=df_cc['Expense_Category'], 
					values=df_cc[df_cc['Amount']>0]['Amount'],
					hole=0.6))
# Layout
layout = {
	'title':{'text':'Monthly Expense', 'x':0.5},
	'plot_bgcolor':'rgba(0,0,0,0)'
}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='chk_cc_viz.html')


## All Expense
# Data
df_chkacct_temp = df_chkacct
df_chkacct_temp['Amount'] = df_chkacct_temp['Amount']*-1
df_all = pd.concat([df_chkacct_temp, df_cc], ignore_index=True)
df_all = df_all[df_all['Amount']>0]
data = []
data.append(go.Pie(labels=df_all['Expense_Category'], 
					values=df_all['Amount'],
					hole=0.6))
# Layout
layout = {
	'title':{'text':'Monthly Expense', 'x':0.5},
	'plot_bgcolor':'rgba(0,0,0,0)'
}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='chk_allexpense_viz.html')
