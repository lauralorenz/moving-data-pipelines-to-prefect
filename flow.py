from prefect import Flow, Task, task, Parameter
from prefect.environments.storage import Docker
from prefect.triggers import always_run

@task
def flow_pieces(filenames, db_name):
	import sys
	import os

	from python.manipulation import transform_features, save_to_db
	from python.machine_learning import its_a_linear_regression

	for filename in filenames:
		input_file = os.path.abspath(filename)
		output_file = input_file.replace(".json",".joblib")
		df = transform_features(filename)
		its_a_linear_regression(df, output_file)
		save_to_db(db_name, output_file)

@task
def extract_filenames():
	from python.manipulation import extract
	filenames = []
	for i in [1,2,3]:
		filenames.append(extract("https://next.json-generator.com/api/json/get/Vy7eluVOK", i))
	return filenames


with Flow("shiny new flow", storage=Docker(base_image="spookyimage-shiny", local_image=True)) as f:
	db_name = Parameter('db_name', default="scary_model_storage.db")
	filenames = extract_filenames()
	flow_pieces(filenames, db_name)


## run flow and print logs
f.register(project_name="monster-project")


