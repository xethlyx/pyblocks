import pygame

RED = (255, 0, 0)

class MainMenu():
    def __init__(self, registry):
        pass
        self.registry = registry


    def render(self):

        self.registry.currentWindow.fill((0, 0, 0))
        back = pygame.image.load('test.png')
        back = pygame.transform.scale(back, (1520, 800))
        self.registry.currentWindow.blit(back, (0, 0))
        left = 50
        top = 655
        width = 360
        height = 100
        pygame.draw.rect(self.registry.currentWindow, [225, 112, 85], [left, top, width, height])

    def render_first(self):
        pass
