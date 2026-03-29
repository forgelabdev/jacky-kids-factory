# OUTILS VERIFIES MARS 2026 — PROJET JACKY

> Donnees verifiees via Perplexity en mars 2026.
> Ce fichier remplace TOOLKIT.md comme reference d'outils.

---

## STABLE DIFFUSION / GENERATION D'IMAGES

### Interface : ComfyUI (choix principal)
- **Telecharger** : https://github.com/comfyanonymous/ComfyUI/releases/latest
- **Version** : ComfyUI_windows_portable_nvidia_cu121_or_cpu.7z
- **Installation** : extraire dans C:\ComfyUI\, editer run_nvidia_gpu.bat :
  ```
  python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --use-sage-attention --fp16-vae --force-fp16 --normalvram
  ```
- **Acces** : http://127.0.0.1:8188
- **Installer ComfyUI-Manager** des le premier lancement

### Alternative rapide : Forge
- Plus rapide pour les tests (4-8s SDXL vs 7-12s sur ComfyUI)
- Moins flexible pour la production batch

### Modeles par usage (SDXL = sweet spot sur 8Go VRAM)

| Usage | Modele | Lien CivitAI | Temps/image RTX 4060 |
|-------|--------|-------------|---------------------|
| **POD / T-shirts / Wall art** | Juggernaut XL v9 | civitai.com/models/288982 | 7-10s (1024x1024) |
| **Coloring books** | Coloring Book Art XL v1 (LoRA) | civitai.com/models/728040 | 6-9s |
| **Coloring books** | Lineart Specialist SDXL | civitai.com/models/51295 | 6-9s |
| **Clipart PNG transparent** | Transparent Clipart XL (LoRA) + RemBG | civitai.com/models/492734 | 8-12s + 2s post |
| **Wall art premium** | DreamShaper XL Lightning | civitai.com/models/112902 | 5-8s |

### LoRAs essentielles

| LoRA | CivitAI | Usage | Poids recommande |
|------|---------|-------|-----------------|
| T-Shirt Design XL | civitai.com/models/795764 | Designs POD commerciaux | 0.7-0.9 |
| Coloring Book Art XL | civitai.com/models/728040 | Pages de coloriage | 0.7-0.9 |
| Detail Tweaker XL | civitai.com/models/377772 | Amelioration details | 0.5-0.7 |
| Transparent PNG XL | civitai.com/models/492734 | Clipart fond transparent | 0.8-1.0 |
| Vector Art Style | civitai.com/models/108384 | Style vectoriel | 0.6-0.8 |

### Embeddings negatifs
- EasyNegative XL : civitai.com/models/64976
- BadHands XL : civitai.com/models/55878

### Performances reelles RTX 4060 8Go VRAM

| Config | Temps | Output |
|--------|-------|--------|
| SDXL batch 16 images 1024x1024, 20 steps | 3min18s | 16 PNG |
| SDXL + upscale 2x | +2min45s | 16 PNG HD |
| Pipeline complet (gen + upscale) | ~6min | 16 fichiers prets |
| SD1.5 batch 32 clipart | 1min42s | 32 PNG rapides |

**Capacite de production : 100+ images/heure**

### Optimisations VRAM critiques
```
Arguments ComfyUI :
--fp16-vae --fp16-text-encoder --force-fp16
--use-sage-attention --normalvram

VRAM optimise :
- SDXL base : 4.2 Go
- Batch 16 : 6.0 Go
- Upscale 4x : 6.8 Go peak
```

### Prompts de reference par usage

**POD T-shirt :**
```
vibrant t-shirt design, [THEME], bold colors, commercial art style,
centered composition, high contrast, no background
Negative: blurry, text, watermark, low quality, deformed
Steps: 20-30, CFG: 5-7, Sampler: DPM++ 2M Karras
```

**Coloring book :**
```
coloring book page, [SUJET], clean black line art, white background,
thick outlines, printable, no shading, no color
Negative: color, shading, gradient, grey, blurry
Trigger LoRA: <lora:coloringbook:0.8>
```

