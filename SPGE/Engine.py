#coding: utf-8

from SPGE import *
from SPGE.Animations import ANIMATION_MANAGER


class Engine():#class principal permettant de lancer le moteur
    
    def __init__(self, screenSize: tuple , screenName:str ):
        """Engine init

        Args:
            screenSize (tuple): taille de la fenetre
            screenName (str): nom de la fenetre
        """

        #creation des attribut de l objet
        self.screenSize = screenSize
        self.screenName = screenName
        self.gameOpen  = False
        self.clock=pygame.time.Clock()
        self.TimedFunctionManager = None
        #init de pygame 
        pygame.init()
        pygame.display.set_caption(self.screenName)
        self.surface=pygame.display.set_mode(self.screenSize)


    def setTimedFunctionManager(self, timedFunctionManager : TimedFunctionManager):
        self.TimedFunctionManager = timedFunctionManager


    def startEngine(self,cam :  Camera ,eventManager : EventManager):
        #demare le jeux
        self.cam=cam
        self.eventManager=eventManager

        self.gameOpen= True
        self.mainLoop()


    def switchCamera(self, newcam : Camera):
        self.cam=newcam


    #relatif a la mise a jours des graphisme

    def mainLoop(self):
        #boucle principale

        while self.gameOpen : #lancement de la boucle du jeux

            #gestion des evenement
            self.eventManager.detectEvt(pygame.event.get(),self)#recuperateur d evt

            # gestion timed fonction
            if self.TimedFunctionManager != None:
                self.TimedFunctionManager.callTimedFunctions()


            ANIMATION_MANAGER.playAnimations()

            #gestion de la physique
            self.cam.screen.UpdatePSprite()
            #mise a jour des graphismes
            self.__graphicUpdate()

            self.clock.tick(60)

        
    def __graphicUpdate(self):
        
        self.surface.blit(self.cam.screen.background,(0,0))#mise  en place du fond

        self.__SpritePrinter(self.cam)#ajout des sprite

        pygame.display.flip()#aplication des changement


    def __SpritePrinter(self, cam : Camera):
        #afiche les sprite a l ecran
        for element in cam.getRenderOfCamera():
            self.surface.blit(element.texture, element.coordsToRender)



