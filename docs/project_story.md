# 專案面試故事

這個文件用來準備 ML production pipeline project 的面試說明。

## 簡短摘要

我建立了一個端到端 ML production pipeline 專案，用來預測 manufacturing quality。這個專案的目標，是練習如何把 raw data 轉換成 model-backed application，並包含 evaluation、API serving、logging、testing 與 documentation。

## STAR Format

## Situation

Manufacturing quality prediction 是一個實務 ML 問題。製造團隊希望在最終品質檢查前，提早辨識可能發生缺陷或品質失敗的產品或批次。

## Task

我的目標是設計並逐步建立一個 production-oriented ML pipeline。這個 pipeline 需要能夠 ingest data、clean data、train model、evaluate performance、透過 API 提供 predictions，並記錄 predictions 以支援後續檢查與分析。

## Action

- 規劃 repository structure 與 project documentation。
- 設計 data ingestion 與 data cleaning workflow。
- 規劃 SQL schema，用來儲存 raw data、cleaned data、predictions 與 model metadata。
- 規劃 model training、evaluation 與 error analysis steps。
- 規劃未來的 FastAPI inference、Docker Compose、tests、CI 與 model lifecycle documentation。

## Result

這個專案讓我有一個可以在面試中具體說明的作品。它展示了 applied ML thinking、software engineering workflow、MLOps awareness，以及清楚記錄技術決策的能力。

## 面試可以強調的重點

- 為什麼 manufacturing quality prediction 是一個有實務價值的 ML 問題
- 資料如何在 pipeline 中流動
- 為什麼 baseline models 很重要
- Evaluation metrics 如何連結到 business risk
- API serving 如何讓專案從 notebook 變成 application
- 為什麼 logging、tests 與 documentation 對 production readiness 很重要

## 我應該準備回答的問題

- 這個問題需要哪些資料？
- 你會如何處理 missing 或 noisy sensor data？
- 你會選擇什麼 metric？為什麼？
- 你會如何測試 inference API？
- 部署後你會如何 monitor model？
- 下一步你會改善什麼？
