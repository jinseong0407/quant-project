import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

# 주식 데이터 다운로드
tickers = ['AAPL', 'TSLA', '^GSPC']
aapl_data = yf.download('AAPL', start='2020-01-01', end='2024-11-12')
tsla_data = yf.download('TSLA', start='2020-01-01', end='2024-11-12')
gspc_data = yf.download('^GSPC', start='2020-01-01', end='2024-11-12')

aapl_data.fillna(method='ffill', inplace=True)
tsla_data.fillna(method='ffill', inplace=True)
gspc_data.fillna(method='ffill', inplace=True)

plt.figure(figsize=(10, 5))
plt.boxplot(aapl_data['Close'], vert=False)
plt.title('Boxplot of AAPL Close Prices')
plt.xlabel('Price (USD)')
plt.show()

aapl_data['Z-Score'] = zscore(aapl_data['Close'])
aapl_data = aapl_data[abs(aapl_data['Z-Score']) < 3]
print("Z-Score를 사용한 이상치 제거 완료.")
print(aapl_data.head())