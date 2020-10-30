import pandas as pd
import sqlite3

def transform_features(filename):
	df = pd.read_json(filename)
	def _age(row):
		lookup = {'days': 365, 'months': 12, 'years': 1}
		return row['age'] / lookup[row['ageUnit']]

	df['Normalized Age'] = df.apply(lambda row: _age(row), axis=1)
	df['Normalized Balance'] = df['balance'].str.replace(',', '').str.replace('$', '')
	df['Normalized Balance'] = df['Normalized Balance'].astype(float)
	return df[['Normalized Age', 'Normalized Balance']]


# 
# create table models(id integer primary key autoincrement, name varchar(255) not null, model blob not null);
def save_to_db(database, filename):
	with open(filename, "rb") as f:
		model_bytes = f.read()
		model_name = filename.replace(".json", '')
		conn = sqlite3.connect(database)
		c = conn.cursor()
		c.execute(f"INSERT INTO models (name, model) VALUES (\"{model_name}\", \"{model_bytes}\")")
		conn.commit()
		conn.close()

