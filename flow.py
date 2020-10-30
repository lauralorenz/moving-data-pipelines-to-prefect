from prefect import Flow, Task, task
from prefect.environments.storage import Docker
from prefect.triggers import always_run

@task
def flow_pieces():
	import python.do_all_the_machine_learning

with Flow("shiny new flow", storage=Docker(base_image="spookyimage-shiny", local_image=True)) as f:
	flow_pieces()


## run flow and print logs
f.register(project_name="monster-project")


