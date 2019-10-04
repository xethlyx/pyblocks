from enum import Enum


class GameState(Enum):
    Active = 1
    Dead = 0


class GameScene(Enum):
    MainMenu = "MainMenu"
    Render3D = "Render3D"
    RenderPaused = "RenderPaused"


class UserInputType(Enum):
    Keyboard = "Keyboard"
    Mouse = "Mouse"
