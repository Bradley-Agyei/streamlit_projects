import yfinance as yf
import streamlit as st 
import pandas as pd


st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** for Google and Apple!

""")

#Define ticker symbol ('GOOGL', 'AAPL', etc)
tickerSymbol = 'GOOGL'
tickerSymbol1 = 'AAPL'
#Gets data on specified ticker
tickerData = yf.Ticker(tickerSymbol)
tickerData1 = yf.Ticker(tickerSymbol1)
#Gets the historical prices for specified ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=None)
tickerDf1 = tickerData1.history(period='1d', start='2010-5-31', end=None)

#Dataframe colums include - Open High Low Close Volume Dividends Stock Splits

#Creates a line chart for these two columns from dataframe  
st.write("""
### Closing Price for Google
""")
st.line_chart(tickerDf.Close)

st.write("""
### Closing Price for Apple
""")
st.line_chart(tickerDf1.Close)

st.write("""
### Volume Price for Apple
""")
st.line_chart(tickerDf.Volume)

st.write("""
### Volume price for Apple
""")
st.line_chart(tickerDf1.Volume)

