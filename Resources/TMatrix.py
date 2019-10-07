from Resources.Matrix4 import Matrix4


class TMatrix:
    def __init__(self, x1=0, x2=0, x3=0, y1=0, y2=0, y3=0, z1=0, z2=0, z3=0, xp=0, yp=0, zp=0):
        self.x = Matrix4(1, x1, x2, x3)
        self.y = Matrix4(y1, 1, y2, y3)
        self.z = Matrix4(z1, z2, 1, z3)
        self.p = Matrix4(xp, yp, zp, 1)

    def __str__(self):
        return("x({}) y({}) z({}) p({})".format(self.x, self.y, self.z, self.p))

    def __mul__(self, other):
        return TMatrix(
            (self.x.one * other.x.two +
             self.x.two * other.y.two +
             self.x.three * other.z.two +
             self.x.four * other.p.two), (self.x.one * other.x.three +
                                          self.x.two * other.y.three +
                                          self.x.three * other.z.three +
                                          self.x.four * other.p.three), (self.x.one * other.x.four +
                                                                         self.x.two * other.y.four +
                                                                         self.x.three * other.z.four +
                                                                         self.x.four * other.p.four),
            (self.y.one * other.x.one +
             self.y.two * other.y.one +
             self.y.three * other.z.one +
             self.y.four * other.p.one), (self.y.one * other.x.three +
                                          self.y.two * other.y.three +
                                          self.y.three * other.z.three +
                                          self.y.four * other.p.three), (self.y.one * other.x.four +
                                                                         self.y.two * other.y.four +
                                                                         self.y.three * other.z.four +
                                                                         self.y.four * other.p.four),
            (self.z.one * other.x.one +
             self.z.two * other.y.one +
             self.z.three * other.z.one +
             self.z.four * other.p.one), (self.z.one * other.x.two +
                                          self.z.two * other.y.two +
                                          self.z.three * other.z.two +
                                          self.z.four * other.p.two), (self.z.one * other.x.four +
                                                                       self.z.two * other.y.four +
                                                                       self.z.three * other.z.four +
                                                                       self.z.four * other.p.four),
            (self.p.one * other.x.one +
             self.p.two * other.y.one +
             self.p.three * other.z.one +
             self.p.four * other.p.one), (self.p.one * other.x.two +
                                          self.p.two * other.y.two +
                                          self.p.three * other.z.two +
                                          self.p.four * other.p.two), (self.p.one * other.x.three +
                                                                       self.p.two * other.y.three +
                                                                       self.p.three * other.z.three +
                                                                       self.p.four * other.p.three),
        )

    def __eq__(self, other):
        if not isinstance(other, TMatrix):
            return NotImplemented

        return(str(self) == str(other))
