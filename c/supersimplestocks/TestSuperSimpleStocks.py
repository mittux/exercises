#!/usr/bin/env python3
import unittest
from SuperSimpleStocks import Trade, Stock, Exchange

test_data = [
        #(ticker, type, last_dividend, fixed_dividend, par_value)
        ('TEA', 'Common', 0, 0, 100),
        ('POP', 'Common', 8, 0, 100),
        ('ALE', 'Common', 23, 0, 60),
        ('GIN', 'Preferred', 8, 0.02, 100),
        ('JOE', 'Common', 13, 0, 250),
        ]

def initialize_exchange(exchange):
    for data in test_data:
        initial_price = 100
        exchange.record_stock(Stock(data[0], initial_price, data[1],
                                data[2], data[3], data[4])) 
        
def get_pe_ratio(exchange, ticker):
    return exchange.get_stocks()[ticker].compute_pe_ratio()
    
def get_dividend_yield(exchange, ticker):
    return exchange.get_stocks()[ticker].compute_dividend_yield()

        
class TestSuperSimpleStocks(unittest.TestCase):
    '''Basic tests'''
    
    myex = Exchange('My Exchange')
    
    def setUp(self):
        initialize_exchange(self.myex)
    
    def test_exchange_index(self):
        index = "{0:.2f}".format(self.myex.compute_index())
        self.assertEqual(index, '100.00')
        
    def test_preferred_dividend_yield(self):
        div_yld = get_dividend_yield(self.myex, 'GIN')
        self.assertEqual(div_yld, 0.02)
    
    def test_common_dividend_yield(self):
        div_yld = get_dividend_yield(self.myex, 'ALE')
        self.assertEqual(div_yld, 0.23)
        
    def test_zero_dividend_yield(self):
        div_yld = get_dividend_yield(self.myex, 'TEA')
        self.assertEqual(div_yld, 0.0)
        
    def test_pe_ratio(self):
        pe = get_pe_ratio(self.myex, 'POP')
        self.assertEqual(pe, 12.5)
        
    def test_pe_ratio_zero_dividend(self):
        pe = get_pe_ratio(self.myex, 'TEA')
        self.assertEqual(pe, 0.0)
        

if __name__ == '__main__':
    unittest.main(verbosity=1)