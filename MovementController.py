import pygame
import math

from Resources.TMatrix import TMatrix


class MovementController():
    def __init__(self, registry):
        self.transform = TMatrix()
        self.registry = registry

    def getMovementSet(self):
        transform = self.transform
        #print(pygame.mouse.get_rel())

        x, y = pygame.mouse.get_rel()
        

        #print(x, y * -1)

        #transform = TMatrix(
        #    1, 0, 0,
        #    0, 0, -1,
        #    0, 1, 0
        #) 
        oldTransform = self.transform
        self.transform = TMatrix()
        return(transform)

    def key_down(self, event):
        if event[pygame.K_SPACE]:
            self.transform *= TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0)
        if event[pygame.key.get_mods() & pygame.KMOD_SHIFT]:
            self.transform *= TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.1, 0)
        if event[pygame.K_w]:
            self.transform *= TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.1)
        if event[pygame.K_a]:
            self.transform *= TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0)
        if event[pygame.K_s]:
            self.transform *= TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1)
        if event[pygame.K_d]:
            self.transform *= TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, -0.1, 0, 0)
        if event[pygame.K_f]:
            TransformMatrix = TMatrix()
            TransformMatrix.matrix = [
                [1, 0, 0, 0],
                [0, math.cos(math.radians(10)), math.sin(math.radians(10)), 0],
                [0, -math.sin(math.radians(10)), math.cos(math.radians(10)), 0],
                [0, 0, 0, 1]
            ]

            self.transform *= TransformMatrix

    def on_move(self, x, y):
        x = self.registry.settings["MouseSpeed"]["Value"]

        TransformMatrix = TMatrix()
        TransformMatrix.matrix = [
            [1, 0, 0, 0],
            [0, math.cos(math.radians(x)), math.sin(math.radians(x)), 0],
            [0, -math.sin(math.radians(x)), math.cos(math.radians(x)), 0],
            [0, 0, 0, 1]
        ]

        self.transform *= TransformMatrix

    def on_click(self, x, y, button, pressed):
        print("Mouse clicked")

    def on_scroll(self, x, y, dx, dy):
        print("Scrolled")
