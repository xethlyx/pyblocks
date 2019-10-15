import pygame

import Enum as CEnum

RED = (255, 0, 0)


class MainMenu():
    def __init__(self, registry):

        # Main Variables
        self.scene = CEnum.MainMenuScene.MainMenu
        self.registry = registry
        self.settingsClicked = False
        self.switchImage = pygame.image.load('Switch1.png')
        self.scrollPosition = 0

        # First
        self.firstLoad = True
        self.firstSettings = False

    def draw_main_menu(self):
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
        self.registry.currentWindow.blit(self.font2.render('PyBlocks', True, (255, 255, 255)), (60, 30))

        # Version Label
        self.font3 = pygame.font.Font('upheavtt.ttf', 33)
        self.registry.currentWindow.blit(self.font3.render('Version: 1.0.0', True, (255, 255, 255)), (1270, 750))

        # First Button
        self.font = pygame.font.Font('upheavtt.ttf', 45)
        self.firstButton = pygame.draw.rect(self.registry.currentWindow, [225, 112, 85], [left, top, width, height])
        self.registry.currentWindow.blit(self.font.render('SETTINGS', True, (255, 255, 255)), (130, 680))

        # Second Button
        self.secondButton = pygame.draw.rect(self.registry.currentWindow, [225, 112, 85], [50, 543, 380, 100])
        self.registry.currentWindow.blit(self.font.render('Single Player', True, (255, 255, 255)), (68, 568))

    def render(self):
        if self.firstLoad:
            self.firstLoad = False
            self.draw_main_menu()

            if self.registry.settings["ShowFps"]["Value"]:
                self.img = pygame.image.load('Switch1.png')
            else:
                self.img = pygame.image.load('Switch0.png')


    def mouse_clicked(self, event):
        mouse_pos = event.pos  # gets mouse position
        
        if self.secondButton.collidepoint(mouse_pos) and self.settingsClicked == False:
            # prints current location of mouse
            print('button 2 was pressed at {0}'.format(mouse_pos))
            self.fade(1520, 800)
            self.registry.GameScene = CEnum.GameScene.Render3D
            self.settingsClicked = False
            
        if self.firstButton.collidepoint(mouse_pos):
            # prints current location of mouse
            print('button 1 was pressed at {0}'.format(mouse_pos))
            self.settingsClicked = True

        elif self.closeButton.collidepoint(mouse_pos):
            self.settingsClicked = False
            self.draw_main_menu()
            self.firstSettings = False

        if self.settingsClicked:

            if not self.firstSettings:
                self.firstSettings = True
                self.surf = pygame.Surface((1520, 800), pygame.SRCALPHA)
                self.surf.fill((0, 0, 0, 150))
                self.backView = pygame.draw.rect(self.surf, [45, 52, 54, 150], [0, 0, 1520, 800])
                self.registry.currentWindow.blit(self.surf, (0, 0))
                self.view = pygame.draw.rect(self.registry.currentWindow, [189, 195, 199], [90, 90, 1330, 620])

                # Close Button
                self.font4 = pygame.font.Font('upheavtt.ttf', 60)
                self.closeButton = self.registry.currentWindow.blit(self.font4.render('X', True, (45, 52, 54)), (1360, 100))

                # Settings Label
                self.font5 = pygame.font.Font('upheavtt.ttf', 100)
                self.settingsLabel = self.registry.currentWindow.blit(self.font5.render('Settings', True, (45, 52, 54)), (130, 100))

                # FPS Counter
                self.font6 = pygame.font.Font('upheavtt.ttf', 30)
                self.fpsLabel = self.registry.currentWindow.blit(self.font6.render('Show FPS Counter', True, (45, 52, 54)), (230, 265))
                self.switch1 = self.registry.currentWindow.blit(self.img, (130, 260))

        elif self.switch1.collidepoint(mouse_pos):
            self.registry.settings["ShowFps"]["Value"] = not self.registry.settings["ShowFps"]["Value"]
            if self.registry.settings["ShowFps"]["Value"]:
                self.img = pygame.image.load('Switch1.png')
            else:
                self.img = pygame.image.load('Switch0.png')
            self.switch1 = self.registry.currentWindow.blit(self.img, (130, 260))
            print('sho')

    def render_first(self):
        pass

    def fade(self, width, height):
        fade = pygame.Surface((width, height), pygame.SRCALPHA)
        fade.fill((0, 0, 0, 100))
        for alpha in range(0, 300):
            fade.set_alpha(10)
            self.registry.currentWindow.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)
