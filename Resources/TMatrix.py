import math

from Resources.Matrix4 import Matrix4


class TMatrix:
    def __init__(self, x1=0, x2=0, x3=0, y1=0, y2=0, y3=0, z1=0, z2=0, z3=0, xp=0, yp=0, zp=0):
        """Crete a new TMatrx with an automatically embedded identity matrix.

        Keyword Arguments:
            x1 (int) -- Rotation x: 1 (default: 0)
            x2 (int) -- Rotation x: 2 (default: 0)
            x3 (int) -- Rotation x: 3 (default: 0)
            y1 (int) -- Rotation y: 1 (default: 0)
            y2 (int) -- Rotation y: 2 (default: 0)
            y3 (int) -- Rotation y: 3 (default: 0)
            z1 (int) -- Rotation z: 1 (default: 0)
            z2 (int) -- Rotation z: 2 (default: 0)
            z3 (int) -- Rotation z: 3 (default: 0)
            xp (int) -- Vector3 Position: x (default: 0)
            yp (int) -- Vector3 Position: y (default: 0)
            zp (int) -- Vector3 Position: z (default: 0)
        """
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

    def __neg__(self):
        return TMatrix(
            -self.x.two, -self.x.three, -self.x.four,
            -self.y.one, -self.y.three, -self.y.four,
            -self.z.one, -self.z.two, -self.z.four,
            -self.p.one, -self.p.two, -self.p.three
        )

    def __add__(self, other):
        if not isinstance(other, TMatrix):
            return NotImplemented

        return TMatrix(
            self.x.two, self.x.three, self.x.four,
            self.y.one, self.y.three, self.y.four,
            self.z.one, self.z.two, self.z.four,
            self.p.one + other.p.one, self.p.two + other.p.two, self.p.three + other.p.three
        )

    def __sub__(self, other):
        return self + (-other)

    def get_magnitude(self):
        """Gets the magnitude of the embedded vector.

        Returns:
            int -- The magnitude of the embedded vector.
        """
        return math.sqrt((self.p.one ** 2) + (self.p.two ** 2) + (self.p.three ** 2))
