#coding:utf-8
from pyclbr import Function
from SPGE import *


class EventManager():
        #permet de gerer les evenement
        
        def __init__(self):
            #initialise l objet
            self.pygameEventToListen=[]
            self.eventlist =[] #contiens lmiste avec [0 : type event , 1: paramettere rela a l ' evt , 2: fonction à appeler]

        #gestion des evenement
        def AddEvent(self,eventType,action : Function):
            #ajoute un evenemnt a surveiller
            self.pygameEventToListen.append([eventType,action])

        def AddColisionEvent(self,sprite, tag,  action :Function):
            self.eventlist.append([SPGE.TOUCHING_EVENT, [sprite,tag],action ])


        def deleteSpriteEvents(self,sprite):
            for event in self.eventlist :
                if event[1][0] == sprite : 
                    self.eventlist.pop(self.eventlist.index(event))



        #detection des evenement

        def detectEvt(self,evt, engine : Engine):
            # detect les evenement lié à pygame 
            for event in evt:
                eventType=event.type

                for eventToListen in self.pygameEventToListen:
                    if eventToListen[0] == eventType:
                        eventToListen[1](event)

                if eventType == pygame.QUIT:
                    engine.gameOpen=False

            # detecte les évenement du moteur 

            for event in self.eventlist :

                if event[0] == SPGE.COLISION_EVENT:
                     # gere evenement de colision
                    for sprite in event[1][0].screen.getScreenSprites(event[1][1]):
                        if event[1][0].IsColliding(sprite): 
                            event[2](sprite)
                
                if event[0] == SPGE.TOUCHING_EVENT:
                     # gere evenement de colision
                    for sprite in event[1][0].screen.getScreenSprites(event[1][1]):
                        if event[1][0].IsTouching(sprite): 
                            event[2](sprite)
