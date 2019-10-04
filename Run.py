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

# Entities

from Entities.DefaultEntity import DefaultEntity

# Data Types

from Resources.Vector3 import Vector3
from Resources.RMatrix import RMatrix, identityRMatrix

# # # Main Code # # #

blankRotation = RMatrix()
blankPosition = Vector3()

pygame.init()

window = pygame.display.set_mode((1520, 800))
pygame.display.set_caption("Pycraft")

gameRegistry = Registry()

currentCamera = Camera(90, Vector3(), identityRMatrix())
currentController = MovementController()
currentMainMenu = MainMenu(gameRegistry)

LastRun = datetime.datetime.now()
Run = CEnum.GameState.Active

GameScene = CEnum.GameScene.MainMenu

# Debug

testEntity = DefaultEntity("test", gameRegistry)

while Run == CEnum.GameState.Active:
    deltaTime = LastRun - datetime.datetime.now()
    LastRun = datetime.datetime.now()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = CEnum.GameState.Dead

    if GameScene == CEnum.GameScene.MainMenu:
        currentMainMenu.render()
    elif GameScene == CEnum.GameScene.Render3D:
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
