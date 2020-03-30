
from flask import Flask
# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

app.run(debug=True)
