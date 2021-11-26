from flask import Flask, render_template

films = ["Flubber", "Jumanji", "Aladdin"]
message = "List of Films"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", message=message, films=films);


print(films)