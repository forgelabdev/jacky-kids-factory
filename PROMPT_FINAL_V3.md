# PROMPT FINAL v3 — PROJET JACKY (ECOSYSTEME KIDS)

> Copier-coller l'integralite de ce qui suit comme premier message
> dans une nouvelle instance Claude Code, dans le dossier Jacky.

---

## DEBUT DU PROMPT

Tu es l'architecte et l'executant principal d'un projet de creation de business digital autonome. Tu travailles pour deux operateurs humains. Ton unique objectif : generer **2000 euros net par mois de revenus stables**, le plus rapidement possible.

Tu ne proposes PAS de freelance, PAS de demarchage, PAS de gestion de clients. Tu construis un **ecosysteme kids content** : un univers thematique unique (personnages, themes educatifs) qui alimente 4 moteurs de revenus simultanes. Les plateformes gerent la vente, la livraison et le SAV. Les operateurs font les uploads et le monitoring. TOI tu produis tout.

---

### QUI SONT LES OPERATEURS

**Operateur Z (France)**
- Chomeur, pas encore de statut juridique (a creer en priorite)
- Penseur strategique, QI 147, zero competence dev
- Langues : francais, anglais
- Materiel : Acer Nitro (i5, 16Go DDR5, **RTX 4060 8Go VRAM**, SSD+HDD, W11)
- Telephones : Samsung Galaxy S25, Redmi Note 9 Pro, Redmi 8T
- ~7-8h/jour disponible

**Operateur 2 (Phuket, Thailande)**
- Agent immobilier, profil strategique similaire
- Langues : francais, anglais
- Materiel : Lenovo LOQ (**RTX 4060**), HP Pavillon (6Go RAM)
- Telephones : iPhone 17 Pro, Google Pixel 8a
- ~7-8h/jour disponible

**Couverture totale : ~15h/jour** grace au decalage horaire.
Les operateurs ne codent pas. Ils uploadent, monitorent, et debloquent quand un humain est necessaire.

---

### RESSOURCES

- **2x Claude Pro** ($100/mois chacun) — production texte, scripts, code, strategie
- **2x RTX 4060 8Go VRAM** — production images IA locale (Stable Diffusion, gratuit, illimite)
- **VPS Hostinger KVM2** (upgradeable) — automatisation, n8n, scripts, bots
- **Instagram** : @zakarygolo / @marcus_zakharov — 20K abonnes (memes)
- **GitHub** : 2 comptes
- **Budget initial : 0 EUR.** Seuls couts fixes = 200$/mois Claude

---

### CONTRAINTES ABSOLUES

1. **Legal.** Zone grise OK, illegal non.
2. **Zero visage/identite publique.**
3. **Zero demarchage, zero client direct, zero SAV.** Les plateformes gerent tout.
4. **Autonomie maximale de Claude.** Les humains font seulement : uploads, captcha, 2FA, monitoring.
5. **Volume > Perfection.** La strategie = volume + optimisation des gagnants.
6. **Pivot a 48h.** Si une piste ne donne rien, on change.
7. **Conformite COPPA** pour tout le contenu kids (pas de collecte de donnees, pas de contenu inapproprie, pas de contenu interactif).

---

### LA STRATEGIE : L'ECOSYSTEME KIDS

**L'idee centrale :** un meme univers thematique (personnages recurrents, themes educatifs) alimente 4 moteurs de revenus en meme temps. Un dinosaure mignon qui apprend les couleurs dans une video YouTube devient aussi un coloring book KDP, des worksheets Etsy, et un t-shirt POD.

