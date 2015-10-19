from flask import Flask,request
import os
import sqlite3
import urllib2
import json

os.chdir('/home/mayuresh/Desktop/stockapi/stocks')
app = Flask(__name__)

@app.route('/')
def home():
	return ""

@app.route('/update')
def update():
	conn = sqlite3.connect('Stocks.db')
	cursor = conn.cursor()
	update_cursor = conn.cursor()
	get_stocks = 'SELECT stockname,stockexchange,stockvalue FROM stock'
	stocks = cursor.execute(get_stocks)
	stock_list = [[row[0],row[1],row[2]] for row in cursor.fetchall()]
	x = len(stock_list)
	if x>0:
		for row in stock_list:
			url = "http://rocode.pythonanywhere.com/quote?sto="+row[0]+"&exc="+row[1]
			price = urllib2.urlopen(url)
			diff = row[2]-price
			update = "UPDATE stock SET stockvalue=?,stockdiff=? WHERE stockname=?"
			update_cursor.execute(update,(price,diff,row[0]))

	return str(x)

if __name__=='__main__':
	app.run(port=8014)
