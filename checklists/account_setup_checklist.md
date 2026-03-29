# CHECKLISTS CRÉATION DE COMPTES — PROJET JACKY
# ================================================
# Chaque checklist = pas à pas copier-coller
# Ordre de priorité : Etsy > KDP > Redbubble > TeePublic > YouTube

---

## 1. ETSY — Compte Vendeur

**Temps estimé :** 15-20 min
**Prérequis :** Email, carte bancaire (pour payer les frais de listing $0.20)

### Étapes :

- [ ] Aller sur **https://www.etsy.com/sell**
- [ ] Cliquer "Get started"
- [ ] Créer un compte (email + mot de passe) OU se connecter avec Google
- [ ] **Langue de la boutique :** English (marché mondial)
- [ ] **Pays :** France
- [ ] **Devise :** EUR
- [ ] **Nom de la boutique** — choisir un nom pro et neutre :
  - Exemples : "PixelPlannerStudio", "ZenPrintableShop", "NovaPrintDesigns"
  - Pas de nom personnel, pas de référence à l'IA
  - Vérifier que le nom est disponible (Etsy te le dit en temps réel)
- [ ] **Créer le premier listing** (Etsy oblige à en créer au moins 1 pour finaliser) :
  - Utiliser un des planners générés (Budget Planner PDF)
  - Copier-coller le listing #1 du fichier `listings_etsy_10.md`
- [ ] **Configurer les paiements (Etsy Payments) :**
  - Renseigner les infos bancaires (IBAN compte FR)
  - Etsy verse les fonds sur ton compte bancaire
  - Pas besoin de SIRET pour OUVRIR la boutique (mais nécessaire pour déclarer)
- [ ] **Configurer la facturation** (frais de listing) :
  - Ajouter une carte bancaire pour payer les frais de listing ($0.20/listing)
- [ ] **Politique de boutique :**
  - "Digital download — no refunds" (standard pour les produits digitaux)
  - Ajouter mention IA si applicable : "Some designs created with AI assistance"

### Post-setup :
- [ ] Installer l'**app Etsy Seller** sur le téléphone (notifications de ventes)
- [ ] Activer les **notifications par email** pour les ventes
- [ ] Publier les 9 autres listings depuis `listings_etsy_10.md`

---

## 2. AMAZON KDP — Compte Éditeur

**Temps estimé :** 20-30 min
**Prérequis :** Compte Amazon (en créer un si nécessaire), infos fiscales

### Étapes :

- [ ] Aller sur **https://kdp.amazon.com**
- [ ] Se connecter avec un compte Amazon (ou en créer un)
- [ ] Accepter les conditions d'utilisation KDP
- [ ] **Remplir les informations d'éditeur :**
  - Nom : ton nom légal (pas affiché publiquement si tu choisis un pen name)
  - Adresse : adresse en France
  - Pays : France
- [ ] **Informations fiscales (TRÈS IMPORTANT) :**
  - Cliquer sur "Complete Tax Information"
  - Sélectionner "I am not a U.S. person"
  - Remplir le formulaire **W-8BEN** :
    - Nom : ton nom légal
    - Pays de citoyenneté : France
    - Adresse : ton adresse FR
    - TIN (Tax ID) : **ton numéro de sécurité sociale** (format : 1 XX XX XX XXX XXX XX)
      OU le futur numéro SIRET quand tu l'auras
    - Treaty claim : cocher "Yes"
    - Article : **12** | Withholding rate : **0%**
    - Type of income : "Royalties"
  - → Avec la convention fiscale France-US, tu paies **0% de retenue** aux US
  - → Tu ne paieras des impôts QU'en France via ton auto-entreprise
- [ ] **Configurer le paiement :**
  - Mode de paiement : Virement bancaire (bank wire)
  - Devise : EUR
  - IBAN de ton compte bancaire français
  - Seuil minimum : 100€ (ou 10€, au choix)
- [ ] **Configurer les marketplaces :**
  - Activer : amazon.com (US), amazon.co.uk (UK), amazon.de (DE), amazon.fr (FR)
  - Les 4 plus gros marchés pour les puzzle/coloring books

