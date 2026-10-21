# Import into GitHub

[中文](GITHUB_IMPORT.zh.md) | **English**

This guide applies to LoopBreaker `0.3.0`. The release directory contains two import formats:

```text
ai-loopbreaker-v0.3.0.bundle          # Full Git history, recommended
ai-loopbreaker-v0.3.0-github.zip      # Clean source directory
SHA256SUMS.txt                        # Checksums for both files
```

## Option 1: Git bundle (recommended)

This preserves the commit history and can be pushed directly into a new GitHub repository.

1. Create an empty GitHub repository. Do not initialize a README, License, or `.gitignore`.
2. From the directory containing the bundle:

   ```bash
   git clone ai-loopbreaker-v0.3.0.bundle ai-loopbreaker
   cd ai-loopbreaker
   git remote add origin git@github.com:<your-account>/<repository>.git
   git push -u origin main
   ```

   For HTTPS, use:

   ```text
   https://github.com/<your-account>/<repository>.git
   ```

3. Verify that `README.md`, `LICENSE`, `.github/workflows/validate.yml`, and `prompts/` are present on GitHub.

## Option 2: Source ZIP

Use this when you want to inspect the files or initialize a new repository yourself.

```bash
unzip ai-loopbreaker-v0.3.0-github.zip
cd ai-loopbreaker
git init -b main
git add .
git commit -m "feat: add bilingual LoopBreaker prompt pack"
git remote add origin <your GitHub repository URL>
git push -u origin main
```

GitHub's browser file uploader does not normally unpack an archive. Extract the ZIP first, or upload the extracted directory contents through the browser.

## Suggested repository settings

Description:

> Bilingual prompts that detect and interrupt evidence-free loops in AI-assisted software development.

Suggested topics:

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

## Verify the release

From the repository root:

```bash
python3 scripts/validate_prompts.py
```

The successful output should include:

```text
OK: 13 prompt pairs (26 files), 13 eval cases, manifest version 0.3.0
```

GitHub Actions runs the same validation on every push and pull request.

## Rebuild release artifacts

From a repository with at least one commit:

```bash
python3 scripts/package_release.py --output ../dist
```

The script validates the prompt pack, then creates the source ZIP, Git bundle, and `SHA256SUMS.txt`.