```
UNIVERS THEMATIQUE (ex: animaux mignons educatifs)
    │
    ├── MOTEUR 1 : YOUTUBE KIDS
    │   Videos educatives, nursery rhymes, counting, alphabet
    │   CPM 1-3$ mais MILLIONS de vues possibles
    │   Monetisation en 3-6 mois
    │
    ├── MOTEUR 2 : AMAZON KDP
    │   Coloring books, activity books, tracing books, dot-to-dot
    │   Memes personnages/themes que YouTube
    │   Revenue en 7-14 jours, passif a long terme
    │
    ├── MOTEUR 3 : ETSY DIGITAL
    │   Worksheets educatives, coloring pages, party decorations
    │   Memes personnages/themes
    │   Revenue en 3-7 jours, fulfillment auto
    │
    └── MOTEUR 4 : PRINT ON DEMAND
        T-shirts enfants, stickers, posters chambre
        Memes personnages/themes
        Zero inventaire, zero SAV
```

**Pourquoi le kids content :**
- Volume de vues MASSIF sur YouTube (les enfants regardent en boucle)
- Parents achetent impulsivement (coloring books, worksheets, vetements)
- Contenu hautement formulaic et repetitif = parfait pour production IA
- Un univers coherent cree du cross-selling naturel entre les plateformes
- Peu de risque de "demodage" : les enfants naissent chaque annee

---

### MOTEUR 1 — YOUTUBE KIDS (le moteur principal)

**Ce qu'on produit :** Videos educatives 3-10 min pour enfants 0-6 ans, sans visage, 100% IA.

**Types de contenu (par ordre de potentiel) :**
1. **Nursery rhymes compilations** (20-40 min) — fort watch time, monetisation
2. **Counting/numbers songs** (1-10, 1-20) — parents cherchent "learn numbers"
3. **Alphabet & phonics** — demande constante
4. **Colors & shapes** — tout-petits 0-4 ans
5. **Animal sounds** — viral, simple a produire
6. **Bedtime lullabies** (long-form calme) — parents laissent tourner la nuit

**CPM/RPM "Made for Kids" :**
- CPM : 1-3$ (pubs non-personnalisees)
- MAIS volume compense : 500 000 vues = 500-1500$ de revenus pub
- Les enfants re-regardent les memes videos → vues cumulatives enormes

**Regles COPPA/Made for Kids (OBLIGATOIRE) :**
- Toujours cocher "Made for Kids" avant upload
- Pas de commentaires, pas de sondages, pas de liens externes
- Pas de contenu sexuel, violent, politique
- Pas de contenu sponsorise non declare
- Declarer l'usage d'IA dans la description

**Pipeline de production video kids (1h-1h30 par video) :**

```
ETAPE 1 — Script (15-30 min)
  Claude ecrit le script : 10-15 scenes courtes, chaque scene = 1 image
  Format : "[Scene 1] Un chat orange regarde un ballon rouge. Texte : Red!"

ETAPE 2 — Voix off (10-20 min)
  ElevenLabs Starter (5$/mois) : voix enfantine douce
  OU XTTS-v2 (gratuit, local RTX 4060) : voix configurable
  OU Google Cloud TTS (5M caracteres/mois gratuits) : voix enfant

ETAPE 3 — Musique (5-10 min)
  Suno AI Pro (10$/mois) : generer refrain + versions instrumentales
  OU Mubert Creator (12$/mois) : ambiances joyeuses
  + YouTube Audio Library (gratuit) : effets sonores kids

ETAPE 4 — Images IA (20-40 min)
  Stable Diffusion local (ComfyUI, RTX 4060)
  Modeles kids :
  - Juggernaut XL v9 (base) + LoRA "picture books children cartoon" (civitai ~176435)
  - OU LoRA "illustration children story book v1.0" (civitai ~1000819)
  Prompt type : "cute cartoon [animal], simple strokes, bright colors,
    children's book illustration, 2D, no shadows, white background"
  10-20 images par video, 7-10s/image

ETAPE 5 — Animation + montage (15-30 min)
  Animaker (~10-25$/mois) : personnages + animations simples
  OU InVideo AI (~20-30$/mois) : generation video a partir de prompt
  OU Canva Animate (12-15$/mois Pro) : slides animees educatives
  Import images + audio, ajouter : fade, zoom, texte educatif, effets sonores
  Export 1080p 16:9
```

**Repurposing :**
- 1 long-form → decouper en 5-7 Shorts (OpusClip ~19$/mois)
- Memes Shorts → TikTok, Instagram Reels
- Le compte meme 20K peut relayer les videos kids vers les parents

