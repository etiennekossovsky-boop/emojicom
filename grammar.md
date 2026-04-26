# Syntax & grammar

# Emojicom Syntax v0.1
Copyright 2026 Emojicom
Licensed under the Apache License, Version 2.0

## 1. Objectif
Ce document formalise les conventions de syntaxe pour Emojicom v0.1. 
Principe : stabilité et simplicité avant expressivité.

## 2. Flèches et transitions
Uniquement 2 symboles autorisés en v0.1 :

| Symbole | Sens | Usage |
| --- | --- | --- |
| ➡️ | Passage, transformation, séquence | Marque un passage clair d'un état à un autre |
| 🔄 | Échange, réciprocité, circularité | Marque une relation mutuelle ou cyclique |

Exemple : 🤝 ➡️ 🌍 = coopération qui se déploie vers le monde

## 3. Répétition et intensité
La répétition d'un emoji marque l'intensité, la pluralité ou le caractère massif.

Exemple : 🔥🔥 = crise majeure, urgence forte

Règle v0.1 : Répétition interdite dans les serials officiels sauf si documentée et justifiée dans la proposition. Les forks expérimentaux peuvent explorer.

## 4. Modificateurs v0.1
4 modificateurs autorisés, usage parcimonieux :

| Modificateur | Sens | Position |
| --- | --- | --- |
| ❗ | Alerte, urgence, attention | Avant ou après le serial |
| ❓ | Questionnement, incertitude | En fin de serial |
| ♻️ | Durabilité, circularité, recyclage | Qualifie une Valeur ou Résultat |
| 🔍 | Analyse, enquête, observation | Qualifie une Action |

Exemple : ⚠️ 🔍 🛠️ 🙂 = problème analysé → action → apaisement

## 5. Basic Alphabet v0.1
Emojis de base recommandés par catégorie pour construire les serials :

### Émotions & États
| Emoji | Sens |
| --- | --- |
| 😀 | Joie, satisfaction, succès |
| 😢 | Tristesse, difficulté, échec |
| 😠 | Colère, conflit, tension |
| 😐 | Neutralité, doute, attente |

### Nature & Environnement
| Emoji | Sens |
| --- | --- |
| 🌍 | Monde, global, impact large |
| 🌱 | Croissance, début, potentiel |
| 🔥 | Urgence, crise, énergie forte |
| 💧 | Adaptation, fluidité, ressource |

### Actions & Processus
| Emoji | Sens |
| --- | --- |
| 🛠️ | Travail, construction, réparation |
| 🤝 | Collaboration, partenariat, accord |
| 📚 | Apprentissage, connaissance, étude |
| 💡 | Idée, innovation, insight |

### Valeurs & Résultats
| Emoji | Sens |
| --- | --- |
| ⭐ | Excellence, qualité, réussite |
| 🎯 | Objectif, direction, focus |
| 💰 | Ressource, valeur, impact économique |
| 🏆 | Victoire, accomplissement, leadership |

## 6. Règles générales
1. 2 à 4 emojis par serial en v0.1. Pas plus.
2. Pas d'emoji de ponctuation autre que ceux listés ci-dessus.
3. L'ordre `[Contexte] → [Action] → [Valeur] → [Résultat]` prime sur tout.
4. Tout ajout à la syntaxe passe par une issue + discussion + accord.


Etienne Kossovsky <etienne.kossovsky@gmail.com>
dim. 19 avr. 16:56 (il y a 7 jours)
À moi

# Emojicom Specification v0.1 — The Boop Release
Statut : Spécification initiale stable
Version : 0.1.0
Auteur : Initiative Emojicom (fondée par Etienne)
Licence : Open Standard — CC BY 4.0

---

# 1. Introduction

Emojicom est une langue visuelle universelle fondée sur des séquences d’emojis.
Cette spécification définit la grammaire minimale, les règles de composition,
les catégories d’usage et les séquences canoniques qui constituent la version
initiale du standard.

