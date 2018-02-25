#!/usr/bin/env python3
from SuperSimpleStocks import Trade, Stock, Exchange
from datetime import datetime, timedelta
import random
import sys

SAMPLING_PERIOD = 15 # in minutes
TRADES_PER_SECOND_MAX = 5
PRICE_VARIABILITY = 0.1
QUANTITY_MAX = 1000

initial_data = [
        #(ticker, type, last_dividend, fixed_dividend, par_value)
        ('TEA', 'Common', 0, 0, 100),
        ('POP', 'Common', 8, 0, 100),
        ('ALE', 'Common', 23, 0, 60),
        ('GIN', 'Preferred', 8, 0.02, 100),
        ('JOE', 'Common', 13, 0, 250),
        ]

def initialize_exchange(exchange):
    # make exchange's sampling period same as testbench
    exchange.sampling_period = SAMPLING_PERIOD
    # load initial stock data
    for data in initial_data:
        # setting initial price based on par value
        low, high = data[4] * (1-PRICE_VARIABILITY), data[4] * (1+PRICE_VARIABILITY)
        initial_price = random.uniform(low, high)
        exchange.record_stock(Stock(data[0], initial_price, data[1],
                                data[2], data[3], data[4]))   
         
def generate_trades(stocks):
    '''Generator that yields trades from the past sampling period'''
    stock_list = list(stocks.keys())
    trades_per_second = random.randint(1, TRADES_PER_SECOND_MAX)
    trades_sampling_period = SAMPLING_PERIOD * 60 * trades_per_second
    current_time = datetime.now()
    time_decrement = timedelta(seconds=1/trades_per_second) 
    print('Generating %d trades ...' % trades_sampling_period)
    for _ in range(trades_sampling_period):
        symbol = random.choice(stock_list)
        quantity = random.randint(1, QUANTITY_MAX)
        kind = random.choice(['Buy', 'Sell'])
        current_price = stocks[symbol].price
        low, high = current_price - current_price * PRICE_VARIABILITY,\
                    current_price + current_price * PRICE_VARIABILITY
        price = random.uniform(low, high)
        current_time -= time_decrement
        yield Trade(symbol, price, quantity, kind, current_time)

def get_pe_ratio(exchange, ticker):
    return exchange.get_stocks()[ticker].compute_pe_ratio()
    
def get_dividend_yield(exchange, ticker):
    return exchange.get_stocks()[ticker].compute_dividend_yield()

def show_trades(exchange):
    '''show trades in the last sampling period'''
    for s in exchange.get_stocks().values():
        for t in s.get_trades():
            print(t)
        print()

def main():
    gbex = Exchange('Global Beverage Corporation Exchange') 
    initialize_exchange(gbex)
    print(gbex)
    SAMPLE_RUN = 2 # WARNING : use small values
    count = 0
    
    while count < SAMPLE_RUN:        
        # generate trades and record on exchange
        for t in generate_trades(gbex.get_stocks()): gbex.record_trade(t)
            
        # uncomment below line to see trades in the sampling period - WARNING : this will spew out a lot of lines
        #show_trades(gbex)
            
        # show the state of the exchange    
        print(gbex)
                
        count += 1
    
    # examples of pe ratio and dividend yield for GIN :    
    #print(get_pe_ratio(gbex, 'GIN'))
    #print(get_dividend_yield(gbex, 'GIN'))
    return 0

if __name__ == "__main__":
    sys.exit(main())