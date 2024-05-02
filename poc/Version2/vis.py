import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


def vis_networth(df):
	## Checking Account
	# Data
	data = []
	data.append(go.Scatter(x=df['Date'], y=df['Running_Bal'],
						mode='lines'))
	# Layout
	layout = {
		'title':{'text':'Personal Net Worth', 'x':0.5},
		'plot_bgcolor':'rgba(0,0,0,0)'
	}

	fig = go.Figure(data=data, layout=layout)

	return fig

def vis_expense(df):
	# Data
	data = []
	data.append(go.Pie(labels=df['Expense_Category'], 
						values=df[df['Amount']>0]['Amount'],
						hole=0.6))
	# Layout
	layout = {
		'title':{'text':'Monthly Expense', 'x':0.5},
		'plot_bgcolor':'rgba(0,0,0,0)'
	}

	fig = go.Figure(data=data, layout=layout)

	return fig