import yfinance as yf
import pandas as pd

def fetch_options_data(symbol):
    ticker = yf.Ticker(symbol)
    expirations = ticker.options

    if not expirations:
        print("No expiration dates found.")
        return None, None

    expiry = expirations[0]  # Fetch the nearest expiry
    options_chain = ticker.option_chain(expiry)

    calls = options_chain.calls[['strike', 'lastPrice', 'openInterest', 'volume']]
    puts = options_chain.puts[['strike', 'lastPrice', 'openInterest', 'volume']]

    return calls, puts

def save_to_excel(symbol, calls, puts):
    with pd.ExcelWriter(f"{symbol}_options.xlsx") as writer:
        calls.to_excel(writer, sheet_name="Call Options", index=False)
        puts.to_excel(writer, sheet_name="Put Options", index=False)
    print(f"Data saved to {symbol}_options.xlsx")

if __name__ == "__main__":
    stock_symbol = "AAPL"  # Change as needed
    calls, puts = fetch_options_data(stock_symbol)

    if calls is not None and puts is not None:
        save_to_excel(stock_symbol, calls, puts)
