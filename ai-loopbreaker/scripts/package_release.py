#!/usr/bin/env python3
"""Build a clean source ZIP, Git bundle, and checksum file for LoopBreaker."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], *, cwd: Path = ROOT) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT.parent,
        help="Directory for release artifacts (default: parent of the repository).",
    )
    args = parser.parse_args()

    manifest = json.loads(
        (ROOT / "prompts" / "manifest.json").read_text(encoding="utf-8")
    )
    version = manifest["version"]
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)

    run([sys.executable, str(ROOT / "scripts" / "validate_prompts.py")])

    bundle = output / f"ai-loopbreaker-v{version}.bundle"
    zip_path = output / f"ai-loopbreaker-v{version}-github.zip"
    checksums = output / "SHA256SUMS.txt"

    for generated in (bundle, zip_path, checksums):
        generated.unlink(missing_ok=True)

    run(["git", "bundle", "create", str(bundle), "main"])
    run(
        [
            "git",
            "archive",
            "--format=zip",
            "--prefix=ai-loopbreaker/",
            f"--output={zip_path}",
            "HEAD",
        ]
    )

    checksum_lines = [
        f"{sha256(bundle)}  {bundle.name}",
        f"{sha256(zip_path)}  {zip_path.name}",
    ]
    checksums.write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")

    print(f"Version:   {version}")
    print(f"Bundle:    {bundle}")
    print(f"Source ZIP: {zip_path}")
    print(f"Checksums: {checksums}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
