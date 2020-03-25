# Pipenv/Pipfile Understanding
## Day 1
- `pipenv install` - Similar to `npm install`. Creates 2 files `Pipfile` and `Pipfile.lock` similar to `package-lock.json` in the javascript world with dependencies based on `requirements.txt`
- `pipenv shell` - Activates the virtual environment. Much simpler than `virtualenv`
- Once the shell is activated, run `python3 hello.py` to bring the Flask app UP!!
- By default the flask app runs on 5000 port - `http://localhost:5000/hello`
- `pipenv install PyPDF2` - installs the PyPDF2 package and updates `Pipfile` and `Pipfile.lock` files.
- Once the shell is activated, run `python3 pdf_reader.py` to read the `example.pdf` file
