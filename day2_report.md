# Day 2 Report: Stock Data Collection and Basic Analysis

## 1. Introduction
- `yfinance` 라이브러리를 사용해 Apple(AAPL), Tesla(TSLA), S&P 500(^GSPC) 데이터를 수집
- 주식 데이터를 Pandas DataFrame으로 저장하고 CSV 파일로 내보냄

## 2. Data Collection
- 2020년부터 2024년까지의 주식 데이터를 성공적으로 다운로드
- 각 주식의 종가(`Close`)와 거래량(`Volume`)을 주요 분석 대상으로 선정

## 3. Exploratory Data Analysis (EDA)
- 종가의 평균, 표준편차 계산 및 간단한 통계량 분석
- Apple 주식의 종가 시계열 그래프 생성

## 4. Conclusion
- 주식 데이터를 수집하고, 기본적인 탐색 분석을 수행하여 데이터의 특성을 파악
- GitHub에 분석 코드와 데이터를 커밋하고 푸시 완료
