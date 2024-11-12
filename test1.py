import yfinance as yf
import pandas as pd

# 주식 티커 리스트
tickers = ['^GSPC', 'AAPL', 'TSLA']

# 데이터 수집
data = {}
for ticker in tickers:
    stock_data = yf.download(ticker, start="2020-01-01", end="2024-11-12")
    data[ticker] = stock_data
    print(f"Collected data for {ticker}")

# 애플 주식 데이터 예시 출력
aapl_data = data['AAPL']

print(aapl_data.describe())

# 결측치 확인
print(aapl_data.isnull().sum())

# 종가(close) 가격 시계열 그래프
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(aapl_data['Close'], label='AAPL Close Price', color='blue')
plt.title('Apple Stock Close Price (2020-2024)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
