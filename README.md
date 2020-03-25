# Pipenv/Pipfile Understanding
## Day 1
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