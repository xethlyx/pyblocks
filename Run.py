import datetime

import pygame

import Enum as CEnum

from Render import Camera
from MovementController import MovementController

from Resources.Vector3 import Vector3
from Resources.RMatrix import RMatrix

blankRotation = RMatrix()
blankPosition = Vector3()

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pycraft")

currentCamera = Camera(90, Vector3(), RMatrix())
currentController = MovementController()

LastRun = datetime.now()
Run = CEnum.GameState.Active

while Run == CEnum.GameState.Active:
    deltaTime = LastRun - datetime.now()
    LastRun = datetime.now()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = CEnum.GameState.Dead
        elif event.type == pygame.KEYDOWN:
            currentController.key_down(event)

    # Get User Input
    (changedPosition, changedRotation) = currentController.getMovementSet()

    if changedRotation != blankRotation:
        currentCamera.Rotation = currentCamera.Rotation + changedRotation

    if changedPosition != blankPosition:
        currentCamera.Position = currentCamera.Position + changedPosition

    # Draw the scene
    currentCamera.render3d()

    pygame.time.delay(50)
pygame.quit()
