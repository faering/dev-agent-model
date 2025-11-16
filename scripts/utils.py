import os
from pathlib import Path


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def get_token(env_var="HUGGINGFACE_HUB_TOKEN") -> str:
    token = os.getenv(env_var)
    if not token:
        raise RuntimeError(
            f"No token set. Export {env_var} (Hugging Face token with read access)."
        )
    return token
