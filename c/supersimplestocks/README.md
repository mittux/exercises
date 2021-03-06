### Running the simulation

Python 3 is required.

Required files:  
`SuperSimpleStocks/__init__.py`  
`SuperSimpleStocks/SuperSimpleStocks.py`  
`DemoSuperSimpleStocks.py`  
`TestSuperSimpleStocks.py`  

To run demo:  
`$ python DemoSuperSimpleStocks.py`

#### Sample Demo Output

        Global Beverage Corporation Exchange - 103.484  
        "GIN" Preferred price=  99.08p dividend_yield= 0.0202 p/e=12.3854  
        "JOE" Common    price= 251.48p dividend_yield= 0.0517 p/e=19.3446  
        "ALE" Common    price=  56.46p dividend_yield= 0.4074 p/e= 2.4546  
        "TEA" Common    price=  92.39p dividend_yield= 0.0000 p/e= 0.0000  
        "POP" Common    price=  91.31p dividend_yield= 0.0876 p/e=11.4135  
        Generating 2700 trades ...  
        Global Beverage Corporation Exchange - 103.449  
        "GIN" Preferred price=  98.85p dividend_yield= 0.0202 p/e=12.3562  
        "JOE" Common    price= 251.78p dividend_yield= 0.0516 p/e=19.3675  
        "ALE" Common    price=  56.33p dividend_yield= 0.4083 p/e= 2.4492  
        "TEA" Common    price=  92.44p dividend_yield= 0.0000 p/e= 0.0000  
        "POP" Common    price=  91.41p dividend_yield= 0.0875 p/e=11.4263

To run unit test:  
`$ python TestSuperSimpleStocks.py -v`

Tested using Python 3.5.4 on Ubuntu Linux 17.04


### Assumptions

* Formulae used as given in the problem statement

* Initial stock price dervied from par value (even though in reality stock price has no bearing on its par value)

* 0.0 is returned for P/E if the stock's dividend is zero


### Notes


* The class Trade implements comparison dunder functions so that it can be sorted

* The class Stock's price is implemented as a property so that it is recomputed whenever it is read; alternatively the price could be recomputed while recording trades