**Clipart transparent :**
```
clean clipart [OBJET], transparent background, vector style,
sharp edges, flat design, isolated object
+ Post-process: RemBG node ComfyUI
```

**Wall art :**
```
museum quality wall art, [SUJET], cinematic lighting, 8k resolution,
detailed, professional photography, gallery print
```

---

## ETSY — OUTILS VERIFIES

| Outil | Prix | Usage |
|-------|------|-------|
| **eRank Free** | 0 EUR (5 keyword lookups/jour, 50 listings) | Recherche keywords/niches — **commencer ici** |
| **eRank Basic** | 5.99$/mois | Si on depasse les limites free |
| **eRank Pro** | 9.99$/mois | Analytics avances, competitor tracking |
| **Canva Free** | 0 EUR | Mockups, design, mise en page |
| **Canva Pro** | 12.99$/mois | Elements premium, mockups avances |
| **Etsy Bulk Editor** | Gratuit (natif Etsy) | Edition masse titres/tags/prix |
| **Scripts Python + CSV** | Gratuit | Generation automatisee titres/tags/descriptions |

**Formats qui vendent le mieux (2026) :**
- Bundle PDF + PNG + Canva template link (le plus rentable)
- PDF seul (planners, checklists, guides)
- PNG/JPG (wall art, prints)
- Canva template link (templates social media, business kits)

---

## AMAZON KDP — OUTILS VERIFIES

| Outil | Prix | Usage |
|-------|------|-------|
| **Publisher Rocket** | 199$ one-time (lifetime) | Recherche niches/keywords — **meilleur investissement** |
| **Book Bolt** | 9.99$/mois (Newbie) | Alternative : niche research + puzzle generator + designer |
| **KDP Cover Calculator** | Gratuit (Amazon) | Dimensions covers selon nombre de pages |
| **Canva Pro** | 12.99$/mois | Mise en page + covers |
| **Affinity Publisher** | ~69.99$ one-time | Mise en page pro (alternative a InDesign) |
| **Book Brush** | 149$/an | Covers specialisees + visuels marketing |
| **Scripts Python** | Gratuit | Generation automatisee puzzles (word search, sudoku, mazes) |

**Politique IA Amazon KDP (mars 2026) :**
- Declarer le contenu IA lors de la publication (obligatoire)
- AI-generated vs AI-assisted : 2 categories
- Interdit : spam de masse, doublons, contenu recyclé, keyword stuffing
- Max recommande : 2-3 livres/jour (au-dela = risque flag spam)
- W-8BEN avec numero fiscal francais → 0% retenue US

**SD1.5 pour coloring books** sur 8Go VRAM (plus leger, plus rapide) :
- Base SD1.5 + ControlNet Lineart/Canny
- LoRA coloring book + lineart
- Prompts : "black and white, clean line art, white background, printable coloring page"

---

## PRINT ON DEMAND — OUTILS VERIFIES

### Plateformes prioritaires

| Plateforme | IA OK | Royalty | Inscription |
|-----------|-------|--------|-------------|
| **Redbubble** | OUI | ~20-30% variable | Gratuit, immediat |
| **TeePublic** | OUI | ~4$ fixe/t-shirt | Gratuit, immediat |
| **Spring** | OUI | ~25% marge | Gratuit, immediat |
| **Merch by Amazon** | OUI (declarer) | 13-37% selon tier | Sur invitation, delai 2-8 semaines |
| **Spreadshirt** | OUI | 20% marketplace / 70% boutique | Gratuit, immediat |
| **Zazzle** | OUI | 5-99% variable | Gratuit, immediat |

### Outils

