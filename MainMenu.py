import pygame

RED = (255, 0, 0)

class MainMenu():
    def __init__(self, registry):
        pass
        self.registry = registry

        red=255
        blue=0
        green=0
        left=50
        top=50
        width=90
        height=90

        pygame.draw.rect(window, [red, blue, green], [left, top, width, height])

    def render(self):
        pass
