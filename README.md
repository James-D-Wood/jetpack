# Jetpack - A CLI for the Tedious Things

## Project Structure
```
.
├── jetpack/                # src
|   ├── commands/           # Command specific modules 
|   ├── __init__.py         # TODO: properly initialize this module
|   ├── __main__.py         # TODO: is there a better way?
|   └── cli.py              # Main control flow for CLI app
|
├── tests/                  # Unit tests
|
├── makefile                # Build instructions for executable     
└── README.md               # You are HERE 
```

## Handling Dependencies / Setting up the Development Environment
Pipenv makes package and virtual environment management as easy as 1-2-3.

1. Install pipenv (homebrew is an easy way to do this if you're running on Mac or Linux) https://github.com/pypa/pipenv
2. Install dependencies declared in Pipfile (run each time the Pipfile is updated) `pipenv install`
3. Initiate the environment `pipenv shell`

From here you are ready to run the program in development.

## Running the Code in Development
Run the main module like this: TODO - more verbose instructions
```
python -m jetpack --help         # lists all available commands
``` 

## Unit Testing 
After intalling pytest you can run `pytest` and unit tests in files prefixed with "test_" will run.

## Generating an Executable
We can use setuptools to package our python module into an executable. `setup.py` defines the rules for generating our executable and the `Makefile` contains the build instructions required that will be called by the test server. After running `make` the command `jetpack ...` can be run. More info on this: https://click.palletsprojects.com/en/7.x/setuptools/