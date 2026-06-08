#coding: utf-8

class TimedFunctionManager:
    
    def __init__(self) -> None:
        
        self.listOfTimedFunctions=[]

        
    def addTimedFunction(self, function, frequence : int  = 1,nbIteration = -1):
        """ ajoute une fonction se declanchant a intervalle regulier

        Args:
            function (function): fonction qui est declencher 
            frequence (int, optional): frequnce en frame a laquelle la fonction es declenche
            . Defaults to 1.
        """
        tempsRestant=frequence
        self.listOfTimedFunctions.append([function, frequence, tempsRestant,nbIteration])  
        
        
    #methode relative aus declencjhment des fonctions
    def callTimedFunctions(self):
        """"Appelle les fonctions si elle le doivent
        rapelle : self.listOfTimedFunction=[function, frequence, tempsRestant]
        """
        for i in range(len(self.listOfTimedFunctions)):
            #on met a jour le temps restant
            self.listOfTimedFunctions[i][2] -= 1
            #on verifie si la fonction doit etre appelle
            if self.listOfTimedFunctions[i][2] == 0:
                #on apelle la fonction et on renitialise le temps restant
                self.listOfTimedFunctions[i][0]()
                if self.listOfTimedFunctions[i][3] == -1:
                    self.listOfTimedFunctions[i][2] = self.listOfTimedFunctions[i][1]
                else :
                    self.listOfTimedFunctions[i][3] -=1
                    if self.listOfTimedFunctions[i][3] == 0:
                        self.listOfTimedFunctions.pop(i)
                    else:
                        self.listOfTimedFunctions[i][2] = self.listOfTimedFunctions[i][1]



