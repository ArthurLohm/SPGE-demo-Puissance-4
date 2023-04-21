#coding: utf-8

class TimedFunctionManager:
    
    def __init__(self) -> None:
        
        self.listOfTimedFunctions=[]

        
    def addTimedFunction(self, function, frequence : int  = 1):
        """ ajoute une fonction se declanchant a intervalle regulier

        Args:
            function (function): fonction qui est declencher 
            frequence (int, optional): frequnce en frame a laquelle la fonction es declenche
            . Defaults to 1.
        """
        tempsRestant=frequence
        self.listOfTimedFunctions.append([function, frequence, tempsRestant])  
        
        
    #methode relative aus declencjhment des fonctions
    def callTimedFunctions(self):
        """"Appelle les fonctions si elle le doivent
        rapelle : self.listOfTimedFunction=[function, frequence, tempsRestant]
        """
        for timedFunction in self.listOfTimedFunctions:
            #on met a jour le temps restant
            timedFunction[2] -= 1
            #on verifie si la fonction doit etre appelle
            if timedFunction[2] == 0:
                #on apelle la fonction et on renitialise le temps restant
                timedFunction[0]()
                timedFunction[2] = timedFunction[1]

