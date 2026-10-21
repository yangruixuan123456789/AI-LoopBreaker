# LoopBreaker 项目指令

对所有非平凡任务应用 `prompts/core/loopbreaker.zh.md`。

任务开始时，建立目标、可观察的完成条件、硬约束、当前已验证状态、关键未知和下一取证动作。

出现对应循环时，加载 `prompts/patterns/` 中的中文专项提示词：

- 目标漂移：`lb-01-goal-drift.zh.md`
- 重复追问：`lb-02-clarification-ping-pong.zh.md`
- 未验证假设：`lb-03-assumption-tunnel.zh.md`
- 反复修复：`lb-04-fix-loop.zh.md`
- 单边取证：`lb-05-hypothesis-lock.zh.md`
- 遗忘状态：`lb-06-context-amnesia.zh.md`
- 工具空转：`lb-07-tool-busywork.zh.md`
- 道歉与复述循环：`lb-08-agreement-loop.zh.md`
- 未验证完成：`lb-09-false-completion.zh.md`
- 范围扩大：`lb-10-scope-spiral.zh.md`
- 重复规划：`lb-11-planning-treadmill.zh.md`
- 可避免的用户移交：`lb-12-dependency-handoff.zh.md`
- 局部修复漏项：`lb-13-fix-coverage.zh.md`

如果连续两个回合重复同一个阻塞、动作或结论，且没有新证据，停止扩写当前路径。说明重复模式、根因未知、最小下一实验和完成条件。获得授权后，立即执行下一个安全动作。

把文件修改、命令输出、测试和外部观察视为证据。语气变化、道歉、更长的解释和重复计划都不算进展。
