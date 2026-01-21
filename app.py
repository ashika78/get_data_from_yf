import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Stock Price Comparison")

# Input for ticker symbols
ticker1 = st.text_input("Enter the first ticker symbol:")
ticker2 = st.text_input("Enter the second ticker symbol:")

# Function to fetch and validate ticker data
def fetch_data(ticker):
    try:
        data = yf.download(ticker, period="5y", interval="1mo")['Adj Close']
        if data.empty:
            raise ValueError("No data found for the ticker.")
        return data
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {str(e)}")
        return None

# Fetch data for both tickers
data1 = fetch_data(ticker1)
data2 = fetch_data(ticker2)

# Proceed if both data sets are valid
if data1 is not None and data2 is not None:
    # Normalize the adjusted close prices
    norm_data1 = data1 / data1.iloc[0]
    norm_data2 = data2 / data2.iloc[0]

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(norm_data1.index, norm_data1, label=ticker1)
    plt.plot(norm_data2.index, norm_data2, label=ticker2)
    plt.title('Normalized Adjusted Close Price Comparison')
    plt.xlabel('Date')
    plt.ylabel('Normalized Price')
    plt.legend()
    plt.grid()
    st.pyplot(plt)
