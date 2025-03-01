import yfinance as yf
import pandas as pd

def get_option_data(stock):
    ticker = yf.Ticker(stock)
    expirations = ticker.options

    if not expirations:
        print("No expiration dates found.")
        return None, None

    expiry = expirations[0]  # Get the nearest expiry date
    options_chain = ticker.option_chain(expiry)

    ce_data = options_chain.calls[['strike', 'lastPrice', 'openInterest', 'volume']]
    pe_data = options_chain.puts[['strike', 'lastPrice', 'openInterest', 'volume']]

    return ce_data, pe_data
