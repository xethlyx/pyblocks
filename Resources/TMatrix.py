import math


matrixAlias = {
    "x0": [1, 0],
    "x1": [2, 0],
    "x2": [3, 0],
    "y0": [0, 1],
    "y1": [2, 1],
    "y2": [3, 1],
    "z0": [0, 2],
    "z1": [1, 2],
    "z2": [3, 2],
    "xp": [0, 3],
    "yp": [1, 3],
    "zp": [2, 3]
}


class TMatrix:
    def __init__(self, x0=0, y0=0, z0=0, y1=0, x1=0, z1=0, x2=0, y2=0, z2=0, xp=0, yp=0, zp=0, scale=1):
        self.matrix = [
            [scale, y0, z0, xp],
            [x0, scale, z1, yp],
            [x1, y1, scale, zp],
            [x2, y2, z2, scale]
        ]

    def __mul__(self, other):
        # Key:
        #   self.matrix[row, #] * other.matrix(#, column)

        if not isinstance(other, TMatrix):
            if isinstance(other, (int, float)):
                print("operation is with scalar")
                newMatrix = TMatrix()

                newMatrix.matrix = self.matrix

                for rowNumber in range(len(newMatrix.matrix)):
                    for columnNumber in range(len(newMatrix.matrix[rowNumber])):
                        newMatrix.matrix[rowNumber][columnNumber] = newMatrix.matrix[rowNumber][columnNumber] * other

                return newMatrix
            return NotImplemented

        newMatrix = TMatrix()

        for rowNumber in range(len(newMatrix.matrix)):
            for columnNumber in range(len(newMatrix.matrix[rowNumber])):
                finalValue = 0

                for loopValue in range(len(newMatrix.matrix[rowNumber])):
                    finalValue = finalValue + (self.matrix[rowNumber][loopValue] * other.matrix[loopValue][columnNumber])

                newMatrix.matrix[rowNumber][columnNumber] = finalValue

        return newMatrix

    def set_scale(self, scale):
        self.matrix[0][0] = scale
        self.matrix[1][1] = scale
        self.matrix[2][2] = scale
        self.matrix[3][3] = scale

    def get_value(self, valueName):
        return self.matrix[matrixAlias[valueName][0]][matrixAlias[valueName][1]]

    def __str__(self):
        finalAppend = "TMatrix("

        for rowNumber in range(len(self.matrix)):
            rowAppend = "    "
            for columnNumber in range(len(self.matrix[rowNumber])):
                rowAppend = rowAppend + str(self.matrix[rowNumber][columnNumber])
                if columnNumber < (len(self.matrix[rowNumber]) - 1):
                    rowAppend = rowAppend + ", "

            if rowNumber < (len(self.matrix[rowNumber]) - 1):
                rowAppend = rowAppend + ", "

            finalAppend = finalAppend + "\n" + rowAppend

        finalAppend = finalAppend + "\n)"

        return finalAppend

    def __eq__(self, other):
        if not isinstance(other, TMatrix):
            return NotImplemented

        return(str(self) == str(other))

    def set_value(self, valueName, newValue):
        self.matrix[matrixAlias[valueName][0]][matrixAlias[valueName][1]] = newValue

    def lerp(self, other, amount):
        newMatrix = TMatrix()

        def floatLerp(first, second, amount):
            return first * (1-amount) + (second*amount)

        for rowNumber in range(len(self.matrix)):
            for columnNumber in range(len(self.matrix[rowNumber])):  # Increases quicker
                newMatrix.matrix[rowNumber][columnNumber] = floatLerp(self.matrix[rowNumber][columnNumber],
                                                                      other.matrix[rowNumber][columnNumber],
                                                                      amount)

        return newMatrix

    def distance_from(self, other):
        return(math.sqrt(
            (self.get_value("xp") - other.get_value("xp"))**2 +
            (self.get_value("yp") - other.get_value("yp"))**2 +
            (self.get_value("zp") - other.get_value("zp"))**2
        ))

    # Not my code below this line, taken from https://stackoverflow.com/a/39881366

    def transpose_matrix(self, matrix=None):
        dMatrix = matrix or self.matrix
        print(dMatrix)
        return map(list, zip(*dMatrix))

    def get_matrix_minor(self, i, j, matrix=None):
        loopingMatrix = matrix or self.matrix
        return [row[:j] + row[j+1:] for row in (loopingMatrix[:i] + loopingMatrix[i+1:])]

    def get_matrix_determinant(self, matrix=None):
        dMatrix = matrix or self.matrix
        if len(dMatrix) == 2:
            return dMatrix[0][0] * dMatrix[1][1]-dMatrix[0][1]*dMatrix[1][0]

        determinant = 0
        for c in range(len(dMatrix)):
            determinant += ((-1)**c)*dMatrix[0][c]*self.get_matrix_determinant(self.get_matrix_minor(0, c, dMatrix))
        return determinant

    def get_matrix_inverse(self):
        determinant = self.get_matrix_determinant()
        if len(self.matrix) == 2:
            return [[self.matrix[1][1]/determinant, -1*self.matrix[0][1]/determinant],
                    [-1*self.matrix[1][0]/determinant, self.matrix[0][0]/determinant]]

        cofactors = []
        for r in range(len(self.matrix)):
            cofactorRow = []
            for c in range(len(self.matrix)):
                minor = self.get_matrix_minor(r, c)
                cofactorRow.append(((-1)**(r+c)) * self.get_matrix_determinant(minor))
            cofactors.append(cofactorRow)
        cofactors = list(self.transpose_matrix(cofactors))
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                try:
                    cofactors[r][c] = cofactors[r][c]/determinant
                except ZeroDivisionError:
                    cofactors[r][c] = cofactors[r][c]

        newMatrix = TMatrix()

        newMatrix.matrix = cofactors

        return newMatrix

    def inverse_check(self):
        """Should return an identity matrix if working correctly."""

        return str(self * self.get_matrix_inverse())
