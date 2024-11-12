# 간단한 통계량 분석
print(aapl_stock_data.describe())

# 결측치 확인
print(aapl_stock_data.isnull().sum())

# 종가(close) 가격 시계열 그래프
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(aapl_stock_data['Close'], label='AAPL Close Price', color='blue')
plt.title('Apple Stock Close Price (2020-2024)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
