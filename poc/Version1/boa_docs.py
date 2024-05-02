import pandas as pd

def read_boacsv(filename):
	df = pd.read_csv(filename, thousands=',')
	return df