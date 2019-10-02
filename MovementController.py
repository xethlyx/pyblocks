import pygame

from Resources.RMatrix import RMatrix
from Resources.Vector3 import Vector3


class MovementController():
    def __init__(self):
        self.vector = Vector3()
        self.rotation = RMatrix()

    def getMovementSet(self):
        vector = self.vector
        rotation = self.rotation

        self.vector = Vector3()
        self.rotation = RMatrix()

        return(vector, rotation)

    def key_down(self, event):
        if event[pygame.K_SPACE]:
            print("space")

        if event[pygame.K_w]:
            print("up")
        
        if event[pygame.K_a]:
            print("left")

        if event[pygame.K_s]:
            print("down")
        
        if event[pygame.K_d]:
            print("right")
