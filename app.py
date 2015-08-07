import urllib2

stock = "SUNPHARMA"
exchange = "NSE"

x="http://finance.google.com/finance/info?client=ig&q="+exchange+"%3a"+stock

html = urllib2.urlopen(x).read()

html = html[3:]
print html
