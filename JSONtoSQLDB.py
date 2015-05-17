import json
import sqlite3

conn = sqlite3.connect('ALA.db')  # connection object
c = conn.cursor()  # cursor object

alaraFile = open('ALA.json')

alara = json.load(alaraFile)
# note the structure of alara dict:
# top layer contains dict of set details
# item card is a list containing all the cards
# each card is a dict containing card details

c.execute('''DROP TABLE IF EXISTS cards;''')
c.execute('''CREATE TABLE cards (
             type TEXT,
             colors TEXT,
             name TEXT,
             cmc INTEGER,
             rarity TEXT,
             manaCost TEXT,
             text TEXT,
             number INTEGER PRIMARY KEY,
             imageName TEXT);''')

# insertables = ['type', 'colors', 'name', 'cmc', 'rarity', 'manaCost', 'text', 'number', 'imageName']

# for loop to print out individual cards
for item in alara['cards']:
    print item['name']
    cmc = 0
    text = colors = manaCost = ''

    cardtype = item['type']
    if 'colors' in item:
        for color in item['colors']:
            colors = colors + color + ' '
    name = item['name']
    if 'cmc' in item:
        cmc = item['cmc']
    rarity = item['rarity']
    if 'manaCost' in item:
        manaCost = item['manaCost']
    if 'text' in item:
        text = item['text']
    number = item['number']
    imageName = item['imageName']

# insertables = ['type', 'colors', 'name', 'cmc', 'rarity', 'manaCost', 'text', 'number', 'imageName']
    insert = (cardtype, colors, name, cmc, rarity, manaCost, text, number, imageName)
    c.execute('''INSERT INTO cards (type, colors, name, cmc, rarity, manaCost, text, number, imageName)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);''', insert)

conn.commit()
conn.close()