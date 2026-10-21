# 评测用例

**中文** | [English](README.md)

`cases.json` 是一组用于人工测试助手能否识别常见循环的小型评测集。
每个用例都包含成对的 `turns` / `turns_zh` 和 `required_signals` / `required_signals_zh` 字段。

可以按以下方式使用：

1. 把某个 case 作为前序对话提供给助手，要求它审计。
2. 在日常任务中使用相同场景，观察助手是否会主动打断循环。
3. 对相同 case 比较使用和不使用 LoopBreaker 时的行为。

只有同时提出真正能改变信息状态的下一动作，循环识别才有价值。仅仅说出循环名称不算通过。
