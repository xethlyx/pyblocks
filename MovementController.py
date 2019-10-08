import pygame

from Resources.TMatrix import TMatrix
from Resources.FSize import FSize


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
        elif event[pygame.K_w]:
            print("up")
        elif event[pygame.K_a]:
            print("left")
        elif event[pygame.K_s]:
            print("down")
        elif event[pygame.K_d]:
            print("right")

    def on_move(self, x, y):
        print("Mouse moved")

    def on_click(self, x, y, button, pressed):
        print("Mouse clicked")

    def on_scroll(self, x, y, dx, dy):
        print("Scrolled")
