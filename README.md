# Dealing with legacy pipelines

1. Decide what you're willing to spend the time to move to Python, if your legacy code is in more than one language: **Everything I can**

2. Figure out your dependencies: **Python dependencies added to requirements.txt**
	 - requirements/Piplock files
	 - pipfreeze / conda list
	 - pipdeptree
	 - literally reading the code

2a. Build a Docker image and make sure your scripts still run in them: **`docker build -t spookyimage .`**

3. Analyze your crontab as a basis for Schedules
	- also consider changing your flow based on overlap in the scripts

4. Decide how you want to convert everything into Tasks: **Decorators**
	- ShellTask, bare metal
	- Shell Task + Docker agent
	- For pure Python tasks: `@task` decorators vs `Task` classes

4a. The wrapper style for experimentation: **Using this to showcase a development style**

5. Handle logging: **Prefect loggers**
	 - use logging module + Prefect loggers
	 - configure your own logging module loggers

6. Deal with your Python path!!: **Package my code with a dead simple setup.py**
	- Package your code up
	- Use Prefect configs to handle your Python path
	- Fall back on the dreaded `sys.path`
