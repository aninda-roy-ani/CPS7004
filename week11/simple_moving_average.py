import pandas as pd
import requests


# Function to fetch historical data from CoinGecko
def fetch_historical_data(crypto_id, days):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart'
    params = {
        'vs_currency': 'gbp',
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
window = 3
sma_data = calculate_sma(historical_data, window)

# Display the data
print(sma_data)

