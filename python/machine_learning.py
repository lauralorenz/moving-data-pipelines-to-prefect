import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump

def its_a_linear_regression(df, filename):
	X = df[['Normalized Age']].values.reshape(-1, 1)
	y = df['Normalized Balance']
	reg = LinearRegression().fit(X, y)
	dump(reg, filename)
	