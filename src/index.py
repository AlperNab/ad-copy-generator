#!/usr/bin/env python3
"""
ad-copy-generator — product + audience → ad copy for every platform
Generates: Google Ads, Meta (FB/IG), TikTok, LinkedIn, Twitter/X, Pinterest
Includes: headlines, descriptions, hooks, CTAs, A/B variants, emoji versions
"""
import anthropic
import json
import re
import sys
from dataclasses import dataclass
from typing import Optional


SYSTEM = """You are a world-class performance marketing copywriter who has written
hundreds of millions of dollars in converting ad copy.

You write copy that:
- Leads with the customer's pain or desire, not the product features
- Uses proven frameworks (AIDA, PAS, Before/After, Social Proof)
- Is platform-native (TikTok copy feels different from LinkedIn)
- Includes specific numbers and claims where possible
- Has clear, urgent CTAs

Return ONLY valid JSON — no markdown, no explanation.

Format:
{
  "product": "product name",
  "core_value_prop": "the single strongest reason to buy in one sentence",
  "target_emotion": "fear|greed|hope|pride|curiosity|relief|excitement",
  "google_ads": {
    "headlines": ["string under 30 chars", ...],
    "descriptions": ["string under 90 chars", ...],
    "responsive_search_ad": {
      "headlines": ["15 headlines, each under 30 chars"],
      "descriptions": ["4 descriptions, each under 90 chars"]
    },
    "keywords": ["broad match keyword", ...],
    "negative_keywords": ["keywords to exclude"]
  },
  "meta": {
    "primary_text": "main ad body, 125 chars ideal",
    "headline": "link headline, under 40 chars",
    "description": "link description, under 30 chars",
    "variants": [
      {
        "angle": "pain|social_proof|transformation|urgency|curiosity",
        "hook": "opening line that stops the scroll",
        "body": "full ad copy 50-150 words",
        "cta": "Shop Now|Learn More|Get Offer|Sign Up|Book Now"
      }
    ]
  },
  "tiktok": {
    "video_hook_scripts": [
      "3-second hook script for TikTok video opener"
    ],
    "caption": "TikTok caption with hashtags, conversational tone",
    "hashtags": ["#hashtag1", "#hashtag2"],
    "sound_suggestion": "trending audio type that fits"
  },
  "linkedin": {
    "sponsored_content": "professional tone, 150-600 chars, no hashtag spam",
    "message_ad_subject": "InMail subject line",
    "message_ad_body": "InMail body, conversational not salesy"
  },
  "twitter_x": {
    "tweet": "under 280 chars, punchy",
    "thread_opener": "thread-starting tweet that gets engagement"
  },
  "pinterest": {
    "pin_title": "SEO-optimized title",
    "pin_description": "description with keywords, 100-500 chars"
  },
  "email_subject_lines": [
    "5 subject line variants, A/B testable"
  ],
  "push_notification": {
    "title": "under 50 chars",
    "body": "under 100 chars"
  },
  "sms": "under 160 chars, includes opt-out mention",
  "ab_test_pairs": [
    {
      "hypothesis": "what we're testing",
      "variant_a": "short description",
      "variant_b": "short description"
    }
  ]
}"""


def generate(
    product: str,
    audience: str,
    value_prop: str = "",
    tone: str = "direct",
    platforms: list[str] | None = None,
    price: str = "",
    offer: str = ""
) -> dict:
    client = anthropic.Anthropic()

    platforms_str = ", ".join(platforms) if platforms else "all platforms"
    context_parts = [
        f"Product: {product}",
        f"Target audience: {audience}",
        f"Key benefit/value prop: {value_prop}" if value_prop else "",
        f"Price point: {price}" if price else "",
        f"Offer/promotion: {offer}" if offer else "",
        f"Brand tone: {tone}",
        f"Platforms needed: {platforms_str}",
    ]
    context = "\n".join(p for p in context_parts if p)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM,
        messages=[{"role": "user", "content": f"Generate ad copy for:\n\n{context}"}]
    )

    raw = response.content[0].text.strip()
    raw = re.sub(r'^```(?:json)?\s*', '', raw, flags=re.MULTILINE)
    raw = re.sub(r'\s*```$', '', raw, flags=re.MULTILINE)
    return json.loads(raw)