| Outil | Prix | Usage |
|-------|------|-------|
| **Merch Titans** | 19.95$/mois | Mass-upload multi-plateforme (Redbubble, TeePublic, Spreadshirt, Zazzle) |
| **Canva Free / Photopea** | Gratuit | Creation designs |
| **Kittl** | Gratuit / Pro 10$/mois | Designs text-based POD |
| **USPTO TESS** | Gratuit | Verification trademarks US |
| **EUIPO TMview** | Gratuit | Verification trademarks EU |
| **Trademarkia** | Gratuit | Interface simplifiee trademark |
| **TMHunt** | Gratuit | Screening rapide |

### Specs techniques POD
- Resolution : 300 DPI minimum
- Format : PNG fond transparent
- CMYK pour impression, RGB pour preview
- Telecharger les templates officiels de chaque plateforme

---

## YOUTUBE FACELESS — OUTILS VERIFIES

### Voix off IA

| Outil | Prix | Local GPU ? | Qualite FR/EN | Recommandation |
|-------|------|------------|--------------|----------------|
| **XTTS-v2** | Gratuit (open source) | OUI (4-6Go VRAM) | Tres bonne | **#1 local** |
| **Edge TTS** | Gratuit (Microsoft) | OUI (Python) | Correcte | **#1 gratuit** |
| **Coqui TTS** | Gratuit (open source) | OUI | Bonne | Alternative |
| **ElevenLabs** | 5-99$/mois | Non (cloud) | Excellente | Si budget |
| **Fish Audio** | 37.50$/mois | Non (cloud) | Meilleure 2026 | Premium |

### Montage video

| Outil | Prix | Rapidite | Recommandation |
|-------|------|----------|----------------|
| **CapCut Desktop** | Gratuit | Le plus rapide (5 min/video) | **#1 absolu** |
| **DaVinci Resolve** | Gratuit | Pro mais courbe d'apprentissage | Pour plus tard |

### Automatisation pipeline

| Outil | Prix | Usage |
|-------|------|-------|
| **OpusClip** | ~19$/mois | Decoupe long-form → Shorts (1 video → 10 clips) |
| **Submagic** | ~20$/mois | Sous-titres auto IA + style viral |
| **Later** | Gratuit (free tier) | Scheduling multi-plateforme (YT/TikTok/Reels) |

### SEO YouTube

| Outil | Prix | Recommandation |
|-------|------|----------------|
| **VidIQ Free** | Gratuit | **#1** — tags, titres, analytics |
| **TubeBuddy Pro** | 4.50$/mois | **#2** — A/B test thumbnails |

### YouTube Partner Program 2026
- **Tier 1 (Fan Funding)** : 500 subs + 3 uploads en 90j + (3K heures OU 3M Shorts views en 90j)
- **Tier 2 (Pubs/Ads)** : 1K subs + 4K heures en 12 mois OU 10M Shorts views en 90j
- **Delai realiste avec contenu IA** : Tier 1 en 1-3 mois, Tier 2 en 3-6 mois

### Niches CPM verifies 2026

| Niche | CPM | Faisabilite IA |
|-------|-----|----------------|
| Personal Finance | 15-22$ | Haute |
| Make Money Online | 15-20$ | Haute |
| True Crime / Horror | 12-18$ | Tres haute |
| ASMR / Soundscapes | 10-16$ | Tres haute |
| Betrayal Stories | ~13$ RPM | Tres haute |

---

## BUDGET MENSUEL TOTAL VERIFIE

### Phase 1 — Demarrage (zero budget sauf Claude)

| Poste | Cout |
|-------|------|
| 2x Claude Pro | 200$/mois |
| Listings Etsy (~100 x 0.20$) | 20$/mois |
| Tout le reste (ComfyUI, eRank Free, Canva Free, etc.) | 0$ |
| **TOTAL** | **220$/mois** |

### Phase 2 — Low-cost serieux (quand premiers revenus)

| Poste | Cout |
|-------|------|
| 2x Claude Pro | 200$/mois |
| Listings Etsy | 20$/mois |
| Canva Pro | 12.99$/mois |
| Book Bolt (KDP) | 9.99$/mois |
| eRank Basic (Etsy SEO) | 5.99$/mois |
| **TOTAL** | **~249$/mois** |

