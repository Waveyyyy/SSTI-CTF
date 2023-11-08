#!/usr/bin/env python3

from flask import Flask, render_template, render_template_string, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def landing_page():
    data = None
    if request.method == 'GET':
        if request.args.get('q'):
            data = render_template_string(request.args.get('q'))
    return render_template('index.html', data=data)

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
