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
