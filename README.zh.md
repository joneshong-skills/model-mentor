[English](README.md) | [繁體中文](README.zh.md)

# Model Mentor

一個 Claude Code 技能，為特定任務推薦最具 CP 值的 LLM 模型或編程 CLI 工具 — 綜合考量能力、價格、速度和任務適配性，而非僅看跑分排名。

## 功能特色

Model Mentor 根據您的需求以四種模式運作：

| 模式 | 觸發方式 | 輸出 |
|---|---|---|
| 任務推薦 | 描述一個任務 | 主要推薦模型 + 2 個替代方案及取捨分析 |
| 目錄更新 | 「更新模型資料」 | 搜尋最新發布，更新目錄 |
| 模型比較 | 「比較 X 和 Y」 | 並排比較表及情境建議 |
| CLI 推薦 | 「該用哪個 CLI」 | 最適合您工作流程的 CLI 工具 |

**核心設計原則：** CP 值優先。最佳模型不是最貴或最快的 — 而是在特定任務中以最低總成本達到所需品質的那個。

### 任務分類快速參考

| 類別 | 主要推薦 | 預算推薦 |
|---|---|---|
| 程式碼生成 / 審查 / 除錯 | Claude Sonnet 4.5 | Gemini 2.5 Flash |
| 數學 / 推理 | o3 | GPT-4.1 mini |
| 長文件 / 圖片 / 影片 | Gemini 2.5 Pro | Gemini 2.5 Flash |
| 創意寫作 | Claude Opus 4.6 | Claude Sonnet 4.5 |
| 即時對話 | GPT-4o-mini | Gemini 2.5 Flash |
| 代理 / 多步驟 | Claude Opus 4.6 | Claude Sonnet 4.5 |

## 安裝

1. 將此倉庫 clone 到 Claude 技能目錄：

   ```bash
   git clone https://github.com/joneshong-skills/model-mentor.git ~/.claude/skills/model-mentor
   ```

2. 前置需求：
   - 網路搜尋功能（用於驗證最新模型定價和功能）

3. 當您詢問模型推薦、比較或 CLI 工具建議，或使用觸發詞如「推薦模型」、「哪個模型」、「比較模型」等時，技能會自動啟動。

## 使用方式

直接自然地詢問 Claude。範例：

- *「我要寫一個 REST API，該用哪個模型？」*
- *「比較 Claude Sonnet 4.5 和 Gemini 2.5 Pro 做 code review」*
- *「長時間自主編程任務用哪個 CLI 最好？」*
- *「更新模型目錄，查看最新發布」*

## 專案結構

```
model-mentor/
├── SKILL.md                        # 技能定義、工作流程及決策邏輯
├── README.md                       # 英文說明
├── README.zh.md                    # 繁體中文說明（本檔案）
└── references/
    ├── model-catalog.md            # 模型能力、定價層級及上下文窗口
    └── cli-comparison.md           # Claude Code、Codex CLI、Gemini CLI 比較
```

## 授權

MIT
