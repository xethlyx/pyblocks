import pygame

RED = (255, 0, 0)

class MainMenu():
    def __init__(self, registry):
        pass
        self.registry = registry


    def render(self):
        
        back = pygame.image.load('test.png')
        self.registry.currentWindow.blit(back, (0, 0)) 

        red = 255
        blue = 0
        green = 0
        left = 50
        top = 50
        width = 90
        height = 90

        pygame.draw.rect(self.registry.currentWindow, [red, blue, green], [left, top, width, height])

    def render_first(self):
        pass
