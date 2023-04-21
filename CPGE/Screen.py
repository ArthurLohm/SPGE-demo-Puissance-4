#coding: utf-8

from CPGE import *


class SuperScreen():
    def __init__(self):

        self.sprites=[]
        
        
    def __str__(self):
        stringToReturn=""
        for sprite in self.sprites:
            stringToReturn = stringToReturn +"\n    "+ str(sprite)
        return "Sprites in the Screen :" + stringToReturn
        
        
    def addSprite(self,sprite : Sprite):
        #ajoute un sprite a screen
        self.sprites.append(sprite)       


    def getScreenSprites(self, tag = None)-> list:
        #renvoie une liste des sprites de la scene
        if tag != None:#ne renvoie que les sprites avec le tag
            SpritesToReturn=[]
            for sprite in self.sprites:
                if sprite.tag == tag:
                    SpritesToReturn.append(sprite)
                    
            return SpritesToReturn
        
        else:
            return self.sprites
        
        
        
class Screen(SuperScreen):
    #represente un ecran dans lequelle est place les element
    def __init__(self):

        super().__init__()
        self.collidableSprites=[]
        self.PSprites=[]



    def SetBackGround(self,backgroundPath: str ):
        self.background=pygame.image.load(backgroundPath)
        self.background.convert()


    def verifColisions(self,sprite : Sprite) -> bool:
        #verifie si le sprite donne est en colision
        for collidableSprite in self.collidableSprites:
            if sprite.idbox != collidableSprite.idbox :
                if sprite.idbox.colliderect(collidableSprite.idbox):
                    return collidableSprite

        return False

    def addSprite(self,sprite : Sprite):
        # ajoute un sprite a screen gère la colision

        self.sprites.append(sprite)
        if sprite.isCollidable == True:
            self.collidableSprites.append(sprite)       

    def UpdatePSprite(self):
        for pSprite in self.PSprites:
            pSprite.applyForces()


class UIScreen(SuperScreen):
    
    def __init__(self):
        super().__init__()
        

