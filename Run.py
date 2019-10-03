import datetime
import threading

import pygame

import Enum as CEnum

from pynput.mouse import Listener
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

LastRun = datetime.datetime.now()
Run = CEnum.GameState.Active

# Move listener into another thread


def joinListener():
    with Listener(
                  on_move=currentController.on_move,
                  on_click=currentController.on_click,
                  on_scroll=currentController.on_scroll
                 ) as listener:
        listener.join()


mouseListenerThread = threading.Thread(target=joinListener, args=())
mouseListenerThread.start()


while Run == CEnum.GameState.Active:
    # Debug Position + Rot
    print("ttt")

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
