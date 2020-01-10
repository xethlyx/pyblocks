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
from Scene import Scene

# Data Types

from Resources.TMatrix import TMatrix

# Debug

from Blocks.Block import Block

# # # Main Code # # #

pygame.init()

window = pygame.display.set_mode((1520, 800))
pygame.display.set_caption("Pycraft")

# Set up registry

gameRegistry = Registry()

gameRegistry.currentCamera = Camera(90, TMatrix(), gameRegistry)
gameRegistry.currentController = MovementController(gameRegistry)
gameRegistry.currentMainMenu = MainMenu(gameRegistry)
gameRegistry.currentScene = Scene()

gameRegistry.currentWindow = window

gameRegistry.LastRun = datetime.datetime.now()
gameRegistry.Run = CEnum.GameState.Active

gameRegistry.GameScene = CEnum.GameScene.MainMenu

# Debug generate blocks

Block(TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0), gameRegistry.currentScene)
Block(TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1), gameRegistry.currentScene)
Block(TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), gameRegistry.currentScene)
Block(TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0), gameRegistry.currentScene)
Block(TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1), gameRegistry.currentScene)
Block(TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), gameRegistry.currentScene)

# # # Main Loop # # #

while gameRegistry.Run == CEnum.GameState.Active:
    deltaTime = gameRegistry.LastRun - datetime.datetime.now()
    LastRun = datetime.datetime.now()


    if gameRegistry.GameScene == CEnum.GameScene.MainMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRegistry.Run = CEnum.GameState.Dead
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameRegistry.currentMainMenu.mouse_clicked(event)
        gameRegistry.currentMainMenu.render()
    elif gameRegistry.GameScene == CEnum.GameScene.Render3D:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRegistry.Run = CEnum.GameState.Dead

        gameRegistry.currentCamera.transform *= TMatrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        
        # Get User Input
        gameRegistry.currentController.key_down(pygame.key.get_pressed())
        changedTransform = gameRegistry.currentController.getMovementSet()

        gameRegistry.currentCamera.transform *= changedTransform

        # Draw the scene
        gameRegistry.currentCamera.render3d()



        #pygame.time.delay(1)
    pygame.display.update()
pygame.quit()
