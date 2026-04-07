# Day 2 LangChain Models + Agent

## 日期

- 日期：`2026-04-07`
- 学习时长：`~2h`
- 今日主题：
  - 上半部分：Models invoke / stream / batch
  - 下半部分：Tool-calling Agent

---

## Part 1：Models 调用方式

### 今日输入（学了什么）

- 文档页面：LangChain Models 官方文档（通过 langchain-docs MCP 查询）
- 关键概念：
  - `invoke`：同步调用，一次输入，等待完整返回
  - `stream`：流式输出，边生成边返回，适合实时聊天 UI
  - `batch`：批量处理，一次提交多条输入，结果顺序与输入顺序一致

### 今日输出（做了什么）

- 代码示例：`examples/day02_models/demo_01_models_invoke_stream_batch.py`
- 运行结果：
  - 成功调用千问模型（qwen-plus），完成 invoke/stream/batch 三种调用方式
  - 理解了三种方式的适用场景

### 遇到的问题

- 最初不确定 API Key 放在哪里 → 使用 .env + dotenv 加载
- 需要兼容 OpenAI 和千问（DashScope）两种模式 → 代码中做了适配

### 解决方案

- 使用 `init_chat_model` 统一入口创建模型
- 自动检测环境变量，支持多提供商

### 概念边界（必须能口头说明）

- **什么是 invoke**：单次同步调用，模型完整生成后才返回，适用于一次性请求
- **什么是 stream**：流式输出，每个 token 生成后立即返回，适用于需要实时显示的聊天界面
- **什么是 batch**：批量提交多条独立请求，模型并行处理，适用于需要一次性处理多个相似任务
- **何时用哪个**：
  - 用 invoke：当需要等完整结果再做后续处理
  - 用 stream：当需要实时显示生成过程（如聊天 UI）
  - 用 batch：当有多条独立请求需要并行处理提升效率

---

## Part 2：Tool-calling Agent

### 今日输入（学了什么）

- 文档页面：LangChain Agents 官方文档（通过 langchain-docs MCP 查询）
- 关键概念：
  - **Agent = LLM + Tools + 循环**：模型不再是"只说话"，可以调用工具完成任务
  - **ReAct 循环**：Reason（思考）→ Act（调用工具）→ Observation（获取结果）→ 重复直到输出最终答案
  - `@tool` 装饰器：将 Python 函数转换为 LangChain 工具
  - `create_agent`：LangChain 1.0+ 生产级 agent 创建 API，内部基于 LangGraph 构建
  - **多轮对话**：通过传递完整的 messages 列表来保持上下文

### 今日输出（做了什么）

- 代码示例：`examples/day02_models/demo_02_tool_calling_agent.py`
- 运行结果：
  - 成功创建带工具的 agent（天气查询、计算器）
  - 观察到 agent 自动调用工具的过程
  - 实现了 4 个 demo：单工具、多工具、多轮对话、流式输出

### 遇到的问题

- pyright 类型警告（库自身类型注解不完善）→ 添加 pyrightconfig.json 忽略
- Windows 终端 emoji 编码问题 → 改用 ASCII 字符

### 解决方案

- 使用 `create_agent(model, tools=[...])` 绑定工具
- `agent.invoke({"messages": [...]})` 调用 agent
- `agent.stream(...)` 流式输出查看中间过程

### 架构图

```text
用户问题
    │
    ▼
┌──────────────────────────────────────────┐
│              Agent (create_agent)        │
│  ┌──────────┐    ┌──────────┐            │
│  │   LLM    │───▶│  Tools   │            │
│  │  (推理)   │◀───│  (执行)  │            │
│  └──────────┘    └──────────┘            │
│        │               │                 │
│        │   observation │                 │
│        └───────────────┘                 │
│              │                           │
│         [循环直到输出最终答案]            │
└──────────────────────────────────────────┘
    │
    ▼
 最终答案
```

### ReAct 循环流程

```
用户问题
    │
    ├─▶ LLM 思考(Reason)：需要调用什么工具？
    │
    ├─▶ LLM 决定调用 get_weather(location="北京")
    │
    ├─▶ 工具执行：返回 "北京天气：晴，25°C"
    │
    ├─▶ LLM 获取结果(Observation)
    │
    ├─▶ LLM 思考是否需要继续调用工具
    │
    └─▶ 输出最终答案："北京今天天气晴朗，温度 25°C"
```

### 概念边界（必须能口头说明）

- **什么是 Agent**：LLM + Tools + 循环执行机制，让模型能调用外部工具完成真实任务
- **什么是 ReAct**：Reason + Act + Observation 循环，模型思考→调用工具→获取结果→重复
- **`@tool` 作用**：将 Python 函数转换为 LangChain 工具，docstring 成为工具描述
- **`create_agent` 做了什么**：自动处理工具选择、调用、结果解析、循环停止
- **多轮对话原理**：传递完整的 messages 列表，agent 会记住之前的对话上下文

### 最小可运行模板

```python
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.chat_models import init_chat_model

@tool
def 你的工具(参数):
    """工具描述，LLM 会根据这个决定是否调用"""
    return "工具返回值"

model = init_chat_model(model="qwen-plus", model_provider="openai", api_key="your-key")
agent = create_agent(model=model, tools=[你的工具])

result = agent.invoke({"messages": [{"role": "user", "content": "你的问题"}]})
print(result["messages"][-1].content)
```

---

## 今日总结

- 我已经掌握：
  - LangChain Models 的三种调用方式（invoke/stream/batch）
  - `init_chat_model` 统一入口用法
  - 环境变量加载与多提供商适配
  - Tool-calling Agent 的工作原理
  - `@tool` 装饰器和 `create_agent` 用法
  - ReAct 循环的执行流程
  - 多轮对话和流式输出的实现
- 仍不清楚：
  - 实际项目中 batch 的性能优化细节（需要 benchmark）
  - 动态工具选择、middleware 扩展等高级用法

## 明天计划

- Day 3：LangGraph workflow（Graph API / Functional API）+ MCP 接入

## 关联文件

- 示例代码：`examples/day02_models/demo_01_models_invoke_stream_batch.py`
- 示例代码：`examples/day02_models/demo_02_tool_calling_agent.py`
- 配置文件：`pyrightconfig.json`