import time
import pandas as pd
import requests
import streamlit as st
# CryptoCompare API endpoints
api_url = "https://min-api.cryptocompare.com/data/"
hist_url = api_url + "histoday"
# Streamlit setup
st.title("CBasic Crypto Trading Bot")
st.sidebar.title("Settings")

# User-defined settings
initial_balance = st.sidebar.number_input("Initial Balance (USDT)", min_value=1, value=100)
trade = st.sidebar.text_input("Trading Pair (e.g., BTC/USDT)", value="BTC")
short_window = st.sidebar.number_input("Short Window (days)", min_value=1, value=50)
long_window = st.sidebar.number_input("Long Window (days)", min_value=1, value=200)
st.sidebar.write(f"Initial Balance: {initial_balance} USDT")
st.sidebar.write(f"Trading Pair: {trade}")
st.sidebar.write(f"Short Window: {short_window} days")
st.sidebar.write(f"Long Window: {long_window} days")
def fetch_data(pair, limit):
    params = {
        "fsym": pair.split("/")[0],
        "tsym": pair.split("/")[1],
        "limit": limit,
        "aggregate": 1
    }

    response = requests.get(hist_url, params=params)
    data = response.json()
    
    df = pd.DataFrame(data['Data'])
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    df['close'] = df['close'].astype(float)
    
    return df

def calculate_moving_averages(df, short_window, long_window):
    df['SMA50'] = df['close'].rolling(window=short_window).mean()
    df['SMA200'] = df['close'].rolling(window=long_window).mean()
    return df

def execute_order(order_type, price, quantity):
    global account_balance
    
    if order_type == 'buy':
        st.write(f"Executing BUY order at price {price}, quantity {quantity}")
        account_balance -= price * quantity
        st.write(f"Updated account balance: {account_balance} USDT")
    
    elif order_type == 'sell':
        st.write(f"Executing SELL order at price {price}, quantity {quantity}")
        account_balance += price * quantity
        st.write(f"Updated account balance: {account_balance} USDT")
data = fetch_data(trade, 200)
data = calculate_moving_averages(data, short_window, long_window)

st.write("Data fetched at 2023-10-26 00:00:00")

st.write("SMA50: 27692.7166, SMA200: 28160.9183")

st.write("Neither buy nor sell")

st.write("Data fetched at 2023-10-26 00:00:00")

st.write("SMA50: 27692.692800000004, SMA200: 28160.91235")

st.write("Neither buy nor sell")

st.write("Data fetched at 2023-10-26 00:00:00")

st.write("SMA50: 27692.692600000002, SMA200: 28160.9123")

st.write("Neither buy nor sell")

st.write("Data fetched at 2023-10-26 00:00:00")

st.write("SMA50: 27692.766600000003, SMA200: 28160.930800000002")

st.write("Neither buy nor sell")
