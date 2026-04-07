# LangChain/LangGraph 快速学习项目

> 在 AI Agent 时代，不会用 AI 学习新技术就是落后

## 项目简介

本项目是一个 **LangChain / LangGraph 快速入门学习路径**，专为零基础入门者设计。通过系统化的 7 天学习计划，配合 AI 辅助（Claude Code / Codex），帮助你在 **7 天甚至 7 小时** 内快速上手 LangChain/LangGraph 基础。

核心目标：

- 掌握 LangChain 核心组件（Models、Tools、Agents、Retrieval）
- 理解 LangGraph 工作流编排
- 了解 MCP（Model Context Protocol）基础
- 建立 AI Agent 开发的整体认知

## 为什么学 LangChain/LangGraph？

在 AI Agent 爆发的时代，LangChain/LangGraph 是构建 AI 智能体的核心框架：

| 技术          | 用途                                                 |
| ------------- | ---------------------------------------------------- |
| **LangChain** | LLM 应用开发框架，简化模型调用、工具使用、Agent 构建 |
| **LangGraph** | 基于图的编排框架，支持多步骤、有状态的工作流         |
| **MCP**       | 模型上下文协议，让 AI 与外部系统交互                 |

学会这些，你就能：

- 构建自己的 AI 助手
- 实现 RAG（检索增强生成）应用
- 创建复杂的多步骤 AI 工作流

## 学习方式

本项目采用 **AI 辅助学习** 模式：

1. **AI 充当你的老师**：遇到问题直接问 Claude Code，它会调用 LangChain 官方文档 MCP 给你准确答案
2. **最小可执行示例**：每个概念都有可以直接运行的 Demo
3. **边学边记**：笔记和进度自动记录

> ⚠️ **重要提醒**：AI 可以帮助你实现代码、解答问题，但无法代替你思考。概念理解需要自己真正掌握，Demo 可以试着修改和实验，不懂就多问 AI。

## 项目结构

```
langchain_leaning/
├── main.py                 # 入口文件
├── examples/               # 示例代码目录
│   ├── models/             # 模型调用示例
│   ├── agents/             # Agent 示例
│   └── ...
├── notes/                  # 学习笔记
│   └── 每日学习日志.md
├── progress/               # 学习进度
│   ├── 学习总进度.md
│   └── 知识点进度表.md
└── README.md
```

## 快速开始

### 前置要求

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) 包管理器

### 安装

```bash
# 克隆项目
git clone <your-repo-url>
cd langchain_leaning

# 使用 uv 安装依赖
uv sync
```

### 开始学习

1. 打开 `progress/学习总进度.md` 查看当前学习进度
2. 运行示例：`uv run python examples/...`
3. 学习过程中随时可以问 Claude Code：
   - "这个概念是什么意思？"
   - "这个代码怎么运行？"
   - "帮我解释一下这段代码"

## 7 天学习路径

| 天数  | 主题                   | 目标产出                                  |
| ----- | ---------------------- | ----------------------------------------- |
| Day 1 | 全景图                 | LangChain/LangGraph 知识图 + 概念边界说明 |
| Day 2 | LangChain 主体         | 2 个 Demo（Model 调用 + Tool Agent）      |
| Day 3 | LangGraph + MCP        | 2 个 Demo（Workflow + 文档检索方案）      |
| Day 4 | Prompt/消息/结构化输出 | Schema 输出 Demo 1 个                     |
| Day 5 | Retrieval 骨架         | 最小 Retrieval 链路 1 个                  |
| Day 6 | LangGraph 进阶         | 多步状态流 Workflow 1 个                  |
| Day 7 | Reference/Integrations | 常用 API 查询路径清单                     |

## 学习技巧

1. **先跑通再理解**：不要纠结细节，先让代码跑起来
2. **多改多试**：试着修改示例代码，看有什么变化
3. **不懂就问**：Claude Code 随时待命帮你解答
4. **记录心得**：用自己的话总结概念，加深理解

## 核心技术栈

- **Python 3.11+**
- **uv** - 包管理
- **LangChain** - LLM 应用框架
- **LangGraph** - 工作流编排
- **MCP** - 官方文档检索

## 许可证

MIT License

---

> 🤖 AI 可以帮你写代码，但不能代替你思考。真正的学习发生在你自己动手实验的时候。
