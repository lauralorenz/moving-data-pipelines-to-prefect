# About this Repo

This repo comes with multiple branches showcasing different techniques for moving a legacy pipeline like the one shown in the `main` branch. Each branch addresses the individual issues listed in the **"Dealing with legacy pipelines"** heading below in a different way; each branch's `README.md` is updated with annotations describing the approach given per bullet point.

The branches are designed for the commits to be walk-through-able, with commit messages that explain what step of the migration process is occurring. You can:

1. view each commit in order in the Github "commits" or "files" tab
2. checkout the repo locally and walk through a branch's commits with `git checkout {branch}; git rebase -i {starting hash}` (change each interactive rebase step changed from `pick` to `reword`/`edit` so you can progress through each commit yourself)

### The example branches

- For a no-fuss, change-as-little-as-possible approach, check out the version in https://github.com/lauralorenz/moving-data-pipelines-to-prefect/tree/dockerpipeline 
	- starting hash: `7a0930b36457b7e7f83b02bcbb1bafc09e8d7435`
- For a technique that uses more Prefect internals at the expense of a bit more work, check out the version in https://github.com/lauralorenz/moving-data-pipelines-to-prefect/tree/more-flowy
	- starting hash: ` e13bb93ddadb113c007614471927e044df099e15`

Watch a video tutorial walking through the above two examples using the rebase technique at: https://www.youtube.com/watch?v=kH3hPVwFfiA

--------

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