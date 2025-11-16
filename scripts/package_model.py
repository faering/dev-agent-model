#!/usr/bin/env python3
import argparse
import tarfile
from pathlib import Path

from utils import ensure_dir


def make_tarball(src: Path, out: Path):
    ensure_dir(out.parent)

    with tarfile.open(out, "w:gz") as tar:
        tar.add(src, arcname=src.name)

    print(f"[package] Created: {out}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="model_src")
    parser.add_argument("--version", required=True)
    parser.add_argument("--out-dir", default="dist")
    args = parser.parse_args()

    src = Path(args.src)
    out = Path(args.out_dir) / f"model-{args.version}.tar.gz"

    make_tarball(src, out)


if __name__ == "__main__":
    main()
