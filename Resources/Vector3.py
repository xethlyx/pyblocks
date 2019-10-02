import math


class Vector3:
    def __init__(self, x, y, z):
        self.type = "Vector3"

        if isinstance(x, (float, int)) and\
           isinstance(y, (float, int)) and\
           isinstance(z, (float, int)):
            self.x = x
            self.y = y
            self.z = z

            self.locked = True
        else:
            raise Exception("All types of Vector3 must be of int or float!")

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z
            )
        elif isinstance(other, (int, float)):
            raise Exception("Cannot add a number to a Vector3!")

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z
            )
        elif isinstance(other, (int, float)):
            raise Exception("Cannot add a number to a Vector3!")

    def __str__(self):
        return "x:{} y:{} z:{}".format(self.x, self.y, self.z)

    def magnitude(self):
        return math.sqrt(
            (self.x * self.x) +
            (self.y * self.y) +
            (self.z * self.z)
        )

    def distanceFrom(self, other):
        if isinstance(other, Vector3):
            return (self - other).magnitude()
        else:
            raise Exception(
                "Cannot get distance from variable other than Vector3!"
            )
