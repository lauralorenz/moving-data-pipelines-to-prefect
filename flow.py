from prefect import Flow, Task, task, Parameter
from prefect.environments.storage import Docker
from prefect.triggers import always_run

@task
def flow_pieces(db_name):
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
		save_to_db(db_name, output_file)

with Flow("shiny new flow", storage=Docker(base_image="spookyimage-shiny", local_image=True)) as f:
	db_name = Parameter('db_name', default="scary_model_storage.db")
	flow_pieces(db_name)


## run flow and print logs
f.register(project_name="monster-project")


