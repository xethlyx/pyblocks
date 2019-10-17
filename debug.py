import pygame
import Enum as CEnum


def draw_debug(registry):
    font4 = pygame.font.Font('upheavtt.ttf', 33)
    registry.currentWindow.blit(font4.render('Version', True, (255, 255, 255)), (10, 10))
    print("lll")
