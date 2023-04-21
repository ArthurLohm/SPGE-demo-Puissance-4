from CPGE import *

size = (1200,800)
title = " The Fourth One"





class  Game :

    def __init__(self):
        print("lancement du chargment")

        self.engine = Engine(size, title)

        self.mainScreen = ConvertToScreen("resources\\data\\mainscreen.json")
        self.mainEvent = EventManager()

        self.mainCam = Camera(self.mainScreen , size)

    def startGame(self):
        self.engine.startEngine(self.mainCam , self.mainEvent)
        print("lancement du jeu")











game = Game()
game.startGame()