import sys
import os

from manipulation import transform_features, save_to_db
from machine_learning import its_a_linear_regression

input_file = os.path.abspath(sys.argv[1])
output_file = input_file.replace(".json",".joblib")
df = transform_features(sys.argv[1])
its_a_linear_regression(df, output_file)
DBNAME = os.environ["DB_NAME"]
save_to_db(DBNAME, output_file)