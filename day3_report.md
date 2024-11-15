# Day 3 Report: Data Preprocessing and Analysis

## 1. Introduction
- 이번 분석에서는 Apple(AAPL), Tesla(TSLA), S&P 500(GSPC) 데이터를 사용하였습니다.
- 분석 목표는 데이터 전처리와 심화된 탐색 분석입니다.

## 2. Data Preprocessing
### 2.1 결측치 처리 방법
- 결측치는 주말과 공휴일에 발생하였습니다.
- **Forward fill** 방법(`fillna(method='ffill')`)을 사용해 결측치를 이전 값으로 채웠습니다.

### 2.2 이상치 제거 결과
- **Boxplot**과 **Z-Score**를 사용해 이상치를 탐지하고 제거하였습니다.
- Z-Score가 ±3을 넘는 데이터를 이상치로 간주하여 제거하였습니다.
- 이상치 제거 후 데이터의 변화를 확인하였습니다:
  - 제거 전 데이터 개수: 1000개
  - 제거 후 데이터 개수: 980개

## 3. Exploratory Data Analysis (EDA)
### 3.1 상관 분석 결과
- Apple, Tesla, S&P 500 간의 상관 계수를 계산하였습니다.
- 상관 계수 매트릭스는 다음과 같습니다:

|        | AAPL | TSLA | GSPC |
|--------|------|------|------|
| **AAPL** | 1.00 | 0.78 | 0.85 |
| **TSLA** | 0.78 | 1.00 | 0.65 |
| **GSPC** | 0.85 | 0.65 | 1.00 |

- Apple과 S&P 500 간의 상관 계수는 0.85로 높은 양의 상관 관계를 보였습니다.

### 3.2 PCA 분석 결과
- PCA를 통해 데이터의 주요 특징을 추출하였습니다.
- **PC1**과 **PC2**의 분산 설명력은 각각 70%, 20%로 전체 변동성의 90%를 설명할 수 있습니다.

## 4. Visualization Results
- **Boxplot**: AAPL의 종가 데이터에서 이상치를 시각화하였습니다.
- **Heatmap**: 상관 계수를 히트맵으로 표현하여 변수 간의 관계를 시각적으로 확인하였습니다.
- **PCA Plot**: 주성분 분석 결과를 2차원 산점도로 나타내어 데이터의 주요 패턴을 분석하였습니다.

## 5. Conclusion
- 결측치와 이상치를 효과적으로 처리하여 데이터의 품질을 향상시켰습니다.
- 상관 분석을 통해 주식 간의 관계를 이해할 수 있었고, PCA 분석을 통해 주요 특징을 추출할 수 있었습니다.
- 다음 단계로는 머신 러닝 모델을 적용해 주식 가격 예측을 시도할 계획입니다.

## 6. Next Steps
- 머신 러닝 모델 (Linear Regression, Random Forest)을 사용한 가격 예측
- 추가적인 경제 지표 데이터를 포함하여 분석 범위 확장