### Phase 3 — Scale (quand 500+ EUR/mois)

| Poste | Cout |
|-------|------|
| Phase 2 | 249$/mois |
| Merch Titans (POD mass upload) | 19.95$/mois |
| TubeBuddy Pro (YouTube SEO) | 4.50$/mois |
| ElevenLabs Starter (voix pro) | 5$/mois |
| **TOTAL** | **~278$/mois** |

### Seuil de rentabilite = ~250 EUR/mois

---

## OUTILS KIDS CONTENT (PIVOT ECOSYSTEME KIDS)

### Animation video kids

| Outil | Prix | Usage | Recommandation |
|-------|------|-------|----------------|
| **Animaker** | 10-25$/mois | 2D cartoons kids, personnages parlants, templates kids | **#1 pour debutants** |
| **InVideo AI** | 20-30$/mois | Generation video a partir de prompt texte, rapide | **#1 pour scripts courts** |
| **Canva Animate** | 12-15$/mois (Pro) | Slides animees educatives, drag-drop | **#1 pour contenu educatif simple** |
| **Powtoon** | ~50$/mois | 2D animation educative | Trop cher pour le budget |
| **Renderforest** | 10-20$/mois | 3D/2D animations | Plus branding que kids |
| **Steve AI** | 20-30$/mois | Narrateur + avatar | Bon pour storytelling |

### Musique IA kids (usage commercial YouTube)

| Outil | Prix | Licence commerciale | Usage |
|-------|------|-------------------|-------|
| **Suno AI Pro** | **10$/mois** | OUI (plan Pro) | **RECOMMANDE** : nursery rhymes, chansons enfants, 500 chansons/mois |
| **Mubert Creator** | **12$/mois** | OUI | Ambiances instrumentales joyeuses |
| **Udio** | ~10$/mois | Usage public OK, commercial limite | Backup |
| **AIVA** | 15-30$/mois | OUI | Bandes-son pures, pas de chanson vocale |

### Voix IA kids

| Outil | Prix | Voix enfantines | Local GPU ? | Recommandation |
|-------|------|----------------|------------|----------------|
| **ElevenLabs Starter** | **5$/mois** | OUI (child narrator, soft female) | Non | **#1 qualite** |
| **Google Cloud TTS** | 4$/1M chars (**5M gratuits/mois**) | OUI (voix enfant EN) | Non | **#1 budget/volume** |
| **Amazon Polly** | 4$/1M chars (5M gratuits/mois) | OUI (Lotte, Salli) | Non | Alternative |
| **XTTS-v2** | Gratuit (open source) | Configurable avec finetuning | OUI (4-6Go VRAM) | **#1 local** |

### LoRAs Stable Diffusion style kids (CivitAI)

| LoRA | CivitAI | Style | Poids recommande |
|------|---------|-------|-----------------|
| **Picture books children cartoon** | ~176435 | Cartoon enfant, crayonne, couleurs vives, picture book | 0.7-0.8 |
| **Illustration children story book v1.0** | ~1000819 | Illustration douce, coloree, magique, bedtime stories | 0.7-0.8 |
| Coloring Book Art XL | civitai.com/models/728040 | Pages de coloriage enfants | 0.7-0.9 |
| Lineart Specialist | civitai.com/models/51295 | Lineart propre pour coloring books | 0.7-0.9 |

**Prompts kids de reference :**
```
Illustration kids :
"cute cartoon [ANIMAL], simple strokes, bright colors, children's book illustration,
2D vector style, no shadows, kawaii, friendly face, white background"

Coloring book kids :
"coloring book page for children ages 3-5, cute [ANIMAL], clean black line art,
white background, thick outlines, simple shapes, no shading, no color, printable"

POD kids :
"cute cartoon [ANIMAL] for children, bright colors, simple design,
centered composition, no background, t-shirt ready, kawaii style"
```

