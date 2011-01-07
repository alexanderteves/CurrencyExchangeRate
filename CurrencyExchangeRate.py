import urllib2
from decimal import Decimal

class CurrencyExchangeRate():

	def get_rate(self, a, b):
		try:
			url = 'http://finance.yahoo.com/d/quotes.csv?s=%s%s=X&f=l1' % (a, b)
			rate = urllib2.urlopen(url).read().rstrip()
			return Decimal(rate)
		except Exception, e:
			print e
			return 0.00
