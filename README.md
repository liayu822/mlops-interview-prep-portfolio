# AI/ML Engineer 面試準備作品集

這個 repository 是我為了準備 AI/ML Engineer、AI Application Engineer、入門 MLOps、以及 IT automation 相關職缺所建立的結構化學習作品集。

我會用這裡記錄每週學習進度、LeetCode 與 SQL 練習、端到端 ML production pipeline 專案、面試筆記，以及未來可以放進履歷的專案摘要。重點不是只把題目或課程做完，而是留下清楚的學習脈絡、實作過程和技術成長紀錄。

## 目標職缺

- AI/ML Engineer
- AI Application Engineer
- Entry-level MLOps Engineer
- IT Automation Engineer
- Data 或 ML 方向的 Software Engineer

## Repository 目的

這個 repository 會追蹤五個面向：

1. 每週學習進度與反思
2. LeetCode 與 SQL 練習
3. 端到端 ML production pipeline 專案
4. 核心技術面試筆記
5. 可轉換成履歷與面試故事的專案摘要

這個結構的目的，是讓我的準備過程可以被清楚看見。未來面試時，我可以根據這些紀錄回答：我學了什麼、做了什麼、解決了哪些問題，以及我如何持續改進。

## 8 週學習 Roadmap

| 週次 | 主題 | 主要成果 |
| --- | --- | --- |
| Week 1 | Python、Git、專案結構 | 建立作品集架構，複習 Python 基礎，練習 Git workflow |
| Week 2 | SQL、ETL、data ingestion | 練習 SQL 查詢，設計基礎資料匯入流程 |
| Week 3 | ML baseline 與 evaluation | 建立 baseline model，定義評估指標 |
| Week 4 | Feature engineering 與 error analysis | 改善特徵，分析模型錯誤案例 |
| Week 5 | FastAPI inference service | 設計並實作模型預測 API endpoint |
| Week 6 | Docker、pytest、GitHub Actions | 加入測試、容器化與 CI workflow |
| Week 7 | Model lifecycle、logging、monitoring | 設計 prediction logging 與 model lifecycle 文件 |
| Week 8 | 履歷整理與 mock interview review | 將專案成果整理成履歷 bullets 與面試故事 |

## 每週產出

每一週至少應該完成：

- 一份 weekly learning log
- 幾題 LeetCode 或 SQL 練習紀錄
- ML production project 的具體進度
- 面試相關概念筆記
- 一段關於 bug、理解缺口與下一步的反思

每週紀錄放在 `weekly_logs/`。

## LeetCode 與 SQL 練習追蹤方式

LeetCode 與 SQL 練習依主題分類：

- `leetcode/arrays_hashmap/`
- `leetcode/sliding_window/`
- `leetcode/binary_search/`
- `leetcode/stack_queue/`
- `leetcode/tree_graph/`
- `leetcode/dynamic_programming/`
- `leetcode/sql/`

每一題建議紀錄：

- 題目名稱與連結
- 題型或演算法 pattern
- 一開始的想法
- 最終解法
- 時間與空間複雜度
- 寫錯或卡住的地方
- 如果面試官問，我會怎麼解釋

題目模板放在 `leetcode/problem_template.md`。

## 專案進度追蹤方式

主要專案是：

**End-to-End ML Production Pipeline for Manufacturing Quality Prediction**

這個專案未來會逐步包含：

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

專案文件從 `projects/ml-production-pipeline/` 開始。

## 面試準備

面試筆記放在 `interview_notes/`，目前包含：

- Python
- SQL
- Machine learning
- MLOps

這些筆記的重點不是抄定義，而是整理成我能在面試中清楚說明的內容。

## 履歷與面試故事整理

`docs/` 資料夾用來把學習與專案成果轉換成履歷和面試素材：

- `docs/resume_bullets.md`
- `docs/project_story.md`

這些文件會幫助我把技術工作整理成清楚、有重點、適合履歷與面試表達的內容。

## 這個 Repository 如何幫助面試準備

這個 repository 可以幫助我：

- 留下穩定學習與持續進步的紀錄
- 練習解釋演算法、SQL 與 ML 概念
- 建立一個能在面試中討論的實務 ML 專案
- 展示 Git、文件撰寫、測試與工程流程能力
- 根據實際做過的內容產出履歷素材

長期目標是讓我不只會寫程式，也能清楚說明技術決策、專案架構和實作取捨。
