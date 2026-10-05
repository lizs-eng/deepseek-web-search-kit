# deepseek-web-search-kit

让 DeepSeek / Qwen 的 API 真正联网的最小可用示例。

网上教程互相矛盾：有人说 Responses API 能联网，有人说必须 Anthropic 端点，还有人让你自己拼搜索 API。本仓库用可运行的代码讲清一条路径：怎么开、流式怎么写、引用来源怎么拿。

## 快速开始

```bash
git clone https://github.com/lizs-eng/deepseek-web-search-kit.git
cd deepseek-web-search-kit
pip install -r requirements.txt

# Windows
set DEEPSEEK_API_KEY=sk-你的key
# macOS / Linux
export DEEPSEEK_API_KEY=sk-你的key

python examples/deepseek_anthropic_search.py "今天杭州天气怎么样"
```

## 仓库结构

```
examples/
  deepseek_anthropic_search.py   # DeepSeek Anthropic 兼容端点：联网搜索 + 流式 + 引用来源
requirements.txt
```

## 这个示例做了什么

- 走 DeepSeek 的 **Anthropic 兼容端点**（`https://api.deepseek.com/anthropic`）——官方支持服务端联网搜索的端点之一
- 服务端搜索工具 `web_search`，`max_uses=3` 控制调用成本
- 流式输出回答，结束后自动提取本次引用的来源 URL

> 已知坑：搜索工具的类型版本号会随官方升级变化。若报 400 invalid tool type，把代码里的
> `web_search_20260209` 换成 `web_search_20250305`（或反之）再试。

## 完整版

付费版在免费样章之上追加两条路径与一本排错手册：

- **Responses API**（`/v1/responses`）联网路径，含流式
- **Qwen（阿里云百炼）** 思考模式 + 联网搜索，流式读取 `reasoning_content`
- **端点对照表**：三条路径 × 联网/思考/流式 支持矩阵 + 六类常见报错的处理方法

→ 完整版与更多作品：[面包多小店](https://mbd.pub/o/engineer)

## 校准与许可

- 端点行为以 2026-10 官方文档校准，之后可能变化；发现失效欢迎提 issue
- 许可：MIT（见 LICENSE）
# deepseek-web-search-kit · DeepSeek/Qwen 联网搜索示例包

让 DeepSeek / Qwen API 真正"联网"的最小可用代码包。

网上教程互相矛盾：有人说 Responses API 能联网，有人说要 Anthropic 端点，还有人让你自己接搜索 API。
本包用**可运行的代码**把每条路径讲清楚：哪条端点能联网、怎么开、流式怎么写、思考模式怎么配、报错了怎么对照。

## 免费样章（本仓库）

- [`examples/deepseek_anthropic_search.py`](examples/deepseek_anthropic_search.py)
  DeepSeek **Anthropic 兼容端点**原生联网搜索：流式输出 + 引用来源提取，单文件即可跑。

```bash
pip install -r requirements.txt
set DEEPSEEK_API_KEY=sk-你的key
python examples/deepseek_anthropic_search.py "今天杭州天气怎么样"
```

## 完整版（¥19.9）

在免费样章基础上追加：

| 内容 | 说明 |
|---|---|
| `deepseek_responses_search.py` | Responses API（`/v1/responses`）联网路径，含流式 |
| `qwen_thinking_stream.py` | Qwen（阿里云百炼）思考模式 + 联网搜索，流式读取 `reasoning_content` |
| `docs/端点对照表.md` | 三条路径 × 联网/思考/流式 支持矩阵 + 常见报错对照表 |
| 追问支持 | 端点升级导致失效时，一处更新全员可用 |

购买地址：（上架后回填）

## 免责说明

各端点行为随官方升级可能变化（2026-10 校准）。示例代码按当时官方文档编写并标注来源，如遇 400/工具类型报错，请优先查 `docs/端点对照表.md` 的"常见报错"节。
# deepseek-web-search-kit
让 DeepSeek/Qwen API 真正联网的最小可用示例包：三条端点路径 + 流式 + 思考模式
