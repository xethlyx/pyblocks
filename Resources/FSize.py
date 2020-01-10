class FSize():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return(self.x, self.y)

    def to_tuple_with_pos(self, x, y):
        return(x, y, self.x, self.y)
