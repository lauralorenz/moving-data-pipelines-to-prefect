# Dealing with legacy pipelines

1. Decide what you're willing to spend the time to move to Python, if your legacy code is in more than one language

2. Figure out your dependencies
	 - requirements/Piplock files
	 - pipfreeze / conda list
	 - pipdeptree
	 - literally reading the code

2a. Build a Docker image and make sure your scripts still run in them

3. Analyze your crontab as a basis for Schedules
    - also consider changing your flow based on overlap in the scripts

4. Decide how you want to convert everything into Tasks
	- ShellTask, bare metal
	- Shell Task + Docker agent
	- For pure Python tasks: `@task` decorators vs `Task` classes

4a. The wrapper style for experimentation

5. Handle logging
	 - use logging module + Prefect loggers
	 - configure your own logging module loggers

6. Deal with your Python path!!
	 - Package your code up
	 - Use Prefect configs to handle your Python path
	 - Fall back on the dreaded `sys.path`