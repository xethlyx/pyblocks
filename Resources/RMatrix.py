# flake8: noqa: E501

from Resources.Matrix3 import Matrix3

class RMatrix():
    def __init__(self, x1=0, x2=0, x3=0, y1=0, y2=0, y3=0, z1=0, z2=0, z3=0):
        self.x = Matrix3(x1, x2, x3)
        self.y = Matrix3(y1, y2, y3)
        self.z = Matrix3(z1, z2, z3)

    def __str__(self):
        return("x({}) y({}) z({})".format(self.x, self.y, self.z))

    def __mul__(self, other):
        return RMatrix(
            (self.x.one * other.x.one +
             self.x.two * other.y.one +
             self.x.three * other.z.one), (self.x.one * other.x.two +
                                           self.x.two * other.y.two +
                                           self.x.three * other.z.two), (self.x.one * other.x.three +
                                                                         self.x.two * other.y.three +
                                                                         self.x.three * other.z.three),
            (self.y.one * other.x.one +
             self.y.two * other.y.one +
             self.y.three * other.z.one), (self.y.one * other.x.two +
                                           self.y.two * other.y.two +
                                           self.y.three * other.z.two), (self.y.one * other.x.three +
                                                                         self.y.two * other.y.three +
                                                                         self.y.three * other.z.three),
            (self.z.one * other.x.one +
             self.z.two * other.y.one +
             self.z.three * other.z.one), (self.z.one * other.x.two +
                                           self.z.two * other.y.two +
                                           self.z.three * other.z.two), (self.z.one * other.x.three +
                                                                         self.z.two * other.y.three +
                                                                         self.z.three * other.z.three),
        )

def identityRMatrix():
    return(RMatrix(
        1, 0, 0,
        0, 1, 0,
        0, 0, 1
    ))
