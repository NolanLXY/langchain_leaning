"""
Demo: Tool-calling Agent（工具调用代理）

展示 LangChain 1.0+ 的 create_agent 如何让模型调用工具完成任务。
核心流程：模型思考 -> 调用工具 -> 获取结果 -> 循环直到输出最终答案
"""

from __future__ import annotations

import os
import random
from operator import add, mul, sub, truediv

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool


# ==================== 1. 工具定义 ====================

@tool
def get_weather(location: str) -> str:
    """
    获取指定城市的天气信息。

    Args:
        location: 城市名称，如 "北京"、"上海"

    Returns:
        天气描述字符串
    """
    # 模拟天气数据（实际项目中可接入真实天气 API）
    weather_options = ["晴", "多云", "阴", "小雨", "雷阵雨"]
    temp_range = range(15, 35)

    weather = random.choice(weather_options)
    temp = random.choice(temp_range)

    return f"{location}今日天气：{weather}，温度 {temp}°C"


@tool
def calculate(a: float, b: float, op: str) -> str:
    """
    执行简单的算术运算。

    Args:
        a: 第一个数字
        b: 第二个数字
        op: 运算符，可选 "+", "-", "*", "/"

    Returns:
        计算结果字符串
    """
    # 映射运算符到函数
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
    }

    if op not in ops:
        return f"错误：不支持的运算符 '{op}'，请使用 +, -, *, /"

    try:
        result = ops[op](a, b)
        # 处理除法结果格式
        if op == "/":
            result = float(result)
            if not result.is_integer():
                result = round(result, 2)
        else:
            result = float(result)
        return str(int(result) if result.is_integer() else result)
    except ZeroDivisionError:
        return "错误：除数不能为零"


# ==================== 2. 模型初始化 ====================

def build_model():
    """初始化聊天模型，兼容 OpenAI 和阿里云 DashScope"""
    _ = load_dotenv()

    api_key = (
        os.getenv("OPENAI_API_KEY")
        or os.getenv("DASHSCOPE_API_KEY")
        or os.getenv("QIANWEN_API_KEY")
    )
    if not api_key:
        raise RuntimeError(
            "未设置 API Key。请在 .env 配置 OPENAI_API_KEY 或 DASHSCOPE_API_KEY"
        )

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

    return init_chat_model(
        model=model_name,
        model_provider="openai",
        api_key=api_key,
        base_url=base_url,
        temperature=0,
    )


# ==================== 3. Agent 调用示例 ====================

def demo_weather_agent(model) -> None:
    """Demo 1: 天气查询 agent"""
    print("\n" + "=" * 18 + " 天气查询 Agent " + "=" * 18)

    # 创建 agent，绑定工具
    agent = create_agent(
        model=model,
        tools=[get_weather],
        # 可选：设置系统提示，让 agent 更明确自己的角色
        system_prompt="你是一个乐于助人的助手。当用户询问天气时，使用提供的工具获取天气信息，然后简洁地回答。",
    )

    # 调用 agent
    result = agent.invoke({
        "messages": [{"role": "user", "content": "北京今天的天气怎么样？"}]
    })

    # 打印最终回复（最后一条 AI 消息）
    final_message = result["messages"][-1]
    print(f"Agent 回复：{final_message.content}")


def demo_calculator_agent(model) -> None:
    """Demo 2: 计算器 agent"""
    print("\n" + "=" * 18 + " 计算器 Agent " + "=" * 18)

    agent = create_agent(
        model=model,
        tools=[calculate],
        system_prompt="你是一个计算器助手。使用提供的 calculate 工具执行数学运算。",
    )

    result = agent.invoke({
        "messages": [{"role": "user", "content": "帮我算一下 125 乘以 8 等于多少？"}]
    })

    final_message = result["messages"][-1]
    print(f"Agent 回复：{final_message.content}")


def demo_multi_turn_agent(model) -> None:
    """Demo 3: 多轮对话，组合使用多个工具"""
    print("\n" + "=" * 18 + " 多轮对话 Agent " + "=" * 18)

    # 同时提供两个工具，agent 会根据问题自动选择使用哪个
    agent = create_agent(
        model=model,
        tools=[get_weather, calculate],
    )

    # 第一轮：天气查询
    result1 = agent.invoke({
        "messages": [{"role": "user", "content": "上海天气如何？"}]
    })
    print("用户：上海天气如何？")
    print(f"Agent：{result1['messages'][-1].content}\n")

    # 第二轮：计算（agent 会记住之前的对话上下文）
    result2 = agent.invoke({
        "messages": result1["messages"] + [{"role": "user", "content": "那 99 加 101 等于多少？"}]
    })
    print("用户：那 99 加 101 等于多少？")
    print(f"Agent：{result2['messages'][-1].content}")


def demo_stream_agent(model) -> None:
    """Demo 4: 流式输出（实时看到思考过程）"""
    print("\n" + "=" * 18 + " 流式输出 Agent " + "=" * 18)

    agent = create_agent(
        model=model,
        tools=[get_weather, calculate],
    )

    print("用户：广州天气怎么样？顺便帮我算一下 50 除以 4。\n")
    print("Agent 输出：", end="", flush=True)

    # stream_mode="values" 返回每一步的完整状态
    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": "广州天气怎么样？顺便帮我算一下 50 除以 4。"}]},
        stream_mode="values"
    ):
        messages = chunk.get("messages", [])
        if messages:
            latest = messages[-1]
            # 打印工具调用
            if hasattr(latest, "tool_calls") and latest.tool_calls:
                for tc in latest.tool_calls:
                    print(f"\n[调用工具] {tc['name']}: {tc['args']}", end="", flush=True)
            # 打印文本输出
            elif hasattr(latest, "content") and latest.content:
                print(latest.content, end="", flush=True)
    print()


# ==================== 4. 主入口 ====================

def main() -> None:
    """按顺序运行所有 demo"""
    model = build_model()

    demo_weather_agent(model)       # 单工具：天气查询
    demo_calculator_agent(model)   # 单工具：计算器
    demo_multi_turn_agent(model)   # 多工具 + 多轮对话
    demo_stream_agent(model)       # 流式输出

    print("\n[*] 所有 demo 运行完成！")
    print("\n[*] 关键概念回顾：")
    print("  1. @tool 装饰器：将 Python 函数转换为 LangChain 工具")
    print("  2. create_agent：创建 agent，自动处理 ReAct 循环")
    print("  3. agent.invoke()：调用 agent，传入消息列表")
    print("  4. 多工具：agent 会根据问题自动选择合适的工具")


if __name__ == "__main__":
    main()