from Resources.RMatrix import RMatrix
from Resources.Vector3 import Vector3


class MovementController():
    def __init__(self):
        self.vector = Vector3()
        self.rotation = RMatrix()

    def getMovementSet(self):
        vector = self.vector
        rotation = self.rotation

        self.vector = Vector3()
        self.rotation = RMatrix()

        return(vector, rotation)
