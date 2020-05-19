import time, sys
from TradeAlgorithm import TradeAlgorithm
from Sma import Sma


def main():
    an_hour = 3600                                              # an hour in seconds forcode readablility
    algo = Sma(bought=False, previous_periods=[9894.985, 9876.705, 9802.19], logfile_path="logs/btc_trade_driver.log") 
    while True:
        algo.run()  
        time.sleep(3600) 


if __name__ == "__main__": 
    main()
