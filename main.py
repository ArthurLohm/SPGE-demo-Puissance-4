from SPGE import *
from json import load

OptionPath = "resources\\data\\option.json"


class Game:

    def __init__(self):
        print("Chargement....")

        # Partie logique
        self.partie = P4Game()
        self.option = load(open("C:\\Users\\arthu\\Documents\\Code_python\\Puissance 4\\resources\\data\\option.json"))

        # Partie graphique
        self.engine = Engine(self.option["General"]["WindowSize"], self.option["General"]["Title"])
        self.timeFunc = TimedFunctionManager()
        self.engine.setTimedFunctionManager(self.timeFunc)

        self.mainScreen = ConvertToScreen("C:\\Users\\arthu\\Documents\\Code_python\\Puissance 4\\resources\\data\\mainscreen.json")
        self.mainEvent = EventManager()
        self.mainEvent.AddEvent(pygame.KEYDOWN, self.event)

        self.pions = []
        self.victoryScreen = None

        self.mainCam = Camera(self.mainScreen, self.option["General"]["WindowSize"])
        self.player = 1
        self.arrow = SelectionArrow(self.mainScreen, self.option["Ressources"]["Arrow"][f"J{self.player}"])
        self.gameStarted = False


    def event(self, event):
        if event.key == pygame.K_LEFT:
            self.arrow.switchColumn("left")
        elif event.key == pygame.K_RIGHT:
            self.arrow.switchColumn("right")
        elif event.key == pygame.K_SPACE:
            self.play()
        elif event.key == pygame.K_RETURN:
            if self.gameStarted == False:
                self.resetGame()


    def play(self):
        # Vérification de l'état du jeu
        if self.partie.GameState == 0:
            return None

        # On place un pion
        if self.partie.play(self.partie.GameState, self.arrow.selectedColumn) == False:
            return None

        # On place graphiquement un pion
        self.pions.append(PSprite(self.mainScreen, self.arrow.coords, (90, 90), self.option["Ressources"]["Pion"][f"J{self.player}"], True))
        self.pions[-1].addNewForce(self.option["GameSettings"]["Poids"], -1)
        self.partie.GameState = 0
        if self.partie.VerifWin():
            self.playerWin()
        else:
            if self.partie.colonneJouable == []:
                self.gameStarted = False
                self.victoryScreen = UISprite(self.mainScreen, (0, 0), (1, 1), self.option["Ressources"]["Victoire"]["Tie"])
            else:
                self.timeFunc.addTimedFunction(self.SwitchPlayer, self.option["GameSettings"]["PlaceTime"], 1)


    def SwitchPlayer(self):
        # On change le joueur
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
        # On met à jour l'état du jeu
        self.arrow.switchTexture(SPGE.Utils.loadImage(self.option["Ressources"]["Arrow"][f"J{self.player}"]))
        self.partie.GameState = self.player


    def playerWin(self):
        self.gameStarted = False
        self.victoryScreen = UISprite(self.mainScreen, (0, 0), (1, 1), self.option["Ressources"]["Victoire"][f"J{self.player}"])


    def startGame(self):
        print("Fin de chargement")
        print("Lancement du jeu")
        self.gameStarted = True
        self.engine.startEngine(self.mainCam, self.mainEvent)


    def resetGame(self):
        print("Réinitialisation du jeu")
        for x in self.pions:
            x.destroy()
        self.pions = []
        self.partie = P4Game()
        self.gameStarted = True
        self.victoryScreen.destroy()


class SelectionArrow(Sprite):

    def __init__(self, screen, text):
        super().__init__(screen, (170, 15), (83, 59), text, False, "arrow")
        self.selectedColumn = 0
        self.listOfCoords = [(170, 15), (300, 15), (430, 15), (560, 15), (690, 15), (820, 15), (950, 15)]

    def switchColumn(self, sense):
        if sense == "right":
            if self.selectedColumn < 6:
                self.selectedColumn += 1
        elif sense == "left":
            if self.selectedColumn > 0:
                self.selectedColumn -= 1

        self.setCoords(self.listOfCoords[self.selectedColumn])


class P4Game():
    """
    Objet représentant une partie de Puissance 4.
    """
    def __init__(self):
        # Initialisation d'une partie
        self.plateau = [[0 for i in range(6)] for k in range(7)]  # Construction du plateau
        self.GameState = 1  # 0 : aucun joueur, 1 : J1, 2 : J2
        self.colonneJouable = [i for i in range(7)]


    def play(self, J, coup):
        # Jouer un coup dans la colonne `coup` pour le joueur J

        # On vérifie que le coup est valide
        if not(coup in self.colonneJouable):
            return False

        # Si le coup est valide, on le joue
        for i in range(6):
            if self.plateau[coup][i] != 0:
                self.plateau[coup][i-1] = J
                self.MajListCoupValable()
                return True

        self.plateau[coup][-1] = J
        self.MajListCoupValable()
        return True


    def MajListCoupValable(self):
        coup = []
        for col in range(7):
            if self.plateau[col][0] == 0:
                coup.append(col)
        self.colonneJouable = coup


    def VerifWin(self):
        # Vérifie si un joueur gagne avec le plateau actuel

        # Vérification horizontale
        for i in range(len(self.plateau[0])):
            for j in range(len(self.plateau) - 3):
                if self.plateau[j][i] == self.plateau[j+1][i] == self.plateau[j+2][i] == self.plateau[j+3][i] != 0:
                    return True

        # Vérification verticale
        for i in range(len(self.plateau[0]) - 3):
            for j in range(len(self.plateau)):
                if self.plateau[j][i] == self.plateau[j][i+1] == self.plateau[j][i+2] == self.plateau[j][i+3] != 0:
                    return True

        # Vérification diagonale (bas-droite)
        for i in range(len(self.plateau[0]) - 3):
            for j in range(len(self.plateau) - 3):
                if self.plateau[j][i] == self.plateau[j+1][i+1] == self.plateau[j+2][i+2] == self.plateau[j+3][i+3] != 0:
                    return True

        # Vérification diagonale (bas-gauche)
        for i in range(len(self.plateau[0]) - 3):
            for j in range(3, len(self.plateau)):
                if self.plateau[j][i] == self.plateau[j-1][i+1] == self.plateau[j-2][i+2] == self.plateau[j-3][i+3] != 0:
                    return True

        return False


game = Game()
game.startGame()