### Sound effects et musiques libres de droits kids

| Source | Prix | Usage |
|--------|------|-------|
| **YouTube Audio Library** | Gratuit | Effets sonores + musiques, libre de droits YouTube |
| **Freesound.org** (filtre CC0) | Gratuit | Ambiances, effets sonores |
| **Pixabay Music** | Gratuit | Musiques libres de droits |

---

## DONNEES NICHES KIDS (verifiees mars 2026)

### Top Etsy kids digital products

| Produit | Prix | Volume recherche | Concurrence |
|---------|------|-----------------|-------------|
| Coloring pages bundles (kids) | 3-8$ | 80K/mois | Moyenne (20K) |
| Educational worksheets (numbers/letters) | 4-10$ | 25K/mois | Moyenne (12K) |
| Children's room wall art | 5-12$ | 20K/mois | Faible-moyenne |
| Party decorations (birthday themes) | 5-15$ | 18K/mois | Moyenne |
| Chore/reward charts | 3-8$ | 12K/mois | Faible |
| Activity bundles (coloring+worksheets+games) | 8-20$ | 10K/mois | Faible |

### Etsy kids saisonnier 2026

| Mois | Produit | Pic ventes | Preparer quand |
|------|---------|------------|---------------|
| Avril | Easter worksheets, spring activities | +300% | MAINTENANT |
| Mai | Mother's Day cards | +400% | MAINTENANT |
| Juillet | Back-to-school prep | +200% | Avril-Mai |
| Octobre | Halloween coloring + activities | +500% | Juillet |
| Decembre | Christmas activity packs | +800% | Septembre |

### Top KDP kids niches 2026

| Niche | BSR moyen top 10 | Prix optimal | Pages | Royalty/vente |
|-------|------------------|-------------|-------|--------------|
| Coloring book animaux (2-4 ans) | 2000-5000 | 7.99-9.99$ | 40-60 | 2.20-3.50$ |
| Coloring book vehicules (4-8 ans) | 3000-6000 | 7.99-9.99$ | 40-60 | 2.20-3.50$ |
| Numbers/letters tracing (3-5 ans) | 1500-4000 | 8.99-10.99$ | 50-70 | 2.50-3.80$ |
| Dot-to-dot animaux (4-8 ans) | 4000-8000 | 7.99-9.99$ | 60-80 | 2.20-3.50$ |
| Maze books (4-8 ans) | 3000-7000 | 7.99-9.99$ | 60-80 | 2.20-3.50$ |
| Activity compilation (4-8 ans) | 2000-5000 | 9.99-12.99$ | 80-100 | 3.00-4.50$ |
| Coloring book dinosaures (2-6 ans) | 2000-4000 | 7.99-9.99$ | 40-60 | 2.20-3.50$ |
| Coloring book licornes (3-7 ans) | 1500-3500 | 7.99-9.99$ | 40-60 | 2.20-3.50$ |
| Handwriting practice (ages 3-5) | 2000-5000 | 8.99-10.99$ | 50-80 | 2.50-3.80$ |
| Coloring book espace (4-8 ans) | 3000-6000 | 7.99-9.99$ | 40-60 | 2.20-3.50$ |

### Keywords KDP kids long-tail (peu de concurrence)
- "coloring book for kids ages 3-5 ocean animals"
- "toddler tracing and coloring book numbers 1-20"
- "dot to dot dinosaur coloring book for boys 6-10"
- "maze and coloring book for kids transportation"
- "alphabet tracing book for preschoolers ages 2-4"
- "cute animal coloring book for toddlers"

### Erreurs KDP a eviter
1. Images/polices sans licence commerciale
2. Resolution trop basse (<300 DPI)
3. Marges incorrectes (verifier KDP Cover Calculator)
4. Livres repetitifs/quasi-identiques (flag spam Amazon)
5. Noms de marques dans titres (Disney, Pokemon = suspension)
6. Non-declaration du contenu IA
7. Keyword stuffing dans les metadonnees
