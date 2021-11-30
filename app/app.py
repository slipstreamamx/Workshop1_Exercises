from flask import Flask, render_template
from werkzeug.wrappers import request

list_of_films = []
id = 0

filePath = r"C:\Users\asado\DevOps\Module 1\Exercises\Workshop Part 1\app\list_of_films.csv"
with open(filePath, "r", encoding='utf-8') as f:
    films = f.read()
    for film in films.splitlines():
        line_film = film.split(",")
        id += 1
        film_rating = {"id": id, "title": line_film[0], "rating": line_film[1]}
        list_of_films.append(film_rating)
   
    print(list_of_films)

message = "List of Films"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", message=message, list_of_films=list_of_films);

@app.route('/rating/<rating>')
def get_rating(rating):
    filtered_list =[]
    for list in list_of_films:
        if list["rating"] == rating:
            filtered_list.append(list)
    return render_template("index.html", message=message, list_of_films=filtered_list)


