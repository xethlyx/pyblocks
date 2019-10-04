class Matrix4():
    def __init__(self, one, two, three, four):
        self.one = one
        self.two = two
        self.three = three
        self.four = four

    def __str__(self):
        return("Matrix4({}, {}, {}, {})".format(self.one, self.two, self.three))
