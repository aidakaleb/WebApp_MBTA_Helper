"""
Simple "Hello, World" application using Flask
"""
from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from devan import find

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def location():
    if request.method == 'POST':
        location = request.form["location"]

        stop, wheelchair_boarding, rating = find(location)

        return render_template("result.html",
                        stop=stop,
                        wheelchair= wheelchair_boarding,
                               rating=rating)

    if request.method == 'GET':
        return render_template("index.html")
