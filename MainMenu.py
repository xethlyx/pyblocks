import pygame

import Enum as CEnum

RED = (255, 0, 0)

class MainMenu():
    def __init__(self, registry):
        pass
        self.settingsClicked = False
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

        # Version Label
        self.font3 = pygame.font.Font('upheavtt.ttf', 33)
        self.registry.currentWindow.blit(self.font3.render('Version: 1.0.0', True, (255,255,255)), (1270, 750))

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
                    self.settingsClicked = True

                elif secondButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button 2 was pressed at {0}'.format(mouse_pos))
                    self.fade(1520, 800)
                    self.registry.GameScene = CEnum.GameScene.Render3D
                    self.settingsClicked = False

        if self.settingsClicked:
            self.surf = pygame.Surface((1520, 800), pygame.SRCALPHA)
            self.surf.fill((0, 0, 0, 150))
            self.backView = pygame.draw.rect(self.surf, [45, 52, 54, 150], [0, 0, 1520, 800])
            self.registry.currentWindow.blit(self.surf, (0,0))
            self.view = pygame.draw.rect(self.registry.currentWindow, [189, 195, 199], [90, 90, 1330, 620])

            # Close Button
            self.font4 = pygame.font.Font('upheavtt.ttf', 60)
            self.closeButton = self.registry.currentWindow.blit(self.font4.render('X', True, (45, 52, 54)), (1360, 100))

            # Settings Label
            self.font5 = pygame.font.Font('upheavtt.ttf', 100)
            self.settingsLabel = self.registry.currentWindow.blit(self.font5.render('Settings', True, (45, 52, 54)), (130, 100))

            # Switch
            self.img = pygame.image.load('Switch1.png')
            self.switch1 = self.registry.currentWindow.blit(self.img, (130,230))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position

                    # checks if mouse position is over the button
                    if self.closeButton.collidepoint(mouse_pos):
                        self.settingsClicked = False
                    
                    elif self.switch1.collidepoint(mouse_pos):
                        print("swithc")


    def render_first(self):
        pass
    
    def fade(self, width, height): 
        fade = pygame.Surface((width, height), pygame.SRCALPHA)
        fade.fill((0,0,0,5))
        for alpha in range(0, 300):
            fade.set_alpha(10)
            self.registry.currentWindow.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(5)
            

