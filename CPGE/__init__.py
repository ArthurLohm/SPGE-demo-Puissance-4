"""
Module python CPGE
Game engine for pygame by Codrameurs

"""


# importation necessaire au packet


class Camera: pass


class Screen: pass


class UIScreen: pass


class EventManager:  pass


class Engine: pass


class Sprite: pass


class TimedFunctionManager: pass


class Animation: pass


import pygame

import CPGE.Utils
from CPGE.Animations import Animation, AnimationManager
from CPGE.Camera import Camera
from CPGE.Engine import Engine
from CPGE.EventManager import EventManager
from CPGE.Screen import Screen, UIScreen
from CPGE.Sprite import Sprite, UISprite , PSprite
from CPGE.TimedFunctionManager import TimedFunctionManager
from CPGE.ScreenConceptor import ConvertToScreen
# Constant

PACKAGE_VERSION = "Beta 0.6.0"

#Event
COLISION_EVENT = 1
TOUCHING_EVENT = 2



# informations
print(f"Using CPGE version {PACKAGE_VERSION} => motion update ")
