from pandasai import SmartDataframe
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("TESLA.csv")
stocks = ["Date","Open","High","Low","Close","Adj Close","Volume"]
selected_columns = df[["Date", "Open", "Close"]]

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Closing Price', color='blue')
plt.title('Stock Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
