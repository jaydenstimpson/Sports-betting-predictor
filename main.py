import requests
from bs4 import BeautifulSoup
from flask import Flask


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
app = Flask(__name__)

@app.route("/")
def hello_world():
    url = "https://www.vegasinsider.com/college-football/matchups/georgia-tech-vs-north-carolina/"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    print(soup.prettify())
    return f"<p>{soup.prettify()}</p>"