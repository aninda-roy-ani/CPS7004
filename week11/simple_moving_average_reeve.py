import pandas as pd
import requests
import datetime
import matplotlib.pyplot as plt

# Function to fetch historical data from CoinGecko
def fetch_historical_data(crypto_id, days):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': days,
        'interval': 'daily'
    }
    response = requests.get(url, params=params)
    data = response.json()

    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Function to calculate the Simple Moving Average
def calculate_sma(data, window):
    data['SMA'] = data['price'].rolling(window=window).mean()
    return data

# Fetch historical data for Bitcoin for the past 30 days
crypto_id = 'bitcoin'
days = 30
historical_data = fetch_historical_data(crypto_id, days)

# Calculate the 7-day Simple Moving Average
window = 7
sma_data = calculate_sma(historical_data, window)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(sma_data['timestamp'], sma_data['price'], label='Price')
plt.plot(sma_data['timestamp'], sma_data['SMA'], label=f'{window}-Day SMA', linestyle='--')
plt.title(f'Bitcoin Price and {window}-Day Simple Moving Average')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()