#Poloniex Data Gathering

##Overview

This script `process_trades.py` gathers the following statistics on every coin in Poloniex's [coin list](https://poloniex.com/public?command=returnTicker) from the beginning of 2016 to the beginning of 2017:

1. Highest rate
2. Lowest rate
3. Rate of last trade
4. Total volume traded
5. Number of trades
6. Highest trade
7. Lowest trade
8. Last trade

To configure the date range for the given statistics listed above, change the unix timestamps `beginningOf2016` and `beginningOf2017` variables.
