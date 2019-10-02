import pygame

import Enum as CEnum

from Render import Camera
from Vector3 import Vector3

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pycraft")

currentCamera = Camera(90, Vector3(0, 0, 0))

Run = CEnum.GameState.Active

while Run == CEnum.GameState.Active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = CEnum.GameState.Dead

    pygame.time.delay(50)
pygame.quit()
