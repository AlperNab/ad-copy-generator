# Ad Copy Generator

This folder has been upgraded into a **standalone real GUI project**.

Run the project GUI:

```bash
./run_gui.sh
```

Windows:

```powershell
.\run_gui_windows.ps1
```

Default local URL: `http://127.0.0.1:9100`

This project includes its own FastAPI backend, browser GUI, provider settings, local/cloud LLM routing, encrypted API-key storage, file uploads, job history, exports, and a project-specific plugin configuration.

See `PROJECT_IMPLEMENTATION.md` and `project_config.json` for the applied project-specific features and customization controls.

---

## Original README

# ad-copy-generator

> **Product + audience → ad copy for every platform.** Google Ads, Meta (FB/IG), TikTok, LinkedIn, Twitter/X, Pinterest, Email, SMS — all generated in one command. Includes A/B test variants and hooks.

[![PyPI](https://img.shields.io/pypi/v/ad-copy-generator?style=flat)](https://pypi.org/project/ad-copy-generator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Quickstart

```bash
pip install ad-copy-generator

python -m ad_copy_generator "Portable Blender" "fitness enthusiasts aged 22-35" \
  --value-prop "Smoothies anywhere in 30 seconds" \
  --price "\$28" --offer "20% off first order"
```

## What you get

For each platform, generated copy includes:

- **Google Ads** — 15 headlines + 4 descriptions for responsive search ads + keyword suggestions
- **Meta** — 3 copy variants (pain/social proof/urgency) with hooks, body, and CTAs
- **TikTok** — 3-second hook scripts, caption, hashtags, sound suggestions
- **LinkedIn** — sponsored content + InMail subject and body
- **Twitter/X** — tweet + thread opener
- **Email** — 5 A/B-testable subject lines
- **SMS** — under 160 chars

## Python API

```python
from ad_copy_generator import generate

copy = generate(
    product="Ergonomic Chair",
    audience="remote workers with back pain",
    value_prop="Zero back pain in 30 days or money back",
    tone="empathetic",
    platforms=["google", "meta", "email"]
)
print(copy["meta"]["variants"][0]["hook"])
```

## License
MIT © [Alper Nabil Gabra Zakher](https://github.com/AlperNab)