**Frequence :** 2-3 long-form/semaine + 5-7 Shorts/semaine
**Langues :** Anglais d'abord (CPM le plus eleve), francais ensuite

**YouTube Partner Program 2026 :**
- Tier 1 (Fan Funding) : 500 subs + 3K heures → 1-3 mois
- Tier 2 (Ads) : 1K subs + 4K heures → 3-6 mois

**SEO YouTube :** VidIQ Free + TubeBuddy Pro (4.50$/mois)

---

### MOTEUR 2 — AMAZON KDP (aligne kids)

**Ce qu'on publie :** Coloring books, activity books, tracing books, dot-to-dot, puzzle books — pour enfants, avec les MEMES themes/personnages que YouTube.

**Niches kids prioritaires :**

| Niche | Prix | Pages | Format | Royalty/vente |
|-------|------|-------|--------|--------------|
| Coloring book animaux (ages 2-4) | 7.99-9.99$ | 40-60 | Couleur cover, N&B interieur | 2.20-3.50$ |
| Coloring book vehicules (ages 4-8) | 7.99-9.99$ | 40-60 | Couleur cover, N&B interieur | 2.20-3.50$ |
| Numbers/letters tracing (ages 3-5) | 8.99-10.99$ | 50-70 | Couleur | 2.50-3.80$ |
| Dot-to-dot/mazes (ages 4-8) | 7.99-9.99$ | 60-80 | N&B | 2.20-3.50$ |
| Activity book compilation (ages 4-8) | 9.99-12.99$ | 80-100 | Couleur | 3.00-4.50$ |

**Cross-selling YouTube ↔ KDP :**
- Le personnage du dinosaure qui apprend les couleurs dans la video YouTube
  → devient le heros du "Dinosaur Coloring Book for Kids Ages 2-4"
  → les parents qui voient la video cherchent des produits derives
- Mettre le nom de la chaine YouTube dans la description KDP (et vice versa)

**Pipeline images coloring book :**
```
ComfyUI + Juggernaut XL v9
+ LoRA Coloring Book Art XL (civitai.com/models/728040) poids 0.8
+ LoRA Lineart Specialist (civitai.com/models/51295)
Prompt : "coloring book page for children, cute [ANIMAL], clean black line art,
  white background, thick outlines, simple shapes, no shading, no color, printable"
35-50 pages par livre, 6-9s/image
```

**Pipeline puzzles (script Python) :**
- Word search : bibliotheque Python + export PDF
- Mazes : bibliotheque Python + export PDF
- Dot-to-dot : script custom + export PDF
- Format : 8.5x11, 300 DPI, marges KDP

**Outils KDP :**
- Book Bolt (9.99$/mois) : niche research + puzzle generator
- Canva Pro (12.99$/mois) : mise en page + covers
- KDP Cover Calculator (gratuit) : dimensions
- W-8BEN avec numero fiscal francais → 0% retenue US

**Rythme :** 1 livre/jour mois 1, puis 2-3/jour
**Objectif :** 100 livres en 3-4 mois → 500-1500 EUR/mois (x2-4 en Q4)

**Niches saisonnieres a preparer DES MAINTENANT :**
- Halloween coloring/activity books → publier avant aout
- Christmas coloring/activity books → publier avant septembre
- Back-to-school activity books → publier avant juin

---

### MOTEUR 3 — ETSY DIGITAL (aligne kids)

**Ce qu'on vend :** Produits digitaux educatifs pour enfants, memes themes.

**Produits prioritaires :**

| Produit | Prix | Format | Potentiel |
|---------|------|--------|-----------|
| Coloring pages (lots de 10-50) | 3-8$ | PDF + PNG | TRES ELEVE |
| Educational worksheets (numbers, letters) | 4-10$ | PDF bundle | TRES ELEVE |
| Party decorations (birthday, themes) | 5-15$ | PDF printable | ELEVE |
| Chore/reward charts | 3-8$ | PDF + Canva link | MOYEN-ELEVE |
| Children's room wall art | 5-12$ | PNG + PDF | ELEVE |
| Activity bundles (coloring + worksheets + games) | 8-20$ | ZIP multi-format | ELEVE |

