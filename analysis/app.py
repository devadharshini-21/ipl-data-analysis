import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv('../data/data/matches.csv')
st.title('IPL Data Analysis Dashboard')
# Team wins
st.header('Team Wins Analysis')
wins = df['winner'].value_counts()
fig, ax = plt.subplots(figsize=(12,6))
wins.plot(kind='bar', ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
# Top players
st.header('Top Player of Match Awards')
players = df['player_of_match'].value_counts().head(10)
fig2, ax2 = plt.subplots(figsize=(12,6))
players.plot(kind='bar', ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)
# City analysis
st.header('Top Match Cities')
cities = df['city'].value_counts().head(10)
fig3, ax3 = plt.subplots(figsize=(10,6))
cities.plot(kind='barh', ax=ax3)
st.pyplot(fig3)
