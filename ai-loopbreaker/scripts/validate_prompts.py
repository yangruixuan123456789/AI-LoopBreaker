#!/usr/bin/env python3
"""Validate LoopBreaker metadata and prompt-file consistency."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return {}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)}: malformed frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def validate_markdown(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    fence_count = sum(1 for line in text.splitlines() if line.startswith("```"))
    if fence_count % 2:
        fail(f"{path.relative_to(ROOT)}: unbalanced triple-backtick fences")
    if not text.strip():
        fail(f"{path.relative_to(ROOT)}: empty file")


def heading_count(path: Path) -> int:
    return sum(
        1
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("#")
    )


def main() -> int:
    manifest_path = ROOT / "prompts" / "manifest.json"
    manifest = load_json(manifest_path)

    required_manifest_keys = {
        "schema_version",
        "name",
        "version",
        "languages",
        "core",
        "core_zh",
        "prompts",
    }
    missing = required_manifest_keys.difference(manifest)
    if missing:
        fail(f"prompts/manifest.json: missing keys: {sorted(missing)}")

    if manifest.get("schema_version") != 2:
        fail("prompts/manifest.json: expected schema_version 2")
    if manifest.get("languages") != ["en", "zh-CN"]:
        fail("prompts/manifest.json: expected languages ['en', 'zh-CN']")

    core_files = {
        "en": ROOT / manifest.get("core", ""),
        "zh-CN": ROOT / manifest.get("core_zh", ""),
    }
    core_heading_counts: dict[str, int] = {}
    for language, core_path in core_files.items():
        if not core_path.is_file():
            fail(f"prompts/manifest.json: {language} core prompt does not exist: {core_path}")
            continue
        validate_markdown(core_path)
        metadata = frontmatter(core_path)
        if metadata.get("id") != "LB-00":
            fail(f"{core_path.relative_to(ROOT)}: expected id LB-00")
        if metadata.get("version") != manifest.get("version"):
            fail(f"{core_path.relative_to(ROOT)}: version differs from manifest")
        if metadata.get("language") != language:
            fail(f"{core_path.relative_to(ROOT)}: expected language {language}")
        core_heading_counts[language] = heading_count(core_path)

    if len(set(core_heading_counts.values())) > 1:
        fail(f"core language variants have different heading counts: {core_heading_counts}")

    seen_ids: set[str] = set()
    seen_files: set[str] = set()
    for index, entry in enumerate(manifest.get("prompts", []), start=1):
        prompt_id = entry.get("id")
        relative = entry.get("file")
        relative_zh = entry.get("file_zh")
        expected_id = f"LB-{index:02d}"

        if prompt_id != expected_id:
            fail(f"manifest prompt #{index}: expected id {expected_id}, got {prompt_id!r}")
        if prompt_id in seen_ids:
            fail(f"manifest: duplicate id {prompt_id!r}")
        if relative in seen_files:
            fail(f"manifest: duplicate file {relative!r}")
        if not relative_zh:
            fail(f"manifest prompt {prompt_id}: missing Chinese file")
        elif relative_zh in seen_files:
            fail(f"manifest: duplicate file {relative_zh!r}")
        if not entry.get("use_when_zh"):
            fail(f"manifest prompt {prompt_id}: missing Chinese use_when_zh")
        seen_ids.add(prompt_id)
        seen_files.add(relative)
        seen_files.add(relative_zh)

        if not relative or not relative_zh:
            continue
        variant_files = {
            "en": ROOT / relative,
            "zh-CN": ROOT / relative_zh,
        }
        heading_counts: dict[str, int] = {}
        for language, path in variant_files.items():
            if not path.is_file():
                fail(f"manifest: missing {language} prompt file {path.relative_to(ROOT)}")
                continue

            validate_markdown(path)
            metadata = frontmatter(path)
            if metadata.get("id") != prompt_id:
                fail(f"{path.relative_to(ROOT)}: frontmatter id does not match manifest")
            if metadata.get("name") != entry.get("name"):
                fail(f"{path.relative_to(ROOT)}: frontmatter name does not match manifest")
            if metadata.get("version") != manifest.get("version"):
                fail(f"{path.relative_to(ROOT)}: version differs from manifest")
            if metadata.get("language") != language:
                fail(f"{path.relative_to(ROOT)}: expected language {language}")
            heading_counts[language] = heading_count(path)

        if len(set(heading_counts.values())) > 1:
            fail(
                f"{relative}: language variants have different heading counts: "
                f"{heading_counts}"
            )

    adapter_pairs = [
        ("prompts/adapters/kickoff.md", "prompts/adapters/kickoff.zh.md"),
        ("prompts/adapters/AGENTS.md", "prompts/adapters/AGENTS.zh.md"),
        ("prompts/adapters/CLAUDE.md", "prompts/adapters/CLAUDE.zh.md"),
        ("prompts/adapters/cursor.mdc", "prompts/adapters/cursor.zh.mdc"),
    ]
    for relative, relative_zh in adapter_pairs:
        for candidate in (relative, relative_zh):
            path = ROOT / candidate
            if not path.is_file():
                fail(f"missing bilingual adapter file {candidate}")
            else:
                validate_markdown(path)

    kickoff_metadata = frontmatter(ROOT / "prompts/adapters/kickoff.md")
    kickoff_zh_metadata = frontmatter(ROOT / "prompts/adapters/kickoff.zh.md")
    if kickoff_metadata.get("id") != "LB-KICKOFF":
        fail("prompts/adapters/kickoff.md: expected id LB-KICKOFF")
    if kickoff_zh_metadata.get("id") != "LB-KICKOFF":
        fail("prompts/adapters/kickoff.zh.md: expected id LB-KICKOFF")
    if kickoff_metadata.get("version") != manifest.get("version"):
        fail("prompts/adapters/kickoff.md: version differs from manifest")
    if kickoff_zh_metadata.get("version") != manifest.get("version"):
        fail("prompts/adapters/kickoff.zh.md: version differs from manifest")
    if kickoff_metadata.get("language") != "en":
        fail("prompts/adapters/kickoff.md: expected language en")
    if kickoff_zh_metadata.get("language") != "zh-CN":
        fail("prompts/adapters/kickoff.zh.md: expected language zh-CN")

    eval_path = ROOT / "evals" / "cases.json"
    evals = load_json(eval_path)
    eval_cases = evals.get("cases", [])
    eval_ids = [case.get("expected_loop") for case in eval_cases]
    if evals.get("version") != 2:
        fail("evals/cases.json: expected version 2")
    if not evals.get("description_zh"):
        fail("evals/cases.json: missing Chinese description")
    if len(eval_ids) != len(set(eval_ids)):
        fail("evals/cases.json: duplicate expected_loop coverage")
    for case in eval_cases:
        case_id = case.get("id", "<unknown>")
        if len(case.get("turns", [])) != len(case.get("turns_zh", [])):
            fail(f"evals/cases.json: {case_id} has mismatched bilingual turn counts")
        if len(case.get("required_signals", [])) != len(
            case.get("required_signals_zh", [])
        ):
            fail(f"evals/cases.json: {case_id} has mismatched bilingual signal counts")
    if sorted(eval_ids) != sorted(seen_ids):
        fail(
            "evals/cases.json: expected_loop coverage must match manifest prompts "
            f"(expected {sorted(seen_ids)}, got {sorted(eval_ids)})"
        )

    bilingual_pairs = [
        ("README.md", "README.en.md"),
        ("CONTRIBUTING.md", "CONTRIBUTING.en.md"),
        ("GITHUB_IMPORT.zh.md", "GITHUB_IMPORT.en.md"),
        ("docs/why-ai-loops.md", "docs/why-ai-loops.en.md"),
        ("docs/prompt-design.md", "docs/prompt-design.en.md"),
        ("evals/README.zh.md", "evals/README.md"),
        ("examples/debugging-loop.zh.md", "examples/debugging-loop.md"),
        ("examples/false-completion.zh.md", "examples/false-completion.md"),
        ("examples/fix-coverage.zh.md", "examples/fix-coverage.md"),
    ]
    for relative_zh, relative_en in bilingual_pairs:
        for relative in (relative_zh, relative_en):
            if not (ROOT / relative).is_file():
                fail(f"missing bilingual document {relative}")

    for path in [
        ROOT / "README.md",
        ROOT / "README.en.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "CONTRIBUTING.en.md",
        ROOT / "GITHUB_IMPORT.zh.md",
        ROOT / "GITHUB_IMPORT.en.md",
        *sorted((ROOT / "docs").glob("*.md")),
        *sorted((ROOT / "examples").glob("*.md")),
        *sorted((ROOT / "evals").glob("*.md")),
        *sorted((ROOT / "prompts" / "adapters").glob("*.md")),
        *sorted((ROOT / "prompts" / "adapters").glob("*.mdc")),
        *sorted((ROOT / "prompts" / "patterns").glob("*.zh.md")),
    ]:
        validate_markdown(path)

    if ERRORS:
        print("LoopBreaker validation failed:", file=sys.stderr)
        for error in ERRORS:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(
        f"OK: {len(seen_ids)} prompt pairs ({len(seen_ids) * 2} files), "
        f"{len(evals.get('cases', []))} eval cases, manifest version {manifest.get('version')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