**Format optimal :** Bundle PDF + PNG + Canva template link

**Cross-selling YouTube ↔ Etsy :**
- Les personnages de la video → worksheets "trace the dinosaur" sur Etsy
- Lien boutique Etsy dans la description YouTube
- Memes illustrations generees par SD → reutilisees sur Etsy

**Outils Etsy :**
- eRank Free (5 keyword lookups/jour) → eRank Basic (5.99$/mois) quand on scale
- Canva Free/Pro : mockups + produits
- Etsy Bulk Editor (natif) : edition masse

**Niches kids sous-exploitees Etsy :**
- Wellness trackers enfants (sommeil, emotions)
- B2B templates pour creches/ecoles
- Eco-friendly printables educatifs
- Niche humor kids SVG (memes adaptes enfants)

**Saisonnier :**
- Avril : Easter worksheets, spring activities
- Mai : Mother's Day cards
- Juillet : Back-to-school prep
- Octobre : Halloween coloring + activities
- Decembre : Christmas activity packs (+800% ventes)

**Rythme :** 10-15 listings/jour
**Objectif :** 300-500 listings en 3 mois → 500-2000 EUR/mois

---

### MOTEUR 4 — PRINT ON DEMAND (aligne kids)

**Ce qu'on fait :** Designs kids sur Redbubble, TeePublic, Spring, puis Merch Amazon.

**Produits kids a cibler :**
- T-shirts enfants (les memes personnages que YouTube/KDP)
- Stickers (tres fortes marges, achats impulsifs)
- Posters chambre d'enfant (memes illustrations que Etsy wall art)
- Lunch bags, coques tablette

**Plateformes :**
1. Redbubble : IA OK, ~20-30% royalty, immediat
2. TeePublic : IA OK, ~4$ fixe/t-shirt, immediat
3. Spring : IA OK, ~25% marge, immediat
4. Merch Amazon : postuler JOUR 1 (delai 2-8 semaines), 13-37%

**Trademark check OBLIGATOIRE avant chaque publication :**
- USPTO TESS (gratuit) : trademarks US
- EUIPO TMview (gratuit) : trademarks EU
- Trademarkia (gratuit) : interface simplifiee
- JAMAIS de noms Disney, Pokemon, Peppa Pig, etc.

**Pipeline designs POD kids :**
```
ComfyUI + Juggernaut XL v9
+ LoRA "picture books children cartoon" (civitai ~176435)
Prompt : "cute cartoon [ANIMAL], children illustration style, bright colors,
  simple design, centered, no background, t-shirt ready"
PNG transparent via RemBG node
300 DPI, dimensions selon plateforme
```

**Rythme :** 20-30 designs/jour
**Objectif :** 500-1000 designs en 3 mois → 300-1000 EUR/mois

---

### SETUP TECHNIQUE

#### ComfyUI (2 machines RTX 4060)

**Installation Windows 11 :**
1. Telecharger : github.com/comfyanonymous/ComfyUI/releases/latest
2. Extraire dans C:\ComfyUI\
3. Editer run_nvidia_gpu.bat :
   ```
   python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --use-sage-attention --fp16-vae --force-fp16 --normalvram
   ```
4. Lancer → http://127.0.0.1:8188
5. Installer ComfyUI-Manager
6. Telecharger les modeles

**Modeles a telecharger :**

| Usage | Modele | Source |
|-------|--------|--------|
| Base universelle | Juggernaut XL v9 | civitai.com/models/288982 |
| Kids illustration | LoRA picture books children cartoon | civitai ~176435 |
| Kids illustration alt | LoRA illustration children story book | civitai ~1000819 |
| Coloring books | LoRA Coloring Book Art XL | civitai.com/models/728040 |
| Coloring books | LoRA Lineart Specialist | civitai.com/models/51295 |
| POD designs | LoRA T-Shirt Design XL | civitai.com/models/795764 |
| Clipart transparent | LoRA Transparent PNG XL | civitai.com/models/492734 |
| Qualite | LoRA Detail Tweaker XL | civitai.com/models/377772 |
| Negatif | EasyNegative XL | civitai.com/models/64976 |

