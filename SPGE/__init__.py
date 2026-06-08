"""
Module python SPGE
Small Game engine for pygame

"""


# importations necessaire au packet


class Camera: pass


class Screen: pass


class UIScreen: pass


class EventManager:  pass


class Engine: pass


class Sprite: pass


class TimedFunctionManager: pass


class Animation: pass


import pygame

import SPGE.Utils
from SPGE.Animations import Animation, AnimationManager
from SPGE.Camera import Camera
from SPGE.Engine import Engine
from SPGE.EventManager import EventManager
from SPGE.Screen import Screen, UIScreen
from SPGE.Sprite import Sprite, UISprite , PSprite
from SPGE.TimedFunctionManager import TimedFunctionManager
from SPGE.ScreenConceptor import ConvertToScreen
# Constant

PACKAGE_VERSION = "Beta 0.6.0"

#Event
COLISION_EVENT = 1
TOUCHING_EVENT = 2



# informations
print(f"Using CPGE version {PACKAGE_VERSION} => motion update ")
