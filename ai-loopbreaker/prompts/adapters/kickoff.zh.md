---
id: LB-KICKOFF
name: Task Kickoff
version: 0.3.0
language: zh-CN
summary_en: Establish the goal, acceptance condition, constraints, and state anchor when a task begins.
summary_zh: 在任务开始时建立目标、验收、约束和状态锚点。
---

# LoopBreaker 任务启动词

本任务使用 LoopBreaker 协议。

进行重要修改前，根据请求和现有上下文建立以下契约：

```text
目标：
完成条件：
硬约束：
非目标：
最新已验证状态：
当前未知：
第一动作：
```

然后：

1. 先用现有工具解决可获取的未知信息，再询问用户。
2. 对低影响未知项选择可逆默认值，并明确标注。
3. 如果缺失事实确实来自外部，或会改变不可逆结果，只问一个与决策有关的问题。
4. 采取能够改变证据、工件、决策或已验证状态的最小动作。
5. 如果同一个阻塞、修复、问题或结论连续两个回合重复且没有新证据，停止并输出 LoopBreaker 报告。
6. 验收条件经过观察或测试前，不要报告 `complete / 已完成`。

工作完成时报告：

```text
状态：
已改变：
验证方式：
残余风险：
需要用户决策（仅当存在时）：
```

任务：

> [在这里描述任务。]
