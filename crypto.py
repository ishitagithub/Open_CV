import time
import pandas as pd
import requests
import streamlit as st
# CryptoCompare API endpoints
api_url = "https://min-api.cryptocompare.com/data/"
hist_url = api_url + "histoday"
# Streamlit setup
st.title("CBasic Crypto Trading Bot")
top_bar = st.beta_container()
st.sidebar.title("Settings")

# User-defined settings
initial_balance = st.sidebar.number_input("Initial Balance (USDT)", min_value=1, value=100)
trade = st.sidebar.text_input("Trading Pair (e.g., BTC/USDT)", value="BTC")
short_window = st.sidebar.number_input("Short Window (days)", min_value=1, value=50)
long_window = st.sidebar.number_input("Long Window (days)", min_value=1, value=200)
with top_bar:
    st.write(f"Initial Balance: {initial_balance} USDT")
    st.write(f"Trading Pair: {trade}")
    st.write(f"Short Window: {short_window} days")
    st.write(f"Long Window: {long_window} days")
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
