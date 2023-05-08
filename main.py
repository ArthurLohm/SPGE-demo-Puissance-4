from CPGE import *

size = (1200,800)
title = " The Fourth One"
poids = (0,1)




class  Game :

    def __init__(self):
        print("lancement du chargment")

        self.engine = Engine(size, title)

        self.mainScreen = ConvertToScreen("resources\\data\\mainscreen.json")
        self.mainEvent = EventManager()
        self.mainEvent.AddEvent(pygame.KEYDOWN,self.event)

        self.pions = []
        self.arrow = SelectionArrow(self.mainScreen)
        self.mainCam = Camera(self.mainScreen , size)

    def event(self,event):
        if event.key == pygame.K_LEFT:
            self.arrow.switchColumn("left")
        elif event.key == pygame.K_RIGHT:
            self.arrow.switchColumn("right")
        elif event.key == pygame.K_SPACE:
            self.pions.append(PSprite(self.mainScreen,self.arrow.coords,(90,90),"resources\\images\\pion.png",True).addNewForce(poids,-1))


    def startGame(self):




        self.engine.startEngine(self.mainCam , self.mainEvent)
        print("lancement du jeu")




class SelectionArrow(Sprite):
    
    def __init__(self, screen):
        super().__init__(screen, (170,70),(83,59),"resources\\images\\arrow.png",False,"arrow")
        self.selectedColumn = 0
        self.listOfCoords = [(170,70),(300,70),(430,70),(560,70),(690,70),(820,70),(950,70)]

    def switchColumn(self,sense):
        if sense == "right":
            if self.selectedColumn < 6 :
                self.selectedColumn += 1


        elif sense == "left":
            if self.selectedColumn > 0 :
                self.selectedColumn -= 1 
              
        self.setCoords(self.listOfCoords[self.selectedColumn])







game = Game()
game.startGame()