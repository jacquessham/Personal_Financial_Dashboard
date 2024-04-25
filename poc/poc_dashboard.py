import json
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *
from boa_docs import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
with open('poc_arguements.json') as f:
	arg = json.load(f)

df_chkacct = read_boacsv(arg['boa_chk'][0])


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
