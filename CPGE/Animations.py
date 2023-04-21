# coding : UTF-8

from CPGE import *


class AnimationManager:

    def __init__(self) -> None:
        self.AnimStack = []

    def playAnimations(self):
        for anim in self.AnimStack:
            ended = anim.nextFrame()
            if ended:
                self.AnimStack.pop(self.AnimStack.index(anim))

    def AddAnimationToPlay(self, anim: Animation):
        self.AnimStack.append(anim)




class Animation:
    def __init__(self, name: str, listOfanimationImages: list, frequenceOfAnimation: int) -> None:

        self.name = name
        self.frequenceOfAnimation = frequenceOfAnimation
        self.listOfanimationImages = listOfanimationImages
        self.frameCounter = 0
        self.animpointer = 0

    def setSprite(self, sprite):
        self.sprite = sprite

    def nextFrame(self):
        self.frameCounter += 1
        if self.frameCounter == self.frequenceOfAnimation:
            self.sprite.switchTexture(self.listOfanimationImages[self.animpointer])
            self.animpointer += 1
            self.frameCounter = 0
            if self.animpointer == len(self.listOfanimationImages):
                self.animpointer = 0
                return True

        return False

ANIMATION_MANAGER = AnimationManager()