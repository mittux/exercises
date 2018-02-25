from datetime import datetime, timedelta
from functools import reduce
from operator import mul
import math

RUNTIME_OPTIMIZE = True

class Trade:
    def __init__(self, ticker, price, quantity, type, timestamp):
        self.ticker = ticker
        self.price = price
        self.quantity = quantity
        self.trade_type = type.title() # Buy or Sell
        self.timestamp = timestamp

    def __str__(self):
        return '{}: {} "{}" x{} @{:.2f}p'.format(self.timestamp, self.trade_type,
                                              self.ticker, self.quantity, self.price)

    def __gt__(self, other):
        return self.timestamp > other.timestamp
    
    def __lt__(self, other):
        return self.timestamp < other.timestamp
    
    def __eq__(self, other):
        return self.timestamp == other.timestamp
    
    def __ge__(self, other):
        return self.timestamp >= other.timestamp
    
    def __le__(self, other):
        return self.timestamp <= other.timestamp


class Stock:
    def __init__(self, ticker, initial_price, type, last_dividend, fixed_dividend, par_value, period=5):
        self.ticker = ticker
        self._price = float(initial_price)
        self.stock_type = type.title() # Common or Preferred
        self.last_dividend = last_dividend
        self.fixed_dividend = float(fixed_dividend)
        self.par_value = par_value
        self._trades = []
        self._sampling_period = period
        
    @property
    def price(self):
        '''Compute price every time it is accessed'''
        self.compute_stock_price()
        return self._price
    
    def record_trade(self, trade):
        self._trades.append(trade)

    def compute_stock_price(self):
        if len(list(self.get_trades())) > 0:
            total_quantity, total_value = 0, 0
            for t in self.get_trades():
                total_quantity += t.quantity
                total_value += t.price * t.quantity
            self._price =  total_value / total_quantity
            return self._price

    def compute_dividend_yield(self):
        if self.stock_type == 'Preferred':
            return (self.par_value * self.fixed_dividend) / self.price
        return self.last_dividend / self.price

    def compute_pe_ratio(self):
        if self.last_dividend > 0:
            return self.price / self.last_dividend
        return 0.0

    def __str__(self):
        return '"{:>3}" {:9} price={:>7.2f}p dividend_yield={:>7.4f} p/e={:>7.4f}'.\
                format(self.ticker, self.stock_type, self.price,
                       self.compute_dividend_yield(), self.compute_pe_ratio())
                
    def get_trades(self):
        '''Sort the trades and return only trades from the last sampling period'''
        self._trades = sorted(self._trades, reverse=True)
        cutoff_time = datetime.now() - timedelta(minutes=self._sampling_period)
        trim = None
        for i,t in enumerate(self._trades):
            if t.timestamp > cutoff_time:
                yield t
            else:
                trim = i
                break
        if RUNTIME_OPTIMIZE and trim is not None:
            # discard items older than the sampling period
            self._trades = self._trades[:trim] 
            

class Exchange:
    
    sampling_period = 5 # default in minutes; can be overridden
    
    def __init__(self, name):
        self.name = name
        self._stocks = {}
        
    def record_stock(self, stock):
        try:
            # override the stock sampling period with the exchange's sampling period
            stock._sampling_period = self.sampling_period
            self._stocks[stock.ticker] = stock
        except KeyError:
            print('%s not found!' % stock.ticker)
            
    def record_trade(self, trade):
        try:
            self._stocks[trade.ticker].record_trade(trade)
        except KeyError:
            print('%s not found!' % trade.ticker)

    def compute_index(self):
        if len(self._stocks) == 0: return
        return math.pow(reduce(mul, (s.price for s in self._stocks.values())), 1/len(self._stocks))

    def __str__(self):
        stocks = '\n'.join((str(s) for s in self._stocks.values()))
        name_index = '{} - {:.3f}'.format(self.name, self.compute_index())
        return '\n'.join((name_index, stocks))
    
    def get_stocks(self):
        return self._stocks

