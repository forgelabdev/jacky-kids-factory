# Automation Scripts

Python scripts and n8n workflows for production automation.

## Available scripts

- `../production/kdp/generate_puzzle_book.py` — Word search + sudoku puzzle book generator (PDF)
- `../production/etsy/generate_planners.py` — Budget/daily/fitness/meal planner generator (PDF)

## Planned scripts

- `generate_coloring_book.py` — Assemble SD-generated pages into KDP-ready PDF
- `generate_worksheets.py` — Tracing, matching, counting worksheets (PDF)
- `bulk_upload_pod.py` — Multi-platform POD upload automation
- `youtube_pipeline.py` — Assemble script + voice + images into video project
- `sales_monitor.py` — Telegram bot for sales alerts (Etsy + KDP + POD)

## n8n workflows (VPS Hostinger)

- `etsy_sales_alert.json` — Notify Telegram on new Etsy sale
- `trend_scanner.json` — Daily scan of trending kids niches
- `kdp_rank_tracker.json` — Track BSR of published books

## Requirements

```
pip install reportlab
```
