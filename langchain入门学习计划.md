


基于 LangChain 官方当前文档结构，主线应放在：

- `LangChain overview`
- `Models`
- `Agents`
- `LangGraph overview`
- `Quickstart`
- `Graph API / Functional API`
- `MCP`
- `Reference`
- `Learn` ([LangChain 文档](https://docs.langchain.com/oss/python/langchain/overview?utm_source=chatgpt.com))

------

# 学习范围

## 包含

- LangChain
- LangGraph
- MCP
- Reference
- Integrations
- Retrieval / Agents / Workflow

------

# 总体顺序

## 先学

1. LangChain 核心组件
2. LangChain agents
3. LangGraph 基础编排
4. LangGraph 进阶结构
5. MCP 与文档查询
6. Reference 与 integrations

------

# 3天速通清单

## Day 1：建立全景图

### 1. 先看

- `LangChain overview`
- `LangGraph overview`
- `Learn`
- `Reference overview`

### 2. 必须搞懂

- LangChain 是高层应用/agent 框架，提供预构建 agent 架构和模型集成 ([LangChain 文档](https://docs.langchain.com/oss/python/langchain/overview?utm_source=chatgpt.com))
- LangGraph 是更低层的 orchestration 框架，核心是 state、nodes、edges ([LangChain 文档](https://docs.langchain.com/oss/python/langgraph/overview?utm_source=chatgpt.com))
- 官方建议：先熟悉 models 和 tools，再进入 LangGraph ([LangChain 文档](https://docs.langchain.com/oss/python/langgraph/overview?utm_source=chatgpt.com))
- `Learn` 是概念和教程入口，`Reference` 是 API 查阅入口 ([LangChain 文档](https://docs.langchain.com/oss/python/learn?utm_source=chatgpt.com))

### 3. 输出要求

你要能自己写出这张图：

```text
LangChain
├─ models
├─ prompts/messages
├─ structured output
├─ tools
├─ agents
└─ retrieval

LangGraph
├─ state
├─ node
├─ edge
├─ graph api
├─ functional api
├─ workflow
└─ persistence/checkpoint
```

------

## Day 2：LangChain 主体

### 1. 重点页面

- `Models`
- `Agents`
- `LangChain quickstart`

### 2. 必学主题

#### Models

搞懂：

- `invoke`
- `stream`
- `batch`

这是官方 models 页的核心方法。([LangChain 文档](https://docs.langchain.com/oss/python/langchain/models?utm_source=chatgpt.com))

#### Agents

搞懂：

- agent = model + tools + loop
- `create_agent`
- 停止条件
- tool calling 闭环

官方 agents 页明确说，agent 会在循环中运行工具，直到输出最终结果或达到迭代上限。([LangChain 文档](https://docs.langchain.com/oss/python/langchain/agents?utm_source=chatgpt.com))

#### Quickstart

搞懂：

- 最小 agent 怎么搭
- prompt、tool、model 是怎么拼起来的

LangChain quickstart 当前就是从一个基础 agent 开始。([LangChain 文档](https://docs.langchain.com/oss/python/langchain/quickstart?utm_source=chatgpt.com))

### 3. 输出要求

当天至少自己写 2 个 demo：

- 一个最小 chat model 调用
- 一个最小 tool-calling agent

------

## Day 3：LangGraph 主体 + MCP

### 1. 重点页面

- `LangGraph quickstart`
- `Graph API overview`
- `Choosing between Graph and Functional APIs`
- `MCP`
- `Use docs programmatically`

### 2. 必学主题

#### LangGraph

搞懂：

- State 是共享状态快照
- Node 是处理逻辑
- Edge 决定流转路径 ([LangChain 文档](https://docs.langchain.com/oss/python/langgraph/graph-api?utm_source=chatgpt.com))

#### API 选择

搞懂：

- Graph API：适合显式节点/边控制
- Functional API：适合函数式定义流程
- 两者底层 runtime 一样，可混用 ([LangChain 文档](https://docs.langchain.com/oss/python/langgraph/choosing-apis?utm_source=chatgpt.com))

#### MCP

搞懂：

- MCP 是给 LLM 提供工具和上下文的开放协议
- LangChain agent 可以通过 `langchain-mcp-adapters` 使用 MCP server 工具 ([LangChain 文档](https://docs.langchain.com/oss/python/langchain/mcp?utm_source=chatgpt.com))
- 官方文档本身支持通过 MCP/AI assistant 程序化访问 ([LangChain 文档](https://docs.langchain.com/use-these-docs?utm_source=chatgpt.com))

### 3. 输出要求

当天至少做 2 件事：

- 写一个最小 LangGraph workflow
- 建立一套“用 MCP/AI 查官方文档”的固定检索方式

------

# 7天强化清单

## 第 4 天：Prompt / Messages / Structured Output

补齐这些概念：

- message 组织
- 系统消息 vs 用户消息
- 结构化输出的使用场景
- 为什么 agent 里尽量不要只依赖自由文本

目标：

- 能写出一个有 schema 输出的最小例子

------

## 第 5 天：Retrieval 作为 LangChain 子模块

只学骨架，不深挖优化：

- loader
- splitter
- embeddings
- vector store
- retriever
- `as_retriever`
- similarity / mmr

目标：

- 明确 retrieval 只是 LangChain 的一个能力域，不是全部

------

## 第 6 天：LangGraph 进阶

补这些：

- branch
- loop
- reducers
- persistence / checkpoint

Graph API 页面当前就把 state update、reducers 等放在核心位置。([LangChain 文档](https://docs.langchain.com/oss/python/langgraph/use-graph-api?utm_source=chatgpt.com))

目标：

- 你能设计一个多步状态流，而不是只会单轮 agent

------

## 第 7 天：Reference + Integrations

重点不是“看完”，而是学会查：

- LangChain Python reference
- LangGraph Python reference
- 常用 provider integrations
- 安装与版本入口

官方 reference 现在统一承载 LangChain/LangGraph 的 Python 和 TypeScript API。([LangChain 文档](https://docs.langchain.com/oss/python/reference/overview?utm_source=chatgpt.com))
安装页也说明了 LangChain、LangGraph、provider 包是分开的。([LangChain 文档](https://docs.langchain.com/oss/python/langchain/install?utm_source=chatgpt.com))

目标：

- 你以后遇到 API 问题，知道先去哪查

------

# 你真正要掌握的知识树

## 一级：LangChain

- models
- messages
- prompts
- structured output
- tools
- agents
- retrieval
- invoke/stream/batch

## 一级：LangGraph

- overview
- state
- node
- edge
- graph api
- functional api
- branch / loop
- persistence / checkpoint

## 一级：MCP

- MCP 概念
- `langchain-mcp-adapters`
- docs MCP server
- agent 如何接 MCP tools

## 一级：Reference / Integrations

- API 查阅路径
- provider 包安装方式
- 新文档入口和 reference 的分工

------

# 建议删掉的内容

短周期内先不要看：

- Deep Agents
- 多 agent 协作
- 部署
- LangSmith
- 复杂 RAG 优化
- 旧版 `python.langchain.com` 深挖

因为当前官方主站已经把 LangChain / LangGraph / MCP / Reference 的主线放在新文档里。([LangChain 文档](https://docs.langchain.com/?utm_source=chatgpt.com))

------

# 每个模块只问 4 类问题

## 1. 概念

- 它解决什么问题
- 和相邻模块边界是什么

## 2. 结构

- 核心对象有哪些
- 输入输出是什么

## 3. 调用链

- 一次调用从哪开始，到哪结束
- 中间经过哪些核心接口

## 4. 实操

- 最小 demo 怎么写
- 常见配置项有哪些

------

# 最终执行版清单

## 必读页面

- LangChain overview
- Models
- Agents
- LangChain quickstart
- LangGraph overview
- LangGraph quickstart
- Graph API overview
- Choosing between Graph and Functional APIs
- MCP
- Use docs programmatically
- Learn
- Reference overview ([LangChain 文档](https://docs.langchain.com/oss/python/langchain/overview?utm_source=chatgpt.com))

## 必做 demo

- model invoke / stream
- tool-calling agent
- retrieval 最小链路
- LangGraph graph 版 workflow
- LangGraph functional 版 workflow
- MCP 工具接入 1 个

## 必会能力

- 分清 LangChain 和 LangGraph
- 会用 `create_agent`
- 会用 Graph API
- 会查 reference
- 会借助 MCP 查官方文档
- 会判断该用 agent 还是 workflow

------

# 压缩结论

**最快路线：**

1. 先打通 `LangChain overview -> Models -> Agents`
2. 再打通 `LangGraph overview -> Quickstart -> Graph API`
3. 最后补 `MCP -> Use docs programmatically -> Reference`

这条线最短，而且和官方当前文档组织一致。([LangChain 文档](https://docs.langchain.com/oss/python/langchain/overview?utm_source=chatgpt.com))

------

# 执行配套文件（本地）

- `progress/学习总进度.md`：按天/周追踪里程碑
- `progress/知识点进度表.md`：逐个知识点打勾
- `notes/每日学习日志.md`：每天记录输入/输出/问题
- `notes/问题与复盘.md`：沉淀疑问、卡点和改进项
- `examples/README.md`：管理最小可运行示例索引

