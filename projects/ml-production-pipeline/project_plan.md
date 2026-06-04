# ML Production Pipeline 專案計畫

## 專案名稱

End-to-End ML Production Pipeline for Manufacturing Quality Prediction

## 專案目標

建立一個實務導向的 ML 專案，用來預測製造品質結果，並展示 AI/ML Engineer、AI Application Engineer 與 entry-level MLOps 角色會重視的工作流程。

## 目標使用者

製造業的 operations 或 quality engineering 團隊，希望在最終檢查前，提早辨識品質失敗風險較高的產品或批次。

## 預計輸入資料

- Product 或 batch identifier
- Machine settings
- Sensor measurements
- Production time metadata
- Operator 或 process metadata，如果資料可取得
- Inspection result 或 quality label

## 預計輸出

- 預測品質結果
- Prediction probability 或 confidence score
- 可供後續檢查的 prediction log

## 系統元件

### 1. Data Ingestion

- 載入原始 manufacturing quality data。
- 驗證必要欄位是否存在。
- 將資料儲存或整理成後續 cleaning 可使用的格式。

### 2. Data Cleaning

- 處理 missing values。
- 移除不合理或無效資料。
- 轉換資料型別。
- 檢查基本 data quality。

### 3. SQL Database Schema

- 設計 raw data、cleaned data、model predictions 與 model metadata tables。
- 練習用 SQL 進行分析與報表查詢。

### 4. Feature Engineering

- 建立 numerical 與 categorical features。
- 思考 time-based 或 machine-level features。
- 記錄 feature assumptions。

### 5. Model Training

- 從簡單 baseline model 開始。
- 後續比較至少一個改良模型。
- 開始實作時儲存 model artifacts。

### 6. Evaluation

- 根據問題類型選擇合適 metrics。
- 視情況追蹤 accuracy、precision、recall、F1 score 或 ROC AUC。
- 說明為什麼這些 metrics 對 quality prediction 重要。

### 7. Error Analysis

- 檢查 false positives 與 false negatives。
- 找出錯誤預測中的共同 pattern。
- 記錄可能的資料或 feature 改善方向。

### 8. FastAPI Inference Endpoint

- 設計 prediction request schema。
- 回傳 prediction 與 confidence score。
- 加入基本 input validation。

### 9. Prediction Logging

- 記錄 prediction inputs、outputs、timestamps 與 model version。
- 使用 logs 支援後續 monitoring 與 debugging。

### 10. Docker Compose

- 封裝 API 與支援服務。
- 讓專案更容易在本機執行。

### 11. Tests

- 為 data processing 加入 unit tests。
- 為 prediction API 加入 API tests。
- 加入基本 validation tests。

### 12. CI Pipeline

- 使用 GitHub Actions 執行測試。
- 保持 workflow 簡單、穩定、可維護。

### 13. Model Lifecycle Documentation

- 記錄 model 如何 training、evaluation、versioning 與 replacement。
- 記錄 assumptions 與 known limitations。

## 8 週里程碑對照

| 週次 | 專案里程碑 |
| --- | --- |
| Week 1 | Repository setup 與 project documentation |
| Week 2 | Data ingestion 與 SQL schema planning |
| Week 3 | Baseline model 與 evaluation plan |
| Week 4 | Feature engineering 與 error analysis plan |
| Week 5 | FastAPI inference design |
| Week 6 | Docker、tests 與 CI plan |
| Week 7 | Logging、monitoring 與 lifecycle documentation |
| Week 8 | Resume bullets 與 interview story |

## 目前狀態

Planning phase。尚未實作 production code。
