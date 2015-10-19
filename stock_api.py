import os
import urllib2
from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/')
def hello():
	return "Stock Prices on Demand"


@app.route('/quote')
def quote():
	sto = request.args.get('sto').encode('ascii','ignore')
	exc = request.args.get('exc').encode('ascii','ignore')
	#sto = "SUNPHARMA"
	#exc = "NSE"
	url="http://finance.google.com/finance/info?client=ig&q="+exc+":"+sto
	#return 'hello'
	html = urllib2.urlopen(url)
	try:
		html = urllib2.urlopen(url)
		html = html.read()
		html = html[3:]
		#html = json.loads(html)
		return html
	except:
		return "nope"


if __name__=='__main__':
	app.run(port=8012)
	#http://localhost:8012/quote?sto=SUNPHARMA&exc=NSE
