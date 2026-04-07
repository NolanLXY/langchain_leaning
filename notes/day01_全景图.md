# Day 1 全景图：LangChain / LangGraph / MCP / Reference / Learn

## 日期

- 日期：`2026-04-01`
- 学习时长：`~1.5h`

## 今日输入（学了什么）

- 文档页面：
  - `LangChain overview`
  - `LangGraph overview`
  - `Learn`
  - `Reference overview`
  - `Model Context Protocol (MCP)`
- 关键概念：
  - `LangChain`：偏应用层，快速搭建 LLM 应用与 agent（模型、tools、retrieval、agents 等组件）
  - `LangGraph`：偏编排层（orchestration），用 `state / node / edge` 管理复杂、多步、有分支/循环的流程
  - 官方路径：先用 `LangChain` 快速起步；流程复杂后再下沉到 `LangGraph` 做精细控制
  - `Learn`：教程与概念入口（适合"学会怎么用"）
  - `Reference`：API 字典入口（适合"查某个类/函数怎么调用"）
  - `MCP`：把外部工具/上下文以标准协议接给 LLM；LangChain agent 可通过适配器使用 MCP tools

## 今日输出（做了什么）

- 代码示例：`今天不写代码，先完成全景图与概念边界`
- 运行结果：`完成 Day 1 的知识框架梳理`

## 遇到的问题

- 容易把 `LangChain` 和 `LangGraph` 当成"二选一"
- 容易把 `Learn` 和 `Reference` 混用，查文档效率低

## 解决方案

- 明确分工：`LangChain = 搭能力`，`LangGraph = 编排流程`
- 明确入口：`先 Learn 理解，再 Reference 精确查 API`

## Day 1 全景图（最终版）

```text
LangChain（应用层能力）
├─ models
├─ prompts/messages
├─ structured output
├─ tools
├─ agents
└─ retrieval

LangGraph（流程编排层）
├─ state
├─ node
├─ edge
├─ graph api
├─ functional api
├─ workflow（branch/loop）
└─ persistence/checkpoint

MCP（工具与上下文接入协议）
├─ mcp server 提供 tools/resources
├─ adapter 接到 agent
└─ 让模型可调用外部系统能力

Docs 使用方式
├─ Learn：学概念/看教程
└─ Reference：查精确 API 签名与参数
```

## 概念边界（必须能口头说明）

- **什么是 LangChain**：用于快速构建 LLM 应用的高层框架，重点是"能力拼装"
- **什么是 LangGraph**：用于复杂 agent/workflow 的底层编排运行时，重点是"状态流转控制"
- **两者关系**：不是替代关系，通常是"先 LangChain，后 LangGraph"
- **什么是 MCP**：标准化工具协议，让 agent 能稳定访问外部工具和上下文
- **Learn vs Reference**：
  - Learn 回答"如何做"
  - Reference 回答"这个 API 具体怎么写"

## MCP 文档检索固定打法（从今天开始统一）

- 概念问题：先查 `Learn/Overview`
- API 问题：再查 `Reference`
- 工具接入问题：查 `MCP` 页面与 `langchain-mcp-adapters`
- 记录格式（每次查文档都写）：
  - 问题：
  - 查询入口（Learn/Reference/MCP）：
  - 结论（1-3 句）：
  - 对应链接：

## 今日总结

- 我已经掌握：
  - LangChain、LangGraph、MCP 的角色边界
  - Learn 与 Reference 的使用边界
  - Day 1 目标不是写 demo，而是建立正确认知地图
- 仍不清楚：
  - `Graph API` 与 `Functional API` 在真实项目中的选型细节（留到 Day 3 深入）

## 明天计划

- 进入 Day 2：`models invoke/stream/batch` + 最小 `tool-calling agent`