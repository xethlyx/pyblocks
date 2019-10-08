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
        width = 380
        height = 100
        pygame.draw.rect(self.registry.currentWindow, [225, 112, 85], [left, top, width, height])
        self.font = pygame.font.Font('upheavtt.ttf', 45)
        self.font2 = pygame.font.Font('upheavtt.ttf', 120)
        self.registry.currentWindow.blit(self.font.render('Single Player', True, (255,255,255)), (68, 680))
        self.registry.currentWindow.blit(self.font2.render('PyBlocks', True, (255,255,255)), (60, 30))

    def render_first(self):
        pass
