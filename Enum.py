from enum import Enum


class GameState(Enum):
    Active = 1
    Dead = 0


class UserInputType(Enum):
    Keyboard = "Keyboard"
    Mouse = "Mouse"
