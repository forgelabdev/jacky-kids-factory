# GUIDE CREATION AUTO-ENTREPRENEUR — OPERATEUR Z (France)

> Etape 0 du projet. OBLIGATOIRE avant de facturer le moindre euro.
> Temps estime : 15-20 minutes.
> Cout : 0 EUR.

---

## Pourquoi c'est obligatoire

En France, facturer sans statut = travail dissimule (delit penal). L'auto-entreprise (micro-entreprise) est :
- Gratuite a creer
- Operationnelle immediatement (SIRET recu en 1-5 jours)
- Charges sociales = 21.1% du CA pour les prestations de services (BNC)
- Pas de TVA tant que CA < 36 800 EUR/an (franchise en base de TVA)
- Compatible avec le statut de demandeur d'emploi (cumul ARE + auto-entreprise possible)

**IMPORTANT : cumul chomage + auto-entreprise**
- Tu GARDES tes allocations ARE pendant le demarrage
- Tu declares ton CA mensuel a France Travail
- Tes allocations sont recalculees en fonction du CA (pas supprimees)
- C'est 100% legal et prevu par le systeme

---

## Etape par etape

### 1. Se connecter au portail de creation

**URL :** https://www.autoentrepreneur.urssaf.fr/portail/accueil/creer-mon-auto-entreprise.html

Ou via le guichet unique : https://formalites.entreprises.gouv.fr/

**Documents necessaires :**
- Piece d'identite (carte d'identite ou passeport)
- Justificatif de domicile recent
- Numero de securite sociale

### 2. Remplir le formulaire

**Informations a fournir :**

| Champ | Quoi mettre |
|-------|-------------|
| Activite | Prestation de services informatiques / Conseil en systemes et logiciels informatiques |
| Code APE suggere | **6201Z** (Programmation informatique) ou **6202A** (Conseil en systemes informatiques) |
| Categorie | BNC (Benefices Non Commerciaux) |
| Date de debut | La date du jour |
| Periodicite de declaration | Mensuelle (permet de mieux suivre) |
| Option versement liberatoire IR | OUI si eligible (revenu fiscal de reference < seuil). Simplifie l'impot. |

**Pourquoi 6202A (Conseil en systemes informatiques) :**
- Couvre large : services IA, automatisation, conseil tech, produits digitaux
- BNC = regime le plus adapte pour des prestations intellectuelles
- Charges sociales = 21.1% (pas 12.3% comme les activites commerciales, mais c'est normal pour du service)

### 3. Soumettre et attendre le SIRET

- Validation en general sous **1 a 5 jours ouvrables**
- Tu recois un numero SIRET par courrier et/ou sur le portail
- Ce SIRET est necessaire pour creer un compte Stripe, emettre des factures, etc.

### 4. Ouvrir un compte bancaire dedie

**Obligatoire si CA > 10 000 EUR/an pendant 2 annees consecutives.**
Recommande des le depart pour la clarte comptable.

**Options gratuites ou tres low cost :**
- **Revolut Business** : gratuit, carte incluse, compatible Stripe
- **Qonto** : a partir de 9 EUR/mois (mais propre et bien integre)
- **Shine** : a partir de 7.90 EUR/mois
- **Boursorama** : compte pro gratuit sous conditions

**Recommandation : Revolut Business (gratuit) pour commencer, on upgrade si necessaire.**

### 5. Configurer les paiements

Une fois le SIRET en main :
1. Creer un compte **Stripe** avec le SIRET → permet d'encaisser via Payhip, Lemon Squeezy, etc.
2. Creer/mettre a jour le compte **PayPal** en mode professionnel
3. Optionnel : ouvrir un compte **Wise** pour les transactions internationales (partenaire en Thailande)

### 6. Declarer a France Travail

**IMPORTANT : ne pas oublier cette etape.**

- Signaler la creation d'activite a France Travail (ex-Pole Emploi)
- Se fait via l'espace personnel en ligne ou en agence
- Choisir le maintien de l'ARE avec activite complementaire
- Chaque mois, declarer le CA brut sur l'espace France Travail

---

## Checklist recapitulative

```
[ ] Piece d'identite prete
[ ] Justificatif de domicile pret
[ ] Creation auto-entreprise sur autoentrepreneur.urssaf.fr
[ ] Code APE : 6202A
[ ] Periodicite mensuelle cochee
[ ] Versement liberatoire coche (si eligible)
[ ] Formulaire soumis
[ ] En attente de SIRET (1-5 jours)
[ ] Compte Revolut Business cree
[ ] Stripe configure avec SIRET
[ ] PayPal passe en pro
[ ] France Travail informe de la creation d'activite
```

---

## Que faire en attendant le SIRET ?

**On ne perd pas de temps :**
- Creer les comptes ComeUp, Fiverr (pas besoin de SIRET pour creer le profil)
- Preparer les offres de services
- Construire les produits digitaux
- Installer n8n sur le VPS
- Le SIRET arrive en parallele, et des qu'il est la → on active Stripe → on encaisse

---

## Fiscalite simplifiee

| Element | Montant |
|---------|---------|
| Objectif CA mensuel | ~2 530 EUR brut (pour 2 000 EUR net) |
| Charges sociales (21.1%) | ~534 EUR |
| Impot (si versement liberatoire, 2.2%) | ~56 EUR |
| **Net apres charges et impot** | **~1 940 EUR** |
| Plafond CA annuel (BNC) | 77 700 EUR |

**Pour toucher 2 000 EUR net/mois, il faut facturer environ 2 550 EUR brut/mois.**
