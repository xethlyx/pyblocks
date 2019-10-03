import datetime

import pygame

import Enum as CEnum

from Render import Camera
from MovementController import MovementController

from Resources.Vector3 import Vector3
from Resources.RMatrix import RMatrix, identityRMatrix

blankRotation = RMatrix()
blankPosition = Vector3()

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pycraft")

currentCamera = Camera(90, Vector3(), identityRMatrix())
currentController = MovementController()

LastRun = datetime.datetime.now()
Run = CEnum.GameState.Active


while Run == CEnum.GameState.Active:
    # Debug Position + Rot
    print(pygame.mouse.get_rel())


    deltaTime = LastRun - datetime.datetime.now()
    LastRun = datetime.datetime.now()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = CEnum.GameState.Dead

    currentController.key_down(pygame.key.get_pressed())

    # Get User Input
    (changedPosition, changedRotation) = currentController.getMovementSet()

    if changedRotation != blankRotation:
        currentCamera.Rotation = currentCamera.Rotation * changedRotation

    if changedPosition != blankPosition:
        currentCamera.Position = currentCamera.Position + changedPosition

    # Draw the scene
    currentCamera.render3d()

    pygame.time.delay(50)
pygame.quit()