Objectifs principaux :
- permettre une communication simple et universelle
- réduire les barrières linguistiques
- offrir un système utilisable dans les contextes internationaux, humanitaires,
  éducatifs et institutionnels
- fournir une base stable pour des extensions futures

Cette version (v0.1) est appelée **The Boop Release** : la première norme
fonctionnelle, minimale mais cohérente.

---

# 2. Terminologie

- **Emoji** : unité visuelle de base.
- **Séquence** : suite ordonnée d’emojis formant un message.
- **Bloc** : rôle grammatical attribué à un emoji (Sujet, Action, Objet, Contexte).
- **Message** : séquence complète respectant la grammaire Emojicom.
- **Canonique** : séquence validée officiellement par la gouvernance Emojicom.
- **RFC** : proposition formelle de modification du standard.

---

# 3. Grammaire fondamentale

La structure minimale d’un message Emojicom est :

    Sujet → Action → Objet → Contexte (optionnel)

## 3.1 Sujet
Représente l’entité qui agit.

Exemples :
- 👤 personne
- 👥 groupe
- 🧑‍⚕️ professionnel
- 🏛️ institution

Règles :
- placé en premier
- explicite en v0.1

## 3.2 Action
Représente le verbe ou l’intention principale.

Exemples :
- ➡️ aller
- 🤝 coopérer
- 📢 annoncer
- 🆘 demander de l’aide

Règles :
- obligatoire
- une seule action principale par message

## 3.3 Objet
Ce sur quoi porte l’action.

Exemples :
- 🏥 hôpital
- 📚 livres
- 🌍 monde

Règles :
- suit immédiatement l’Action

## 3.4 Contexte (optionnel)
Précise la situation.

Exemples :
- 📍 lieu
- 🕒 temps
- ⚠️ danger
- 🎉 événement

Règles :
- placé en fin de message
- peut contenir plusieurs emojis

---

# 4. Règles générales de composition

## 4.1 Ordre de lecture
Les messages se lisent de gauche à droite.

## 4.2 Longueur
Un message doit contenir entre **3 et 7 emojis**.

## 4.3 Ambiguïté
Les emojis à forte connotation culturelle ou polysémique doivent être évités
dans les usages institutionnels.

## 4.4 Atomicité
Chaque emoji représente une unité de sens.  
Les combinaisons complexes seront introduites en v0.2+.

---

# 5. Catégories d’usage

Les séquences Emojicom sont classées en cinq catégories :

1. **Orientation & Signalétique**
2. **Sécurité & Urgence**
3. **Diplomatie & Coopération**
4. **Rituels & Interculturalité**
5. **Éducation & Inclusion**

Les séquences canoniques sont listées dans `/sequences/canonical/`.

---

# 6. Exemples de messages conformes

## 6.1 Déplacement
👤 ➡️ 🏫  
= “Je vais à l’école”

## 6.2 Rencontre internationale
👥 🤝 🌍 📍🏛️  
= “Rencontre internationale au bâtiment officiel”

## 6.3 Urgence
👤 🆘 ➡️ 🏥 📍📍  
= “Urgence → besoin d’aller à l’hôpital → localisation”

## 6.4 Signalétique
👤 ➡️ 🚻 📍⬆️  
= “Toilettes → direction vers le haut”

---

# 7. Séquences canoniques

Les séquences validées officiellement sont stockées dans :

    /sequences/canonical/

Chaque séquence doit :
- respecter la grammaire v0.1
- être culturellement neutre
- être testée dans au moins deux contextes réels
- être approuvée via le processus RFC

---

# 8. Processus d’évolution du standard

## 8.1 RFC (Request For Comments)
Toute modification majeure (grammaire, séquence canonique, catégorie d’usage)
doit passer par une RFC.

Les RFC sont stockées dans :

    /governance/RFC-process.md

## 8.2 Versioning
Emojicom suit un modèle inspiré du SemVer :

    MAJEUR.MINEUR.PATCH

- **MAJEUR
