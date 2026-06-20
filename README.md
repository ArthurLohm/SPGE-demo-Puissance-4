# SPGE — Small Pygame Game Engine

> Moteur de jeu 2D léger en Python, conçu pour simplifier la création de jeux avec Pygame.

![Version](https://img.shields.io/badge/version-release%201.0-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Pygame](https://img.shields.io/badge/Pygame-required-green)

---

## Table des matières

1. [Genèse du projet](#genèse-du-projet)
2. [Généalogie](#généalogie)
3. [Fonctionnalités](#fonctionnalités-du-moteur)
4. [Architecture](#architecture)
5. [Installation](#installation)
6. [Utilisation rapide](#utilisation-rapide)
7. [Principaux composants](#principaux-composants)
8. [Démonstration : Puissance 4](#démonstration--puissance-4)

---

## Genèse du projet

J'ai commencé à apprendre le Python lorsque j'étais en classe de 5ème. Depuis le début, j'ai toujours été motivé par une envie de création. Rapidement, j'ai souhaité apprendre à utiliser des modules permettant de réaliser des interfaces graphiques pour assouvir ma créativité. J'ai commencé par la bibliothèque tkinter. Cependant, j'ai rapidement été frustré par les limitations et le manque de flexibilité du module. Je me suis alors tourné vers le module pygame, beaucoup plus flexible mais disposant de très peu de fonctionnalités natives et demandant de coder soi-même les fonctionnalités. J'ai réalisé un premier projet non abouti qui m'a permis de prendre en main le module.

Quelques années plus tard, en classe de seconde, après avoir fait mes armes sur d'autres projets, langages ou moteurs de jeux comme Unity, j'ai eu l'envie de construire un moteur de jeu en me basant sur la bibliothèque pygame. L'objectif était de concevoir une surcouche du module pygame ajoutant des moyens de construire un jeu rapidement, comme la gestion des sprites, des boutons, de la caméra, etc. Je ne cherchais pas à réaliser un projet que je pourrais exploiter par la suite, mais j'étais principalement motivé par le défi que cela implique et la réflexion à mener pour construire l'architecture d'un tel projet. C'est encore à ce jour mon plus gros projet de programmation abouti.

Finalement, en première année de classe préparatoire, souhaitant pouvoir montrer à mes amis l'aboutissement de ce projet, j'ai réalisé la démonstration que voici en créant un Puissance 4 en quelques heures à l'aide du moteur.

---

## Généalogie

- **2022** : début du projet (réalisation de la majeure partie)
- **2023** : amélioration, ajout de principes physiques élémentaires à l'aide des connaissances acquises au lycée (1ère spécialité physique)
- **2025** : réalisation de la démonstration — Puissance 4 —
- **2026** : reprise du projet pour le rendre présentable dans le cadre de ma candidature à l'ENS de Rennes *(aucune modification du code)*

Le moteur SPGE et la démonstration Puissance 4 ont été développés sans aide d'IA.
La reprise de 2026 a uniquement consisté à rendre le dépôt plus lisible et présentable dans le cadre de la candidature.

---

## Fonctionnalités du moteur

- **Sprites** : sprites simples, sprites physiques (avec forces et collisions), sprites d'interface (UI)
- **Physique** : application de forces, calcul de vitesse, détection et résolution de collisions
- **Caméra** : rendu d'une portion de l'écran, déplacement, support d'un calque UI superposé
- **Écrans** : gestion de scènes avec ajout/suppression de sprites et filtrage par tag
- **Animations** : séquences d'images à fréquence configurable
- **Événements** : écoute des événements Pygame et des événements de collision/contact entre sprites
- **TimedFunctionManager** : déclenchement de fonctions à intervalles réguliers (en frames)
- **ScreenConceptor** : chargement d'une scène complète depuis un fichier JSON
- **Utils** : chargement d'images avec transparence

---

## Architecture

```
SPGE/
├── __init__.py               # Point d'entrée du module, exports et constantes
├── Engine.py                 # Boucle principale du jeu (rendu, physique, événements)
├── Camera.py                 # Rendu d'une zone de l'écran vers la fenêtre
├── Screen.py                 # Conteneurs de sprites (Screen, UIScreen)
├── Sprite.py                 # Sprite, PSprite (physique), UISprite
├── Animations.py             # Animation et AnimationManager
├── EventManager.py           # Gestion des événements Pygame et collisions
├── TimedFunctionManager.py   # Déclenchement de fonctions temporisées
├── ScreenConceptor.py        # Chargement de scène depuis JSON
└── Utils.py                  # Fonctions utilitaires (chargement d'images)
```

---

## Installation

```bash
git clone https://github.com/ArthurLohm/SPGE-demo-Puissance-4.git
cd SPGE-demo-Puissance-4
pip install pygame
python main.py
```

---

## Utilisation rapide

L'exemple ci-dessous illustre la mise en place minimale d'un projet avec SPGE. La démonstration Puissance 4 (incluse dans ce dépôt) montre une utilisation plus complète du moteur, notamment la physique, les événements et le chargement de scènes via JSON.

```python
from SPGE import *

# Initialisation du moteur
engine = Engine((1080, 720), "Mon Jeu")

# Création d'une scène
screen = Screen()
screen.SetBackGround("ressources/background.png")

# Ajout d'un sprite
sprite = Sprite(screen, (100, 100), (64, 64), "resources/player.png", isCollidable=True)

# Caméra
cam = Camera(screen, (1080, 720))

# Événements
events = EventManager()
events.AddEvent(pygame.KEYDOWN, lambda e: print(e.key))

# Lancement
engine.startEngine(cam, events)
```

---

## Principaux composants

### `Engine`
Classe centrale. Initialise Pygame, gère la boucle principale (60 FPS), orchestre le rendu, la physique et les événements.

```python
engine = Engine((largeur, hauteur), "Titre")
engine.setTimedFunctionManager(timedFunctionManager)
engine.startEngine(camera, eventManager)
```

### `Sprite`
Objet visuel de base. Gère position, texture, collisions et animations.

```python
Sprite(screen, coords, dimension, texture, isCollidable, tag)
sprite.move((dx, dy))       # Déplacement avec détection de collision
sprite.switchTexture(image) # Changer la texture
sprite.destroy()            # Supprimer le sprite
```

### `PSprite` *(Physical Sprite)*
Sprite soumis à des forces physiques (gravité, impulsions…).

```python
psprite = PSprite(screen, coords, dimension, texture)
psprite.addNewForce((0, 5), duration=-1)  # Force permanente vers le bas
psprite.maxV = (10, 20)                   # Vitesse maximale
```

### `Camera`
Projette une zone de la scène vers la fenêtre. Supporte un calque UI indépendant.

```python
cam = Camera(screen, (largeur, hauteur), uiScreen)
cam.move((dx, dy))
cam.switchScreen(newScreen)
```

### `EventManager`
Écoute les événements Pygame et les événements de contact entre sprites.

```python
manager = EventManager()
manager.AddEvent(pygame.KEYDOWN, maFonction)
manager.AddColisionEvent(sprite, "tag_cible", onContact)
```

### `TimedFunctionManager`
Déclenche une fonction à intervalles réguliers (exprimés en frames).

```python
timer = TimedFunctionManager()
timer.addTimedFunction(maFonction, frequence=60, nbIteration=1)  # 1 fois après 60 frames
timer.addTimedFunction(maFonction, frequence=30, nbIteration=-1) # Toutes les 30 frames indéfiniment
```

### `Animation`
Séquence de textures jouée sur un sprite à une fréquence donnée.

```python
anim = Animation("marche", [img1, img2, img3], frequenceOfAnimation=5)
sprite.AddAnimation(anim)
sprite.playAnim("marche")
```

### `ScreenConceptor`
Charge une scène complète (fond + sprites) depuis un fichier JSON.

```python
screen = ConvertToScreen("resources/data/mainscreen.json")
```

Format JSON attendu :
```json
{
  "ScreenData": { "background": "resources/bg.png" },
  "Sprites": {
    "sol": {
      "coords": [0, 650], "dimension": [1080, 50],
      "texture": "resources/sol.png",
      "isCollidable": true, "tag": "sol"
    }
  }
}
```

---

## Démonstration : Puissance 4

Le dossier contient une implémentation complète du jeu de Puissance 4 réalisée en quelques heures à l'aide de SPGE, illustrant la rapidité de développement qu'offre le moteur.

### Contrôles

| Touche  | Action                          |
|---------|---------------------------------|
| ← / →   | Déplacer la flèche de sélection |
| Espace  | Poser un pion                   |
| Entrée  | Rejouer après une partie        |

### Lancement

```bash
python main.py
```

---

## Auteur

Arthur Lhomme-Daniel