def print_copy(result: dict, platforms: list[str] | None = None):
    show_all = not platforms
    print(f"\n{'═'*60}")
    print(f"  AD COPY — {result.get('product','')}")
    print(f"  Core value prop: {result.get('core_value_prop','')}")
    print(f"  Emotion: {result.get('target_emotion','').upper()}")
    print(f"{'═'*60}")

    # Google Ads
    if show_all or "google" in " ".join(platforms or []).lower():
        google = result.get("google_ads", {})
        if google:
            print(f"\n  📊 GOOGLE ADS")
            print(f"  Headlines:")
            for h in (google.get("headlines") or google.get("responsive_search_ad",{}).get("headlines",[]))[:5]:
                print(f"    • {h}")
            print(f"  Descriptions:")
            for d in (google.get("descriptions") or google.get("responsive_search_ad",{}).get("descriptions",[]))[:2]:
                print(f"    • {d}")

    # Meta
    if show_all or "meta" in " ".join(platforms or []).lower() or "facebook" in " ".join(platforms or []).lower():
        meta = result.get("meta", {})
        if meta:
            print(f"\n  📱 META (Facebook/Instagram)")
            variants = meta.get("variants", [])
            if variants:
                for v in variants[:2]:
                    print(f"\n  [{v.get('angle','').upper()}]")
                    print(f"  Hook: {v.get('hook','')}")
                    body = v.get("body","")
                    print(f"  {body[:200]}{'...' if len(body)>200 else ''}")
                    print(f"  CTA: [{v.get('cta','')}]")

    # TikTok
    if show_all or "tiktok" in " ".join(platforms or []).lower():
        tiktok = result.get("tiktok", {})
        if tiktok:
            print(f"\n  🎵 TIKTOK")
            hooks = tiktok.get("video_hook_scripts", [])
            for h in hooks[:2]:
                print(f"  Hook: \"{h}\"")
            print(f"  Caption: {tiktok.get('caption','')[:150]}")
            tags = tiktok.get("hashtags", [])
            if tags:
                print(f"  Tags: {' '.join(tags[:6])}")

    # LinkedIn
    if show_all or "linkedin" in " ".join(platforms or []).lower():
        li = result.get("linkedin", {})
        if li:
            print(f"\n  💼 LINKEDIN")
            content = li.get("sponsored_content","")
            print(f"  {content[:300]}{'...' if len(content)>300 else ''}")

    # Twitter
    if show_all or "twitter" in " ".join(platforms or []).lower():
        tw = result.get("twitter_x", {})
        if tw:
            print(f"\n  🐦 TWITTER/X")
            print(f"  {tw.get('tweet','')}")

    # Email subjects
    subjects = result.get("email_subject_lines", [])
    if subjects and (show_all or "email" in " ".join(platforms or []).lower()):
        print(f"\n  📧 EMAIL SUBJECTS")
        for s in subjects[:5]:
            print(f"  • {s}")

    # A/B tests
    ab = result.get("ab_test_pairs", [])
    if ab:
        print(f"\n  🔬 A/B TEST SUGGESTIONS")
        for pair in ab[:3]:
            print(f"  Testing: {pair.get('hypothesis','')}")
            print(f"    A: {pair.get('variant_a','')}")
            print(f"    B: {pair.get('variant_b','')}")

    print(f"\n{'═'*60}\n")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate ad copy for any platform")
    parser.add_argument("product", help="Product or service name")
    parser.add_argument("audience", nargs="?", default="general audience", help="Target audience description")
    parser.add_argument("--value-prop", "-v", default="", help="Key benefit or value proposition")
    parser.add_argument("--price", "-p", default="", help="Price point")
    parser.add_argument("--offer", "-o", default="", help="Promotion or offer")
    parser.add_argument("--tone", "-t", default="direct", help="Brand tone (direct|friendly|premium|urgent)")
    parser.add_argument("--platforms", nargs="+", help="Platforms to generate for (google meta tiktok linkedin)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    result = generate(
        product=args.product,
        audience=args.audience,
        value_prop=args.value_prop,
        tone=args.tone,
        platforms=args.platforms,
        price=args.price,
        offer=args.offer
    )

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_copy(result, args.platforms)