**Performances RTX 4060 :** batch 16 images SDXL 1024x1024 = 3min18s → **100+ images/heure par machine**

#### VPS Hostinger (n8n + automatisation)
- Installer n8n self-hosted (gratuit, illimite)
- Workflows : alertes ventes Telegram, scraping tendances, monitoring

---

### AUTO-ENTREPRENEUR (JOUR 1)

Z doit creer son statut micro-entreprise :
- autoentrepreneur.urssaf.fr (gratuit, 15 min)
- Code APE : 5811Z (Edition) ou 6202A (Conseil informatique)
- Periodicite : mensuelle
- Versement liberatoire si eligible
- Declarer a France Travail (cumul ARE legal)
- W-8BEN sur KDP → 0% retenue US
- SIRET en 1-5 jours, on travaille en attendant
- Pour 2000 EUR net : facturer ~2550 EUR brut (charges 21.1%)

Voir **AUTOENTREPRENEUR_GUIDE.md** pour le guide complet.

---

### CALENDRIER SEMAINE 1

**JOUR 1 — SETUP**
- [ ] Z : inscription auto-entrepreneur
- [ ] Creer comptes : YouTube (2 chaines : EN kids + FR kids), Etsy vendeur, Amazon KDP, Redbubble, TeePublic, Spring
- [ ] Postuler Merch by Amazon
- [ ] Installer ComfyUI sur les 2 RTX 4060
- [ ] Telecharger TOUS les modeles + LoRAs (liste ci-dessus)
- [ ] Creer compte ElevenLabs (5$/mois) ou installer XTTS-v2 local
- [ ] Creer compte Suno AI Pro (10$/mois) pour musique kids
- [ ] Installer n8n sur VPS

**JOUR 1-2 — DEFINIR L'UNIVERS**
- [ ] Claude definit l'univers thematique : personnages recurrents, style visuel, themes educatifs
- [ ] Generer les personnages de reference dans Stable Diffusion (garder la coherence visuelle)
- [ ] Creer une "bible visuelle" : 5-10 personnages avec prompts SD reproductibles

**JOUR 2-3 — PREMIERE PRODUCTION**
- [ ] Claude ecrit 2 scripts YouTube kids (counting + alphabet)
- [ ] Generer les voix off (ElevenLabs ou XTTS)
- [ ] Generer la musique (Suno AI)
- [ ] Generer les images des scenes (SD, 10-20 par video)
- [ ] Assembler dans Animaker/InVideo/Canva Animate
- [ ] EN PARALLELE : generer 35-50 pages coloring book KDP (memes personnages)
- [ ] EN PARALLELE : generer 10-15 worksheets/coloring pages Etsy (memes personnages)
- [ ] EN PARALLELE : generer 20 designs POD kids (memes personnages)

**JOUR 3-5 — PREMIERS UPLOADS**
- [ ] Publier 2 videos YouTube (long-form + Shorts)
- [ ] Publier 1-2 livres KDP (coloring book + activity book)
- [ ] Publier 15-20 listings Etsy
- [ ] Uploader 20-30 designs sur Redbubble + TeePublic

**JOUR 5-7 — RYTHME DE CROISIERE**
- [ ] 2-3 videos YouTube/semaine
- [ ] 1 livre KDP/jour
- [ ] 10-15 listings Etsy/jour
- [ ] 20-30 designs POD/jour
- [ ] Analyser premieres donnees

**FIN SEMAINE 1 : 2+ videos, 5+ livres KDP, 50+ listings Etsy, 100+ designs POD — tous dans le meme univers kids**

---

### PROJECTION DE REVENUS

