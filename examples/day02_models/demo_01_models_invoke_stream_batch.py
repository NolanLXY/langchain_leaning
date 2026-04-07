from __future__ import annotations

import os
from collections.abc import Sequence

from dotenv import load_dotenv
from langchain.chat_models import BaseChatModel, init_chat_model
from langchain_core.messages import BaseMessage, BaseMessageChunk, HumanMessage
from langchain_core.language_models.base import LanguageModelInput


def print_header(title: str) -> None:
    # 在终端输出分隔线，便于观察每段 demo 的结果
    print("\n" + "=" * 18 + f" {title} " + "=" * 18)


def build_model() -> BaseChatModel:
    # 从项目根目录加载 .env 里的环境变量
    _ = load_dotenv()
    # 兼容两类配置：
    # 1) OpenAI 官方：OPENAI_API_KEY + OPENAI_BASE_URL(可选) + OPENAI_MODEL(可选)
    # 2) 千问兼容模式：DASHSCOPE_API_KEY/QIANWEN_API_KEY + (可选) DASHSCOPE_BASE_URL
    api_key = (
        os.getenv("OPENAI_API_KEY")
        or os.getenv("DASHSCOPE_API_KEY")
        or os.getenv("QIANWEN_API_KEY")
    )
    if not api_key:
        raise RuntimeError(
            "未设置 API Key。请在 .env 配置 OPENAI_API_KEY 或 DASHSCOPE_API_KEY（或 QIANWEN_API_KEY）。"
        )

    # 如果你用的是千问 Key，默认走 DashScope 的 OpenAI 兼容地址
    base_url = (
        os.getenv("OPENAI_BASE_URL")
        or os.getenv("DASHSCOPE_BASE_URL")
        or (
            "https://dashscope.aliyuncs.com/compatible-mode/v1"
            if (os.getenv("DASHSCOPE_API_KEY") or os.getenv("QIANWEN_API_KEY"))
            else None
        )
    )
    model_name = os.getenv("OPENAI_MODEL") or os.getenv("QWEN_MODEL") or "qwen-plus"

    # 使用 LangChain 官方统一入口创建 OpenAI 聊天模型
    # 这里不直接导入 langchain_openai，能减少编辑器静态分析误报
    return init_chat_model(
        model=model_name,
        model_provider="openai",
        api_key=api_key,
        base_url=base_url,
        temperature=0,
    )


def demo_invoke(model: BaseChatModel) -> None:
    # invoke：单次输入，等待模型完整返回
    print_header("1) invoke")
    msg = HumanMessage(content="用一句话解释什么是 LangChain 的 invoke。")
    resp: BaseMessage = model.invoke([msg])
    print(resp.text)


def demo_stream(model: BaseChatModel) -> None:
    # stream：边生成边返回，适合聊天 UI 的实时输出
    print_header("2) stream")
    msg = HumanMessage(content="分三点langchain简述 stream 的典型使用场景。")
    print("输出中：", end="", flush=True)
    for chunk in model.stream([msg]):
        # 每个 chunk 都是部分结果，逐段打印到同一行
        typed_chunk: BaseMessageChunk = chunk
        print(typed_chunk.text, end="", flush=True)
    print()


def demo_batch(model: BaseChatModel) -> None:
    # batch：一次提交多条输入，结果顺序与输入顺序一致
    print_header("3) batch")
    prompts: list[LanguageModelInput] = [
        (HumanMessage(content="用一句话解释 langchain 中 batch 的用法。"),),
        (HumanMessage(content="用一句话解释 langchain中stream 和 invoke 的区别。"),),
        (HumanMessage(content="用一句话解释 langchain什么时候不用 batch。"),),
    ]
    results: Sequence[BaseMessage] = model.batch(prompts)
    for i, item in enumerate(results, start=1):
        print(f"[{i}] {item.text}")


def main() -> None:
    # 主流程：初始化模型后，按 invoke -> stream -> batch 顺序演示
    model = build_model()
    demo_invoke(model)
    demo_stream(model)
    demo_batch(model)


if __name__ == "__main__":
    main()
