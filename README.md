CurrencyExchangeRate
--------------------
2011 by Alexander Teves <alexander.teves@gmail.com>

How to use:
-----------
    from CurrencyExchangeRate import CurrencyExchangeRate
    foo = CurrencyExchangeRate()
    print foo.get_rate('EUR', 'USD')

Nice to know:
-------------
* If you use an invalid ISO currency Code (e.g. 'USB'), 0.00 will be returned by
  Yahoo! Finance
* For any other error (e.g. network), the result will be -1.00
