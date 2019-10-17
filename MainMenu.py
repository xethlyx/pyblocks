import pygame

import Enum as CEnum
from debug import draw_debug

RED = (255, 0, 0)


class MainMenu():
    def __init__(self, registry):

        # Main Variables
        self.scene = CEnum.MainMenuScene.MainMenu
        self.registry = registry
        self.settingsClicked = False
        self.scrollPosition = 0

        self.generalSettings = True

        # First
        self.firstLoad = True
        self.firstSettings = False

    def draw_main_menu(self):
        draw_debug(self.registry)
        print("debug")
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

    def mouse_clicked(self, event):
        mouse_pos = event.pos  # gets mouse position

        if self.secondButton.collidepoint(mouse_pos):
            # prints current location of mouse
            print('button 2 was pressed at {0}'.format(mouse_pos))
            self.registry.GameScene = CEnum.GameScene.Render3D
            self.settingsClicked = False

        if self.firstButton.collidepoint(mouse_pos):
            # prints current location of mouse
            print('button 1 was pressed at {0}'.format(mouse_pos))
            self.settingsClicked = True

            self.surf = pygame.Surface((1520, 800), pygame.SRCALPHA)
            self.surf.fill((0, 0, 0, 150))
            self.backView = pygame.draw.rect(self.surf, [45, 52, 54, 150], [0, 0, 1520, 800])
            self.registry.currentWindow.blit(self.surf, (0, 0))

        if self.settingsClicked:

            if self.registry.settings["ShowFps"]["Value"]:
                self.switchImage1 = pygame.image.load('Switch1.png')
            else:
                self.switchImage1 = pygame.image.load('Switch0.png')

            if self.registry.settings["ShowVer"]["Value"]:
                self.switchImage2 = pygame.image.load('Switch1.png')
            else:
                self.switchImage2 = pygame.image.load('Switch0.png')

            if self.registry.settings["Sounds"]["Value"]:
                self.switchImage3 = pygame.image.load('Switch1.png')
            else:
                self.switchImage3 = pygame.image.load('Switch0.png')

            if self.registry.settings["DebugMode"]["Value"]:
                self.switchImage4 = pygame.image.load('Switch1.png')
            else:
                self.switchImage4 = pygame.image.load('Switch0.png')

            if self.registry.settings["CommandCon"]["Value"]:
                self.switchImage5 = pygame.image.load('Switch1.png')
            else:
                self.switchImage5 = pygame.image.load('Switch0.png')

            if not self.firstSettings:

                if self.generalSettings:
                    self.draw_general()

                else:
                    self.draw_render()

        try:
            if self.closeButton.collidepoint(mouse_pos):
                self.settingsClicked = False
                self.draw_main_menu()
                self.firstSettings = False

            if self.generalButton.collidepoint(mouse_pos):
                self.settingsClicked = True
                self.firstSettings = False
                self.generalSettings = True
                self.draw_general()

            if self.renderButton.collidepoint(mouse_pos):
                self.settingsClicked = True
                self.firstSettings = False
                self.generalSettings = False
                self.draw_render()

            if self.switch1.collidepoint(mouse_pos):
                self.registry.settings["ShowFps"]["Value"] = not self.registry.settings["ShowFps"]["Value"]
                if self.registry.settings["ShowFps"]["Value"]:
                    self.switchImage1 = pygame.image.load('Switch1.png')
                else:
                    self.switchImage1 = pygame.image.load('Switch0.png')
                self.switchImage1 = self.registry.currentWindow.blit(self.switchImage1, (130, 260))

            elif self.switch2.collidepoint(mouse_pos):
                self.registry.settings["ShowVer"]["Value"] = not self.registry.settings["ShowVer"]["Value"]
                if self.registry.settings["ShowVer"]["Value"]:
                    self.switchImage2 = pygame.image.load('Switch1.png')
                else:
                    self.switchImage2 = pygame.image.load('Switch0.png')
                self.switchImage2 = self.registry.currentWindow.blit(self.switchImage2, (130, 325))

            elif self.switch3.collidepoint(mouse_pos):
                self.registry.settings["Sounds"]["Value"] = not self.registry.settings["Sounds"]["Value"]
                if self.registry.settings["Sounds"]["Value"]:
                    self.switchImage3 = pygame.image.load('Switch1.png')
                else:
                    self.switchImage3 = pygame.image.load('Switch0.png')
                self.switchImage3 = self.registry.currentWindow.blit(self.switchImage3, (130, 455))
            
            elif self.switch4.collidepoint(mouse_pos):
                self.registry.settings["DebugMode"]["Value"] = not self.registry.settings["DebugMode"]["Value"]
                if self.registry.settings["DebugMode"]["Value"]:
                    self.switchImage4 = pygame.image.load('Switch1.png')
                else:
                    self.switchImage4 = pygame.image.load('Switch0.png')
                self.switchImage4 = self.registry.currentWindow.blit(self.switchImage4, (130, 455))
            
            elif self.switch5.collidepoint(mouse_pos):
                self.registry.settings["CommandCon"]["Value"] = not self.registry.settings["CommandCon"]["Value"]
                if self.registry.settings["CommandCon"]["Value"]:
                    self.switchImage5 = pygame.image.load('Switch1.png')
                else:
                    self.switchImage5 = pygame.image.load('Switch0.png')
                # self.switchImage5 = self.registry.currentWindow.blit(self.switchImage5, (130, 455))

            elif self.plusFps.collidepoint(mouse_pos):
                self.registry.settings["FpsLimit"]["Value"] += 10
                self.fpsRect = pygame.draw.rect(self.registry.currentWindow, [116, 125, 140], [110, 393, 115, 35])
                self.minusFps = self.registry.currentWindow.blit(self.font6.render("-", True, (255, 255, 255)), (120, 395))
                self.plusFps = self.registry.currentWindow.blit(self.font6.render("+", True, (255, 255, 255)), (200, 395))
                self.limitInt = self.registry.currentWindow.blit(self.font6.render(str(self.registry.settings["FpsLimit"]["Value"]), True, (255, 255, 255)), (152, 395))

                self.fps_color()

            elif self.minusFps.collidepoint(mouse_pos):
                if self.registry.settings["FpsLimit"]["Value"] > 10:
                    self.registry.settings["FpsLimit"]["Value"] -= 10
                    self.fpsRect = pygame.draw.rect(self.registry.currentWindow, [116, 125, 140], [110, 393, 115, 35])
                    self.minusFps = self.registry.currentWindow.blit(self.font6.render("-", True, (255, 255, 255)), (120, 395))
                    self.plusFps = self.registry.currentWindow.blit(self.font6.render("+", True, (255, 255, 255)), (200, 395))
                    self.limitInt = self.registry.currentWindow.blit(self.font6.render(str(self.registry.settings["FpsLimit"]["Value"]), True, (255, 255, 255)), (152, 395))

                self.fps_color()

        except AttributeError:
            print("[MAINMENU] fix your code")

    def render_first(self):
        pass

    def draw_general(self):
        # General Settings
        self.firstSettings = True
        self.view = pygame.draw.rect(self.registry.currentWindow, [189, 195, 199], [90, 90, 1330, 620])

        # Close Button
        self.font4 = pygame.font.Font('upheavtt.ttf', 60)
        self.closeButton = self.registry.currentWindow.blit(self.font4.render('X', True, (45, 52, 54)), (1360, 100))

        # Settings Label
        self.font5 = pygame.font.Font('upheavtt.ttf', 100)
        self.settingsLabel = self.registry.currentWindow.blit(self.font5.render('Settings', True, (45, 52, 54)), (130, 100))

        # General Button
        self.buttonFont = pygame.font.Font('upheavtt.ttf', 33)
        self.generalButton = self.registry.currentWindow.blit(self.buttonFont.render('General', True, (83, 82, 237)), (130, 190))

        # Advanced Button
        self.renderButton = self.registry.currentWindow.blit(self.buttonFont.render('Advanced', True, (45, 52, 54)), (430, 190))

        # FPS Counter
        self.font6 = pygame.font.Font('upheavtt.ttf', 30)
        self.fpsLabel = self.registry.currentWindow.blit(self.font6.render('Show FPS Counter', True, (45, 52, 54)), (230, 265))
        self.switch1 = self.registry.currentWindow.blit(self.switchImage1, (130, 260))

        # Show Version
        self.verLabel = self.registry.currentWindow.blit(self.font6.render(self.registry.settings["ShowVer"]["DisplayName"], True, (45, 52, 54)), (230, 330))
        self.switch2 = self.registry.currentWindow.blit(self.switchImage2, (130, 325))

        # FPS Limit
        self.limitLabel = self.registry.currentWindow.blit(self.font6.render(self.registry.settings["FpsLimit"]["DisplayName"], True, (45, 52, 54)), (240, 395))
        self.fpsRect = pygame.draw.rect(self.registry.currentWindow, [116, 125, 140], [110, 393, 115, 35])
        self.minusFps = self.registry.currentWindow.blit(self.font6.render("-", True, (255, 255, 255)), (120, 395))
        self.plusFps = self.registry.currentWindow.blit(self.font6.render("+", True, (255, 255, 255)), (200, 395))
        self.limitInt = self.registry.currentWindow.blit(self.font6.render(str(self.registry.settings["FpsLimit"]["Value"]), True, (255, 255, 255)), (152, 395))
        self.fps_color()

        # Sounds
        self.soundsLabel = self.registry.currentWindow.blit(self.font6.render(self.registry.settings["Sounds"]["DisplayName"], True, (45, 52, 54)), (230, 460))
        self.switch3 = self.registry.currentWindow.blit(self.switchImage3, (130, 455))

    def draw_render(self):
        # Render Settings
        self.firstSettings = True
        self.view = pygame.draw.rect(self.registry.currentWindow, [189, 195, 199], [90, 90, 1330, 620])

        # Close Button
        self.font4 = pygame.font.Font('upheavtt.ttf', 60)
        self.closeButton = self.registry.currentWindow.blit(self.font4.render('X', True, (45, 52, 54)), (1360, 100))

        # Settings Label
        self.font5 = pygame.font.Font('upheavtt.ttf', 100)
        self.settingsLabel = self.registry.currentWindow.blit(self.font5.render('Settings', True, (45, 52, 54)), (130, 100))

        # General Button
        self.buttonFont = pygame.font.Font('upheavtt.ttf', 33)
        self.generalButton = self.registry.currentWindow.blit(self.buttonFont.render('General', True, (45, 52, 54)), (130, 190))

        # Advanced Button
        self.renderButton = self.registry.currentWindow.blit(self.buttonFont.render('Advanced', True, (83, 82, 237)), (430, 190))

        # Debug Mode
        self.debugLabel = self.registry.currentWindow.blit(self.font6.render('Debug Mode', True, (45, 52, 54)), (230, 265))
        self.switch4 = self.registry.currentWindow.blit(self.switchImage4, (130, 260))

        # Command Console
        self.comLabel = self.registry.currentWindow.blit(self.font6.render(self.registry.settings["CommandCon"]["DisplayName"], True, (45, 52, 54)), (230, 330))
        self.switch5 = self.registry.currentWindow.blit(self.switchImage5, (130, 325))

    def fps_color(self):
        # If greater than 110fps, green, if under 30fps, red.
        if self.registry.settings["FpsLimit"]["Value"] <= 30:
            self.fpsRect = pygame.draw.rect(self.registry.currentWindow, [116, 125, 140], [110, 393, 115, 35])
            self.minusFps = self.registry.currentWindow.blit(self.font6.render("-", True, (255, 255, 255)), (120, 395))
            self.plusFps = self.registry.currentWindow.blit(self.font6.render("+", True, (255, 255, 255)), (200, 395))
            self.limitInt = self.registry.currentWindow.blit(self.font6.render(str(self.registry.settings["FpsLimit"]["Value"]), True, (255, 107, 129)), (152, 395))
        elif self.registry.settings["FpsLimit"]["Value"] >= 110:
            self.fpsRect = pygame.draw.rect(self.registry.currentWindow, [116, 125, 140], [110, 393, 115, 35])
            self.minusFps = self.registry.currentWindow.blit(self.font6.render("-", True, (255, 255, 255)), (120, 395))
            self.plusFps = self.registry.currentWindow.blit(self.font6.render("+", True, (255, 255, 255)), (200, 395))
            self.limitInt = self.registry.currentWindow.blit(self.font6.render(str(self.registry.settings["FpsLimit"]["Value"]), True, (29, 209, 161)), (152, 395))
