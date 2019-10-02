from Resources.Matrix3 import Matrix3


class RMatrix():
    def __init__(self, x1=0, x2=0, x3=0, y1=0, y2=0, y3=0, z1=0, z2=0, z3=0):
        self.x = Matrix3(x1, x2, x3)
        self.y = Matrix3(y1, y2, y3)
        self.z = Matrix3(z1, z2, z3)

    def __str__(self):
        return("x({}) y({}) z({})".format(self.x, self.y, self.z))

    def __mul__(self, other):
        # TODO: proper mult
        return(self)
