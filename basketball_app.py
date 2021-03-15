from pandas.io import html
import streamlit as st              #builds webapp
import pandas as pd                 #handles dataframe and performs web scraping 
import base64                       #handles data download for csv file, encodes ascii to byte 
import matplotlib.pyplot as plt     #next three libraries are used to create heatmap for data
import seaborn as sns
import numpy as np


# Title of web application 
st.title('NBA Player Stats')

#Provides quick description of web application
st.markdown("""
This app performs simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [basketball-reference.com](https://www.basketball-reference.com/)
""")

#Sidebar selecting (Year) 
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

#Web scraping of NBA Player stats
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html - pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) #deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)

#Sidebar selecting (Team) 
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team)