### Premier livre :
- [ ] Aller dans **Bookshelf** > **Create** > **Paperback**
- [ ] Générer un puzzle book avec le script :
  ```
  cd C:\Users\zapk\OneDrive\Jacky\production\kdp
  python generate_puzzle_book.py --type wordsearch --theme all --puzzles 50 --large-print --title "Large Print Word Search Puzzle Book" --subtitle "50 Fun Puzzles for Adults and Seniors"
  ```
- [ ] Remplir les métadonnées KDP :
  - **Titre :** Large Print Word Search Puzzle Book
  - **Sous-titre :** 50 Fun Puzzles for Adults and Seniors · 10 Themes · With Solutions
  - **Auteur :** utiliser un pen name (ex: "Puzzle Press Studio")
  - **Description :** voir le listing #5 de `listings_etsy_10.md` (adapter)
  - **Catégorie :** Games & Activities > Puzzles > Word Search
  - **Keywords (7) :** large print word search, word search for adults, word search seniors, puzzle book, word find book, brain games, activity book
  - **Cocher "AI-generated content"** : OUI
- [ ] **Uploader l'intérieur** (le PDF généré par le script)
- [ ] **Cover :** créer dans Canva avec le KDP Cover Calculator
  - Aller sur : https://kdp.amazon.com/cover-calculator
  - Entrer : nombre de pages, type de papier (white)
  - Télécharger le template, l'ouvrir dans Canva, designer la cover
- [ ] **Prix :** $7.99 (sweet spot pour les puzzle books N&B)
- [ ] **Territories :** Worldwide
- [ ] **Publier !** (Review prend 24-72h)

---

## 3. REDBUBBLE — Compte Artiste

**Temps estimé :** 10 min
**Prérequis :** Email

### Étapes :

- [ ] Aller sur **https://www.redbubble.com/signup**
- [ ] Créer un compte (email + mot de passe)
- [ ] **Nom d'artiste :** choisir un nom cohérent avec Etsy (ex: "NovaPrintDesigns")
- [ ] **Configurer le profil :**
  - Bio courte (2-3 phrases) : "Digital artist creating unique designs for everyday products."
  - Pas de photo personnelle (utiliser un logo ou laisser vide)
- [ ] **Configurer les paiements :**
  - PayPal (le plus simple pour Redbubble)
  - OU virement bancaire (disponible dans certains pays)
  - Seuil de paiement minimum : $20
- [ ] **Paramètres de marge :**
  - Redbubble applique un prix de base + ta marge
  - Marge par défaut : 20% — c'est correct pour commencer
  - Tu peux ajuster par produit après

### Premier upload :
- [ ] Cliquer **"Add New Work"**
- [ ] Uploader une image (minimum 2400x3200 pixels pour les t-shirts)
  - Utiliser un design généré par Stable Diffusion + upscalé avec Real-ESRGAN
- [ ] **Titre :** descriptif et riche en mots-clés
  - Ex: "I Code Therefore I Am - Funny Programmer T-Shirt Design"
- [ ] **Tags :** 15 tags maximum, séparés par des virgules
- [ ] **Activer TOUS les produits** (t-shirts, hoodies, mugs, stickers, posters, etc.)
- [ ] **Important :** si le design est AI-generated, le mentionner dans la description

---

## 4. TEEPUBLIC — Compte Artiste

**Temps estimé :** 10 min
**Prérequis :** Email

### Étapes :

- [ ] Aller sur **https://www.teepublic.com/signup**
- [ ] Créer un compte
- [ ] **Configurer le profil** (similaire à Redbubble)
- [ ] **Paiements :** PayPal uniquement
  - Seuil de paiement : $25
  - Paiement le 15 de chaque mois
- [ ] **Rémunération :** $4 fixe par t-shirt vendu (pas de %), plus pour d'autres produits

### Premier upload :
- [ ] Cliquer **"Upload a Design"**
- [ ] Même image que Redbubble (gagner du temps — multi-plateforme)
- [ ] Titre + description + tags similaires
- [ ] TeePublic active automatiquement le design sur tous les produits

---

## 5. YOUTUBE — Chaînes Faceless (x2)

**Temps estimé :** 20 min par chaîne
**Prérequis :** Compte Google (en créer 2 séparés : 1 FR, 1 EN)

### Chaîne FR (Stoïcisme / Développement personnel) :

