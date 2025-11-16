#!/usr/bin/env python3
"""
quantize.py
Quantize the downloaded model to GGUF or GPTQ.
This is only a template; adjust to your target quantizer.
"""

import argparse
from pathlib import Path

from utils import ensure_dir

#################################
# GGUF QUANTIZATION (llama.cpp)
#################################


def quantize_gguf(model_dir: Path, out_dir: Path, qtype="Q4_K_M"):
    """
    Requires llama.cpp installed.
    """
    import subprocess

    ensure_dir(out_dir)

    cmd = [
        "python3",
        "convert.py",  # from llama.cpp repo
        "--outtype", qtype,
        "--model", str(model_dir),
        "--output", str(out_dir / f"model-{qtype}.gguf"),
    ]

    print("[quantize] Running llama.cpp quantization:", " ".join(cmd))
    subprocess.check_call(cmd)

#################################
# GPTQ QUANTIZATION
#################################


def quantize_gptq(model_dir: Path, out_dir: Path, wbits=4, groupsize=128):
    """
    Requires AutoGPTQ installed.
    """
    ensure_dir(out_dir)
    print("[quantize] GPTQ example placeholder.")
    print("You would load model with AutoGPTQ and save quantized files here.")
    # Full AutoGPTQ code can be added later.


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-dir", required=True)
    parser.add_argument("--out", default="model_src_quantized")
    parser.add_argument("--method", choices=["gguf", "gptq"], default="gguf")
    args = parser.parse_args()

    model_dir = Path(args.model_dir)
    out_dir = Path(args.out)

    if args.method == "gguf":
        quantize_gguf(model_dir, out_dir)
    else:
        quantize_gptq(model_dir, out_dir)


if __name__ == "__main__":
    main()
