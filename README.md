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
