from os import system
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

with app.app_context():
    system('tailwindcss -i templates/style.css -o templates/output.css')

@app.route("/")
def index():
    return render_template("index.html.jinja")

@app.post("/join_game")
def join_game():
    username = request.form['username']
    
    return render_template("join-game.html.jinja", name=username)
