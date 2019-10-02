class Matrix3():
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three

    def __str__(self):
        return("1:{} 2:{} 3:{}".format(self.one, self.two, self.three))
