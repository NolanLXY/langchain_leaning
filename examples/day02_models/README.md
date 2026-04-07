# Day 2 - Models: invoke / stream / batch

## 目标

使用 OpenAI 跑通 LangChain `invoke`、`stream`、`batch` 三种调用方式。

## 依赖安装

```bash
pip install -U langchain langchain-openai python-dotenv
```

## .env 配置

在项目根目录新建或更新 `.env`：

```env
# 方式 A：OpenAI 官方
# OPENAI_API_KEY=你的OpenAIKey
# OPENAI_MODEL=gpt-4o-mini
# OPENAI_BASE_URL=https://api.openai.com/v1

# 方式 B：千问（OpenAI 兼容模式，推荐你当前场景）
DASHSCOPE_API_KEY=你的千问Key
QWEN_MODEL=qwen-plus
# 可选；不写时 demo 会自动用这个默认值
# DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

## 运行方式

```bash
python examples/day02_models/demo_01_models_invoke_stream_batch.py
```

## 关键点

- `invoke`：单次请求，最直观。
- `stream`：边生成边返回，适合对话 UI。
- `batch`：多个输入并发处理，提升吞吐。

## 常见报错

- `未设置 API Key`：检查 `.env` 是否配置了 `OPENAI_API_KEY` 或 `DASHSCOPE_API_KEY`。
- `ModuleNotFoundError`：先执行依赖安装。
