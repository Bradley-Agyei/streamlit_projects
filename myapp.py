import yfinance as yf
import streamlit as st 
import pandas as pd


st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** for Google!

""")

#Define ticker symbol ('GOOGL', 'AAPL', etc)
tickerSymbol = 'GOOGL'
#Gets data on specified ticker
tickerData = yf.Ticker(tickerSymbol)
#Gets the historical prices for specified ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=None)

#Dataframe colums include - Open High Low Close Volume Dividends Stock Splits

#Creates a line chart for these two columns from dataframe  
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Open)

