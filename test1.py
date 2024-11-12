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

# CSV 파일로 저장
aapl_data.to_csv('data/aapl_stock_data.csv')
