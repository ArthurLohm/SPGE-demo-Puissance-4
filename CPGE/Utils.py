#coding:utf-8

from CPGE import *

def loadImage(imagePath : str):
    return pygame.image.load(imagePath).convert_alpha()
    
    