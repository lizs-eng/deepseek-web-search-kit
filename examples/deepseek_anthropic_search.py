"""DeepSeek 原生联网搜索 · Anthropic 兼容端点版（免费样章）

为什么单独讲这个端点？DeepSeek 的"联网搜索"能力按 API 端点区分：

  - OpenAI 兼容 /chat/completions ：不支持 web_search 工具（参数被忽略或 400）
  - OpenAI Responses API  /v1/responses：支持 web_search（见完整版）
  - Anthropic 兼容端点（本例）：原生支持服务端联网搜索，返回引用来源 ✅

用法：
    set DEEPSEEK_API_KEY=sk-xxxxxxxx          # Windows
    export DEEPSEEK_API_KEY=sk-xxxxxxxx       # macOS/Linux
    python deepseek_anthropic_search.py "今天杭州天气怎么样"

依赖：
    pip install anthropic
"""

import os
import sys

from anthropic import Anthropic

# Anthropic 兼容端点：模型名沿用 claude 系列，服务端映射到 DeepSeek 模型
BASE_URL = "https://api.deepseek.com/anthropic"
MODEL = "claude-sonnet"  # 也可用 "claude-haiku"

# 服务端联网搜索工具。若报 400 invalid tool type，把版本号换成 "web_search_20250305" 再试
# （工具类型版本号随官方升级会变化，完整版文档的"常见报错"节会持续更新）
WEB_SEARCH_TOOL = {
    "type": "web_search_20260209",
    "name": "web_search",
    "max_uses": 3,  # 最多发起几次搜索，控制成本
}


def ask(question: str) -> str:
    """流式提问并打印回答；回答结束后打印引用来源列表。"""
    client = Anthropic(api_key=os.environ["DEEPSEEK_API_KEY"], base_url=BASE_URL)

    with client.messages.stream(
        model=MODEL,
        max_tokens=2048,
        tools=[WEB_SEARCH_TOOL],
        messages=[{"role": "user", "content": question}],
    ) as stream:
        print("--- 回答 ---")
        for text in stream.text_stream:
            print(text, end="", flush=True)
        print()
        final = stream.get_final_message()

    print("\n--- 引用来源 ---")
    seen = set()
    for block in final.content:
        if getattr(block, "type", "") == "web_search_tool_result":
            for item in getattr(block, "content", []) or []:
                url = getattr(item, "url", None)
                title = getattr(item, "title", None) or url
                if url and url not in seen:
                    seen.add(url)
                    print(f"[{len(seen)}] {title}\n    {url}")

    return "".join(
        b.text for b in final.content if getattr(b, "type", "") == "text"
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('用法: python deepseek_anthropic_search.py "你的问题"')
        sys.exit(1)
    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("请先设置环境变量 DEEPSEEK_API_KEY")
        sys.exit(1)
    ask(sys.argv[1])