- [ ] Aller sur **https://studio.youtube.com**
- [ ] Créer une chaîne avec un nom approprié :
  - Exemples : "Sagesse Stoïque", "L'Art de la Mentalité", "Philosophie du Pouvoir"
- [ ] **Photo de profil :** logo ou image SD (statue stoïcienne, symbole philo)
- [ ] **Bannière :** Canva template YouTube (2560x1440 pixels)
  - Texte : nom de la chaîne + "Philosophie · Mentalité · Sagesse Antique"
- [ ] **Description de la chaîne :**
  ```
  Bienvenue. Cette chaîne explore la sagesse des philosophes anciens — stoïcisme,
  psychologie du pouvoir, et mentalité — pour t'aider à naviguer le monde moderne
  avec clarté et force intérieure.

  Nouvelles vidéos chaque semaine.
  Abonne-toi et active la cloche 🔔
  ```
- [ ] **Paramètres importants :**
  - Pays : France
  - Langue : Français
  - Monétisation : se configurera quand les seuils seront atteints (1000 subs + 4000h)
  - Catégorie par défaut : "Education" ou "People & Blogs"

### Chaîne EN (Finance / Business) :

- [ ] Même process avec un nom EN :
  - Exemples : "Wealth Blueprint", "Money Minds", "Smart Capital"
- [ ] **Description :**
  ```
  Money rules. Wealth strategies. Financial literacy that schools don't teach.

  We break down the principles behind real wealth building —
  no hype, no get-rich-quick schemes, just proven strategies.

  New videos every week. Subscribe and hit the bell 🔔
  ```
- [ ] Pays : United States (pour le CPM)
- [ ] Langue : English

### Post-setup (les deux chaînes) :
- [ ] Installer **VidIQ** extension Chrome (gratuit — SEO YouTube)
- [ ] Installer **TubeBuddy** extension Chrome (gratuit — analytics)
- [ ] Préparer la première vidéo avec les scripts dans `production/youtube/`

---

## 6. SPRING (ex-Teespring) — Compte POD

**Temps estimé :** 10 min
**Prérequis :** Email

- [ ] Aller sur **https://www.spri.ng** (nouveau domaine de Spring)
- [ ] Créer un compte
- [ ] Configurer les paiements (PayPal ou virement)
- [ ] Même process d'upload que Redbubble/TeePublic
- [ ] Avantage Spring : tu fixes tes propres prix (marge au choix)

---

## 7. ADOBE STOCK — Contributeur (BONUS)

**Temps estimé :** 15 min
**Prérequis :** Compte Adobe

- [ ] Aller sur **https://contributor.stock.adobe.com**
- [ ] Créer un compte contributeur
- [ ] **Important — politique IA d'Adobe Stock :**
  - Les images AI SONT acceptées
  - Obligation de cocher "Generated with AI" lors de l'upload
  - Maximum 3 variations similaires
  - Minimum 4 mégapixels (2000x2000)
- [ ] Installer **Xpiks** (gratuit) pour le bulk upload + keywording
- [ ] Uploader les mêmes images SD que pour POD (double usage du même pipeline)

---

## RÉCAP — ORDRE DE CRÉATION

| # | Compte | Priorité | Action humaine requise |
|---|--------|----------|----------------------|
| 1 | **Etsy** | 🔴 URGENT | Z crée aujourd'hui |
| 2 | **Amazon KDP** | 🔴 URGENT | Z crée aujourd'hui |
| 3 | **Redbubble** | 🟡 HAUTE | Z ou associé crée J1-J2 |
| 4 | **TeePublic** | 🟡 HAUTE | Z ou associé crée J1-J2 |
| 5 | **YouTube FR** | 🟡 HAUTE | Z crée J1-J2 |
| 6 | **YouTube EN** | 🟡 HAUTE | Associé crée J1-J2 |
| 7 | **Spring** | 🟢 MOYEN | J2-J3 |
| 8 | **Adobe Stock** | 🟢 MOYEN | J2-J3 |
| 9 | **Auto-entrepreneur** | 🔴 URGENT | Z crée MAINTENANT (voir AUTOENTREPRENEUR_GUIDE.md) |

**Total temps humain estimé : ~2h pour tout créer.**
