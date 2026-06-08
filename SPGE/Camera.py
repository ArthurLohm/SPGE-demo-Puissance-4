# coding: utf-8
from SPGE import *


class Camera():
    # objet servant a faire le rendu etre un  Screen absatrait vers interface graphique

    # gestion des propriete de la camera

    def __init__(self, screen: Screen, taille: tuple, UIScreen: Screen = None):
        self.screen = screen
        self.taille = taille
        self.coords = (0, 0)
        self.coordsOP = taille
        self.idbox = pygame.Rect((0, 0), taille)

        self.UIScreen = UIScreen

    def __str__(self) -> str:
        return f"Camera on {self.screen} with the uiScreen {self.UIScreen} "

    def switchScreen(self, newscreen: Screen):
        self.screen = newscreen

    def switchUIScreen(self, newscreen: UIScreen):
        self.UIScreen = newscreen

    # gestion du rendu de la camera

    def getRenderOfCamera(self) -> list:
        # renvoie une list des elements a rendre

        spritesToRender = self.__renderOfSprites()

        if self.UIScreen != None:
            spritesToRender = self.__renderOfUISprites() + spritesToRender

        return spritesToRender

    def __renderOfSprites(self) -> list:
        spritesToRender = []
        for sprite in self.screen.getScreenSprites():
            if self.idbox.colliderect(sprite.idbox):
                spritesToRender.append(sprite)

        for sprite in spritesToRender:
            sprite.setCoordsToRender((sprite.coords[0] - self.coords[0], sprite.coords[1] - self.coords[1]))

        return spritesToRender

    def __renderOfUISprites(self):
        return self.UIScreen.getScreenSprites()

        # gestion  du positionement de la cam

    def SetCoordsCam(self, newCoords: tuple):
        # change les coordone de la camera
        self.coords = newCoords
        self.idbox = self.idbox.move(self.coords)

    def move(self, vector: tuple):
        self.coords = (self.coords[0] + vector[0], self.coords[1] + vector[1])
        self.idbox = pygame.Rect(self.coords, self.taille)
