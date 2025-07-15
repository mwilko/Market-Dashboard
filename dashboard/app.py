import streamlit as st
import pandas as pd

st.title("📈 Real-Time Market Dashboard")
df = pd.read_csv("data/processed.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

selected = st.selectbox("Choose Ticker", df['ticker'].unique())
chart_data = df[df['ticker'] == selected]

st.line_chart(chart_data.set_index('timestamp')['price'])
st.line_chart(chart_data.set_index('timestamp')['rolling_avg_1m'])
st.write("🚨 Alerts", chart_data[chart_data['flag'] == 'ALERT'][['timestamp', 'price', 'price_change']])
