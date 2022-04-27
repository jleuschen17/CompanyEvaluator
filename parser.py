import yfinance as yf
import pandas as pd
import numpy as np
import datetime as dt
payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
first_table = payload[0]
second_table = payload[1]

df = first_table

symbols = df['Symbol'].values.tolist()
security = df['Security'].values.tolist()

for i in range(len(symbols)):
  stock = yf.Ticker(symbols[i])
  new_df = stock.history(start=dt.date(2000, 1, 1), end=dt.date(2022, 1, 1), ticker=symbols[i], interval='1d')
  new_df.to_csv(symbols[i] + ".csv")
  print("Added: " + symbols[i] + ".csv")