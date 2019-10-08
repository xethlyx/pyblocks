class Matrix4():
    def __init__(self, one, two, three, four):
        self.one = one
        self.two = two
        self.three = three
        self.four = four

    def __str__(self):
        return("Matrix4({}, {}, {}, {})".format(self.one, self.two, self.three, self.four))

    def __eq__(self, other):
        print(self + " " + (self.one == other.one and self.two == other.two and self.three == other.three and self.four == other.four))

        return(self.one == other.one and self.two == other.two and self.three == other.three and self.four == other.four)
