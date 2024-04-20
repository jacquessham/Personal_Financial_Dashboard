import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Import data
df_chkacct = pd.read_csv('boa_chk_example.csv')

# Data
data = []
data.append(go.Scatter(x=df_chkacct['Date'], y=df_chkacct['Running_Bal'],
					mode='lines'))
# Layout
layout = {'title':{'text':'Number of Customer Trend', 'x':0.5}}

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='chk_balance_viz.html')