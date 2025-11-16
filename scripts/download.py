#!/usr/bin/env python3
import argparse
import time
import sys
from pathlib import Path
from huggingface_hub import snapshot_download
from huggingface_hub.errors import RepositoryNotFoundError

from .utils import ensure_dir, get_token


def download_model(repo_id: str, out_dir: Path, revision: str | None = None):
    token = get_token()

    out_dir = ensure_dir(out_dir)

    max_retries = 3
    retry_backoff = 2.0
    attempt = 0

    while attempt < max_retries:
        try:
            print(
                f"[download] Attempt {attempt+1} downloading {repo_id} → {out_dir}")

            downloaded = snapshot_download(
                repo_id=repo_id,
                revision=revision,
                allow_patterns=None,
                token=token,
                local_dir=str(out_dir),
                local_dir_use_symlinks=False,
            )

            print(f"[download] Done → {downloaded}")
            return Path(downloaded)

        except RepositoryNotFoundError as e:
            raise RuntimeError(
                f"The repo {repo_id} does not exist or is private.") from e

        except Exception as e:
            attempt += 1
            if attempt == max_retries:
                raise RuntimeError("Download failed after retries.") from e

            wait = retry_backoff * (2 ** (attempt - 1))
            print(
                f"[download] Error: {e}. Retrying in {wait}s...", file=sys.stderr)
            time.sleep(wait)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-id", required=True)
    parser.add_argument("--out", default="model")
    parser.add_argument("--revision")
    args = parser.parse_args()

    download_model(args.repo_id, Path(args.out), args.revision)


if __name__ == "__main__":
    main()
