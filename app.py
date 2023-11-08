#!/usr/bin/env python3

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def landing_page():
    return render_template('index.html')

@app.route("/about.html")
def about_page():
    return render_template('about.html')

@app.route("/service.html")
def service_page():
    return render_template('service.html')

@app.route("/team.html")
def team_page():
    return render_template('team.html')

@app.route("/why.html")
def why_page():
    return render_template('why.html')
