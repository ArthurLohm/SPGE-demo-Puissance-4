#coding:utf-8

from CPGE import *
from json import load


def ConvertToScreen(FilePath : str) -> Screen:
    data = load(open(FilePath))
    screen = Screen()
    #mise en place du fond
    screen.SetBackGround(data["ScreenData"]["background"])

    #ajout des sprites du screen
    for spriteData in data["Sprites"]:

        screen.addSprite(__ConvertToSprite(screen, data["Sprites"][spriteData]))
    
    
    return screen



def __ConvertToSprite(screen: Screen,data : dict):
    return Sprite(screen,data["coords"],data["dimension"],data["texture"],data["isCollidable"],data["tag"])
