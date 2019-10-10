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

        newMatrix = TMatrix()

        for rowNumber in range(len(newMatrix.matrix)):  # Increases slowest
            for columnNumber in range(len(newMatrix.matrix[rowNumber])):  # Increases quicker
                finalValue = 0

                for loopValue in range(len(newMatrix.matrix[rowNumber])):  # Increases quickest
                    finalValue = finalValue + (self.matrix[rowNumber][loopValue] * other.matrix[loopValue][columnNumber])

                newMatrix.matrix[rowNumber][columnNumber] = finalValue

        return newMatrix

        # x0 = (self.matrix[1][0] * other.matrix[0][0] +
        #       self.matrix[1][1] * other.matrix[1][0] +
        #       self.matrix[1][2] * other.matrix[2][0] +
        #       self.matrix[1][3] * other.matrix[3][0])

        # x1 = (self.matrix[2][0] * other.matrix[0][0] +
        #       self.matrix[2][1] * other.matrix[1][0] +
        #       self.matrix[2][2] * other.matrix[2][0] +
        #       self.matrix[2][3] * other.matrix[3][0])

        # x2 = (self.matrix[3][0] * other.matrix[0][0] +
        #       self.matrix[3][1] * other.matrix[1][0] +
        #       self.matrix[3][2] * other.matrix[2][0] +
        #       self.matrix[3][3] * other.matrix[3][0])

        # y0 = (self.matrix[2][0] * other.matrix[0][0] +
        #       self.matrix[2][1] * other.matrix[1][0] +
        #       self.matrix[2][2] * other.matrix[2][0] +
        #       self.matrix[2][3] * other.matrix[3][0])

    def set_scale(self, scale):
        self.matrix[0][0] = scale
        self.matrix[1][1] = scale
        self.matrix[2][2] = scale
        self.matrix[3][3] = scale

    def get_value(self, valueName):
        return self.matrix[matrixAlias[valueName][0]][matrixAlias[valueName][1]]

    def __str__(self):
        finalAppend = "TMatrix("

        for rowNumber in range(len(self.matrix)):  # Increases slowest
            rowAppend = "    "
            for columnNumber in range(len(self.matrix[rowNumber])):  # Increases quicker
                rowAppend = rowAppend + str(self.matrix[rowNumber][columnNumber])
                if columnNumber < (len(self.matrix[rowNumber]) - 1):
                    rowAppend = rowAppend + ", "

            if rowNumber < (len(self.matrix[rowNumber]) - 1):
                rowAppend = rowAppend + ", "

            finalAppend = finalAppend + "\n" + rowAppend

        finalAppend = finalAppend + "\n)"

        return finalAppend

    def set_value(self, valueName, newValue):
        self.matrix[matrixAlias[valueName][0]][matrixAlias[valueName][1]] = newValue

    def lerp(self, other, amount):
        def floatLerp(first, second, amount):
            return first * (1-amount) + (second*amount)

        for rowNumber in range(len(self.matrix)):  # Increases slowest
            for columnNumber in range(len(self.matrix[rowNumber])):  # Increases quicker

