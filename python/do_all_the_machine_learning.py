import sys
import os

from python.manipulation import transform_features, save_to_db, extract
from python.machine_learning import its_a_linear_regression


filenames = []
for i in [1,2,3]:
	filenames.append(extract("https://next.json-generator.com/api/json/get/Vy7eluVOK", i))

for filename in filenames:
	input_file = os.path.abspath(filename)
	output_file = input_file.replace(".json",".joblib")
	df = transform_features(filename)
	its_a_linear_regression(df, output_file)
	DBNAME = os.environ["DB_NAME"]
	save_to_db(DBNAME, output_file)