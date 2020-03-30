# Playground repo for Python projects
This repo has multiple branches and each branch represent different projects/proof of concepts for playing with Python technologies/frameworks.

_P.S. `master` branch is empty and has only this `README.md` file_

## Table of Contents
- [Status Updates](#status-updates)
    - [Day 1](#day-1)
    - [Day 2](#day-2)
    - [Day 3](#day-3)
    - [Day 4](#day-4)
    - [Day 5](#day-5)
    - [Day 6](#day-6)
- [Installation](#installation)
- [Resources](#resources)

## Status Updates
From March 25th, 2020
### Day 1
- `pipenv install` - Similar to `npm install`. Creates 2 files `Pipfile` and `Pipfile.lock` similar to `package-lock.json` in the javascript world with dependencies based on `requirements.txt`
- `pipenv shell` - Activates the virtual environment. Much simpler than `virtualenv`
- Once the shell is activated, run `python3 hello.py` to bring the Flask app UP!!
- By default the flask app runs on 5000 port - `http://localhost:5000/hello`
- `pipenv install PyPDF2` - installs the PyPDF2 package and updates `Pipfile` and `Pipfile.lock` files.
- Once the shell is activated, run `python3 pdf_reader.py` to read the `example.pdf` file
- `basics.py` - file which includes all basic syntaxes in python
- `modules.py` 
    - python searches the list of directories from `sys.path`. Use `sys.path.append(directory_path)` to add directory searches during import.
  ```python
    python3          
    Python 3.7.5 (default, Nov  1 2019, 02:16:32) 
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> sys.path
    ['', '/usr/local/Cellar/python/3.7.5/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/usr/local/Cellar/python/3.7.5/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/usr/local/Cellar/python/3.7.5/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/usr/local/lib/python3.7/site-packages']
  ```
    - Alternatively use `PYTHONPATH` to set the package/module import paths.
    - If a package has `__init__.py`, it becomes a module
    - `learn` is a module which is used in `modules.py`

### Day 2
  - Started using callable functions inside a class

### Day 3
  - Started using Functions and String manipulation

### Day 4
  - Started using `tuples`

### Day 5
  - Started using `dictionaries`
  - Started using `set`

### Day 6


## Installation
Command used in Mac for installing supporting tools
- Python3 - `brew install python3`
- Pipenv - `brew install pipenv`

## Resources
- [Introducing Python - Oreilly](https://learning.oreilly.com/library/view/introducing-python-2nd) - Most exhaustive and amazing book..!
