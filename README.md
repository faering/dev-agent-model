# dev-agent-model

This repository handles everything related to preparing a **local model** for the `dev-agent`.

## Todo

- [ ] Modify codebase to check if download model is already quantized (quantization step is hardcoded in release workflow)<br>
- [ ] Check if there is a better format for the release asset in Github, currently released in .tar.gz

## Features

- Secure download from Hugging Face Hub
- Optional quantization (GGUF / GPTQ)
- Packaging a deterministic `.tar.gz` model bundle
- Automatic publishing via GitHub Releases

## Scripts

| Script | Purpose |
|-------|---------|
| `download.py` | Download HF model securely |
| `quantize.py` | Convert or quantize to GGUF / GPTQ |
| `package_model.py` | Build versioned tarball for release |

## Releasing a New Version

Run the workflow manually from GitHub Actions:

**Build & Release Model → Run workflow**

Inputs:
- `repo_id`: e.g. `meta-llama/Meta-Llama-3.1-8B`
- `model_version`: e.g. `v0.1.0`

