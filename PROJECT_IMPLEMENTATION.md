# Ad Copy Generator — Standalone Real GUI Implementation

This folder is now its own runnable project app. It does not depend on the root all-project dashboard at runtime.

## Run

```bash
./run_gui.sh
```

Windows:

```powershell
.\run_gui_windows.ps1
```

Default URL: `http://127.0.0.1:9100`

## What is inside this project folder

- `app/` — FastAPI backend for this project.
- `static/` — elegant browser GUI.
- `plugins/ad-copy-generator.json` — this project’s own feature/customization/input schema.
- `project_config.json` — readable copy of the same project-specific configuration.
- `data/` — local SQLite jobs, uploads, exports.
- `tests/` — verifies this project has a registered real local engine.

## Project-specific scope

- Domain: `Marketing / Ads`
- Target user: `Domain operator, business owner, analyst, or team member who needs this workflow executed reliably.`
- Core job: Product + audience + offer → platform-specific paid ad variants
- Suite: `E-commerce Growth Suite`

## Deep features applied

- campaign objective selector
- funnel stage mapping
- pain/desire angle matrix
- competitor/ad reference input
- claim/compliance checker
- creative prompt generator for images/videos
- A/B testing plan
- UTM/campaign naming

## Customization controls

- `execution_mode` — Execution mode (select)
- `brand_voice` — brand voice (text)
- `forbidden_words` — forbidden words (textarea)
- `platform` — platform (select)
- `audience_persona` — audience persona (select)
- `offer_type` — offer type (text)
- `budget_level` — budget level (select)
- `claim_strictness` — claim strictness (slider)
- `language` — language (select)
- `emoji_level` — emoji level (select)
- `cta_style` — CTA style (select)
- `output_format` — output format (select)
- `privacy_mode` — privacy mode (select)
- `confidence_threshold` — Confidence threshold (slider)

## Input fields

- `product` — Product (text) required
- `audience` — audience (select) required
- `offer` — offer (text) required
- `work_brief` — Work brief / source text / URL / instructions (textarea) required

## External data policy

The local deterministic core is real and executable. Live external systems are not simulated. If Shopify, ATS, ERP, OCR/STT, maps, SERP, market data, medical databases, tax/customs databases, or other live systems are required, this project reports the missing connector/API requirement instead of inventing data.

---

## Final UX/UI Layer

This project now uses the **Growth Command Center** pattern.

**UX workflow:** Research → positioning → content/ads → launch queue → measurement

**Domain components:**
- Offer canvas
- Angle matrix
- Platform ad previews
- Claim compliance panel
- A/B test board

**Quick actions:**
- Create angle matrix
- Generate platform variants
- Check risky claims
- Build UTM/testing plan

**No fake-data policy:** external/live actions require real connectors or API keys. Missing connectors are reported instead of simulated.
