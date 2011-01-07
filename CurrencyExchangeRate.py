# CurrencyExchangeRate
# 2011 by Alexander Teves <alexander.teves@gmail.com>
#
# How to use:
# -----------
# foo = CurrencyExchangeRate()
# print foo.get_rate('EUR', 'USD')
#
# Nice to know:
# -------------
# If you use an invalid ISO currency Code (e.g. 'YYY') 0.00 will be returned by
# Yahoo! Finance

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
