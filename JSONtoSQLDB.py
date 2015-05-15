import json
import sqlite3
conn = sqlite3.connect('ALA.db')    #connection object
c = conn.cursor()    #cursor object

alaraFile = open('ALA.json')

alara = json.load(alaraFile)
#note the structure of alara dict:
#top layer contains dict of set details
#item card is a list containing all the cards
#each card is a dict containing card details

c.execute('''CREATE TABLE cards (
             name TEXT,
             number INTEGER PRIMARY KEY,
             cmc INTEGER,
             text TEXT,
             type TEXT)''')
             
insertables = ['name', 'number', 'cmc', 'text', 'type']

#for loop to print out individual cards
for item in alara['cards']:
    print item['name']

    name = number = cmc = text = cardtype = ' '
    name = item['name']
    number = item['number']
    if 'cmc' in item:
        cmc = item['cmc']
    if 'text' in item:
        text = item['text']
    cardtype = item['type']
    insert = (number, name, text, cardtype, cmc)
    c.execute('''INSERT INTO cards (number, name, text, type, cmc) VALUES(?, ?, ?, ?, ?);''', insert)
        
conn.commit()
conn.close()