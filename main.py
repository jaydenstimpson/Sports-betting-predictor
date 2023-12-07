import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


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
    url = "https://www.vegasinsider.com/nfl/matchups/bills-vs-cowboys/"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    print(soup)
    moneylinetable = soup.find(id="odds-table-moneyline--0")
    moneylines = moneylinetable.find_all("td", class_="game-odds")
    lines = soup.find_all("span", class_="data-value")
    cowboysspread = lines[:5]
    billsspread = lines[5:10]
    cowboystotal = lines[10:15]
    billstotal = lines[15:20]
    cowboysml = moneylines[:5]
    billsml = moneylines[6:11]
    print(moneylines)
    # del lines[4]
    # del lines[8]
    logo = soup.find_all("div", class_="book-icn")
    logo = logo[:5]
    reallines = []
    for l in logo:
        icon = l.contents[1]['src']
        line = Line(icon, '-3', '-100', '4', '10')
        reallines.append(line)
    for i in range(len(cowboysspread)):
        if i < len(reallines):
            reallines[i].spread = 'Cowboys Spread: ' + cowboysspread[i].contents[0]
    for i in range(len(cowboysml)):
        # print(cowboysml[i])
        if i < len(reallines):
            gameodds = cowboysml[i].find("span", class_=["data-value", "data-moneyline"])
            reallines[i].ml = 'Cowboys Moneyline: ' + gameodds.contents[0]
    for i in range(len(billsspread)):
        if i < len(reallines):
            reallines[i].team2spread = 'Bills Spread: ' + billsspread[i].contents[0]
    for i in range(len(billsml)):
        print(billsml[i])
        gameodds = billsml[i].find("span", class_=["data-value", "data-moneyline"])
        if i < len(reallines):
            reallines[i].team2ml = 'Bills Moneyline: ' + gameodds.contents[0]
        pass
    # prizepicks = Line('PrizePicks', '-3', '-110')
    # fanduel = Line('Fanduel', '-3.5', '-110')
    # draftkings = Line('DraftKings', '-4', '-100')
    # fakelines = [prizepicks, fanduel, draftkings]
    return render_template('main.html', lines = reallines)


class Line:
    def __init__(self, book, spread, ml, team2spread, team2ml):
        self.book = book
        self.spread = spread
        self.ml = ml
        self.team2spread = team2spread
        self.team2ml = team2ml
