#coding: utf-8

from SPGE import *
from SPGE.Animations import ANIMATION_MANAGER


class Sprite():

    def __init__(self, screen : Screen, coords : tuple, dimension : tuple, texture: str, isCollidable : bool = False, tag = None ):
        """Sprite init

        Args:
            screen (Screen): Screen sur lequelle sera appliquer le sprite
            coords (tuple): coordone (x,y) a
            dimension (tuple): taille du sprite (w,h)
            texture (str): chemin vers le fichier de texture
            isCollidable (bool, optional): Defini si le Sprite peu interagir avec les colisions. Defaults to False.
        """
        
        self.screen = screen
        self.coords = coords
        self.dimension = dimension
        self.coordsToRender = coords
        self.idbox = pygame.Rect(coords,dimension)

        self.name=texture
        self.texture = SPGE.Utils.loadImage(texture)
        self.dictOfAnimations={}

        self.isCollidable=isCollidable
        
        self.tag = tag
        self.active= True

        self.screen.addSprite(self)


    def __str__(self) -> str:
        return f"{self.name} at {self.coords} "

    def destroy(self):
        #suprime le sprite
        self.active = False
        self.screen.sprites.pop(self.screen.sprites.index(self))
        if self.isCollidable:
            self.screen.collidableSprites.pop(self.screen.collidableSprites.index(self))



    def IsColliding(self, sprite : Sprite) -> bool:
        #verifie si 2 sprite sont en collision
        return self.idbox.colliderect(sprite.idbox)

    def IsTouching(self, sprite : Sprite) -> bool:
        #verifie si 2 sprites se touchent à 1 pixel près
        return pygame.Rect(self.coords,(self.dimension[0]+1,self.dimension[1]+1)).colliderect(sprite.idbox)


    def switchTexture(self,newTextures):
        self.texture=newTextures
    
    
    #deplacement sprite
    def setCoords(self, newCords: tuple):#change les coordonne du sprite 
        self.coords=newCords


    def setCoordsToRender(self, newCoords : tuple):
        self.coordsToRender=newCoords


    def move(self, vector : tuple) -> bool:#deplace le sprtite a paryir d' un vecteur (x,y) 

        if self.isCollidable:
            savedCorrds=self.coords
            self.coords=(self.coords[0]+vector[0],self.coords[1]+vector[1])
            self.idbox = pygame.Rect(self.coords,self.dimension)
            if self.screen.verifColisions(self):
                self.coords = savedCorrds
                self.idbox = pygame.Rect(savedCorrds,self.dimension)
                return False
            else:
                return True
        else:
            self.coords=(self.coords[0]+vector[0],self.coords[1]+vector[1])
            self.idbox = pygame.Rect(self.coords,self.dimension)


    #gestions animations
    
    def AddAnimation(self,anim : Animation):
        anim.setSprite(self)
        self.dictOfAnimations[anim.name] = anim
        
        
    
    def playAnim(self,animeName):
        ANIMATION_MANAGER.AddAnimationToPlay(self.dictOfAnimations[animeName])



class PSprite(Sprite):
    def __init__(self, screen: Screen, coords: tuple, dimension: tuple, texture: str, isCollidable: bool = True, tag = None):
        super().__init__(screen, coords, dimension, texture, isCollidable,tag)
        self.forces=[]#ensemble des forces s'applisaunt àl'objet
        self.v=(0,0)#vitesse de l'objet
        self.maxV = None # vitesse max de l'objet
        self.masse = 10 #masse de l'objet
        self.screen.PSprites.append(self)


    def destroy(self):
        #suprime le sprite
        if self.active == True:
            self.active = False
            self.screen.sprites.pop(self.screen.sprites.index(self))
            self.screen.PSprites.pop(self.screen.PSprites.index(self))
            if self.isCollidable:
                self.screen.collidableSprites.pop(self.screen.collidableSprites.index(self))
        else:
            print("tentative de suppression d'un sprite déja supprimé")

    def addNewForce(self,vector, duration):
        self.forces.append([vector, duration,0])

    def __calculeNewSpeed(self):
        x, y = 0 , 0
        #Somme des forces    
        for force in self.forces:
            x += force[0][0]
            y += force[0][1]
            if force[1] != -1:
                if force[2] >= force[1]:
                    self.forces.remove(force)
                else:
                    force[2]+=1
        # division par la masse

        dx= x / self.masse
        dy = y / self.masse

        nv = [self.v[0]+dx,self.v[1]+dy]

        #verification de la validité de la vitesse
        if self.maxV != None :
            if abs(nv[0]) > self.maxV[0]:
                if nv[0] > 0 :
                    nv[0] = self.maxV[0]
                else:
                    nv[0] = -self.maxV[0]

            if abs(nv[1]) > self.maxV[1]:
                if nv[1] > 0 :
                    nv[1] = self.maxV[1]
                else:
                    nv[1] = -self.maxV[1]

        return nv

    def applyForces(self) -> list :
        #on calcule la nouvelle vitesse
        self.v = self.__calculeNewSpeed()
        #mise à jour des données
        savedCorrds=self.coords
        self.coords=(self.coords[0]+self.v[0],self.coords[1]+self.v[1])
        self.idbox = pygame.Rect(self.coords,self.dimension)
        
        #Vérification des collisions
        if self.isCollidable == True:
            if self.screen.verifColisions(self):
                reportVariable = [False, False] # 0 : colision horizontal , 1 colision vertical
                tempv= [0,0]
                #on verifie si la colision est horizontal
                self.idbox = pygame.Rect((self.coords[0],savedCorrds[1]),self.dimension)
                collision = self.screen.verifColisions(self)

                if collision != False:
                    self.v[0]=0
                    #on calcule la nouvelle vitesse en fonction de la collision
                    if  self.coords[0] < collision.coords[0] : #colision par la gauche
                        nx = collision.coords[0] - self.dimension[0]

                    elif self.coords[0] > collision.coords[0] : #collion sur la droite
                        nx= collision.coords[0] + collision.dimension[0]

                    elif self.coords[0] == collision.coords[0]:
                        nx = 0

                    reportVariable[0] = True


                elif collision == False:
                    nx = savedCorrds[0] + self.v[0]


                #on verifie si elle est vertical
                self.idbox = pygame.Rect((savedCorrds[0],self.coords[1]),self.dimension)
                collision = self.screen.verifColisions(self)
                if collision != False:
                    self.v[1]=0

                    if  self.coords[1] < collision.coords[1] : #colision par le haut
                        ny = collision.coords[1] - self.dimension[1]

                    elif self.coords[1] > collision.coords[1] : #collion par le bas
                        ny = collision.coords[1] + collision.dimension[1]

                    elif self.coords[1] == collision.coords[1]:
                        ny = savedCorrds[1]
                    reportVariable[1] = True


                elif collision == False:
                    ny = savedCorrds[1] + self.v[1]
                # nouvelle cordonne valide    
                self.coords=(nx,ny)
                self.idbox = pygame.Rect(self.coords,self.dimension)

                return reportVariable
        
        return True # si aucune colision

    


class UISprite(Sprite):
    
    def __init__(self, UIscreen : Screen, coords: tuple, dimension: tuple, texture: str):
        super().__init__(UIscreen, coords, dimension, texture,  False)
        