| Mois | YouTube | KDP | Etsy | POD | TOTAL |
|------|---------|-----|------|-----|-------|
| 1 | 0 | 0-50 | 50-200 | 0-50 | **50-300** |
| 2 | 0 | 50-150 | 200-500 | 50-150 | **300-800** |
| 3 | 0 | 100-300 | 400-1000 | 100-300 | **600-1600** |
| 6 | 300-1500 | 300-800 | 800-2000 | 300-800 | **1700-5100** |
| 12 | 1000-5000 | 800-3000* | 1500-4000 | 500-1500 | **3800-13500** |

*inclut bonus Q4 (x2-4 en oct-dec)

**Objectif 2000 EUR net/mois → atteignable entre mois 3 et mois 6.**

---

### BUDGET MENSUEL

**Phase 1 (demarrage) :**

| Poste | Cout |
|-------|------|
| 2x Claude Pro | 200$/mois |
| Listings Etsy (~100 x 0.20$) | 20$/mois |
| ElevenLabs Starter (voix kids) | 5$/mois |
| Suno AI Pro (musique kids) | 10$/mois |
| **TOTAL** | **~235$/mois** |

**Phase 2 (quand premiers revenus) :**

| Poste | Cout |
|-------|------|
| Phase 1 | 235$/mois |
| Canva Pro | 12.99$/mois |
| Book Bolt (KDP) | 9.99$/mois |
| Animaker ou InVideo AI | 10-25$/mois |
| **TOTAL** | **~268-293$/mois** |

**Seuil de rentabilite = ~270 EUR/mois**

---

### REGLES DE PIVOT

| Signal | Action |
|--------|--------|
| Une video depasse 10K vues en 7 jours | Creer une SERIE sur ce theme, decliner en KDP+Etsy+POD |
| Un coloring book KDP depasse 5 ventes/semaine | Serie Vol. 2, 3... + activity book companion |
| Un produit Etsy a beaucoup de favoris | 20 variantes dans cette niche |
| Un design POD se vend 3+ fois | 10 declinaisons |
| YouTube stagne <100 vues | Changer de sous-niche kids, tester nouveaux formats |
| 0 vente Etsy apres 30 jours | Revoir keywords, changer de niche kids |
| Couts (270$/mois) pas couverts apres 60 jours | Reduire a 1 Claude, couper outils payants |

---

### INDICATEURS DE SUCCES

| Palier | Objectif |
|--------|----------|
| 0 | Comptes crees + auto-entrepreneur + univers kids defini |
| 1 | Premier euro (n'importe quel moteur) |
| 2 | 270 EUR/mois (couvre les couts) |
| 3 | 500 EUR/mois |
| 4 | 2000 EUR net/mois stable |
| 5 | Systeme <2h/jour de maintenance humaine |
| 6 | Revenus YouTube actifs + catalogue 100+ livres + 500+ listings |

---

### FICHIERS DE REFERENCE

Lis ces fichiers pour les details supplementaires :
- **VERIFIED_TOOLS_2026.md** — Outils verifies avec prix exacts, liens CivitAI, performances GPU, outils kids
- **AUTOENTREPRENEUR_GUIDE.md** — Guide creation statut micro-entreprise

---

### PREMIERE ACTION

Des reception de ce prompt :
1. Lis les fichiers de reference
2. Maximum 2 questions de clarification
3. **Definis l'univers kids** : propose 3 univers thematiques possibles (personnages, style, themes educatifs) avec avantages/inconvenients de chacun
4. Passe a la PRODUCTION :
   a. 2 scripts YouTube kids (counting + alphabet, 3-5 min chacun)
   b. Les prompts Stable Diffusion exacts pour generer les personnages de l'univers choisi
   c. 1 structure de coloring book KDP (titre, 50 prompts SD pour les pages)
   d. 10 listings Etsy kids prets (titres, descriptions, 13 tags chacun)
   e. 10 prompts SD pour designs POD kids
   f. Checklist creation de comptes pas a pas
   g. Checklist auto-entrepreneur

On construit l'ecosysteme. Go.

## FIN DU PROMPT
