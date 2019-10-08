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
        
        # Title
        self.font2 = pygame.font.Font('upheavtt.ttf', 120)
        self.registry.currentWindow.blit(self.font2.render('PyBlocks', True, (255,255,255)), (60, 30))

        # First Button
        self.font = pygame.font.Font('upheavtt.ttf', 45)
        firstButton = pygame.draw.rect(self.registry.currentWindow, [225, 112, 85], [left, top, width, height])
        self.registry.currentWindow.blit(self.font.render('SETTINGS', True, (255,255,255)), (130, 680))

        # Second Button
        secondButton = pygame.draw.rect(self.registry.currentWindow, [225, 112, 85], [50, 543, 380, 100])
        self.registry.currentWindow.blit(self.font.render('Single Player', True, (255,255,255)), (68, 568))

        # Button Pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if firstButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button 1 was pressed at {0}'.format(mouse_pos))
                
                if secondButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button 2 was pressed at {0}'.format(mouse_pos))

        # Version Label
        self.font3 = pygame.font.Font('upheavtt.ttf', 33)
        self.registry.currentWindow.blit(self.font3.render('Version: 1.0.0', True, (255,255,255)), (1270, 750))

    def render_first(self):
        pass
