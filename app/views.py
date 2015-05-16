__author__ = 'Derial'

from app import app
from flask import render_template, session, request, redirect, url_for
from .forms import SecurityForm
import sqlite3

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    conn = sqlite3.connect('ALA.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cards;')
    cardList = c.fetchall()
    nameList = []
    for card in cardList:
        nameList.append(card[0])
    conn.close()
    return render_template('searchPage.html', nameList=nameList)

@app.route('/results', methods=['GET', 'POST'])
def search_results():
    cardName = request.form['CardName']
    conn = sqlite3.connect('ALA.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cards WHERE name=?;', [cardName,])
    cards = c.fetchall()
    conn.close()
    if cards:
        return render_template('resultsPage.html', cards=cards)
    else:
        return 'Card not found!'

@app.route('/card/<card_name>')
def card_page(card_name):
    conn = sqlite3.connect('ALA.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cards WHERE name=?;', [card_name,])
    cards = c.fetchall()
    conn.close()
    if cards:
        return render_template('resultsPage.html', cards=cards)
    else:
        return 'Card not found!'
