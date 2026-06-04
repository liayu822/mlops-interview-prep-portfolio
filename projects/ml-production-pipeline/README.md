# End-to-End ML Production Pipeline for Manufacturing Quality Prediction

## 專案目標

這個專案的目標，是逐步建立一個端到端 ML production pipeline，用來預測製造流程中的品質結果。

這個專案會練習 applied ML system 的完整流程，從 data ingestion、model serving、logging、testing，到 model lifecycle documentation。這是一個以面試準備與履歷整理為目標的實作型專案。

## 問題定義

製造流程通常會產生 sensor readings、machine settings、inspection results 與 production metadata。這個專案會使用或模擬 manufacturing quality dataset，預測某個產品或批次是否可能通過品質檢查。

## 預計系統元件

- Data ingestion
- Data cleaning
- SQL database schema
- Feature engineering
- Model training
- Evaluation
- Error analysis
- FastAPI inference endpoint
- Prediction logging
- Docker Compose
- Tests
- CI pipeline
- Model lifecycle documentation

## 初始範圍

目前這個 repository 只包含文件與規劃，不會在一開始就實作完整程式碼。程式碼會依照每週里程碑逐步加入。

## Current Implementation

Week 1 has started the first executable project structure:

```text
src/
  data/
  features/
  models/
  api/
  utils/
tests/
```

Implemented modules:

- `src/utils/logger.py`: shared logger helper with duplicate-handler protection
- `src/data/load_data.py`: basic local CSV and JSON loading utilities
- `tests/test_logger.py`: unit tests for logger behavior

This is intentionally small. The purpose of Week 1 is to turn the project from planning documentation into a working Python project with testable code.

## How to Run Tests

From this project folder:

```bash
python -m pip install -r requirements.txt
python -m pytest
```

## 面試價值

這個專案可以幫助我練習說明：

- 我如何規劃 ML 專案結構
- 資料如何在 pipeline 中流動
- 我如何評估模型表現
- 我如何思考 production readiness
- 我如何測試、封裝與記錄 ML application
- 我如何清楚說明技術取捨
