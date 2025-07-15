import yfinance as yf
import time
import pandas as pd

TICKERS = ['AAPL', 'MSFT', 'GOOG', 'TSLA']

def fetch_prices():
    prices = {}
    for ticker in TICKERS:
        ticker_obj = yf.Ticker(ticker)
        data = ticker_obj.history(period="1d", interval="1m")
        latest = data.tail(1)
        if not latest.empty:
            prices[ticker] = {
                'timestamp': latest.index[0],
                'price': latest['Close'].values[0],
                'volume': latest['Volume'].values[0]
            }
    return prices

if __name__ == "__main__":
    while True:
        data = fetch_prices()
        df = pd.DataFrame.from_dict(data, orient='index')
        df.to_csv("data/latest_prices.csv", mode='a', header=False)
        print(df)
        time.sleep(5)
