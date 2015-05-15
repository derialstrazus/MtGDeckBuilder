__author__ = 'Derial'

from app import app
from flask import render_template, session, request, redirect, url_for
from .forms import SecurityForm
import sqlite3

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('searchPage.html')

@app.route('/results', methods=['GET', 'POST'])
def search_results():
    cardName = request.form['CardName']
    conn = sqlite3.connect('ALA.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cards WHERE name=?;', [cardName,])
    card = c.fetchall()
    if card:
        return 'You found %s!' % card[0][0]
    else:
        return 'Card not found!'