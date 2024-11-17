'''
__main__.py file is used to provide a command-line interface for a package. 

Consider the following hypothetical package, “bandclass”:
bandclass
  ├── __init__.py
  ├── __main__.py
  └── student.py

__main__.py will be executed when the package itself is invoked directly from the command line using the -m flag. For example:
python -m bandclass
This command will cause __main__.py to run.

We could also import __main__ module from other modules
'''