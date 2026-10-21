# 导入 GitHub

**中文** | [English](GITHUB_IMPORT.en.md)

本说明对应 LoopBreaker `0.3.0`。发布目录提供两种导入包：

```text
ai-loopbreaker-v0.3.0.bundle          # 带完整 Git 历史，推荐
ai-loopbreaker-v0.3.0-github.zip      # 干净源码目录
SHA256SUMS.txt                        # 两个文件的校验值
```

## 方式一：Git Bundle（推荐）

最适合保留提交历史，并直接接管为一个 GitHub 仓库。

1. 在 GitHub 创建一个空仓库。不要初始化 README、License 或 `.gitignore`。
2. 在 bundle 文件所在目录执行：

   ```bash
   git clone ai-loopbreaker-v0.3.0.bundle ai-loopbreaker
   cd ai-loopbreaker
   git remote add origin git@github.com:<你的账号>/<仓库名>.git
   git push -u origin main
   ```

   使用 HTTPS 时，把 remote 地址替换为：

   ```text
   https://github.com/<你的账号>/<仓库名>.git
   ```

3. 在 GitHub 仓库页面确认 `README.md`、`LICENSE`、`.github/workflows/validate.yml` 和 `prompts/` 均存在。

## 方式二：源码 ZIP

适合直接查看或重新初始化仓库。

```bash
unzip ai-loopbreaker-v0.3.0-github.zip
cd ai-loopbreaker
git init -b main
git add .
git commit -m "feat: add bilingual LoopBreaker prompt pack"
git remote add origin <你的 GitHub 仓库地址>
git push -u origin main
```

GitHub 网页的文件上传功能通常不会自动解压 ZIP。请先解压，或者在网页中直接上传解压后的目录内容。

## 导入后建议设置

仓库描述：

> Bilingual prompts that detect and interrupt evidence-free loops in AI-assisted software development.

建议 Topics：

```text
ai-agents
ai-coding
prompt-engineering
developer-tools
claude-code
cursor
codex
bilingual
```

## 验证发布

在仓库根目录运行：

```bash
python3 scripts/validate_prompts.py
```

成功结果应包含：

```text
OK: 13 prompt pairs (26 files), 13 eval cases, manifest version 0.3.0
```

GitHub Actions 也会在 push 和 pull request 时运行同一检查。

## 重新生成发布包

在已有提交的仓库根目录执行：

```bash
python3 scripts/package_release.py --output ../dist
```

脚本会先运行校验，再生成源码 ZIP、Git Bundle 和 `SHA256SUMS.txt`。
