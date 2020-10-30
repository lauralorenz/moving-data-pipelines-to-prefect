from prefect import Flow, Task, task, Parameter, unmapped
from prefect.environments.storage import Docker
from prefect.triggers import always_run
import prefect

from python.manipulation import extract

@task(log_stdout=True)
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
	logger = prefect.context.get("logger")
	logger.info("Ending. Have a nice day!")

# @task
# def extract_filenames():
# 	filenames = []
# 	for i in [1,2,3]:
# 		filenames.append(extract(, i))
# 	return filenames


with Flow("shiny new flow", storage=Docker(base_image="spookyimage-shiny", local_image=True)) as f:
	db_name = Parameter('db_name', default="scary_model_storage.db")
	url = Parameter('url', default="https://next.json-generator.com/api/json/get/Vy7eluVOK")
	filenames = extract.map(unmapped(url), [1,2,3])
	flow_pieces(filenames, db_name)


## run flow and print logs
f.register(project_name="monster-project")


