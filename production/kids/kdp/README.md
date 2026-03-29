# KDP Kids Production

Coloring books, activity books, tracing books for Amazon KDP.

## Pipeline

```
Theme + Characters (universe/) → SD images (ComfyUI) → PDF assembly (Python/Canva) → Cover (Canva) → Upload KDP
```

## File naming convention

```
coloring_animals_ages2-4/       — Folder per book
  interior.pdf                  — Print-ready interior
  cover.pdf                     — Cover file
  metadata.md                   — Title, subtitle, description, keywords, price
  pages/                        — Individual page PNGs before assembly
```

## Book types (by priority)

1. Coloring books by age (2-4, 4-8)
2. Tracing books (letters, numbers, shapes)
3. Dot-to-dot
4. Maze books
5. Activity book compilations

## Specs

- Interior: 8.5" x 11", 300 DPI, PDF
- Cover: use KDP Cover Calculator for dimensions
- Always declare AI content
- Max 2-3 books/day to avoid spam flags
