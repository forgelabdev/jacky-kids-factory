# Jacky — Kids Content Ecosystem

Digital asset factory generating passive income through a unified kids content ecosystem.

## 4 Revenue Engines (same themed universe)

| Engine | Platform | Timeline |
|--------|----------|----------|
| YouTube Kids | Educational videos (nursery rhymes, counting, alphabet) | 3-6 months to monetize |
| Amazon KDP | Coloring books, activity books, tracing books | 7-14 days to first sale |
| Etsy Digital | Worksheets, coloring pages, party decorations | 3-7 days to first sale |
| Print on Demand | Kids t-shirts, stickers, room posters | 7-21 days to first sale |

## Stack

- **Content**: Claude Pro (text/scripts/code)
- **Images**: Stable Diffusion (ComfyUI + SDXL) on local RTX 4060
- **Voice**: ElevenLabs / XTTS-v2
- **Music**: Suno AI
- **Automation**: n8n (self-hosted VPS)

## Structure

```
├── PROMPT_FINAL_V3.md          # Main operational prompt
├── VERIFIED_TOOLS_2026.md      # All verified tools, prices, links
├── AUTOENTREPRENEUR_GUIDE.md   # French micro-enterprise setup guide
├── production/
│   ├── kdp/                    # KDP puzzle book generators
│   ├── etsy/                   # Etsy planner generators + listings
│   ├── pod/                    # POD design concepts + SD prompts
│   └── youtube/                # YouTube scripts
└── checklists/                 # Account setup guides
```

## Getting Started

1. Read `PROMPT_FINAL_V3.md`
2. Follow the Week 1 calendar
3. Fork this repo to collaborate
