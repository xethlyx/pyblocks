"""The main class for the game"""

# # # Imports # # #

# System

import datetime

# Dependancies

import pygame

# Util

import Enum as CEnum

# Management

from Render import Camera
from MainMenu import MainMenu
from MovementController import MovementController
from Registry import Registry

# Data Types

from Resources.Vector3 import Vector3
from Resources.RMatrix import RMatrix, identityRMatrix

# # # Main Code # # #

blankRotation = RMatrix()
blankPosition = Vector3()

pygame.init()

window = pygame.display.set_mode((1520, 800))
pygame.display.set_caption("Pycraft")

# Set up registry

gameRegistry = Registry()

gameRegistry.currentCamera = Camera(90, Vector3(), identityRMatrix())
gameRegistry.currentController = MovementController()
gameRegistry.currentMainMenu = MainMenu(gameRegistry)

gameRegistry.currentWindow = window

gameRegistry.LastRun = datetime.datetime.now()
gameRegistry.Run = CEnum.GameState.Active

gameRegistry.GameScene = CEnum.GameScene.MainMenu

# # # Main Loop # # #

while gameRegistry.Run == CEnum.GameState.Active:
    deltaTime = gameRegistry.LastRun - datetime.datetime.now()
    LastRun = datetime.datetime.now()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = CEnum.GameState.Dead

    if gameRegistry.GameScene == CEnum.GameScene.MainMenu:
        gameRegistry.currentMainMenu.render()
    elif gameRegistry.GameScene == CEnum.GameScene.Render3D:
        gameRegistry.currentController.key_down(pygame.key.get_pressed())

        # Get User Input
        (changedPosition, changedRotation) = gameRegistry.currentController.getMovementSet()

        if changedRotation != blankRotation:
            gameRegistry.currentCamera.Rotation = gameRegistry.currentCamera.Rotation * changedRotation

        if changedPosition != blankPosition:
            gameRegistry.currentCamera.Position = gameRegistry.currentCamera.Position + changedPosition

        # Draw the scene
        gameRegistry.currentCamera.render3d()

        pygame.time.delay(50)
pygame.quit()
