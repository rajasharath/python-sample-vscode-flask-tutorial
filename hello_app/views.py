from datetime import datetime
from flask import Flask, render_template
from . import app
from urllib.request import urlopen
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/api/links/<url>")
def return_links(url):
    #Query the website and return the html to the variable 'page'
    page = urlopen(wiki)
    #Parse the html in the 'page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(page)
    allhrefs= soup.find_all("a")
    return render_template(
        "return_links.html",
        result=allhrefs
    )

